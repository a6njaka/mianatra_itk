import wx
import cv2
import vlc
import threading
from PIL import Image, ImageDraw

class MediaPlayer:
    def __init__(self, panel):
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.is_playing = False
        self.panel = panel  # Reference to the panel

    def play_media(self, file_path):
        if self.is_playing:
            self.player.stop()
            self.is_playing = False

        Media = self.Instance.media_new(file_path)
        self.player.set_media(Media)

        # Get the handle of the panel
        handle = self.panel.GetHandle()
        self.player.set_hwnd(handle)

        self.player.play()
        self.is_playing = True


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

        # Create a toolbar
        toolbar = self.CreateToolBar()

        # Add some tools to the toolbar
        tool1 = toolbar.AddTool(wx.ID_ANY, "Tool 1", wx.Bitmap("tool1.png"), "Tool 1 tooltip")
        tool2 = toolbar.AddTool(wx.ID_ANY, "Tool 2", wx.Bitmap("tool2.png"), "Tool 2 tooltip")

        # Realize the toolbar
        toolbar.Realize()

        # Create a sizer to center the panels
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Create the Home panel
        self.home_panel = wx.Panel(self, size=(854, 480))
        home_sizer = wx.BoxSizer(wx.VERTICAL)
        self.home_panel.SetSizer(home_sizer)

        self.video_display = wx.StaticBitmap(self.home_panel, size=(640, 480))
        video_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.video_display.SetSizer(video_sizer)
        # video_sizer.Add(self.video_display, 0, wx.ALL | wx.CENTER, 5)
        self.player = None

        self.player2 = MediaPlayer(self.home_panel)


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
        sizer.Add(self.home_panel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10)
        sizer.Add(tools_panel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10)

        self.SetSizer(sizer)
        self.Maximize(True)  # Maximize the window
        self.Centre()

        # Event handlers
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_BUTTON, self.OnPreview, preview_button)
        self.Bind(wx.EVT_BUTTON, self.OnNext, next_button)
        self.Bind(wx.EVT_TOOL, self.OnTool1, tool1)
        self.Bind(wx.EVT_TOOL, self.OnTool2, tool2)

    def OnTool1(self, event):
        print("Tool 1 clicked")

    def OnTool2(self, event):
        print("Tool 2 clicked")

    @staticmethod
    def play_mp3_vlc(file_path):
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(file_path)
        player.set_media(Media)
        player.play()

    def OnPreview(self, event):
        # self.player2.play_media(r"D:\SONG\00000\Tsy mankaiza.MP3")
        # self.player2.play_media(r"E:\Clips\D-LAIN - MISENGE (Official Music Video 2021).mp4")
        image_bitmap = self.load_image(r"D:\Njaka_Project\Mianatra_Itk\test.png")

        # Clear the previous image from the sizer (optional)
        self.home_panel.GetSizer().Clear(True)

        # Add the image bitmap to the home_panel's sizer
        self.home_panel.GetSizer().Add(image_bitmap, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        # Update the layout to display the image
        self.home_panel.Layout()
        self.Layout()

    def OnExit(self, event):
        self.Close()

    def load_image(self, filename):
        bitmap = wx.Bitmap(filename, wx.BITMAP_TYPE_ANY)
        static_bitmap = wx.StaticBitmap(self.home_panel, bitmap=bitmap)
        return static_bitmap

    def OnAbout(self, event):
        wx.MessageBox("FIANARANA: Your Personalized Tool", "About FIANARANA", wx.OK | wx.ICON_INFORMATION)



    # def OnPreview(self, event):
    #     # self.play_video(r"D:\TMP\cours.mp4")
    #     image_bitmap = self.load_image(r"D:\Njaka_Project\Mianatra_Itk\test.png")
    #     image_bitmap.SetPosition((10, 10))
    #     print("NJK")
    #     # wx.MessageBox("Preview clicked", "Message", wx.OK | wx.ICON_INFORMATION)

    def OnNext(self, event):
        # Clear the previous content from the sizer
        # self.home_panel.GetSizer().Clear(True)
        #
        # # Stop the current video if it's playing
        # if self.player and self.player.is_playing():
        #     self.player.stop()
        #
        # # Play the new video
        # self.play_video(r"D:\TMP\cours.mp4")
        #
        # # Add the video display to the sizer
        # self.home_panel.GetSizer().Add(self.video_display, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        #
        # # Update the layout
        # self.home_panel.Layout()
        # self.Layout()
        self.display_pil_image()

    def display_pil_image(self):
        # Create a new PIL Image (red background)
        pil_image = Image.new('RGB', (100, 50), color=(255, 0, 0))

        # Convert PIL Image mode to 'RGB' if necessary
        pil_image = pil_image.convert('RGB')  # Ensure RGB mode for wxPython

        # Get image data as a list of bytes
        image_data = pil_image.tobytes()

        # Create a wx.Image from the bytes
        wx_image = wx.Image(pil_image.width, pil_image.height)
        wx_image.SetData(image_data)  # Use SetData instead of CopyFromBuffer

        # Create a wx.Bitmap from the wx.Image
        wx_bitmap = wx.Bitmap(wx_image)

        # Clear the panel and add the bitmap to the sizer
        self.home_panel.GetSizer().Clear(True)
        # self.home_panel.GetSizer().Add(wx_bitmap, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        static_bitmap = wx.StaticBitmap(self.home_panel, wx.ID_ANY, wx_bitmap)
        self.home_panel.GetSizer().Add(static_bitmap, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        # Update the layout
        self.home_panel.Layout()
        self.Layout()

    def play_video(self, video_path):
        # self.Instance = vlc.Instance()
        # self.player = self.Instance.media_player_new()
        # self.media = self.Instance.media_new(video_path)
        # self.player.set_media(self.media)
        #
        # handle = self.video_display.GetHandle()
        # self.player.set_hwnd(handle)
        #
        # self.player.play()
        #
        # thread = threading.Thread(target=self.update_video)
        # thread.start()
        if self.player is None:
            self.Instance = vlc.Instance()
            self.player = self.Instance.media_player_new()

            # Update the media source for the existing player
        self.media = self.Instance.media_new(video_path)
        self.player.set_media(self.media)

        handle = self.video_display.GetHandle()
        self.player.set_hwnd(handle)

        self.player.play()


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
