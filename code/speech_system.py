import Polly_connection


class ToMP3:
    """class to change text to an mp3 file. saves it to Audio file. uses Boto3 Polly."""

    def __init__(self):
        """load PollyClient on start-up"""
        self.client = Polly_connection.PollyClient()

    def fileToMP3(self, inputText="Issue, Error, no text found.", bookTitle="chapter"):
        """inputted text to mp3 saved as inputted book title."""
        with self.client as cl:
            output = cl.synthesize_speech(Text=inputText, OutputFormat="mp3", VoiceId='Brian')

        with open("../Audio/Holder/" + bookTitle + ".mp3", 'wb') as opened_file:
            opened_file.write(output['AudioStream'].read())
    #  add choice changer - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html
    #  check for failed task - get_speech_synthesis_task - use timer
    #  check what boto3 is already set to and return it

