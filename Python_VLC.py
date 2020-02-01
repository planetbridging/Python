import os
os.add_dll_directory(r'C:\\Program Files (x86)\\VideoLAN\\VLC\\')
#os.add_dll_directory(os.getcwd())
import vlc


class Player():
    def __init__(self):
        self._instance = vlc.Instance(['--video-on-top'])
        self._player = self._instance.media_player_new()
        self._player.set_fullscreen(True)
        self.Running = False
        self.PlayerPostion = 0.0

    def play(self, path):
        self.media = self._instance.media_new(path)
        self._player.set_media(self.media)
        self._player.play()
        self.Running = True
        self.playing()
        
    def playing(self):
        while self.Running:
            self.PlayerPostion = self._player.get_position()
            #print(self._player.get_position())
            pass

    def stop(self):
        self._player.stop()

test = "play.mkv"
Spelar = Player()
Spelar.play(test)
print("yay")
