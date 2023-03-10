import os
import requests


class startUp():
    def __init__(self):
        print("starting checks")
        path = os.getcwd()

        if not os.path.exists(path[:-5] + "/Audio"):
            print("issue - making Audio and Holder file")
            os.makedirs(path[:-5] + "/Audio")
            os.makedirs(path[:-5] + "/Audio/Holder")

        if not os.path.exists(path[:-5] + "/Audio/Holder"):
            print("issue - making Holder file")
            os.makedirs(path[:-5] + "/Audio/Holder")

        self.fileChecker(path)
        self.addOnChecker()
        self.connectionCheck()

        print("checks done")

    def fileChecker(self, path):
        """checks for all needed py files."""
        fileNames = ["FolderManager.py", "GUI.py", "GUI_Root.py", "GUI_side_alone.py", "Polly_connection.py",
                     "main.py", "speech_system.py",
                     "startUpCheck.py", "WebScrapper.py"]
        # check for way to auto check git and for new changes

        for fileName in fileNames:
            if not os.path.exists(path + "/" + fileName):
                raise Exception("missing files - please check for " + fileName + " and download.")

    def addOnChecker(self):
        """checks the needed files for aws and ffmpeg are installed"""

        path = os.path.expanduser("~/.aws")
        if not os.path.isfile(path + "/credentials"):
            raise Exception("Warning aws credentials not found in users files. This is needed for text to speech. "
                            "for a quick guide check: https://boto3.amazonaws.com/v1/documentation/api/latest/guide"
                            "/quickstart.html.")

        if not os.path.isdir("C:/ffmpeg") or not os.path.isdir("C:/ffmpeg/bin"):
            raise Exception("Warning ffmpeg files not found in C files. This is needed for text to speech. "
                            "for a quick guide check: https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/ or "
                            "https://github.com/jiaaro/pydub#installation .")

        # find way to check if path was made for ffmpeg

    def connectionCheck(self):

        try:
            res = requests.get('https://www.royalroad.com/home')
            if (res.status_code):
                pass
        except:
            raise Exception("warning - connection to unable to be made")


