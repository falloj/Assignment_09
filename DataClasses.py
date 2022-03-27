#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Modified to add Track class, added methods to CD class to handle tracks
# JFallon, 2022-03-26, Modified to add code to Track class
# JFallon, 2022-03-27, added code to remove track, changed "__tracks" to "__cd_tracks" in __sort_tracks() and get_tracks()
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

class Track():
    """Stores Data about a single Track:

    properties:
        position: (int) with Track position on CD / Album
        title: (str) with Track title
        length: (str) with length / playtime of Track
    methods:
        get_record() -> (str)

    """
    # TODone add Track class code
    # -- Constructor -- #
    # Note:  I changed my code from LAB08_E to hopefully improve it. I tried using a modified 
    # version of my LAB08_E code in Assignment 08, but recieved feedback that it was incorrect
    def __init__(self, position: int, title: str, length: str) -> None: 
    # I modeled the __init__ format for class Track() after the starter code for class CD()
        """Set position, title, and length of new track"""
        #   -- Attributes -- #
        try:
            self.__position = int(position)
            self.__title = str(title)
            self.__length = str(length)
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # Track position
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        self.__positon = value
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        self.__title = value
        
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value):
        self.__length = value

    # -- Methods -- #
    # TODone Add Track class methods
    def __str__(self):
        """Returns Track details as formatted string"""
        return 'Position: {}, Title: {}, Length: {}'.format(self.position, self.title, self.length)

    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""
        return '{},{},{}'.format(self.position, self.title, self.length)


class CD:
    """Stores data about a CD / Album:

    properties:
        cd_id: (int) with CD  / Album ID
        cd_title: (string) with the title of the CD / Album
        cd_artist: (string) with the artist of the CD / Album
        cd_tracks: (list) with track objects of the CD / Album
    methods:
        get_record() -> (str)
        add_track(track) -> None
        rmv_track(int) -> None
        get_tracks() -> (str)
        get_long_record() -> (str)

    """
    # TODone Modify CD class as required
    # -- Constructor -- #
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str, cd_tracks = []) -> None:
        # set cd_tracks = to empty list to make it an optional argument 
        """Set ID, Title and Artist of a new CD Object"""
        #    -- Attributes  -- #
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            self.__cd_tracks = list(cd_tracks)
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be Integer')

    # CD title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')

    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be String!')

    # CD tracks
    @property
    def cd_tracks(self):
        return self.__cd_tracks
    
    @cd_tracks.setter
    def cd_tracks(self, value):
        try:
            self.__cd_tracks = list(value)
        except Exception:
            raise Exception('Tracks should have a list of values!')

    # -- Methods -- #
    def __str__(self):
        """Returns: CD details as formatted string"""
        return '{:>2}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)

    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)

    def add_track(self, track: Track) -> None:
        """Adds a track to the CD / Album


        Args:
            track (Track): Track object to be added to CD / Album.

        Returns:
            None.

        """
        # TODone append track
        # The track must be appended to the list of tracks and passed to CD object as an attribute
        try:
            self.cd_tracks.append(track) # modeled this after example on pg. 253 of text book
        except Exception:
            raise Exception('Sorry, adding that track did not work.')
        
        # TODone sort tracks
        self.__sort_tracks()

    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from Album


        Args:
            track_id (int): ID of track to be removed.

        Returns:
            None.

        """
        # TODone remove track
        # I could not get this part on my own
        # first I was trying to use "remove", but ultimately I peeked at the solution, which gave me idea to use "del"
        try:
            delID = int(track_id) - 1
            del self.cd_tracks[delID] # tracks are sorted when added, so this should work
            print('\nThat track has been removed.\n')
            self.__sort_tracks()
        except Exception:
            raise Exception('Sorry, there was a problem removing that track.')

    def __sort_tracks(self):
        """Sorts the tracks using Track.position. Fills blanks with None"""
        # I changed "__tracks" to "__cd_tracks". I could not get the method to run otherwise.
        n = len(self.__cd_tracks)
        for track in self.__cd_tracks:
            if (track is not None) and (n < track.position):
                n = track.position
        tmp_tracks = [None] * n
        for track in self.__cd_tracks:
            if track is not None:
                tmp_tracks[track.position - 1] = track
        self.__cd_tracks = tmp_tracks

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string):formatted string of tracks.

        """
        # I changed "__tracks" to "__cd_tracks".  I could not get the method to run otherwise.
        self.__sort_tracks()
        if len(self.__cd_tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__cd_tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                result += str(track) + '\n'
        return result

    def get_long_record(self) -> str:
        """gets a formatted long record of the Album: Album information plus track details


        Returns:
            result (string): Formatted information about ablum and its tracks.

        """
        result = self.get_record() + '\n'
        result += self.get_tracks() + '\n'
        return result