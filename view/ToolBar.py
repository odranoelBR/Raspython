import wx


class ToolBar(wx.ToolBar):

    def __init__(self, parent):
        wx.ToolBar.__init__(self, parent)

        self.BackgroundColour = '#0A8B9E'
        self.SetSize([965,50])

        self.sair = self.AddLabelTool(wx.ID_ANY, 'Sair', wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_TOOLBAR, [32,32]))
        self.info = self.AddLabelTool(wx.ID_ANY, 'Info', wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_TOOLBAR, [32,32]))
        self.Realize()

        self.Bind(wx.EVT_TOOL, self.onQuit, self.sair)

        self.anexarEventos()


    def onQuit(self,event):
        self.Close()

    def anexarEventos(self):
        self.Bind(wx.EVT_BUTTON, self.onQuit, self.sair)