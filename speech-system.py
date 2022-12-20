import Polly_connection

class ToMP3:
    def __init__(self):
        self.client = Polly_connection.PollyClient()

    def FileToMP3(self, inputText="Error, no text found.", bookTitle = "chapter"):
        with self.client as cl:
            output = cl.synthesize_speech(Text=inputText, OutputFormat="mp3", VoiceId='Aditi')

        with open("Audio/" + bookTitle + ".mp3", 'wb') as opened_file:
            opened_file.write(output['AudioStream'].read())

hello = ToMP3()
hello.FileToMP3("some text found!", "chapter 58 - the way to the gate")

print("done")
