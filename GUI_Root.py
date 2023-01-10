import wx


class GUI:
    """A user GUI menu to play system commands"""

    def __init__(self):
        self.app = wx.App()

    def __enter__(self):
        return self.app

    def __exit__(self, exc_type, exc_value, traceback):
        print("duck")
        try:
            self.app.destroy()
        except AttributeError:
            pass
