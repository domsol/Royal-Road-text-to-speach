import wx
import wx.media

class TestPanel():
    def __init__(self):
        self.Bind(wx.media.EVT_MEDIA_STOP, self.OnMediaStop, self.mediactrl)

    def OnMediaStop(self, evt):
        if self.userWantsToSeek:
            evt.Veto()

if __name__ == '__main__':
    app = wx.App()
    Frame = TestPanel()
    Frame.Show()
    app.MainLoop()