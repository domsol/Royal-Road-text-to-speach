import boto3


class PollyClient:
    """class that calls polly from boto3 and can be used in a 'with' statement to make sure it shuts down."""

    def __init__(self):
        """load boto3 polly client"""
        self.client = boto3.client('polly')

    def __enter__(self):
        """returns the polly client"""
        return self.client

    def __exit__(self, exc_type, exc_value, traceback):
        """on closing end client"""
        self.client.close()
