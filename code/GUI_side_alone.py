import WebScrapper
import speech_system
import FolderManager
import os
from pydub import AudioSegment


class GUITools:
    """used by the GUI to do back end. Keeps code in a more readable state."""

    def __init__(self):

        self.chapterDetails = list
        self.chapterTitle = list
        self.bookName = list

    def split_chapter(self, book=str):
        """split string from a list in 2999 pieces"""

        chapter = WebScrapper.scrapper().loadChapter(book)
        self.chapterDetails = chapter[2]
        self.chapterTitle = chapter[0]
        self.bookName = chapter[4]

        left = 0
        right = 2999
        holder = []
        while True:
            if len(self.chapterDetails[left:]) < 2999:
                holder.append(self.chapterDetails[left:])
                break
            else:
                holder.append(self.chapterDetails[left:right])
                left = right
                right += 2999

        return holder

    def mergeAudio(self):
        """merge the mp3 files to one audio file. saves or makes new file for audio."""
        unsortedFolder = FolderManager.MP3FileHandler().listAllFile("Holder")
        sortedFolder = FolderManager.MP3FileHandler().sortFiles(unsortedFolder)
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

        path = os.getcwd()[:-5]

        self.bookName = "".join(filter(whitelist.__contains__, self.bookName))
        self.chapterTitle = "".join(filter(whitelist.__contains__, self.chapterTitle))

        combined = AudioSegment.from_file(path + "/Audio/Holder/" + sortedFolder[0], format="MP3")
        FolderManager.MP3FileHandler().delFile(path + "/Audio/Holder/" + sortedFolder[0])

        for files in sortedFolder[1:]:
            sound = AudioSegment.from_file(path + "/Audio/Holder/" + files, format="MP3")
            combined = combined + sound
            FolderManager.MP3FileHandler().delFile(path + "/Audio/Holder/" + files)

        #  fine a way to only do this without use always using it
        FolderManager.MP3FileHandler().makeFile(path + "/Audio/" + self.bookName.replace(" ", "_"))

        location = (path + "/Audio/" + self.bookName.replace(" ", "_") + "/" + self.chapterTitle + ".mp3")
        combined.export(location, format="mp3")

        return location
        # to do: make it delete all files it used apart from one it just made, make it save all the clips to -
        # a temp folder then save new chapters to a book folder

    #   functions/event, used to change data and mostly backend

    def chapterMP3Maker(self, chapter=str):
        """splits chapter into 2999 char then to a mp3 file"""

        c = self.split_chapter(chapter)
        self.mp3Convert(c)
        path = self.mergeAudio()
        return path

    #  static methods
    @staticmethod
    def play_media_player(path=str):
        """runs the selected media file from folder as if clicked"""
        if path is None:
            return 0

        if os.path.isfile(path):
            os.startfile(path)
        else:
            try:
                os.startfile((os.path.dirname(__file__) + path))
            except FileNotFoundError:
                raise Exception("File not found. error in selecting saved file")

        return 1

    @staticmethod
    def mp3Convert(chapters=list):
        """changes inputted list text to mp3 file. saved to holder file."""
        counter = 0
        # make it make a folder to save it too
        for words in chapters:
            speech_system.ToMP3().fileToMP3(inputText=words, bookTitle=str(counter))
            counter += 1
