import wx
import WebScrapper
import GUI_side_alone


#  https://www.wxpython.org/ look to change the GUI to a better front end like this
#  https://github.com/Phanabani/minecraft-playtime-calculator
#  https://github.com/Phanabani/minecraft-playtime-calculator/blob/master/minecraft_playtime_calculator/ui.py#L149


class MainPage(wx.Frame):
    """GUI interface for system. main page, uses GUI side alone for back end events."""

    def __init__(self, parent):
        super(MainPage, self).__init__(parent, title="TTSRR",
                                       size=(350, 250))


        self.mainPageOpen = True
        self.changePage = True
        self.searchResults = []

        self.panel = wx.Panel(self)
        self.buttonHolder = {}

        self.InitUI()
        self.Show()

        self.currentBook = list
        self.chapterBrokenUp = list


        self.side_alone = GUI_side_alone.GUITools()

    #  UI set location of main page

    def InitUI(self):
        """Main GUI code. This load 'home' interface. Sets the location of buttons and text boxes."""
        #  search input

        wx.StaticText(self.panel, label="Search book", pos=(10, 12))
        self.searchBar = wx.TextCtrl(self.panel, size=(200, 20), pos=(80, 10), style=wx.TE_PROCESS_ENTER)
        self.searchBar.Bind(wx.EVT_TEXT_ENTER, self.ButtonsearchOnEnter)

        # Home page recommend book buttons

        self.MainPageBooks()

        # book details on the right side to books listings

        self.textBoxTitle = wx.TextCtrl(self.panel, size=(250, 40), pos=(700, 20), style=wx.TE_READONLY | wx.TE_MULTILINE,
                                        value="Title")
        self.textBoxAuthor = wx.TextCtrl(self.panel, size=(250, 40), pos=(700, 70), style=wx.TE_READONLY | wx.TE_MULTILINE,
                                         value="Author")
        self.textBoxBlerb = wx.TextCtrl(self.panel, size=(250, 100), pos=(700, 120), style=wx.TE_READONLY | wx.TE_MULTILINE,
                                        value="Blurb")

        #  to do: add a book image at some point.

        self.ListChapters = wx.ListCtrl(self.panel, size=(250, 100), pos=(700, 230),
                                        style=
                                    wx.BORDER_SUNKEN | wx.TE_MULTILINE
                                        )
        self.ListChapters.InsertColumn(0, '', width=50)
        self.ListChapters.InsertColumn(1, 'Chapter', width=200)

        #  buttons locations and names. linked to event (bind), see below.

        btnRead = wx.Button(self.panel, label="Read", pos=(700, 350))
        btnRead.Bind(wx.EVT_BUTTON, self.readButton)

        btnFileOpen = wx.Button(self.panel, label="Open File", pos=(775, 350))
        btnFileOpen.Bind(wx.EVT_BUTTON, self.OnOpen)

        btnHome = wx.Button(self.panel, label="Home", pos=(290, 9))
        btnHome.Bind(wx.EVT_BUTTON, self.ButtonChangePage)

    #  different layouts for UI

    def searchResultBook(self):
        """show results from searching for book in search bar in GUI."""
        self.changePage = False
        self.mainPageOpen = False
        counter = 0

        self.searchTitle = wx.StaticText(self.panel, label="Search Results:", pos=(15, 35))

        self.btnSelBook = wx.Button(self.panel, label="Select Book", pos=(600, 350))
        self.btnSelBook.Bind(wx.EVT_BUTTON, self.buttonSelectBook)

        self.searchResultBox = wx.ListCtrl(self.panel, size=(500, 500), pos=(15, 55),
                                           style=
                                    wx.BORDER_SUNKEN | wx.TE_MULTILINE
                                           )
        self.searchResultBox.InsertColumn(0, '', width=50)
        self.searchResultBox.InsertColumn(1, 'Books', width=200)

        self.searchResults = (WebScrapper.scrapper().SearchResultBookLinks(self.searchBar.GetValue()))

        self.searchResultBox.DeleteAllItems()
        for books in self.searchResults:
            self.searchResultBox.InsertItem(counter, str(counter + 1))
            self.searchResultBox.SetItem(counter, 1, books.rsplit('/', 1)[1].replace("-", " ") + "\n")
            counter += 1

    def MainPageBooks(self):
        """shows the home page recommended books"""
        books = WebScrapper.scrapper().HomePageBookLinks()
        self.mainPageOpen = True

        #  the locations of the buttons on UI (y)
        bookLoc = 55

        # counter for counting buttons place and other loops
        counter = 0

        #  list books and ranks
        self.LUTitle = wx.StaticText(self.panel, label="LATEST UPDATES", pos=(15, 35))
        self.RSTitle = wx.StaticText(self.panel, label="RISING STARS", pos=(330, 35))
        self.BCTitle = wx.StaticText(self.panel, label="BEST COMPLETED", pos=(15, 315))
        self.BOTitle = wx.StaticText(self.panel, label="BEST ONGOING", pos=(330, 315))

        for book in books:
            if counter == 10:
                bookLoc = 55
            elif counter == 17 or counter == 37:
                bookLoc = 335

            if counter < 10:
                #  latest update
                self.buttonHolder["Button{0}{1}".format(1, bookLoc)] = wx.Button(self.panel, -1, label=book[15:].replace("-", " "), pos=(15, bookLoc))
                self.buttonHolder["Button{0}{1}".format(1, bookLoc)].Bind(wx.EVT_BUTTON, lambda event, temp=book: self.showBookDetails(event, temp))
            elif counter < 17:
                #  Rising star
                self.buttonHolder["Button{0}{1}".format(2, bookLoc)] = wx.Button(self.panel, -1, label=book[15:].replace("-", " "), pos=(330, bookLoc))
                self.buttonHolder["Button{0}{1}".format(2, bookLoc)].Bind(wx.EVT_BUTTON, lambda event, temp=book: self.showBookDetails(event, temp))
            elif counter < 37:
                #  best completed
                #  due to doubling of book names. to do: fix doubling of chapter names in list
                if (counter % 2) == 0:
                    bookLoc -= 25

                    self.buttonHolder["Button{0}{1}".format(3, bookLoc)] = wx.Button(self.panel, -1, label=book[15:].replace("-", " "), pos=(15, bookLoc))
                    self.buttonHolder["Button{0}{1}".format(3, bookLoc)].Bind(wx.EVT_BUTTON, lambda event, temp=book: self.showBookDetails(event, temp))
            elif counter < 37:
                #  due to doubling of book names.
                #  error: not showing up
                if (counter % 2) == 0:
                    bookLoc -= 25

                    self.buttonHolder["Button{0}{1}".format(4, bookLoc)] = wx.Button(self.panel, -1, label=book[15:].replace("-", " "), pos=(15, bookLoc))
                    self.buttonHolder["Button{0}{1}".format(4, bookLoc)].Bind(wx.EVT_BUTTON, lambda event, temp=book: self.showBookDetails(event, temp))
            elif counter < 57:
                #  best ongoing
                #  due to doubling of book names.
                if (counter % 2) == 0:
                    bookLoc -= 25


                    self.buttonHolder["Button{0}{1}".format(5, bookLoc)] = wx.Button(self.panel, -1, label=book[15:].replace("-", " "), pos=(330, bookLoc))
                    self.buttonHolder["Button{0}{1}".format(5, bookLoc)].Bind(wx.EVT_BUTTON, lambda event, temp=book: self.showBookDetails(event, temp))
            bookLoc += 25
            counter += 1

    #  button events, once clicked on event is run

    def readButton(self, event):
        """ read button on the GUI. send path to be loaded as mp3 then read"""
        path = str
        item = self.ListChapters.GetFocusedItem()
        counter = 0
        for chapter in self.currentBook[3]:
            if item == counter:
                path = self.side_alone.chapterMP3Maker("https://www.royalroad.com" + chapter)
                break
            counter += 1

        issue = self.side_alone.play_media_player(path)

        if not issue:
            self.issueError()

    def readButtonSearch(self, event):
        """ read button on the GUI. send path to be loaded as mp3 then read"""
        path = str
        item = self.ListChapters.GetFocusedItem()
        counter = 0
        for chapter in self.currentBook[3]:
            if item == counter:
                path = self.side_alone.chapterMP3Maker("https://www.royalroad.com" + chapter)
                break
            counter += 1

        issue = self.side_alone.play_media_player(path)

        if not issue:
            self.issueError()


    def showBookDetails(self, event, my_value=str):
        """sets the book details in text boxes (title, blurb, chapters) once book button selected"""
        counter = 0
        self.currentBook = WebScrapper.scrapper().loadBook("https://www.royalroad.com" + my_value)
        self.textBoxTitle.SetValue(self.currentBook[0])
        self.textBoxAuthor.SetValue(self.currentBook[1])
        self.textBoxBlerb.SetValue(self.currentBook[2])
        self.ListChapters.DeleteAllItems()
        for chapter in self.currentBook[3]:
            self.ListChapters.InsertItem(counter, str(counter + 1))
            self.ListChapters.SetItem(counter, 1, chapter.rsplit('/', 1)[1].replace("-", " ") + "\n")
            counter += 1

    def ButtonChangePage(self, event):
        """home button which refreshes home page or changes from search page to home page"""
        if self.mainPageOpen:
            self.changePage = False
        else:
            self.changePage = True

        self.ChangePageType(event)

    def ButtonsearchOnEnter(self, event):
        """search event which refreshes search page or changes from home page to search page"""
        if self.mainPageOpen:
            self.changePage = True
        else:
            self.changePage = False

        self.ChangePageType(event)

    def buttonSelectBook(self, event):
        bookLocation = self.searchResultBox.GetFocusedItem()

        book = self.searchResults[bookLocation]
        self.showBookDetails(event, book)

    def OnOpen(self, event):
        """opens users file so they can select an MP3 file"""

        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Open audio file", wildcard="MP3 files (*.MP3)|*.MP3",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:

                return 0  # the user changed their mind
            else:
                issue = self.side_alone.play_media_player(fileDialog.GetPath())

                if not issue:
                    self.issueError()

    def ChangePageType(self, event):
        """change and reload the pages based on current page"""
        for button in self.buttonHolder:
            self.buttonHolder[button].Destroy()

        self.buttonHolder.clear()

        #  refresh the home page

        if self.mainPageOpen and not self.changePage:

            #  remove all old listed books
            self.LUTitle.Destroy()
            self.RSTitle.Destroy()
            self.BCTitle.Destroy()
            self.BOTitle.Destroy()

            #  reload the different book types
            self.MainPageBooks()

        #  change to search page

        elif self.mainPageOpen and self.changePage:
            #  remove all book types
            self.LUTitle.Destroy()
            self.RSTitle.Destroy()
            self.BCTitle.Destroy()
            self.BOTitle.Destroy()

            #  set main page to false to show search page open
            self.mainPageOpen = False

            #  load the search page
            self.searchResultBook()

        #  refresh the search page

        elif not self.mainPageOpen and not self.changePage:

            #  remove the old book and title
            self.searchTitle.Destroy()
            self.searchResultBox.Destroy()
            self.btnSelBook.Destroy()

            #  reload the new search results
            self.searchResultBook()

        # change to home page

        elif not self.mainPageOpen and self.changePage:
            #  remove the old book and title
            self.searchTitle.Destroy()
            self.searchResultBox.Destroy()
            self.btnSelBook.Destroy()

            #  mark it to show it's now the main page
            self.mainPageOpen = True

            #  load new main page
            self.MainPageBooks()


    @staticmethod
    def issueError():
        """error return for GUI methods command."""
        print("Error - issue with return value")


def main():
    """load UI main"""
    app = wx.App()
    frame = MainPage(None)
    frame.Show()
    app.MainLoop()
