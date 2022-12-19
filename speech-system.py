import Polly_connection

class ToMP3:
    def __init__(self):
        self.client = Polly_connection.PollyClient()

    def FileToMP3(self):
        with self.client as cl:
            output = cl.synthesize_speech(Text="Ice lice", OutputFormat="mp3", VoiceId='Aditi')

        with open('speech.mp3', 'wb') as opened_file:
            opened_file.write(output['AudioStream'].read())


hello = ToMP3()
hello.FileToMP3()

print("done")
