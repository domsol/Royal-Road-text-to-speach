import os


class readAndWriteSettings:
    """Opens the setting file to read or write to it. used to store details even once application is closed. not in
    use ATM """

    def readSettings(self):
        """read and returns the info in setting file."""
        settings = {"THEME_SELECT": "",
                    "TEST": ""}
        switch = True
        settingKeyName = ""
        try:
            with open("settings.txt", "r") as FileContent:

                a = (FileContent.read()).replace("\n","")
                b = a.split(".")
                for settingType in b:
                    if switch:
                        switch = False
                        settingKeyName = settingType

                    elif not switch:
                        settings[settingKeyName] = settingType.strip()
                        switch = True

            return settings

        except FileNotFoundError:
            self.fileNotFound()
            self.readSettings()

    def writeSettings(self, settingName=str, newContext=str):
        """write to the file with new text."""
        #  set all setting name, loop to check setting to new setting, change that setting to new context
        first = True
        settings = self.readSettings()
        settings[settingName] = newContext

        with open("settings.txt", "w") as FileContent:
            for settingTypes in settings:
                if first:
                    FileContent.write(settingTypes + "." + settings[settingTypes])
                    first = False
                else:
                    FileContent.write(".\n" + settingTypes + "." + settings[settingTypes])
        return 0

    @staticmethod
    def fileNotFound():
        """If no file found under the name settings.txt then make a setting."""
        with open("settings.txt", "x") as FileContent:
            FileContent.write("THEME_SELECT.Light.")


class MP3FileHandler:

    def __init__(self):
        """Loads the path to file and if not found will make one."""
        self.path = os.getcwd()[:-5]

        if not os.path.exists(self.path):
            self.folderNotFound(self.path)

    def listAllFile(self, folder=str):
        """Lists all the files inside Audio folder. Used to list all mp3 for merging."""
        files = os.listdir(self.path + "/Audio/" + folder)
        if len(files) == 0:
            self.folderNotFound(self.path + "/Audio/" + folder)
            return False
        else:
            return files

    def sortFiles(self, folder=list):
        """Sorts the unsorted files in list then returns."""

        folder.sort(key=self.sortSetting)
        return folder

    def sortSetting(self, elem=str):
        """key for sorting. gets the numbers of file and changes it to int value."""

        a = int((elem[:-4]))
        return a

    @staticmethod
    def folderNotFound(path=str):
        """If file not found, makes one. Reduces errors or deleted file."""

        os.makedirs(path)

    @staticmethod
    def delFile(fileName=str):
        """removes a file when given file name"""
        if os.path.exists(fileName):
            os.remove(fileName)

    @staticmethod
    def makeFile(fileName=str):
        """makes a file when given file name"""
        if not os.path.exists(fileName):
            os.makedirs(fileName)
