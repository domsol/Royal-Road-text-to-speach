from bs4 import BeautifulSoup
import requests

class scrapper():
    """class to load webpage royal road - https://www.royalroad.com/home"""

    #  need to do links to other webpages such as most popular.
    #  should also do a login. maybe a different class for that however.

    def HomePageBookLinks(self):
        """lists all books on front page. need to do the POPULAR THIS WEEK"""
        source = requests.get("https://www.royalroad.com/home").text
        soup = BeautifulSoup(source, "lxml")

        links = []
        for thumb in soup.find_all('div', class_='list-thumb'):  # Thanks Angela
            links.append(thumb.contents[1]['href'])

        return links

    def chaptersList(self, webpage):
        """get all the chapters of a book."""
        soup = BeautifulSoup(requests.get(webpage).text, "lxml")
        links = []

        for pointer in soup.find_all("tr", style="cursor: pointer"):
            links.append(pointer["data-url"])

        return links

    def loadBook(self, webpage):
        """Load books content. look to update search methods."""
        soup = BeautifulSoup(requests.get(webpage).text, "lxml")
        # UnboundLocalError issue if book name wrong. issue shouldn't happen with UI but should fine a way to manage
        # error.

        bookTitle, bookWriter, context = self.bookDetails(webpage)
        links = self.chaptersList(webpage)

        try:
            bookTitle = soup.find("h1", class_="font-white").text
            bookWriter = soup.find("a", class_="font-white").text
            context = soup.find("div", class_="hidden-content").text
        except AttributeError or UnboundLocalError:
            print("no details found for book title or detail. \n")

        if not links:
            return False

        return bookTitle, bookWriter, context, links

    def loadChapter(self, webpage):
        """load book chapter."""
        aurtherNotes = ""

        soup = BeautifulSoup(requests.get(webpage).text, "lxml")

        bookTitle = soup.find("h1", class_="font-white").text
        bookWriter = soup.find("a", class_="font-white").text
        aurther = soup.find_all("div", class_="portlet-body author-note")
        if len(aurther) == 1:
            aurtherNotes = aurther[0].text
        elif len(aurther) == 2:
            aurtherNotes = aurther[0].text + aurther[1].text

        context = soup.find("div", class_="chapter-inner chapter-content").text

        return(bookTitle, bookWriter, aurtherNotes, context)

gold = scrapper()
print(gold.loadChapter("https://www.royalroad.com/fiction/36735/the-perfect-run/chapter/569531/2-story-branching"))
