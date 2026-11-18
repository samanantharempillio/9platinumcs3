### 1. Answer the following questions:
  a. What is duck typing, as explained in the video?
      
      * Duck typing is a style of coding in which an object's suitability for an operation is determined by the presence of 
        specific methods and properties, rather than its explicit class or inheritance
  
  b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from 
  the Animal class?
  
      * The Car class needed to have the same method name that the loop calls. This allows Python to execute the method even 
        without inheritance from the Animal class.

### 2. Python Code: 

```python 
#Create the classes Car, Boat, and Drone
class Car:
  def move(self):
    print("The car drives on the road.")

class Boat:
  def move(self):
    print("The boat sails on water.")

class Drone:
  def move(self):
    print("The drone flies in the sky.")

#Create Function
def start_trip(vehicle):
    vehicle.move()

#Create Objects
car = Car()
boat = Boat()
drone = Drone()

#Call Function
start_trip(car)
start_trip(boat)
start_trip(drone)
```
