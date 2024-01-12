import requests
import json
import os
import shutil
import zipfile

forbidden_chars = ["/", "\\", "<", ">", ":", '"', "|", "?", "*", "."]

def sanitize_problem_name(problem):
    for bad_char in forbidden_chars:
        problem = problem.replace(bad_char, " ")
    problem = problem.strip()
    return problem

def transform_file(name):
    path = os.path.abspath(os.path.dirname(__file__)) #dmoj-submission-uploader
    filespath = os.path.join(path, "static/files")
    zippath = os.path.join(path, "static/files/" + name + "-data.zip")
    staticpath = os.path.join(path, "static")
    oldsubpath = os.path.join(staticpath, "submissions")
    newsubpath = os.path.join(staticpath, "new_subs")
    if os.path.exists(oldsubpath):
        shutil.rmtree(oldsubpath)
    if os.path.exists(newsubpath):
        shutil.rmtree(newsubpath)
    if os.path.exists(os.path.join(staticpath, "processed_submissions.zip")):
        os.remove(os.path.join(staticpath, "processed_submissions.zip"))
    with zipfile.ZipFile(zippath, 'r') as zip_ref:
        zip_ref.extractall(staticpath)
    os.remove(os.path.join(staticpath, "submissions/info.json"))
    os.mkdir(newsubpath)

    problems_url = "https://dmoj.ca/api/v2/problems"
    response = requests.get(problems_url)
    pagecount = response.json()["data"]["total_pages"]

    to_problem_name = {}
    to_points = {}
    problem_data = {}
    for page in range(0, pagecount):
        response = requests.get(problems_url + "?page=" + str(page + 1))
        problem_list = response.json()["data"]["objects"]
        for problem in problem_list:
            problem_data[sanitize_problem_name(problem["name"])] = problem
            to_problem_name[problem["code"]] = problem["name"]
            to_points[problem["code"]] = problem["points"]

    sub_url = "https://dmoj.ca/api/v2/submissions?user=" + name + "&results=AC"
    response = requests.get(sub_url)
    pagecount = response.json()["data"]["total_pages"]
    
    full_solve = {}
    to_problem_code = {}
    for page in range(0, pagecount):
        response = requests.get(sub_url + "&page=" + str(page + 1))
        sub_list = response.json()["data"]["objects"]
        for sub in sub_list:
            if sub["points"] == to_points[sub["problem"]]:
                full_solve[sub["id"]] = True
                to_problem_code[sub["id"]] = sub["problem"]
        
    subs = os.listdir(oldsubpath)
    
    for filename in subs:
        subcode = int(filename[:filename.rfind('.')])
        ext = filename[(filename.rfind('.') + 1):]
        if subcode not in full_solve.keys():
            continue
        new_file_name = sanitize_problem_name(to_problem_name[to_problem_code[subcode]])
        new_file_path = os.path.join(newsubpath, new_file_name)
        if not os.path.exists(new_file_path):
            os.mkdir(new_file_path)
        shutil.move(os.path.join(oldsubpath, filename), os.path.join(new_file_path, filename))
    
    newsub = os.listdir(newsubpath)
    for problem in newsub:
        infopath = os.path.join(os.path.join(newsubpath, problem), "info.md")
        with open(infopath, 'w', newline='') as file:
            json.dump(problem_data[problem], file)

    print(len(os.listdir(newsubpath)), "problems processed")
    shutil.make_archive(os.path.join(os.path.join(staticpath, "files"), "processed_submissions"), "zip", staticpath, "new_subs")
    os.remove(os.path.join(filespath, name + "-data.zip"))
    if os.path.exists(oldsubpath):
        shutil.rmtree(oldsubpath)
    if os.path.exists(newsubpath):
        shutil.rmtree(newsubpath)
    return "Submissions have been processed: "
"""
sub_by_problem = {}


for submission in sub_list:
    if submission["result"] != "AC":
        continue
    submission_id = submission["id"]
    problem_code = submission["problem"]
    if problem_code not in sub_by_problem:
        sub_by_problem[problem_code]=list()
    sub_by_problem[problem_code].append(submission_id)

for e in sub_by_problem:
    print(e, problem_dict[e], "------")
    for f in sub_by_problem[e]:
        print(f)
    print()
"""