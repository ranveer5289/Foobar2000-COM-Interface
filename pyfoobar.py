#!/usr/bin/python
# coding=UTF-8

# Copyright (c) 2009, Ranveer Raghuwanshi
# All rights reserved.

import win32com.client
import win32gui
import datetime


ProgID = "Foobar2000.Application.0.7"
foobar_COM_object = win32com.client.Dispatch(ProgID)
ClassName = "{E7076D1C-A7BF-4f39-B771-BCBE88F2A2A8}"
playback = foobar_COM_object.Playback


class foobar():


        hwnd = None

        def __init__(self):
               self.hwnd = win32gui.FindWindow(ClassName,None)
                

        def isPlaying(self):
              return playback.IsPlaying

        def play(self):
               playback.Start()

        def stop(self):
               playback.Stop()

        def pauseplay(self):
               playback.Pause()

        def isPaused(self):
              return playback.IsPaused

        def next(self):
               playback.Next()

        def previous(self):
               playback.Previous()

        def playRandom(self):
               playback.Random()

        def seekPosition(self):
               return playback.Position

        def lengthOfTrack(self):
                secs = playback.Length
                return str(datetime.timedelta(seconds = int(secs)))

        def currentVolumeLevel(self):
                return str(playback.Settings.Volume) + "dB"

        def mute(self):
                playback.Settings.Volume = -100

        def setVolumeLevel(self,value):
                '''Set volume level to given value
                   0dB corresponds to MAX_VALUE and -100dB corresponds to MIN_VALUE
                   So, -100 <= value <= 0'''
                playback.Settings.Volume = value

        def currentActivePlaylist(self):
                return str(foobar_COM_object.Playlists.ActivePlaylist.Name)

        def parseWindowTitle(self):
                
                trackinfo = win32gui.GetWindowText(self.hwnd)
                trackinfo = trackinfo.split('@')


                if len(trackinfo) <= 1:
                        return {'track':None,'artist':None}


                try:
                        track,artist,_ = trackinfo

                except ValueError:
                        return {'track':None,'artist':None}
                else:
                        return {'track':track, 'artist':artist}

        def getCurrentTrack(self):

                        track = self.parseWindowTitle()['track']

                        if track is not None:
                                return track
                        else:
                                return "trackname metadata doesn't exist or check if foobar is playing "

        def getCurrentArtist(self):
                        artist = self.parseWindowTitle()['artist']

                        if artist is not None:
                                        return artist
                        else:
                                        return "artist metadata doesn't exist or check if foobar is playing"


        #def getCurrentPlayingAlbum(self):
        #       return self.parseWindowTitle()['album']

        def isCurrentlyPlaying(self):
                return 'Currently playing "{0}" by "{1}"'.format(self.getCurrentTrack(),self.getCurrentArtist())





if __name__ == "__main()__":

        f = foobar()
