#!/usr/bin/python
# coding=UTF-8

#Copyright (c) 2012, Ranveer Raghuwanshi
#All rights reserved.

import win32com.client
import win32gui

ProgID = "Foobar2000.Application.0.7"
foobar_COM_object = win32com.client.Dispatch(ProgID)
playback = foobar_COM_object.Playback

class foobar():

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
                return str(playback.FormatTitle("[%length%]"))


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

        def getCurrentTrack(self):
                if self.isPlaying():
                        track = str(playback.FormatTitle("[%title%]"))
                        if len(track) == 0:
                                return "check metadata"
                        else:
                                return track
                else:
                        return "Check foobar running or not"


        def getCurrentArtist(self):
                if self.isPlaying():
                        artist = str(playback.FormatTitle("[%artist%]"))
                        if len(artist) == 0:
                                return "check metadata"
                        else:
                                return artist
                else:
                        return "Check foobar running or not"
                

        def getCurrentAlbum(self):
                if self.isPlaying():
                        album = str(playback.FormatTitle("[%album%]"))
                        if len(album) == 0:
                                return "check metadata"
                        else:
                                return album
                else:
                        return "Check foobar running or not"
                

        def isCurrentlyPlaying(self):
                return 'Currently playing "{0}" by "{1}"'.format(self.getCurrentTrack(),self.getCurrentArtist())





if __name__ == "__main()__":

        f = foobar()

