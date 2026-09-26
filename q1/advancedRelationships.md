# Advanced Class Relationships:
## Previous Activities:
 * [classAttributes](classObjectUML.md)
 * [classRelationships](classRelationships.md)

## Existing System Description:
## Inheritance Relationship
Parent: Songs
Child: Instrumental
Explanation: An instrumental inherits all the attributes of a song like genre, artist, album, and year but removes the lyrics sung in the song.

## Inheritance UML
<img width="1414" height="2000" alt="Songs" src="https://github.com/user-attachments/assets/bf8f5191-a85e-446b-ac4a-9872bc29f940" />

## Composition/Agregation

Playlist -contains--> Songs
 
I chose agregation because a Playlist contains Songs objects, but the songs can exist independently from the playlist. A song can be created before being added to a playlist, and the same song object could potentially be used by another playlist. Therefore, the relationship is a weak HAS-A relationship, which matches aggregation.

## Advanced UML Diagram
<img width="1400" height="1700" alt="Songs (1)" src="https://github.com/user-attachments/assets/577d6041-6a31-4f73-87d2-495714ad0942" />

## Python Implementation

class Songs:

    def __init__(self, name, artist, album, year, genre):
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre
        self.__is_playing = False

    def play(self):
        self.__is_playing = True
        print(self.name + " is now playing.")

    def pause(self):
        self.__is_playing = False
        print(self.name + " is now paused.")

    def fast_forward(self, seconds):
        print(self.name + " fast forwarded by", seconds, "seconds.")

    def skip(self):
        print("Skipped " + self.name)

    def get_status(self):
        if self.__is_playing:
            return "Playing"
        else:
            return "Paused"



class Lyrics(Songs):

    def __init__(self, name, artist, album, year, genre, lyrics):
        super().__init__(name, artist, album, year, genre)
        self.lyrics = lyrics

    def display_lyrics(self):
        print("\nLyrics of", self.name + ":")
        print(self.lyrics)


class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def display_songs(self):
        print("Playlist:", self.name)

        for song in self.songs:
            print("-", song.name, "by", song.artist)


song1 = Lyrics(
    "Ma Meilleure Ennemie",
    "Stromae",
    "Arcane Season 2",
    2024,
    "French Pop",
    "Lyrics go here..."
)

song2 = Lyrics(
    "Style",
    "Hearts2Hearts",
    "The Chase",
    2025,
    "K-Pop",
    "Lyrics go here..."
)

song3 = Songs(
    "I'm Like a Lawyer with the Way I'm Always Trying to Get You Off (Me & You)",
    "Fall Out Boy",
    "Infinity on High",
    2007,
    "Pop Punk"
)


playlist1 = Playlist("My Favorites")

playlist1.add_song(song1)
playlist1.add_song(song2)
playlist1.add_song(song3)


print("----------------")

print("Song:", song1.name)
print("Artist:", song1.artist)
print("Album:", song1.album)
print("Genre:", song1.genre)

print()

song1.play()
print("Status:", song1.get_status())
print()

song1.display_lyrics()

print("--------------")

print("Playlist:", playlist1.name)

playlist1.display_songs()

print("\nNumber of songs:", len(playlist1.songs))

print("-------------")

print("Song 1:", song1.name)
print("Song 2:", song2.name)
print("Song 3:", song3.name)

## Test Run
<img width="675" height="525" alt="Screenshot 2026-09-26 at 9 43 51 PM" src="https://github.com/user-attachments/assets/5b76b56d-99cc-4bf0-b1e3-00e2853ae167" />

## Object Diagram
<img width="1920" height="1080" alt="Playlist = My Favorites (1)" src="https://github.com/user-attachments/assets/6c364ab7-fa2d-41f9-b4fa-709217234054" />

## Reflection
### 1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
 - I chose song as the parent class and lyrics as the child class because lyrics are a part of a song that has nearly all it's attributes. Lyrics already needs it's parent class attributes to even exist. It adds the attribute display_lyrics() to provide more specific information about the song. Therefore the relationship between the parent class Songs and child class lyrics follows a IS-A principle.  

### 2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
- inheritance allowed Lyrics to reuse the attributes and methods already defined in the Songs class. Instead of rewriting name, artist, album, year, genre, play(), pause(), and the other methods, Lyrics receives them from Songs. The super().__init__() statement calls the parent constructor to initialize the inherited attributes. This makes the code shorter and avoids unnecessary repetition.

### 3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
- The relationship between Playlist and Songs is aggregation because a playlist contains songs that can exist independently. The songs are created before they are added to the playlist, so the playlist does not own their entire lifecycle.

### 4. What is the difference between Association from Part III and the advanced relationship you implemented?
- Association describes a general relationship between two classes, like a Playlist being connected to Songs. Aggregation is more specific as it describes a whole-part relationship where the whole contains existing objects. In this system, the Playlist contains Songs, but the songs can still exist independently. Therefore, aggregation gives the relationship a more specific meaning than the general association from Part III.

### 5. How does your design follow the DRY principle?
- The design follows the DRY principle by avoiding repeated code between Songs and Lyrics. The common song attributes and methods are defined once in the parent Songs class. Lyrics inherits these features using super().__init__() instead of defining them again. This makes the system easier to maintain because changes to common song behavior can be made in one place.
