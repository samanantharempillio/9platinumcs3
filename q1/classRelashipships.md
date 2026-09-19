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
