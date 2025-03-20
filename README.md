# calculator-package
adip-calculator-unique
adip-calculator-unique is a Python package designed for performing basic arithmetic operations. Whether you're building a complex application or need a reliable tool for simple mathematical tasks, this package provides the essential functions for everyday calculations.

The package includes five key operations: add, subtract, multiply, divide, and modulo. Each function takes two numerical inputs and returns the corresponding result.

Features
Add: Performs addition of two numbers.
Subtract: Subtracts one number from another.
Multiply: Multiplies two numbers.
Divide: Divides two numbers with error handling for division by zero.
Modulo: Returns the remainder of a division operation.
Installation
Using pip
To install adip-calculator-unique, use the following pip command:

bash
Copy
Edit
pip install adip-calculator-unique
Usage
Below is an example of how to use adip-calculator-unique to perform basic arithmetic operations:

python
Copy
Edit
from adip_calculator_unique import add, subtract, multiply, divide, modulo

# Add two numbers
result_add = add(5, 3)
print(f"5 + 3 = {result_add}")

# Subtract two numbers
result_subtract = subtract(10, 3)
print(f"10 - 3 = {result_subtract}")

# Multiply two numbers
result_multiply = multiply(4, 3)
print(f"4 * 3 = {result_multiply}")

# Divide two numbers
try:
    result_divide = divide(10, 2)
    print(f"10 / 2 = {result_divide}")
except ValueError as e:
    print(e)

# Modulo of two numbers
result_modulo = modulo(10, 3)
print(f"10 % 3 = {result_modulo}")
Functions Available:
add(a: float, b: float) → float
Adds two numbers and returns the sum.

subtract(a: float, b: float) → float
Subtracts the second number from the first and returns the difference.

multiply(a: float, b: float) → float
Multiplies two numbers and returns the product.

divide(a: float, b: float) → float
Divides the first number by the second. Raises a ValueError if attempting to divide by zero.

modulo(a: float, b: float) → float
Returns the remainder when dividing the first number by the second.

Contributing
We welcome contributions to this project. If you encounter any bugs, have suggestions for improvements, or want to enhance the functionality, feel free to fork the repository and submit a pull request.

Steps to contribute:
Fork the repository to your own GitHub account.
Clone your forked repo to your local machine:
bash
Copy
Edit
git clone https://github.com/your-username/adip-calculator-unique.git
Create a new branch:
bash
Copy
Edit
git checkout -b feature/your-feature-name
Make your changes and commit them:
bash
Copy
Edit
git add .
git commit -m "Your commit message"
Push your changes:
bash
Copy
Edit
git push origin feature/your-feature-name
Submit a pull request to the main repository.
CI/CD with GitHub Actions
This project is integrated with GitHub Actions for continuous integration and deployment (CI/CD). Every time a change is pushed to the main branch, the CI pipeline runs tests, builds the package, and automatically deploys it to PyPI. This ensures that all updates are automatically published without manual intervention.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Support
If you encounter any issues or need assistance with the package, please open an issue in the GitHub repository. We will be happy to help resolve any questions or problems you may have.

About this Project
adip-calculator-unique was created to provide a simple, reliable tool for performing basic arithmetic operations in Python. Whether you're working on a larger project or need a quick solution for mathematical calculations, this package is designed to be lightweight and easy to use.
