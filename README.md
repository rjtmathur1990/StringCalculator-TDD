String Calculator TDD Kata
Overview
This repository contains the implementation of the String Calculator following the principles of Test-Driven Development (TDD). The goal of this exercise is to demonstrate how code evolves through incremental development and rigorous testing.

Features
Add Method: A simple method that takes a string of numbers separated by delimiters and returns their sum.
Supports Multiple Numbers: Handles any number of comma-separated values.
Newline Delimiters: Allows mixing commas and newline characters as delimiters.
Custom Delimiters: Supports custom delimiters specified in the format //[delimiter]\n[numbers].
Negative Numbers Handling: Throws an exception if any negative numbers are provided and lists all negative numbers in the error message.
Getting Started
Prerequisites
Python 3.6+
unittest (comes pre-installed with Python)
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/StringCalculator-TDD.git
cd StringCalculator-TDD
Install Dependencies:

No external dependencies are required.
Running the Tests
To ensure all tests pass and the implementation is correct, run the following command in the root directory:

bash
Copy code
python -m unittest discover
This will execute all the tests defined in test_string_calculator.py and validate the add method implementation.

Usage
You can use the StringCalculator class in your own projects. Below is a simple usage example:

python
Copy code
from string_calculator import StringCalculator

calculator = StringCalculator()

result = calculator.add("1,2,3")  # Returns 6
print(result)
TDD Process
This project was developed using the TDD methodology:

Write a Test: Start with the simplest test case.
Run All Tests: Ensure the new test fails (red phase).
Implement the Code: Write the minimal code needed to pass the test (green phase).
Refactor: Clean up the code while ensuring all tests still pass.
Repeat: Continue this cycle for each new feature or improvement.
Contributing
Contributions are welcome! If you have any improvements, bug fixes, or suggestions, feel free to open an issue or submit a pull request.

Steps to Contribute:
Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-name).
Open a pull request.
