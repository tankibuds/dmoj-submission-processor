# tankibuds' DMOJ Submission Processor

This is a tool to process all of a user's [DMOJ](https://dmoj.ca) AC submissions into a downloadable zip.
It uses DMOJ's submission dump feature, which is unreasonably difficult to deal with and poorly formatted, to create a neat and organized file system. Submissions are grouped into their respective problem subfolder, with each containing addional info fetched from the DMOJ API.

## Usage

Ensure that all the required packages in requirements.txt have been installed.

Navigate to the folder containing `main.py` and run the command:

`python main.py`

Then open the link from the terminal, enter your DMOJ username, and upload the zip file obtained from the "Download your data" button in your user profile and filter by the result AC.

![DMOJ data download image](https://media.discordapp.net/attachments/1091348803401023560/1195511876575035602/image.png?ex=65b44232&is=65a1cd32&hm=dc155592f69cf5d64a63d81a293750bb194b94e5901a564c195eaa741d62dbcc&=&format=webp&quality=lossless&width=1440&height=502)

Note that submissions may take up to a minute to process depending on how many submissions the user has.

![submission uploader image](https://cdn.discordapp.com/attachments/1091348803401023560/1195512816929603645/image.png?ex=65b44313&is=65a1ce13&hm=cfdcc3b4c978cb67a7f13d64537b6027e7c24f94983f3fe238b1f64e3532c8ef&)
