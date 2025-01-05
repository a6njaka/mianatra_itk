import wx
import os
import load_exo
import random
import vlc
import re


class MediaPlayer:
    def __init__(self):
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.is_playing = False

    def play_media(self, file_path):
        if self.is_playing:
            self.player.stop()
            self.is_playing = False

        Media = self.Instance.media_new(file_path)
        self.player.set_media(Media)

        # Get the handle of the panel

        # Set video dimensions
        self.player.video_set_aspect_ratio("854:x")

        self.player.play()
        self.is_playing = True


njk = MediaPlayer