import wx
import os
from PIL import Image, ImageDraw, ImageFont
import random
import lib_addition_3ch_hor


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 450), style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE)

        # Load background image
        img_path = os.path.join("images", "A1.png")
        self.background_image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)

        # Limit the width of the background image to 800 pixels while maintaining the aspect ratio
        if self.background_image.GetWidth() > 854:
            new_width = 854
            new_height = int(854 * self.background_image.GetHeight() / self.background_image.GetWidth())
            self.background_image = self.background_image.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)

        self.background_bitmap = wx.Bitmap(self.background_image)

        # Create home panel
        self.home_panel = wx.Panel(self, -1)

        # Create a menu bar
        menu_bar = wx.MenuBar()

        # Create a file menu
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_ANY, "Settings", "Open settings")
        file_menu.Append(wx.ID_EXIT, "Exit", "Exit the application")
        menu_bar.Append(file_menu, "&File")

        # Create a help menu
        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "About", "About this application")
        menu_bar.Append(help_menu, "&Help")

        # Set the menu bar
        self.SetMenuBar(menu_bar)

        # Bind the menu items to events
        self.Bind(wx.EVT_MENU, self.OnSettings, file_menu.FindItemByPosition(0))
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)

        # Create a toolbar
        toolbar = self.CreateToolBar()

        # Add some tools to the toolbar
        tool1 = toolbar.AddTool(wx.ID_ANY, "Tool 1", wx.Bitmap("tool1.png"), "Tool 1 tooltip")
        tool2 = toolbar.AddTool(wx.ID_ANY, "Tool 2", wx.Bitmap("tool2.png"), "Tool 2 tooltip")

        # Realize the toolbar
        toolbar.Realize()
        self.SetToolBar(toolbar)

        # Create StatusBar
        self.CreateStatusBar()
        self.SetStatusText("Ready")

        # Create a sizer to layout controls
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add a StaticBitmap for the background
        self.background_staticbitmap = wx.StaticBitmap(self.home_panel, -1, self.background_bitmap)
        main_sizer.Add(self.background_staticbitmap, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10)  # Set proportion to 1 to make it expand

        # Bind click event to the background image
        self.background_staticbitmap.Bind(wx.EVT_LEFT_DOWN, self.on_background_click)

        # Create a horizontal sizer for the StaticBitmaps
        self.bitmap_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create StaticBitmaps with red borders
        img_paths = ["C1.png", "C2.png", "C3.png", "C4.png", "C5.png"]
        self.static_bitmaps = []
        self.messages = [
            "You clicked on image 1!",
            "You clicked on image 2!",
            "You clicked on image 3!",
            "You clicked on image 4!",
            "You clicked on image 5!"
        ]

        for index, img_path in enumerate(img_paths):
            full_path = os.path.join("images", img_path)
            img = wx.Image(full_path, wx.BITMAP_TYPE_ANY)
            bitmap = wx.Bitmap(img)
            static_bitmap = wx.StaticBitmap(self.home_panel, -1, bitmap)
            static_bitmap.SetMinSize(bitmap.GetSize())  # Maintain aspect ratio
            static_bitmap.Bind(wx.EVT_LEFT_DOWN, self.on_bitmap_click)  # Bind click event
            static_bitmap.SetBackgroundColour("red")
            static_bitmap.SetCursor(wx.Cursor(wx.CURSOR_HAND))  # Change cursor to hand
            static_bitmap.index = index  # Store the index for reference
            self.static_bitmaps.append(static_bitmap)
            self.bitmap_sizer.Add(static_bitmap, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        # Add bitmap_sizer at the bottom with a 10-pixel space from StatusBar
        main_sizer.Add(self.bitmap_sizer, 0, wx.ALIGN_CENTER | wx.BOTTOM, 20)

        # Create textCtrl
        self.valiny = wx.TextCtrl(self.home_panel, -1, "", size=(854, -1), style=wx.TE_LEFT | wx.TE_PROCESS_ENTER)
        self.valiny.SetFont(wx.Font(26, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        self.valiny.SetFocus()  # Set initial focus to textCtrl
        self.valiny.Bind(wx.EVT_TEXT_ENTER, self.on_enter_pressed)  # Bind EVT_TEXT_ENTER
        main_sizer.Add(self.valiny, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)

        # Create OK button
        self.ok_button = wx.Button(self.home_panel, -1, "OK")
        font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.ok_button.SetFont(font)
        self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok_button)
        main_sizer.Add(self.ok_button, 0, wx.ALIGN_CENTER | wx.BOTTOM, 20)

        self.home_panel.SetSizer(main_sizer)
        self.home_panel.Layout()

        self.Bind(wx.EVT_TOOL, self.OnTool1, tool1)
        self.Bind(wx.EVT_TOOL, self.OnTool2, tool2)

        self.Show()

    def test_app(self, level):
        image_data = lib_addition_3ch_hor.addition_3ch_hor(level)

        wx_image = wx.Image(854, 480)
        wx_image.SetData(image_data)
        wx_bitmap = wx.Bitmap(wx_image)

        self.background_staticbitmap.SetBitmap(wx_bitmap)
        self.home_panel.Refresh()

    def OnSettings(self, event):
        wx.MessageBox("Settings", "Info", wx.OK | wx.ICON_INFORMATION)

    def OnExit(self, event):
        self.Close(True)

    def OnAbout(self, event):
        wx.MessageBox("Fianarana 1.0", "About", wx.OK | wx.ICON_INFORMATION)

    def OnTool1(self, event):
        # Call the test_app function
        self.test_app(level=0)

        # Hide img_paths and display self.valiny and self.ok_button
        for static_bitmap in self.static_bitmaps:
            static_bitmap.Hide()
        self.valiny.Show()
        self.ok_button.Show()
        self.home_panel.Layout()

    def OnTool2(self, event):
        # Hide self.valiny and self.ok_button, then display img_paths
        self.valiny.Hide()
        self.ok_button.Hide()
        for static_bitmap in self.static_bitmaps:
            static_bitmap.Show()
        self.home_panel.Layout()

    def on_ok_button(self, event):
        # Change the background image
        img_path = os.path.join("images", "A3.png")  # Replace with the desired image path
        new_image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
        # Limit the width of the new image to 800 pixels while maintaining the aspect ratio
        if new_image.GetWidth() > 854:
            new_width = 854
            new_height = int(854 * new_image.GetHeight() / new_image.GetWidth())
            new_image = new_image.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)
        new_bitmap = wx.Bitmap(new_image)
        self.background_staticbitmap.SetBitmap(new_bitmap)
        self.home_panel.Refresh()
        self.SetStatusText("Background image changed.")
        self.home_panel.Layout()

    def on_background_click(self, event):
        wx.MessageBox("Image Clicked", "Info", wx.OK | wx.ICON_INFORMATION)

    def on_enter_pressed(self, event):
        self.on_ok_button(event)
        # self.valiny.SetValue("Mety Tsara")  # Display the message when Enter is pressed

    def on_bitmap_click(self, event):
        # Get the clicked static bitmap
        clicked_bitmap = event.GetEventObject()
        # Get the index of the clicked image
        index = clicked_bitmap.index
        # Display message box with the customized message
        wx.MessageBox(self.messages[index], "Info", wx.OK | wx.ICON_INFORMATION)
        # Change the border color to red
        clicked_bitmap.SetBackgroundColour("red")
        clicked_bitmap.Refresh()
        self.home_panel.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, "My GUI")
    app.MainLoop()