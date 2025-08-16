"""
Simple Calculator Program
This module provides basic arithmetic operations with proper
error handling and clean coding style (PEP8 compliant).
"""

from typing import Union


Number = Union[int, float]


def add(x: Number, y: Number) -> Number:
    """Return the sum of two numbers."""
    return x + y


def subtract(x: Number, y: Number) -> Number:
    """Return the difference of two numbers."""
    return x - y


def multiply(x: Number, y: Number) -> Number:
    """Return the product of two numbers."""
    return x * y


def divide(x: Number, y: Number) -> Number:
    """Return the division of two numbers.

    Raises:
        ValueError: If the denominator is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def main() -> None:
    """Demonstrate calculator operations."""
    try:
        num1: float = 10
        num2: float = 5

        print("Addition:", add(num1, num2))
        print("Subtraction:", subtract(num1, num2))
        print("Multiplication:", multiply(num1, num2))
        print("Division:", divide(num1, num2))

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
