import WebScrapper
import speech_system
import FolderManager
from pydub import AudioSegment


class GUI_tools:
    def __init__(self):

        self.chapterDetails = list
        self.chapterTitle = list
        self.bookName = list


    def split_chapter(self, book):
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

    def MP3Convert(self, chapters = list):
        """changes inputted list text to mp3 file. saved to holder file."""
        counter = 0
        # make it make a folder to save it too
        for words in chapters:
            speech_system.ToMP3().fileToMP3(inputText=words, bookTitle=str(counter))
            counter += 1

    def mergeAudio(self):
        """merge the mp3 files to one audio file. saves or makes new file for audio."""
        path = "../TTS/Audio/Holder/"
        unsortedFolder = FolderManager.MP3FileHandler().listAllFile("Holder")
        sortedFolder = FolderManager.MP3FileHandler().sortFiles(unsortedFolder)
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

        self.bookName = "".join(filter(whitelist.__contains__, self.bookName))
        self.chapterTitle = "".join(filter(whitelist.__contains__, self.chapterTitle))

        combined = AudioSegment.from_file(path + "/" + sortedFolder[0], format="MP3")
        FolderManager.MP3FileHandler().delFile(path + "/" + sortedFolder[0])

        for files in sortedFolder[1:]:
            sound = AudioSegment.from_file(path + "/" + files, format="MP3")
            combined = combined + sound
            FolderManager.MP3FileHandler().delFile(path + "/" + files)

        #  fine a way to only do this without use always using it
        FolderManager.MP3FileHandler().makeFile("../TTS/Audio/" + self.bookName.replace(" ", "_"))

        combined.export("../TTS/Audio/" + self.bookName.replace(" ", "_") + "/" + self.chapterTitle + ".mp3", format="mp3")
        #to do: make it delete all files it used apart from one it just made, make it save all the clips to a temp folder then save new chapters to a book folder


"""
a = GUI_tools()


c = a.split_chapter("https://www.royalroad.com/fiction/21220/mother-of-learning/chapter/301784/3-the-bitter-truth")
a.MP3Convert(c)

a.mergeAudio()
print("done")
"""