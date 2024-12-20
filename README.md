# lab1
# Hotel Revenue Calculator

This project demonstrates a Windows Forms application written in C# that calculates the revenue of a hotel based on the number of occupied and available rooms, as well as the price per room.

## Features
- **User Input:** Input fields for hotel name, occupied rooms, total rooms, and price per room.
- **Revenue Calculation:** Displays the calculated revenue in a message box when the button is clicked.
- **Class Diagram:** Clear separation of responsibilities between the form logic (`Form1`) and the hotel logic (`Hotel` class).

## Screenshots
### User Interface
![Screenshot of the application](screenshot_form.png)

### Class Diagram
![Class Diagram](class_diagram.png)

## Class Overview
### Hotel Class
```plaintext
- String Name
- int allplace
- int ocplace
- decimal price

+ Hotel(Name: String, allplace: int, ocplace: int, price: decimal)
+ GetName() : String
+ GetAllPlace() : int
+ GetOcPlace() : int
+ GetPrice() : decimal
+ revenue() : decimal
```
The `Hotel` class encapsulates the logic for storing and manipulating hotel data.

### Form1 Class
```plaintext
+ Form1()
+ Form1_Load(sender: object, e: EventArgs)
+ button1_Click(sender: object, e: EventArgs)
```
`Form1` serves as the user interface and interacts with the `Hotel` class to perform calculations.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/hotel-revenue-calculator.git
   ```
2. Open the project in Visual Studio.
3. Build and run the project.

## Usage
1. Enter the hotel details in the respective fields:
   - Name
   - Occupied Rooms
   - Total Rooms
   - Price per Room
2. Click the **Calculate Revenue** button.
3. The revenue will be displayed in a message box.

## License
This project is licensed under the MIT License.
