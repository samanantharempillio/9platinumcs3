## Code:

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

song1 = Songs(
    "Ma Meilleure Ennemie",
    "Stromme (feat. Pomme)",
    "Arcan League of Legends: Season 2",
    2024,
    "Pop"
)

song2 = Songs(
    "Style",
    "Hearts2Hearts",
    "Style",
    2025,
    "Kpop"
)
print("Before: ")
print("Song 1:", song1.name, "-", song1.get_status())
print("Song 2:", song2.name, "-", song2.get_status())

print("\nPlaying Song 1...")
song1.play()

print("After: ")
print("Song 1:", song1.name, "-", song1.get_status())
print("Song 2:", song2.name, "-", song2.get_status())



## Diagram                         

                         Songs
                    +-------------+
                    |   Class     |
                    |   Blueprint |
                    +-------------+
                       /       \
                      /         \
                     ↓           ↓

          song1 : Songs             song2 : Songs
+----------------------------+   +----------------------------+
| name = Ma Meilleure Ennemie|   | name = Style               |
| artist = Stromae           |   | artist = Hearts2Hearts     |
| album = Arcane Season 2    |   | album = The Chase           |
| year = 2024                |   | year = 2025                |
| genre = French Pop         |   | genre = K-Pop               |
| is_playing = True          |   | is_playing = False          |
+----------------------------+   +----------------------------+

## Short Analysis : 

### 1. Why did you make your chosen attribute private?

I made "is playing" attribute private because it represents the internal playing state of the song. If other parts of the program could directly change it, they could accidentally change the state of the song. Instead, the play() and pause() methods control whether the song is playing. This makes the object's state more organized and protected.

### 2. Which method changes the state of your object?

The play() and pause() methods change the state of my Songs object. They change the private attribute, "is playing" from False to True, or vice versa. 

### 3. How did your two objects demonstrate that instances are independent?

My two objects, song1 and song2, were created from the same Songs class but had different information. When I called song1.play(), only song1 changed from "Paused" to "Playing". song2 remained "Paused". This shows that each object maintains its own independent state.

### 4. What is the difference between your class diagram and your object diagram?

The class diagram shows the blueprint for the class, Songs, including its attributes, data types, visibility, and methods. The object diagram shows the objects created from that class. The class diagram also describes what objects can have, while the object diagram shows what specific objects actually contain.
