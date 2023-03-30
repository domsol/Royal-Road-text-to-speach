from bs4 import BeautifulSoup
import requests


class scrapper:
    """class to load webpage royal road - https://www.royalroad.com/home"""

    #  need to do links to other webpages such as most popular.
    #  should also do a login. maybe a different class for that however.

    def loadBook(self, webpage=str):
        """Load books content. look to update search methods."""
        soup = BeautifulSoup(requests.get(webpage).text, "lxml")
        # UnboundLocalError issue if book name wrong. issue shouldn't happen with UI but should fine a way to manage
        # error.

        bookTitle = str
        bookWriter = str
        context = str
        links = self.chaptersList(webpage)

        try:
            bookTitle = soup.find("h1", class_="font-white").text
            bookWriter = soup.find("a", class_="font-white").text
            context = soup.find("div", class_="hidden-content").text
        except AttributeError or UnboundLocalError:
            print("no details found for book title or detail. \n")

        if not links:
            print("Error, links not found")
            return False

        return bookTitle, bookWriter, context, links

    @staticmethod
    def HomePageBookLinks():
        """lists all books on front page. need to do the POPULAR THIS WEEK"""
        source = requests.get("https://www.royalroad.com/home").text
        soup = BeautifulSoup(source, "lxml")

        links = []
        for thumb in soup.find_all('div', class_='list-thumb'):  # Thanks Angela
            links.append(thumb.contents[1]['href'])

        return links

    @staticmethod
    def SearchResultBookLinks(search=str):
        """lists all books in search menu. should redo as isn't great"""
        searchInput = ""
        counter = 1
        links = []
        booksFound = True

        for item in search.split(" "):
            searchInput += item + "%20"

        while True:
            if counter > 100:
                print("error, overflowing search result.")
                break

            searchPageLink = ("https://www.royalroad.com/fictions/search?page=" + str(counter) + "&title=" + searchInput)
            source = requests.get(searchPageLink).text
            soup = BeautifulSoup(source, "lxml")
            counter += 1

            booksFound = False

            for thumb in soup.find_all('h2', class_='fiction-title'):  # Thanks Angela
                links.append(thumb.contents[1]['href'])
                booksFound = True

            if not booksFound:
                break

        return links

    @staticmethod
    def chaptersList(webpage):
        """get all the chapters of a book."""
        soup = BeautifulSoup(requests.get(webpage).text, "lxml")
        links = []

        for pointer in soup.find_all("tr", style="cursor: pointer"):
            links.append(pointer["data-url"])

        return links

    @staticmethod
    def loadChapter(webpage):
        """load book chapter details"""
        authorNotes = "No writer notes"

        soup = BeautifulSoup(requests.get(webpage).text, "lxml")
        bookName = soup.find("h2", class_="font-white inline-block").text
        chapterTitle = soup.find("h1", class_="font-white").text
        bookWriter = soup.find("a", class_="font-white").text
        author = soup.find_all("div", class_="portlet-body author-note")
        if len(author) == 1:
            authorNotes = author[0].text
        elif len(author) == 2:
            authorNotes = author[0].text + author[1].text

        context = soup.find("div", class_="chapter-inner chapter-content").text
        context = context.replace('”', '').replace('“', '').replace('"', '').replace("'", "").replace("’", "").\
            replace("‘", "")

        return chapterTitle, bookWriter, context, authorNotes, bookName
