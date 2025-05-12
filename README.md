This is a tool to process all of a user's [DMOJ](https://dmoj.ca) AC submissions into a downloadable zip.
It uses DMOJ's submission dump feature, which is unreasonably difficult to deal with and poorly formatted, to create a neat and organized file system. Submissions are grouped into their respective problem subfolder, with each containing addional info fetched from the DMOJ API.

## Usage

Ensure that all the required packages in requirements.txt have been installed.

Navigate to the folder containing `main.py` and run the command:

`python main.py`

Then open the link from the terminal, enter your DMOJ username, and upload the zip file obtained from the "Download your data" button in your user profile and filter by the result AC.

Note that submissions may take up to a minute to process depending on how many submissions the user has.
