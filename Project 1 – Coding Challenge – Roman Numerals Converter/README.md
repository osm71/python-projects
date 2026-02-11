Roman Numerals Converter

Purpose

This project converts decimal numbers (between 1 and 3999) into Roman numerals. The program only converts numbers to Roman numerals and validates user input.

This project is part of my learning journey toward DevOps engineering.

⸻

Problem Statement

Write a Python program that converts a given number into Roman numerals while following these rules:

Roman numerals are represented using seven symbols:

Symbol  Value
I       1
V       5
X       10
L       50
C       100
D       500
M       1000

Numbers are normally written from largest to smallest from left to right.

Subtraction rules apply in the following cases:
	•	I can be placed before V (5) and X (10) to make 4 and 9.
	•	X can be placed before L (50) and C (100) to make 40 and 90.
	•	C can be placed before D (500) and M (1000) to make 400 and 900.


⸻

Program Features
	•	Accepts numbers between 1 and 3999
	•	Validates user input
	•	Handles invalid inputs safely
	•	Runs continuously until the user types exit
	•	Uses functions for clean and maintainable code

⸻

How to Run

python3 roman_numerals_converter.py

⸻

Example Usage

Input       Output
-----       ------
3           III
9           IX
58          LVIII
1994        MCMXCIV

Invalid Inputs:

-8      → Not Valid Input !!!
4500    → Not Valid Input !!!
Ten     → Not Valid Input !!!
Exit    → Exiting the program... Good Bye


⸻

Project Structure

Project 1 – Coding Challenge – Roman Numerals Converter/
│
├── roman_numerals_converter.py
└── README.md


⸻

Technologies Used
	•	Python 3


⸻

Developed as part of Python coding practice and algorithm development.