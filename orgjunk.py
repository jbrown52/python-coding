# this program organizes loose files 

#https://www.geeksforgeeks.org/how-to-move-files-and-directories-in-python/ <------ shutil utility can move folders around 

# https://www.geeksforgeeks.org/junk-file-organizer-python/ <--- this is where I found the tutorial for this 

# improvements: 

#this worked great! I should find out a way to add to DIRECTORIES when the program encounters a file type not listed. 

# I also want to look into creating an EXE that will run this anywhere on the pc i want and move files somewhere other than current space it's in. 

# it should be able to organize folders too one day. 

from pathlib import Path
import os

# whats a pirates favorite programming tool? 

#ARRRRRays
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],

    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg"  ],

    "VIDEOS" : [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx", ".mobi"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "C++": [".cpp"], 

    "XML": [".xml"],
    "EXE": [".exe"],

    "SHELL": [".sh"],
}

# map file formats to directories 
FILE_FORMATS = {
    file_format: directory for directory, file_formats in DIRECTORIES.items() for file_format in file_formats

}

# map extensions with the directory
# checks for directory name as defined above 
#if no directory is found a new directory is created to store the new file extension
def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok = True) 
            file_path.rename(directory_path.joinpath(file_path))
            

        for dir in os.scandir():
            try: # First time using and seeing try I guess it attempts to move a file and if not just skips it. 
                # in a python class it probably would have just been an if else and crapped itself when finding a file type not listed
                os.rmdir(dir)
            except:
                pass


if __name__ == "__main__": # why the double spaces on either side? going to have to look that up. 
    organize_junk()