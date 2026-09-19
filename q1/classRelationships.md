# Class Relationships: Association and Multiplicity

## Previous Work:

  ## Existing Class
  Class: Songs
  Description: Represents individual songs. It stores information like the song name, the artist who sang and/or made it, the album it came from, the year it was released, and which genre it belongs to.
  
  ## New Related Class
  Class: Playlist
  Description: Playlist is simply just a collection of the class Songs that a user may want to listen to.
  
  ## Association
  Relationship: Playlist contains Songs
  Explanation:  Playlist is an object that stores a collection of songs.
        
    
  ## Multiplicity
  Multiplicity: Playlist#1 = 0
  Explanation: The playlist has just been created, so there are no songs yet to be stored in it.
  
  ## UML Class Relationship Diagram

  <img width="1920" height="1080" alt="Playlist" src="https://github.com/user-attachments/assets/e66b47c2-93e4-49f6-bf82-df63563284d3" />

  # Python Implementation :
[classRelationships.py](https://github.com/user-attachments/files/32407648/classRelationships.py)

# Test Run: 
<img width="1920" height="1080" alt="Untitled design" src="https://github.com/user-attachments/assets/15d70b2e-abe4-42a4-a9d0-893a69b60f52" />

# Object Relationship Diagram :
<img width="1920" height="1080" alt="Playlist = My Favorites" src="https://github.com/user-attachments/assets/c07d617a-4f2b-4e3d-bfc3-4c55b4076445" />


## Analysis
### What is the association between your two classes?
The class playlist makes objects that store's objects from the Class Songs.

### What multiplicity did you choose and why?
I chose to give the playlist a multiplicity of 0 as it has yet to store an objects from the class Songs.

### How did you implement the relationship in Python?
I implemented the relationship by creating a songs list inside the Playlist class through the add_song() method which receives a Songs object as a parameter and adds that object to the list.

### Why did you store an object reference instead of copying its data?
I stored an object reference because the playlist should connect directly to the actual Songs object

### If your relationship uses many, why is a list appropriate?
A list is appropriate because one playlist can contain multiple songs. The list stores references to the actual Songs objects and let's users add news songs whenever they want. 
