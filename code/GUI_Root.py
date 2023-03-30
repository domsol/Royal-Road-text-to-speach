import wx


class GUI:
    """A user GUI menu to play system commands"""

    def __init__(self):
        """start GUI app using wx"""
        self.app = wx.App()

    def __enter__(self):
        """returns wx app"""
        return self.app

    def __exit__(self, exc_type, exc_value, traceback):
        """destroy wx app if it exists, if doesn't exists (GUI closed) then pass"""
        try:
            self.app.destroy()
        except AttributeError:
            pass
