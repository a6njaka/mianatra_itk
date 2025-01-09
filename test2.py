import vlc
import time


def play_combined_mp3(mp3_files):
    # Create an instance of the VLC media player
    instance = vlc.Instance()
    player = instance.media_player_new()

    # Create a media list
    media_list = instance.media_list_new()

    # Add each MP3 file to the media list
    for mp3_file in mp3_files:
        media = instance.media_new(mp3_file)
        media_list.add_media(media)

    # Create a list player
    list_player = instance.media_list_player_new()
    list_player.set_media_player(player)
    list_player.set_media_list(media_list)

    # Start playing
    list_player.play()

    # Keep the player running (optional)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        list_player.stop()


# Example usage:
mp3_files = [r"D:\Njaka_Project\Mianatra_Itk\mp3\right.mp3",
             r"D:\Njaka_Project\Mianatra_Itk\mp3\wrong.mp3",
             r"D:\Njaka_Project\Mianatra_Itk\mp3\bravo.mp3"]
play_combined_mp3(mp3_files)
