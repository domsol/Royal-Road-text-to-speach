import wx
import GUI_Root
import WebScrapper
import FolderManager
import speech_system


#  https://www.wxpython.org/ look to change the GUI to a better front end like this
#  https://github.com/Phanabani/minecraft-playtime-calculator

#  https://github.com/Phanabani/minecraft-playtime-calculator/blob/master/minecraft_playtime_calculator/ui.py#L149

class MainPage(wx.Frame):

    def __init__(self, parent, title):
        super(MainPage, self).__init__(parent, title="TTSRR",
                                       size=(350, 250))

        self.InitUI()
        self.Show()
        self.currectbook = list
        self.chapterBrokenUp = list

    def InitUI(self):
        panel = wx.Panel(self)
        books = WebScrapper.scrapper().HomePageBookLinks()
        bookLoc = 45
        counter = 0
        wx.StaticText(panel, label="LATEST UPDATES", pos=(15, 20))

        wx.StaticText(panel, label="RISING STARS", pos=(330, 20))

        for book in books:
            if counter == 10:
                bookLoc = 45

            if counter < 10:
                my_btn = wx.Button(panel, -1, label=book[15:].replace("-", " "), pos=(15, bookLoc))
                my_btn.Bind(wx.EVT_BUTTON, lambda event, temp=book: self.dispenser_pause(event, temp))
            elif counter < 17:
                my_btn = wx.Button(panel, -1, label=book[15:].replace("-", " "), pos=(330, bookLoc))
                my_btn.Bind(wx.EVT_BUTTON, lambda event, temp=book: self.dispenser_pause(event, temp))

            bookLoc += 25
            counter += 1

        self.t1 = wx.TextCtrl(panel, size=(250, 40), pos=(700, 20), style=wx.TE_READONLY | wx.TE_MULTILINE,
                              value="Title")
        self.t2 = wx.TextCtrl(panel, size=(250, 40), pos=(700, 70), style=wx.TE_READONLY | wx.TE_MULTILINE,
                              value="Author")
        self.t3 = wx.TextCtrl(panel, size=(250, 100), pos=(700, 120), style=wx.TE_READONLY | wx.TE_MULTILINE,
                              value="Blerb")

        #  add a book image at some point.

        self.ListCtrl = wx.ListCtrl(panel, size=(250, 100), pos=(700, 230),
                                    style=
                                    wx.BORDER_SUNKEN | wx.TE_MULTILINE
                                    )
        self.ListCtrl.InsertColumn(0, '', width=50)
        self.ListCtrl.InsertColumn(1, 'Chapter', width=200)

        btnRead = wx.Button(panel, label="read", pos=(700, 350))
        btnRead.Bind(wx.EVT_BUTTON, self.toRead)

    def toRead(self, event):
        item = self.ListCtrl.GetFocusedItem()
        counter = 0
        for chapter in self.currectbook[3]:
            if item == counter:
                self.chapterSpliter(WebScrapper.scrapper().loadChapter("https://www.royalroad.com" + chapter))
                break
            counter += 1

    def dispenser_pause(self, event, my_value):
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

    def chapterSpliter(self, chapterDeatails):

        self.chapterBrokenUp.clear()
        totalChapter = ("chapter " + chapterDeatails[0] + "\n writer: " + chapterDeatails[1] + "\n " + chapterDeatails[2])

    def chapSplitter(self, totalChapter):

        if totalChapter.len() < 3000:
            self.chapterBrokenUp.append(totalChapter)
        else:




def main():
    app = wx.App()
    ex = MainPage(None, title='Sizing')
    ex.Show()
    app.MainLoop()


main()
