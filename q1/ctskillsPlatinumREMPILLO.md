# Computational Thinking Exercise: "Smart School Canteen Queue"

### Name: Samantha Maria G. Rempillo
### Section: 9-Platinum
# 
## Step 1: Identify the Big Problem
Main Problem: The canteen's lunch break process is slow and extremely ineficient due to a number of factors like student's taking too long to order,payments and change are manually calculated by the cashier with increases inefficientcy, and there is no available system to monitor food inventory.

## Step 2: Identifying 3 to 4 Sub-problems
1. Students need an organized way to line up and be served in the correct order. The system should keep track of students waiting and identify whose turn it is.

2. The system needs to record the student's selected food items and quantities. It should automatically calculate the total cost instead of requiring the cashier to calculate it manually.

3. The system should accept the amount of money given by the student and automatically calculate the correct change. It should also check if the student has given enough money.

4. The system should keep track of how many of each food item remain. When an item is running low or sold out, the system should notify the canteen staff.

## Step 3: Define Computational Thinking Approaches

| **Sub-Problem**                                  | **CT Skill**                               | **Example Solution**                                                                                                                                          |
| ------------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Managing the student queue                       | Decomposition + Algorithm Design      | Break the queue into steps: add student → assign queue number → serve the first student → remove the student after their order is completed.                  |
| Processing food orders and calculating the total | Abstraction + Algorithm Design        | Store each food item's name and price, then calculate the total using the selected items and their quantities.                                                |
| Processing payment and calculating change        | Algorithm Design + Pattern Recognition | Use the same calculation for every transaction: Change = Payment − Total. If payment is less than the total, ask for additional payment.                  |
| Monitoring food inventory                        | Decomposition + Pattern Recognition    | Track the quantity of each food item and subtract the quantity whenever an item is purchased. Check for patterns such as items repeatedly reaching low stock. |

## Step 4: 
START

Display available food items and their prices

Student enters their queue number

Display food menu

REPEAT
Student selects a food item
Student enters the quantity

Check if enough items are available

IF enough items are available THEN
  Add item cost to total
  Subtract selected quantity from inventory
ELSE
  Display "Item is out of stock"
END IF

 Ask if student wants to order another item

UNTIL student chooses to stop ordering

Display total amount

Ask student to enter payment

WHILE payment < total
 Display "Insufficient payment"
 Ask student to enter additional payment
END WHILE

Calculate change:
    change = payment - total

Display total
Display payment
Display change

Serve the student

Move to the next student in the queue

END

