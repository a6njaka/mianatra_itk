import wx
import cv2
import vlc
import threading


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(1000, 700))

        # Create a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to FIANARANA")

        # Create a menu bar
        menubar = wx.MenuBar()

        # Create the "File" menu
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT, "Exit")
        menubar.Append(fileMenu, "&File")

        # Create the "Help" menu
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT, "About")
        menubar.Append(helpMenu, "&Help")

        self.SetMenuBar(menubar)

        # Create a sizer to center the panels
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Create the Home panel
        home_panel = wx.Panel(self, size=(854, 480))
        home_sizer = wx.BoxSizer(wx.VERTICAL)
        home_panel.SetSizer(home_sizer)

        self.video_display = wx.StaticBitmap(home_panel, size=(640, 480))
        video_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.video_display.SetSizer(video_sizer)
        # video_sizer.Add(self.video_display, 0, wx.ALL | wx.CENTER, 5)


        # Create the Tools panel
        tools_panel = wx.Panel(self, size=(854, 150))
        tools_sizer = wx.BoxSizer(wx.VERTICAL)
        tools_panel.SetSizer(tools_sizer)

        # Create the PreviewNext panel
        preview_next_panel = wx.Panel(tools_panel, size=(854, 50))
        preview_next_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create the Preview and Next buttons
        preview_button = wx.Button(preview_next_panel, label="Preview")
        next_button = wx.Button(preview_next_panel, label="Next")

        # Add the buttons to the PreviewNext panel's sizer
        preview_next_sizer.Add(preview_button, 1, wx.EXPAND | wx.ALL, 5)
        preview_next_sizer.Add(next_button, 1, wx.EXPAND | wx.ALL, 5)

        preview_next_panel.SetSizer(preview_next_sizer)
        tools_sizer.Add(preview_next_panel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10)

        # Add the panels to the main sizer
        sizer.Add(home_panel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10)
        sizer.Add(tools_panel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10)

        self.SetSizer(sizer)
        self.Maximize(True)  # Maximize the window
        self.Centre()

        # Event handlers
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_BUTTON, self.OnPreview, preview_button)
        self.Bind(wx.EVT_BUTTON, self.OnNext, next_button)

    def OnExit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("FIANARANA: Your Personalized Tool", "About FIANARANA", wx.OK | wx.ICON_INFORMATION)

    def OnPreview(self, event):
        self.play_video(r"D:\TMP\cours.mp4")
        # wx.MessageBox("Preview clicked", "Message", wx.OK | wx.ICON_INFORMATION)

    def OnNext(self, event):
        wx.MessageBox("Next clicked", "Message", wx.OK | wx.ICON_INFORMATION)

    def play_video(self, video_path):
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.media = self.Instance.media_new(video_path)
        self.player.set_media(self.media)

        handle = self.video_display.GetHandle()
        self.player.set_hwnd(handle)

        self.player.play()

        thread = threading.Thread(target=self.update_video)
        thread.start()

    def update_video(self):
        while self.player.is_playing():
            frame = self.player.video_get_spu()
            height, width = frame.shape[:2]
            image = wx.Bitmap.FromBuffer(width, height, frame)
            wx.CallAfter(self.video_display.SetBitmap, image)
            wx.CallAfter(self.Refresh)
            cv2.waitKey(30)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, "FIANARANA")
    frame.Show()
    app.MainLoop()
