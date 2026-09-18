# SG4 - Understanding Classes and Objects

<img width="1414" height="2000" alt="Class Songs" src="https://github.com/user-attachments/assets/cae16e14-d7f6-4b8c-afed-20b160b2fae4" />

#
## 1. Why did you choose this class?
 I choose songs as my class because it was the most polymorphic thing I could think of at the moment.

## 2. Which property do you think is the most important? Why?
 For me, the Song's name is the most important as it is one of the only properties that helps it be distinguished from other songs.

## 3. Which method do you think is the most useful? Why?
 The play method is the most useful as it allows users to listen to the song.

 

 ## Design Revision :
Changes from my previous design:
  * added a private is_playing attribute to keep track of whether the song is currently playing.
  * kept the original Songs class, properties, and methods while making the methods more functional.

## Public and Private Attributes :
| Attribute    | Visibility | Reason                                                                           |
| ------------ | ---------- | -------------------------------------------------------------------------------- |
| `name`       | Public     |  song's name can be accessed to identify the song.                            |
| `artist`     | Public     |  artist's name can be accessed normally.                                      |
| `album`      | Public     |  album name can be accessed normally.                                         |
| `year`       | Public     |  release year can be accessed when displaying song information.               |
| `genre`      | Public     |  genre can be accessed to describe the song.                                  |
| `is_playing` | Private    |  playing status should be controlled by methods rather than changed directly. |

## Updated UML Diagram :
<img width="1414" height="2000" alt="Class Songs (2)" src="https://github.com/user-attachments/assets/83dda9c2-3d11-42c7-969a-fb48a3dfac0e" />
