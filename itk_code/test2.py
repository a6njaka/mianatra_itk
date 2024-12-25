import wx
import os

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 450))

        # Load background image
        img_path = os.path.join("images", "A1.png")
        self.background_image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
        self.background_bitmap = wx.Bitmap(self.background_image)

        # Create home panel
        self.home_panel = wx.Panel(self, -1)

        # Create a sizer to layout controls
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add a StaticBitmap for the background
        self.background_staticbitmap = wx.StaticBitmap(self.home_panel, -1, self.background_bitmap)
        sizer.Add(self.background_staticbitmap, 1, wx.EXPAND)

        # Create StaticBitmaps
        self.static_bitmaps = []
        for i in range(1, 6):
            img_path = os.path.join("images", f"C{i}.png")
            img = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
            bitmap = wx.Bitmap(img)
            self.static_bitmaps.append(wx.StaticBitmap(self.home_panel, -1, bitmap))

        # Position StaticBitmaps (adjust positions as needed)
        positions = [(50, 50), (200, 50), (350, 50), (500, 50), (650, 50)]
        for i, bitmap in enumerate(self.static_bitmaps):
            bitmap.SetPosition(positions[i])
            sizer.Add(bitmap)

        # Create textCtrl
        self.valiny = wx.TextCtrl(self.home_panel, -1, "", size=(400, -1), style=wx.TE_CENTER)
        self.valiny.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        sizer.Add(self.valiny, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        # Create OK button
        self.ok_button = wx.Button(self.home_panel, -1, "OK")
        self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok_button)
        sizer.Add(self.ok_button, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        self.home_panel.SetSizer(sizer)

        self.Show()

    def on_ok_button(self, event):
        # No need to explicitly reset background as it's handled by the StaticBitmap
        pass

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, "My GUI")
    app.MainLoop()