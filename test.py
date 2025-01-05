import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create a status bar
        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetFieldsCount(4)  # Split into 4 parts
        self.status_bar.SetStatusWidths([-1, 100, 100, 150])  # Set relative widths

        # Add a progress bar to the last part
        self.add_progress_bar_to_status_bar()

        # Bind the resize event to dynamically adjust the progress bar's size
        self.Bind(wx.EVT_SIZE, self.on_resize)

        # Initialize progress value
        self.progress = 0

        # Simulate progress updates with a timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(500)  # Update every 500ms

    def add_progress_bar_to_status_bar(self):
        # Create a panel for embedding controls in the status bar
        self.progress_panel = wx.Panel(self.status_bar)
        self.progress_panel.SetBackgroundColour(self.status_bar.GetBackgroundColour())

        # Create a progress bar in determinate mode
        self.progress_bar = wx.Gauge(self.progress_panel, range=100, style=wx.GA_HORIZONTAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.progress_bar, 1, wx.EXPAND | wx.ALL, 1)
        self.progress_panel.SetSizer(sizer)

        # Set the initial position and size of the panel
        self.update_progress_bar_position()

    def update_progress_bar_position(self):
        """Update the position and size of the progress panel based on the status bar field."""
        rect = self.status_bar.GetFieldRect(3)  # Field index 3 (last field)
        self.progress_panel.SetPosition((rect.x, rect.y))
        self.progress_panel.SetSize((rect.width, rect.height))
        self.progress_panel.Layout()

    def on_resize(self, event):
        """Handle window resizing and adjust the progress bar's size."""
        self.update_progress_bar_position()
        event.Skip()  # Ensure the default resize behavior happens

    def on_timer(self, event):
        # Manually update the progress bar
        self.progress = (self.progress + 10) % 101  # Increment progress
        self.progress_bar.SetValue(self.progress)   # Set progress value


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Status Bar with Resizable Progress Bar", size=(600, 400))
        frame.Show()
        return True


if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
