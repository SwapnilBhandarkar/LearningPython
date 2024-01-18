class Song:
        """_summary_"""
        def __init__(self, title,duration):
                self.title = title
                self.albums=None
                self.duration=duration    

class Artists:
        """_summary_
        """ 
        def __init__(self,name):
                self.name = name
                self.albums=[]
                self.songs=[]
        def add_album(self,album):
                self.albums.append(album)
        def add_song(self,song):
                self.songs.append(song)
class Album:
        def __init__(self,title,artist):
                self.title=title
                self.artist=artist
                self.tracks=[]
        def add_track(self,song):
                self.tracks.append(song)
                song.album=self #set album to song
class Playlist:
        """_summary_
        """        
        def __init__(self,title) :
                self.title=title
                self.songs=[]
        def add_songs(self,song):
                self.songs.append(song)
a1=Artists('a1')
a2=Artists('a2')
s1=Song('s1',180)
s2=Song('s2',200)
al1=Album("al1","artist1")
al1.add_track(s1)
print(f'{s1}')

                
                
        
                
                  



