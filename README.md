🧠 Logic Box
Pattern Generator & Number Analyzer

Logic Box is a beginner-friendly, menu-driven Python project created to practice core programming concepts such as loops, conditional statements, user input, type casting, pattern generation, and number analysis.

📌 Project Overview

Logic Box provides two interactive features:

⭐ Pattern Generator — Generates a star pattern based on the number of rows entered by the user.
🔢 Number Analyzer — Analyzes a range of numbers, identifies each number as even or odd, and calculates the total sum.

The program uses a continuous menu, allowing the user to perform multiple operations without restarting the program.

✨ Features

⭐ 1. Pattern Generator

The user enters the required number of rows, and the program generates a right-angled star pattern using nested for loops.

Example
Enter the number of rows for the pattern: 5

Pattern:
*
**
***
****
*****

The outer loop controls the rows, while the inner loop prints the required number of stars in each row.

🔢 2. Number Analyzer

The user enters a starting number and an ending number.

The program:

Checks every number in the selected range.
Identifies whether each number is even or odd.
Calculates the total sum of all numbers in the range.

Example

Enter the start of the range: 1
Enter the end of the range: 5

Number 1 is odd
Number 2 is even
Number 3 is odd
Number 4 is even
Number 5 is odd

Sum of all numbers from 1 to 5 is: 15

🔄 3. Interactive Menu

The program continues running until the user selects the Exit option.

Select an option:

1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

If the user enters an invalid option, the program displays:

Invalid choice. Please enter 1, 2 or 3.

🧠 Python Concepts Used

Concept	                 Purpose

while loop	       Keeps the menu running continuously
for loop	         Processes rows and numbers
Nested for loop	   Generates the star pattern
if-elif-else	     Makes decisions based on conditions
input()	           Takes input from the user
int()	             Converts user input into integers
range()            Generates a sequence of numbers
% operator	       Checks whether a number is even or odd
break	             Stops the program when Exit is selected
Variables	         Store input and calculated values

🔁 Program Flow
                 🧠 LOGIC BOX
                      │
                      ▼
                 Display Menu
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Pattern     Number        Exit
       Generator   Analyzer        │
          │           │             ▼
          ▼           ▼          Program
      Nested Loop  Even/Odd        Ends
                    + Sum
          │           │
          └───────────┘
                │
                ▼
          Return to Menu
          
🎯 Project Objective

The main objective of this project is to understand how basic Python programming concepts can be combined to build an interactive console application.

This project focuses on:

-Programming logic
-Looping skills
-Conditional decision-making
-User input handling
-Basic mathematical operations
-Menu-driven program structure

🛠️ Technologies Used
🐍 Python 3
💻 Python IDLE / Python IDE
📦 No external libraries required

▶️ How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open the project folder.
4. Run the Python file.
5. Select an option from the menu.
6. Enter the required values.
7.Select 3 to exit the program.

Run from Terminal
python py2.py

📸 View Project Output

(<img width="363" height="426" alt="ss" src="https://github.com/user-attachments/assets/05298106-613e-4a6e-92cb-761f914b6d84" />)

▶️ Video Demonstration

🎬 Watch Project Demo

(https://github.com/user-attachments/assets/6f227224-08de-4e6a-9dc3-a3c5148dd4a5)

📂 Project Structure
Logic-Box/
│
├── py2.py
├── README.md
│
├── screenshots/
│   └── output.jpg
│
└── video/
    └── project-demo.mp4
    
📈 Future Improvements

The project can be extended by adding:

⭐ More pattern types
🔢 Prime number checking
🔄 Palindrome number checking
✖️ Factorial calculation
📊 Multiplication tables
🛡️ Better input validation
🖥️ Graphical User Interface (GUI)
👩‍💻 Project Details
Detail	Information
Project Name	Logic Box
Project Type	Python Mini Project
Language	Python
Level	Beginner
Main Features	Pattern Generation & Number Analysis
🌟 Key Learning

Small programs build strong programming logic.

Through Logic Box, I learned how loops, conditions, variables, user input, operators, and basic mathematical operations can work together to create a simple but functional Python application.

🙌 Thank You

Thank you for taking the time to explore Logic Box! 🐍💻✨
