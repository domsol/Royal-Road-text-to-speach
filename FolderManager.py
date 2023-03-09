import os


class readAwriteSettings:
    """Opens the setting file to read or write to it. used to store details even once application is closed."""

    def readSettings(self):
        """read and returns the info in setting file."""
        try:
            with open("settings.txt", "r") as FileContent:
                return FileContent.read()
        except FileNotFoundError:
            self.fileNotFound()
            self.readSettings()

    def fileNotFound(self):
        """If no file found under the name settings.txt then make a setting."""
        with open("settings.txt", "x") as FileContent:
            FileContent.write("THEME_SELECT=\nDark")

    def writeSettings(self, newContext):
        """write to the file with new text."""
        #  this should be improved at later date
        context = self.readSettings()
        toChange = newContext.split("=")
        toChange[0] = toChange[0] + "="
        changeNext = False
        items = []
        click = False

        for a in context.split("\n"):
            if changeNext == False:
                items.append(a)
            else:
                changeNext = False
                items.append(toChange[1])

            if a.rstrip() == toChange[0]:
                changeNext = True


        with open("settings.txt", "w") as fileContent:
            for b in items:
                if click:
                    fileContent.write(b)
                else:
                    fileContent.write(b + "\n")


class MP3FileHandler:

    def __init__(self):
        """Loads the path to file and if not found will make one."""
        self.path = "../TTS/Audio"

        if not os.path.exists(self.path):
            self.folderNotFound(self.path)

    def listAllFile(self, folder):
        """Lists all the files inside a folder. Used to list all mp3 for merging."""
        files = os.listdir(self.path + "/" + folder)
        if len(files) == 0:
            self.folderNotFound(self.path + "/" + folder)
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

"""
A = MP3FileHandler()
gold = A.listAllFile("test")
print(A.sortFiles(gold))
"""
