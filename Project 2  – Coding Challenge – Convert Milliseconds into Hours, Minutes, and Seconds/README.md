# Milliseconds to Time Converter

## Purpose
This project converts a given number of milliseconds into hours, minutes, and seconds.  
It validates user input and formats the output in a clean, human-readable way.
This project is part of my learning journey toward DevOps engineering.

---

## Problem Statement
Write a Python program that:

- Converts milliseconds to hours, minutes, and seconds.
- Only shows non-zero values in the output (e.g., if hours = 0, it is omitted).
- Ignores fractional milliseconds if the value is over 1000 ms.
- Displays milliseconds directly if the input is less than 1000.

The program should also:

- Validate user input:
  - Accept decimal numbers greater than 0.
  - Warn if input is invalid or less than 1.
- Run continuously until the user types `exit` (case insensitive).

---

## Program Features

- Input validation for numbers and strings  
- Clean, human-readable output  
- Skips 0 values in hours, minutes, or seconds  
- Uses a main function for structure and readability  

---

## How to Run

```bash
python milliseconds_converter.py


⸻

Example Usage

Input       Output
-----       -----------------------
555         just 555 millisecond/s
2001        2 second/s
60011       1 minute/s
122011      2 minute/s 2 second/s
3661011     1 hour/s 1 minute/s 1 second/s
7200011     2 hour/s
7322011     2 hour/s 2 minute/s 2 second/s
-8          Not Valid Input !!!
Ten         Not Valid Input !!!
Exit        Exiting the program... Good Bye


⸻

Project Structure

Project 2  – Coding Challenge – Convert Milliseconds into Hours, Minutes, and Seconds/
│
├── milliseconds_converter.py
└── README.md


⸻
Technologies Used

Python 3
⸻
Author

Developed as part of Python hands-on coding challenges for learning purposes.