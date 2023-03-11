import os


class read_and_write_Settings:
    """Opens the setting file to read or write to it. used to store details even once application is closed."""


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
                    if switch == True:
                        switch = False
                        settingKeyName = settingType

                    elif switch == False:
                        settings[settingKeyName] = settingType.strip()
                        switch = True

            return settings

        except FileNotFoundError:
            self.fileNotFound()
            self.readSettings()

    def fileNotFound(self):
        """If no file found under the name settings.txt then make a setting."""
        with open("settings.txt", "x") as FileContent:
            FileContent.write("THEME_SELECT=\nDark")

    def writeSettings(self, settingName, newContext):
        """write to the file with new text."""
        #  set all setting name, loop to check setting to new setting, change that setting to newcontext
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


class MP3FileHandler:

    def __init__(self):
        """Loads the path to file and if not found will make one."""
        self.path = os.getcwd()[:-5]

        if not os.path.exists(self.path):
            self.folderNotFound(self.path)

    def listAllFile(self, folder):
        """Lists all the files inside Audio folder. Used to list all mp3 for merging."""
        files = os.listdir(self.path + "/Audio/" + folder)
        if len(files) == 0:
            self.folderNotFound(self.path + "/Audio/" + folder)
            return False
        else:
            return files

    def folderNotFound(self, path):
        """If file not found, makes one. Reduces errors or deleted file."""

        os.makedirs(path)

    def sortSetting(self, elem):
        """key for sorting. gets the numbers of file and changes it to int value."""

        a = (int((elem[:-4])))
        return a

    def sortFiles(self, folder):
        """Sorts the unsorted files in list then returns."""

        folder.sort(key=self.sortSetting)
        return folder

    def delFile(self, fileName):
        if os.path.exists(fileName):
            os.remove(fileName)

    def makeFile(self, fileName):
        if not os.path.exists(fileName):
            os.makedirs(fileName)

a = read_and_write_Settings()
print(a.writeSettings("THEME_SELECT", "hello"))
