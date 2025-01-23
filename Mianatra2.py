import wx
import os
import load_exo
import random
import vlc
import re
import time
from datetime import datetime
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
from openpyxl.styles import PatternFill
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class MediaPlayer:
    def __init__(self, panel):
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.is_playing = False
        self.panel = panel

    def play_media(self, file_path):
        if self.is_playing:
            self.player.stop()
            self.is_playing = False

        Media = self.Instance.media_new(file_path)
        self.player.set_media(Media)

        # Get the handle of the panel
        handle = self.panel.GetHandle()
        self.player.set_hwnd(handle)

        # Set video dimensions
        self.player.video_set_aspect_ratio("854:x")

        self.player.play()
        self.is_playing = True
        if re.search("mp3$", file_path) is not None:
            self.panel.Hide()
        else:
            self.panel.Show()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 450), style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE)

        # Change the current working directory
        os.chdir(r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2")
        # os.chdir(r"C:\Users\NJAKA\Mianatra2")

        self.choice_answer_available = False
        self.log_txt_file = "log_exo_itokiana.txt"
        self.log_excel_file = "log_exo_itokiana.xlsx"

        # Load background image
        img_path = os.path.join("images", "orange_ice_mint.jpg")
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
        restart_item = file_menu.Append(wx.ID_ANY, "Restart\tCtrl+R", "Open settings")
        file_menu.Append(wx.ID_ANY, "Settings\tCtrl+S", "Open settings")
        file_menu.Append(wx.ID_EXIT, "Exit\tAlt+F4", "Exit the application")
        menu_bar.Append(file_menu, "&File")

        # Create a help menu
        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "About", "About this application")
        menu_bar.Append(help_menu, "&Help")

        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        # Set the menu bar
        self.SetMenuBar(menu_bar)

        # Create a toolbar
        toolbar = self.CreateToolBar()

        # Add some tools to the toolbar
        tool1 = toolbar.AddTool(wx.ID_ANY, "Tool 1", wx.Bitmap("images/tool1.png"), "Tool 1 tooltip")
        tool2 = toolbar.AddTool(wx.ID_ANY, "Tool 2", wx.Bitmap("images/tool2.png"), "Tool 2 tooltip")

        # Realize the toolbar
        toolbar.Realize()
        self.SetToolBar(toolbar)

        # Create a status bar
        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetFieldsCount(5)  # Split into 4 parts
        self.status_bar.SetStatusWidths([-1, -1, -1, -1, 100])  # Set relative widths

        # Add a progress bar to the last part
        self.add_progress_bar_to_status_bar()
        self.progress_bar.SetValue(0)

        # Create a sizer to layout controls
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add a StaticBitmap for the background
        self.background_staticbitmap = wx.StaticBitmap(self.home_panel, -1, self.background_bitmap)
        main_sizer.Add(self.background_staticbitmap, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10)  # Set proportion to 1 to make it expand

        self.bitmap_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.bitmap_sizer, 0, wx.ALIGN_CENTER | wx.BOTTOM, 20)

        self.video_panel = wx.Panel(self.home_panel, style=wx.SIMPLE_BORDER)
        # self.video_panel.SetMaxSize((854, -1))
        main_sizer.Add(self.video_panel, 1, wx.EXPAND | wx.ALL, 10)

        self.video_panel.Hide()
        # Create textCtrl
        self.valiny = wx.TextCtrl(self.home_panel, -1, "", size=(854, -1), style=wx.TE_LEFT | wx.TE_PROCESS_ENTER)
        self.valiny.SetFont(wx.Font(21, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        self.valiny.SetFocus()  # Set initial focus to textCtrl
        main_sizer.Add(self.valiny, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)

        # Create OK button
        self.ok_button = wx.Button(self.home_panel, -1, "START")
        self.ok_button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.ok_button.SetFont(font)
        main_sizer.Add(self.ok_button, 0, wx.ALIGN_CENTER | wx.BOTTOM, 20)

        self.player = MediaPlayer(self.video_panel)

        self.home_panel.SetSizer(main_sizer)
        self.valiny.Hide()
        # self.create_static_bitmaps()

        self.home_panel.Layout()

        self.Bind(wx.EVT_TOOL, self.OnTool1, tool1)
        self.Bind(wx.EVT_TOOL, self.OnTool2, tool2)
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.valiny.Bind(wx.EVT_TEXT_ENTER, self.on_enter_pressed)
        self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok_button)
        self.background_staticbitmap.Bind(wx.EVT_LEFT_DOWN, self.on_background_click)
        self.Bind(wx.EVT_MENU, self.OnRestart, restart_item)
        self.Bind(wx.EVT_MENU, self.OnSettings, file_menu.FindItemByPosition(1))
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)

        self.all_exo = {}
        self.current_exo_name = ""
        self.exo_done = []
        self.exo_list = []
        self.all_exo_completed = False

        self.stage_min = 2
        self.stage_max = 5
        self.stage_rand = False
        self.stage_level = 0
        self.stage_type = "entry"
        self.stage_case_sensitive = False
        self.stage_library = None
        self.stage_comment = "Comment"

        self.stage_current_index = None
        self.stage_index_done = []

        self.Show()
        self.Maximize()
        self.ok_button.SetFocus()

    @staticmethod
    def unmute_and_set_volume_to_50_percent():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(0, None)
        volume.SetMasterVolumeLevelScalar(0.5, None)
        print("System unmuted and volume set to 50%.")

    def update_log_file(self, text):
        text_list = [text]
        if type(text) is list:
            text_list = text
            text = " | ".join(map(str, text))
        daty = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        try:
            with open(self.log_txt_file, "a") as file:
                file.write(f"{daty} | {text}" + "\n")
        except PermissionError:
            pass

        # Log for excel
        print(f"-->Excel: {text_list}")
        if os.path.isfile(self.log_excel_file):
            book = load_workbook(self.log_excel_file)
            sheet = book.active
        else:
            book = Workbook()
            sheet = book.active
            sheet.append(("Daty", "Marina/Diso", "Fanazarana", "Index", "Fanazavana", "Valiny natao"))
            column_width = {"A": 25, "B": 15, "C": 30, "D": 15, "E": 30, "F": 30}
            for col in column_width:
                sheet.column_dimensions[col].width = column_width[col]
                sheet[f"{col}1"].font = Font(bold=True)
                sheet[f"{col}1"].fill = PatternFill(start_color="00A9E6", fill_type="solid")
        sheet.append([daty] + text_list)
        try:
            book.save(self.log_excel_file)
        except PermissionError:
            pass
        book.close()

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
        rect = self.status_bar.GetFieldRect(4)  # Field index 3 (last field)
        self.progress_panel.SetPosition((rect.x, rect.y))
        self.progress_panel.SetSize((rect.width, rect.height))
        self.progress_panel.Layout()

    def on_resize(self, event):
        """Handle window resizing and adjust the progress bar's size."""
        self.update_progress_bar_position()
        event.Skip()  # Ensure the default resize behavior happens

    def display_exo(self):
        print("---->>display_exo")
        self.valiny.Show()
        self.valiny.SetValue("")
        self.valiny.SetFocus()
        self.home_panel.Layout()
        self.video_panel.Hide()
        self.background_staticbitmap.Show()
        # self.player.player.stop()
        print("    -->>", "image1 : ", type(self.all_exo[self.current_exo_name]['exo'][self.stage_current_index]['image1']))
        print("    -->>", "image2 : ", type(self.all_exo[self.current_exo_name]['exo'][self.stage_current_index]['image2']))
        mp3 = self.all_exo[self.current_exo_name]['exo'][self.stage_current_index]['mp3']
        print("    -->>", "mp3 : ", mp3)
        print("    -->>", "answer : ", self.all_exo[self.current_exo_name]['exo'][self.stage_current_index]['answer'])
        print("    -->>", "text : ", self.all_exo[self.current_exo_name]['exo'][self.stage_current_index]['text'])

        self.load_image(self.all_exo[self.current_exo_name]['exo'][self.stage_current_index]['image1'])
        self.background_staticbitmap.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.play_combined_mp3(mp3)

    def get_exo_index(self):
        print("--->>get_exo_index")
        ret = ""
        list1 = list(range(len(self.all_exo[self.current_exo_name]["exo"])))
        list2 = self.stage_index_done
        r = self.all_exo[self.current_exo_name]["rand"]
        nd = [x for x in list1 if x not in list2]
        print("     full: ", list1)
        print("     done: ", self.stage_index_done)
        print("     not done: ", nd)
        if 0 < len(nd) and len(self.stage_index_done) < self.stage_min:
            if r:
                ret = random.choice(nd)
            else:
                ret = nd[0]
        else:
            ret = None
        self.stage_current_index = ret
        print("     -->index =", ret)

    def get_exo_name(self):
        print("-" * 100)
        print("--->>get_exo_name")
        self.stage_current_index = None
        list1 = self.exo_list
        list2 = self.exo_done
        ret = ""

        try:
            self.progress_bar.SetValue(int(len(self.exo_done) / len(self.exo_list) * 100))
        except ZeroDivisionError:
            pass

        # print(f"     --VS-->>{self.exo_done} VS {self.exo_list}")

        # TODO: randomize the exo
        r = False
        nd = [x for x in list1 if x not in list2]
        if len(nd) > 0:
            if r:
                print(f"     -->exo Name: {nd[0]}")
                tmp_exo_name = nd[random.choice(list1)]
                ret = tmp_exo_name
                self.exo_done.append(ret)
            else:
                print(f"     -->exo Name: {nd[0]}")
                tmp_exo_name = nd[0]
                ret = nd[0]
                self.exo_done.append(ret)
            self.SetStatusText(f"Exercise: {tmp_exo_name} (Level={self.stage_level}, Case={self.stage_case_sensitive})", 1)
        else:
            self.all_exo_completed = True
            print("Completed2")
            self.SetStatusText(f"Exercise: Completed", 1)
            self.display_exo_complete()
            ret = None
        self.current_exo_name = ret
        self.SetStatusText(f"Level: {len(self.exo_done)}/{len(self.exo_list)}", 3)

    def verify_correctness_all_exo(self):
        print("---->>verify_correctness_all_exo")
        new_all_exo = {}
        for exo in self.exo_list:
            try:
                if not len(self.all_exo[exo]["exo"]) == 0:
                    new_all_exo[exo] = self.all_exo[exo]
                    print(f"    -->Correct '{exo}'")
                else:
                    print(f"    -->Removed '{exo}'  -->{new_all_exo[exo]}")

            except KeyError as e:
                print(f"    -->Removed '{exo}' --> {e}")
        self.all_exo = new_all_exo
        self.exo_list = list(self.all_exo)

    def verify_answer(self):
        print("--->>verify_answer")
        print(f"    --1->>{self.current_exo_name}")
        print(f"    --2->>{self.stage_current_index}")
        user_answer = self.valiny.GetValue()
        exo_answer = self.all_exo[self.current_exo_name]["exo"][self.stage_current_index]["answer"]
        print(f"    '{user_answer}' VS '{exo_answer}'")

        match = exo_answer.search(user_answer)
        if f"{user_answer}".strip() == "":
            # self.player.play_media(r"mp3/wrong.mp3")
            time.sleep(1)
        elif match:
            self.valiny.SetValue("")
            self.stage_index_done.append(self.stage_current_index)
            print("    --->>MARINA")
            self.SetStatusText("MARINA !")
            self.valiny.SetValue("")
            self.player.play_media(r"mp3/right.mp3")
            self.load_image(self.all_exo[self.current_exo_name]['exo'][self.stage_current_index]['image2'])
            # self.valiny.Hide()
            self.home_panel.Layout()
            time.sleep(2)
            # self.valiny.Show()
            # self.valiny.Enable(True)
            self.update_log_file(["Marina", self.current_exo_name, self.stage_current_index, self.all_exo[self.current_exo_name]['exo'][self.stage_current_index]['text'], user_answer])

            return True
        else:
            print("    --->>DISO")
            self.SetStatusText("DISO !")
            self.valiny.SetValue("")
            self.player.play_media(r"mp3/wrong.mp3")
            time.sleep(2)
            if self.stage_min < self.stage_max:
                self.stage_min += 1
            self.update_log_file(["Diso", self.current_exo_name, self.stage_current_index, self.all_exo[self.current_exo_name]['exo'][self.stage_current_index]['text'], user_answer])
            return False

    def get_level_config(self):
        print("---->>get_level_config")
        if self.current_exo_name in self.exo_list:
            self.stage_min = self.all_exo[self.current_exo_name]["min"]
            self.stage_max = self.all_exo[self.current_exo_name]["max"]
            self.stage_rand = self.all_exo[self.current_exo_name]["rand"]
            self.stage_level = self.all_exo[self.current_exo_name]["level"]
            self.stage_type = self.all_exo[self.current_exo_name]["type"]
            self.stage_case_sensitive = self.all_exo[self.current_exo_name]["case sensitive"]
            self.stage_library = self.all_exo[self.current_exo_name]["library"]
            self.stage_comment = self.all_exo[self.current_exo_name]["comment"]

            print(f"     ->stage_min: {self.stage_min}")
            print(f"     ->stage_max: {self.stage_max}")
            print(f"     ->stage_rand: {self.stage_rand}")
            print(f"     ->stage_level: {self.stage_level}")
            print(f"     ->stage_type: {self.stage_type}")
            print(f"     ->stage_case_sensitive: {self.stage_case_sensitive}")
            print(f"     ->library: {self.stage_library}")
            print(f"     ->stage_comment: {self.stage_comment}")

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

    def OnSettings(self, event):
        wx.MessageBox("Settings", "Info", wx.OK | wx.ICON_INFORMATION)

    def OnRestart(self, event):
        wx.MessageBox("OnRestart", "Info", wx.OK | wx.ICON_INFORMATION)

    def OnExit(self, event):
        self.Close(True)

    def OnAbout(self, event):
        wx.MessageBox("Fianarana 1.0", "About", wx.OK | wx.ICON_INFORMATION)

    def OnTool1(self, event):
        print("-->OnTool1 Clicked")
        # self.player.play_media(r"D:\SONG\00000\Tsy mankaiza.MP3")
        self.player.play_media(r"D:\Clips\GASY TSARA MIDERA - FIDERANA MANDRAVA SAKANA.mp4")
        self.background_staticbitmap.Hide()
        self.home_panel.Layout()
        self.home_panel.Layout()

    def OnTool2(self, event):
        print("-->OnTool2 Clicked")
        self.player.play_media(r"D:\SONG\00000\Tsy mankaiza.MP3")
        self.video_panel.Hide()

    def load_image(self, img_path):
        if os.path.isfile(img_path):
            new_image = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
            if new_image.GetWidth() > 854:
                new_width = 854
                new_height = int(854 * new_image.GetHeight() / new_image.GetWidth())
                new_image = new_image.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)
            new_bitmap = wx.Bitmap(new_image)
            self.background_staticbitmap.SetBitmap(new_bitmap)
            self.home_panel.Refresh()

        # Bytes_Type
        if type(img_path) is bytes:
            # image_data = lib_addition_3ch_hor.get_image(0)
            image_data = img_path
            wx_image = wx.Image(854, 480)
            wx_image.SetData(image_data)
            wx_bitmap = wx.Bitmap(wx_image)
            self.background_staticbitmap.SetBitmap(wx_bitmap)
            self.home_panel.Refresh()

        # self.SetStatusText("Background image changed.")
        self.home_panel.Layout()

    def load_all_exo(self):
        print("---->>load_all_exo")
        p1 = load_exo.ExoSchedule()
        self.all_exo = p1.all_exo
        self.exo_list = list(self.all_exo)
        self.all_exo_completed = False

    def on_ok_button(self, event):
        print(f"---->>OK_BUTTON")
        # if self.ok_button.GetLabel() == "OK":
        #     self.get_exo()
        if self.ok_button.GetLabel() == "START":
            print("  -->>START")
            self.ok_button.SetLabel("OK")
            self.load_all_exo()
            self.verify_correctness_all_exo()
            self.stage_index_done = []
            self.get_exo_name()
            self.get_level_config()
            self.home_panel.Layout()
            if self.current_exo_name is not None:
                self.get_exo_index()
                if self.stage_current_index is not None:
                    self.display_exo()

        elif self.current_exo_name is None and self.ok_button.GetLabel() != "BRAVO !":
            self.display_exo_complete()
        elif self.ok_button.GetLabel() == "OK":
            if self.verify_answer():
                self.get_exo_index()
            if self.stage_current_index is not None:
                self.display_exo()
            else:
                self.stage_index_done = []
                self.get_exo_name()
                self.get_level_config()
                if self.current_exo_name is not None:
                    self.get_exo_index()
                    if self.stage_current_index is not None:
                        self.display_exo()
        self.SetStatusText(f"Stage {len(self.stage_index_done) + 1}/{self.stage_min} (Max : {self.stage_max})", 2)

    def display_exo_complete(self):
        # TODO: Display Bravo image
        self.ok_button.SetLabel("BRAVO !")
        img_path = os.path.join("images", "Bravo.jpg")
        self.player.play_media(r"mp3/bravo.mp3")
        self.load_image(img_path)
        self.valiny.Hide()
        self.home_panel.Layout()

    def on_background_click(self, event):
        all_mp3 = []
        try:
            files_exist = True
            all_mp3 = self.all_exo[self.current_exo_name]['exo'][self.stage_current_index]['mp3']
            if len(all_mp3) > 0:
                for mp3 in all_mp3:
                    if not os.path.isfile(mp3):
                        files_exist = False
                        break
                if files_exist:
                    self.play_combined_mp3(all_mp3)
        except:
            print(f"MP3 not correct! ---> {all_mp3}")

        # wx.MessageBox("Image Clicked", "Info", wx.OK | wx.ICON_INFORMATION)

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

    @staticmethod
    def play_combined_mp3(mp3_files):
        files_exist = True
        if len(mp3_files) > 0:
            for mp3 in mp3_files:
                if not os.path.isfile(mp3):
                    files_exist = False
                    break
        if files_exist and len(mp3_files) > 0:
            instance = vlc.Instance()
            player = instance.media_player_new()
            media_list = instance.media_list_new()

            for mp3_file in mp3_files:
                media = instance.media_new(mp3_file)
                media_list.add_media(media)

            list_player = instance.media_list_player_new()
            list_player.set_media_player(player)
            list_player.set_media_list(media_list)

            list_player.play()

            # Wait for playback to finish
            while list_player.get_state() != vlc.State.Ended:
                time.sleep(0.1)

            # Close the player after playback
            list_player.stop()
            list_player.release()
            player.release()
            instance.release()
        else:
            print("MP3 not correct!")
            print(f"MP3 not correct! --2-> {mp3_files}")


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, "FIANARANA 1.0")
    app.MainLoop()
