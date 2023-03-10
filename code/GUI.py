import wx
import WebScrapper
import GUI_side_alone

#  https://www.wxpython.org/ look to change the GUI to a better front end like this
#  https://github.com/Phanabani/minecraft-playtime-calculator

#  https://github.com/Phanabani/minecraft-playtime-calculator/blob/master/minecraft_playtime_calculator/ui.py#L149

class MainPage(wx.Frame):

    def __init__(self, parent):
        super(MainPage, self).__init__(parent, title="TTSRR",
                                       size=(350, 250))

        self.InitUI()
        self.Show()

        self.currectbook = list
        self.chapterBrokenUp = list

    #  UI set location of main page

    def InitUI(self):
        """Main GUI code. This load 'home' interface. Sets the location of buttons and text boxes."""
        panel = wx.Panel(self)
        books = WebScrapper.scrapper().HomePageBookLinks()

        #  the locations of the buttons on UI (y)
        bookLoc = 45

        # counter for counting buttons place and other loops
        counter = 0

        #  list books and ranks
        wx.StaticText(panel, label="LATEST UPDATES", pos=(15, 20))
        wx.StaticText(panel, label="RISING STARS", pos=(330, 20))
        wx.StaticText(panel, label="BEST COMPLETED", pos=(15, 300))
        wx.StaticText(panel, label="BEST ONGOING", pos=(330, 300))

        for book in books:
            if counter == 10:
                bookLoc = 45
            elif counter == 17 or counter == 37:
                bookLoc = 325

            if counter < 10:
                my_btn = wx.Button(panel, -1, label=book[15:].replace("-", " "), pos=(15, bookLoc))
                my_btn.Bind(wx.EVT_BUTTON, lambda event, temp=book: self.dispenser_pause(event, temp))
            elif counter < 17:
                my_btn = wx.Button(panel, -1, label=book[15:].replace("-", " "), pos=(330, bookLoc))
                my_btn.Bind(wx.EVT_BUTTON, lambda event, temp=book: self.dispenser_pause(event, temp))
            elif counter < 37:
                #  due to doubling of book names. to do: fix doubling of chapter names in list
                if (counter % 2) == 0:
                    bookLoc -= 25

                    my_btn = wx.Button(panel, -1, label=book[15:].replace("-", " "), pos=(15, bookLoc))
                    my_btn.Bind(wx.EVT_BUTTON, lambda event, temp=book: self.dispenser_pause(event, temp))
            elif counter < 37:
                #  due to doubling of book names.
                if (counter % 2) == 0:
                    bookLoc -= 25

                    my_btn = wx.Button(panel, -1, label=book[15:].replace("-", " "), pos=(15, bookLoc))
                    my_btn.Bind(wx.EVT_BUTTON, lambda event, temp=book: self.dispenser_pause(event, temp))
            elif counter < 57:
                #  due to doubling of book names.
                if (counter % 2) == 0:
                    bookLoc -= 25

                    my_btn = wx.Button(panel, -1, label=book[15:].replace("-", " "), pos=(330, bookLoc))
                    my_btn.Bind(wx.EVT_BUTTON, lambda event, temp=book: self.dispenser_pause(event, temp))
            bookLoc += 25
            counter += 1

        # book details on the right side to books listings

        self.t1 = wx.TextCtrl(panel, size=(250, 40), pos=(700, 20), style=wx.TE_READONLY | wx.TE_MULTILINE,
                              value="Title")
        self.t2 = wx.TextCtrl(panel, size=(250, 40), pos=(700, 70), style=wx.TE_READONLY | wx.TE_MULTILINE,
                              value="Author")
        self.t3 = wx.TextCtrl(panel, size=(250, 100), pos=(700, 120), style=wx.TE_READONLY | wx.TE_MULTILINE,
                              value="Blurb")

        #  to do: add a book image at some point.

        self.ListCtrl = wx.ListCtrl(panel, size=(250, 100), pos=(700, 230),
                                    style=
                                    wx.BORDER_SUNKEN | wx.TE_MULTILINE
                                    )
        self.ListCtrl.InsertColumn(0, '', width=50)
        self.ListCtrl.InsertColumn(1, 'Chapter', width=200)

        #  buttons locations and names. linked to event (bind), see below.

        btnRead = wx.Button(panel, label="Read", pos=(700, 350))
        btnRead.Bind(wx.EVT_BUTTON, self.readButton)

        btnFileOpen = wx.Button(panel, label="Open File", pos=(775, 350))
        btnFileOpen.Bind(wx.EVT_BUTTON, self.OnOpen)

    #  button events, once clicked on event is run

    def readButton(self, event):
        """ read button on the GUI. send path to be loaded as mp3 then read"""
        item = self.ListCtrl.GetFocusedItem()
        counter = 0
        for chapter in self.currectbook[3]:
            if item == counter:
                path = self.chapterMP3Maker("https://www.royalroad.com" + chapter)
                break
            counter += 1

        issue = GUI_side_alone.GUI_tools().play_media_player(path)

        if not issue:
            self.issueError()

    def dispenser_pause(self, event, my_value):
        """sets the book details in text boxes (title, blurb, chapters) once book button selected"""
        counter = 0
        self.currectbook = WebScrapper.scrapper().loadBook("https://www.royalroad.com" + my_value)
        self.t1.SetValue(self.currectbook[0])
        self.t2.SetValue(self.currectbook[1])
        self.t3.SetValue(self.currectbook[2])
        self.ListCtrl.DeleteAllItems()
        for chapter in self.currectbook[3]:
            self.ListCtrl.InsertItem(counter, str(counter + 1))
            self.ListCtrl.SetItem(counter, 1, chapter.rsplit('/', 1)[1].replace("-", " ") + "\n")
            counter += 1

    #   functions/event, used to change data and mostly backend

    def chapterMP3Maker(self, chapter):
        """splits chapter into 2999 char then to a mp3 file"""

        a = GUI_side_alone.GUI_tools()
        c = a.split_chapter(chapter)
        a.MP3Convert(c)
        path = a.mergeAudio()
        return path


    def OnOpen(self, event):
        """opens users file so they can select an MP3 file"""

        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Open audio file", wildcard="MP3 files (*.MP3)|*.MP3",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:

                return 0  # the user changed their mind
            else:
                issue = GUI_side_alone.GUI_tools().play_media_player(fileDialog.GetPath())

                if not issue:
                    self.issueError()


    def issueError(self):
        """error return for GUI methods command."""
        print("Error - issue with return value")


def main():
    app = wx.App()
    frame = MainPage(None)
    frame.Show()
    app.MainLoop()

