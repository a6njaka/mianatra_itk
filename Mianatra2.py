import wx
import os
import lib_addition_3ch_hor
import load_exo
import random


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 450), style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE)

        self.choice_answer_available = False

        # Load background image
        img_path = os.path.join("images", "A3.png")
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
        tool1 = toolbar.AddTool(wx.ID_ANY, "Tool 1", wx.Bitmap("images/tool1.png"), "Tool 1 tooltip")
        tool2 = toolbar.AddTool(wx.ID_ANY, "Tool 2", wx.Bitmap("images/tool2.png"), "Tool 2 tooltip")

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

        # self.create_static_bitmaps()

        # Add bitmap_sizer at the bottom with a 10-pixel space from StatusBar
        main_sizer.Add(self.bitmap_sizer, 0, wx.ALIGN_CENTER | wx.BOTTOM, 20)

        # Create textCtrl
        self.valiny = wx.TextCtrl(self.home_panel, -1, "", size=(854, -1), style=wx.TE_LEFT | wx.TE_PROCESS_ENTER)
        self.valiny.SetFont(wx.Font(21, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        self.valiny.SetFocus()  # Set initial focus to textCtrl
        self.valiny.Bind(wx.EVT_TEXT_ENTER, self.on_enter_pressed)  # Bind EVT_TEXT_ENTER
        main_sizer.Add(self.valiny, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)

        # Create OK button
        self.ok_button = wx.Button(self.home_panel, -1, "START")
        font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.ok_button.SetFont(font)
        self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok_button)
        main_sizer.Add(self.ok_button, 0, wx.ALIGN_CENTER | wx.BOTTOM, 20)

        self.home_panel.SetSizer(main_sizer)
        self.valiny.Hide()
        self.home_panel.Layout()

        self.Bind(wx.EVT_TOOL, self.OnTool1, tool1)
        self.Bind(wx.EVT_TOOL, self.OnTool2, tool2)

        self.all_exo = {}
        p1 = load_exo.ExoSchedule()
        self.all_exo = p1.all_exo
        self.current_exo_name = ""
        self.exo_list = list(self.all_exo)
        self.exo_done = []
        self.all_exo_completed = False

        self.stage_min = 2
        self.stage_max = 5
        self.stage_rand = False
        self.stage_level = 0
        self.stage_type = "entry"
        self.stage_case_sensitive = False
        self.stage_comment = "Comment"

        self.stage_current_index = None
        self.stage_index_done = []

        self.Show()

    def next_exo(self):
        print("---->>next_exo")
        if self.current_exo_name not in self.exo_list:
            self.current_exo_name = self.get_next_exo_name()
            self.refresh_level_config()

        if self.current_exo_name in self.exo_list:
            if len(self.stage_index_done) <= self.stage_min:
                self.stage_current_index = self.get_exo_next_index()
                print(f"     INDEX = {self.stage_current_index}")
            else:
                self.exo_done.append(self.current_exo_name)
                print(f"     Stage complete")
                self.current_exo_name = self.get_next_exo_name()
                self.refresh_level_config()

    def get_exo_next_index(self):
        print("--->>get_exo_next_index")
        list1 = list(range(len(self.all_exo[self.current_exo_name]["exo"])))
        list2 = self.stage_index_done
        r = self.all_exo[self.current_exo_name]["rand"]
        nd = [x for x in list1 if x not in list2]
        print("     full: ", list1)
        print("     done: ", self.stage_index_done)
        print("     not done: ", nd)
        if len(nd) > 0:
            if r:
                return random.choice(list1)
            else:
                return nd[0]
        else:
            return None

    def get_next_exo_name(self):
        print("-"*100)
        print("--->>get_next_exo_name")
        self.stage_current_index = None
        list1 = self.exo_list
        list2 = self.exo_done

        # TODO: randomize the exo
        r = False
        nd = [x for x in list1 if x not in list2]
        if len(nd) > 0:
            if r:
                return nd[random.choice(list1)]
            else:
                print(f"    --->exo Name: {nd[0]}")
                return nd[0]
        else:
            self.all_exo_completed = True
            return None

    def verify_correctness_all_exo(self):
        print("---->>verify_correctness_all_exo")

    def verify_answer(self):
        print("--->>verify_answer")
        print(f"    --1->>{self.current_exo_name}")
        print(f"    --2->>{self.stage_current_index}")
        # for e in self.all_exo:
        #     print(f"{e}: {self.all_exo[e]}")
        user_answer = self.valiny.GetValue()
        exo_answer = self.all_exo[self.current_exo_name]["exo"][self.stage_current_index]["answer"]
        print(f"    '{user_answer}' VS '{exo_answer}'")
        if f"{user_answer}" == f"{exo_answer}":
            self.stage_index_done.append(self.stage_current_index)
            print("    --->>MARINA")
            return True
        else:
            print("    --->>DISO")
            return False

    def refresh_level_config(self):
        if self.current_exo_name in self.exo_list:
            self.stage_min = self.all_exo[self.current_exo_name]["min"]
            self.stage_max = self.all_exo[self.current_exo_name]["max"]
            self.stage_rand = self.all_exo[self.current_exo_name]["rand"]
            self.stage_level = self.all_exo[self.current_exo_name]["level"]
            self.stage_type = self.all_exo[self.current_exo_name]["type"]
            self.stage_case_sensitive = self.all_exo[self.current_exo_name]["case sensitive"]
            self.stage_comment = self.all_exo[self.current_exo_name]["comment"]

    def create_static_bitmaps(self):
        """Creates StaticBitmaps with red borders and adds them to the bitmap_sizer."""
        img_paths = ["C1.png", "C2.png", "C3.png", "C4.png", "C5.png"]
        self.static_bitmaps = []

        for index, img_path in enumerate(img_paths):
            full_path = os.path.join("images", img_path)
            img = wx.Image(full_path, wx.BITMAP_TYPE_ANY)
            bitmap = wx.Bitmap(img)
            static_bitmap = wx.StaticBitmap(self.home_panel, -1, bitmap)
            static_bitmap.SetMinSize(bitmap.GetSize())
            static_bitmap.Bind(wx.EVT_LEFT_DOWN, self.on_bitmap_click)
            static_bitmap.SetBackgroundColour("red")
            static_bitmap.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            static_bitmap.index = index
            self.static_bitmaps.append(static_bitmap)
            self.bitmap_sizer.Add(static_bitmap, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.choice_answer_available = True

    def hide_static_bitmaps(self):
        """Hides all StaticBitmaps."""
        for static_bitmap in self.static_bitmaps:
            static_bitmap.Hide()
        self.choice_answer_available = False

    def show_static_bitmaps(self):
        """Shows all StaticBitmaps."""
        for static_bitmap in self.static_bitmaps:
            static_bitmap.Show()
        self.choice_answer_available = True

    def test_app(self, level):
        image_data = lib_addition_3ch_hor.get_image(level)

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
        if self.choice_answer_available:
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

    def load_image(self, img_path):
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

    def on_ok_button(self, event):
        # wx.MessageBox(self.ok_button.GetLabel(), "Info", wx.OK | wx.ICON_INFORMATION)
        if self.ok_button.GetLabel() == "START":
            self.ok_button.SetLabel("OK")
            self.verify_correctness_all_exo()
            self.stage_index_done = []
            self.valiny.Show()
            self.home_panel.Layout()
            # Change the background image
            # img_path = os.path.join("images", "A2.png")
            # self.load_image(img_path)
        else:
            self.verify_answer()
        self.next_exo()

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
        wx.MessageBox(f"Vous avez choisi l'image {index + 1}!", "Info", wx.OK | wx.ICON_INFORMATION)
        # Change the border color to red
        clicked_bitmap.SetBackgroundColour("red")
        clicked_bitmap.Refresh()
        self.home_panel.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, "Fianarana")
    app.MainLoop()
