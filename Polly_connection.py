import boto3

class PollyClient:
  """class that calls polly from boto3 and can be used in a 'with' statement to make sure it shuts down."""

  def __init__(self):
    self.client = boto3.client('polly')

  def __enter__(self):
    return self.client

  def __exit__(self, exc_type, exc_value, traceback):
    self.client.close()