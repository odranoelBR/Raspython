import wx
import wx.html as html

class HelpWindow(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title,style = wx.NO_BORDER, size=(800, 600))

        toolbar = self.CreateToolBar()
        toolbar.AddLabelTool(1, 'Exit', wx.Bitmap('view/img/close.png'))


        vbox2 = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        help = html.HtmlWindow(self, -1, style=wx.NO_BORDER)
        help.LoadPage('view/help.html')

        vbox2.Add(help, 1, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, self.OnClose, id=1)
        self.Bind(wx.EVT_TOOL, self.OnHelp, id=2)

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)

        self.CreateStatusBar()

        self.Centre()
        self.Show(True)

    def OnClose(self, event):
        self.Close()

    def OnHelp(self, event):
        self.splitter.SplitVertically(self.panelLeft, self.panelRight)
        self.panelLeft.SetFocus()

    def CloseHelp(self, event):
        self.splitter.Unsplit()
        self.panelLeft.SetFocus()

    def OnKeyPressed(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_F1:
            self.splitter.SplitVertically(self.panelLeft, self.panelRight)
            self.panelLeft.SetFocus()
