# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can group an item's name, price, and quantity together inside an Item object. The variables can be kept private so that they cannot be changed directly from outside the object. Instead, methods such as setPrice(), setQuantity(), or updateStock() can be used to safely modify the information. This prevents incorrect changes and keeps the inventory data organized.

### 2. Abstraction
Abstraction can be used to create an Item class that represents the important information about each product, such as its name, price, and quantity. Instead of dealing with many individual variables, the program can create multiple Item objects for the different products in the store.

### 3. Inheritance
Encapsulation can group an item's name, price, and quantity together inside an Item object. The variables can be kept private so that they cannot be changed directly from outside the object. Instead, methods such as setPrice(), setQuantity(), or updateStock() can be used to safely modify the information. This prevents incorrect changes and keeps the inventory data organized.

### 4. Polymorphism
Polymorphism allows different types of items to use the same method while performing the action in their own way. For example, a general displayInfo() method could be used for Food, Drinks, and SchoolSupplies, but each type could display different information. The inventory system can therefore treat different products as Item objects while still allowing each product type to behave differently when necessary. This makes the program more flexible and easier to expand.

  
## Reflection
For this specific problem, encapsulation is the most useful of the four pillars. It allows the name, price, and quantity of each product to be grouped together in a single Item object instead of using many separate variables. It also allows the data to be protected and modified through methods such as addItem(), removeItem(), and updateStock(). This makes the inventory system more organized, manageable, and easier to maintain.
