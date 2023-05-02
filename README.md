# Royal Road Text to Speech

This systems turns books from the website Royal Road into an mp3 file which can be played outload. It's still in it's basic stages making use of Amazons AWS services and media editting tools which means some basic set-up is needed to use it. I do not own or claim to own any of the books on the website nor am I working for or with the website. please support the website and it's content makers by leaving reviews on their books and checking out the website: https://www.royalroad.com/home .

# install

To install you will need to:
1. clone this project: guide - https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
2. make a account for amazon AWS: guide - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html . Follow this guide to produce a folder containing config and credenials file in user folders. e.g. C:\User\name\.aws.
3. download ffmpg: guide - https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/ or https://github.com/jiaaro/pydub#installation . install to the C:\ file like C:\ffmpeg\bin which holds all the files.
4. run the 'requirements.txt' file included with the project download: using the command promt (type cmd in file explorer in code folder) and run 'pip install -r requirements.txt'. 
5. may need to run (pip install -r requirements.txt --upgrade). Python 3.10 is current default, tested on windows 10 .

once these steps are taken you can run the software by using the bat file 'run royal road TTS.bat'.

please check License.txt for more details on license.

# Interface

![image](https://user-images.githubusercontent.com/74562643/235756382-0aa47d90-6276-481a-8db5-a56bb91d34fc.png)

Home page. Shows some of the books on the Royal Road home page on the left. On the right is the book details.

To read a book select the title on the right then click the chapter on the right. Under that click the Read button. To load pre-saved mp3 file select the Open file button, select the mp3 file and then open it.

To reload the book select Home at the top of the page. To search for a book select the top right text box. write the name of the book press enter.

![image](https://user-images.githubusercontent.com/74562643/235757793-d9181a5f-c855-4dbc-b31d-f1ace62810b1.png)

This will load upto 1000 books that match this. A simple search like 'a' whill cause a  deplay as it searchs so many books. To select the book do the same as main page by selecting the book title. 

To return to the home page, select Home button at the top of the right hand page. 

