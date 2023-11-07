"""Exercises 2.4 Function Design Recipe"""

__author__ = "Ayaan Adrito"

import math

def even(n: int) -> bool:
    """Determine if n is divisible by 2
    
    >>> even(2)
    true
    >>> even(7)
    false
    """

    return n % 2 == 0

def to_celsius(temp: float) -> float:
    """Convert temp Fahrenheit to Celsius
    
    >>> to_celsius(32)
    0
    >>> to_celsius(50)
    10
    >>> to_celsius(95)
    35
    """
    
    return (temp - 32) / 1.8

def to_kelvin(temp: float) -> float:
    """Convert temp Celsius to Kelvin
    
    >>> to_kelvin(0)
    273.15
    >>> to_kelvin(5)
    278.15
    >>> to_kelvin(13)
    286.15
    """

    return temp + 273.15

def hypotenuse(x: float, y: float) -> float:
    """Calculate hypotenuse from two side lengths x and y
    
    >>> hypotenuse(3, 4)
    5
    >>> to_kelvin(10, 10)
    14.14
    """

    return math.sqrt(x*x + y*y)

def is_hypotenuse(x: float, y: float, z: float) -> float:
    """Determine if lengths x, y, and z can form a right triangle
    
    >>> is_hypotenuse(3, 4, 5)
    True
    >>> is_hypotenuse(6, 8, 10)
    True
    >>> is_hypotenuse(1, 2, 3)
    False
    """
    return math.sqrt(x*x + y*y) == z

def rectangle_permimeter(x: float, y: float) -> float:
    """Calculate perimeter of rectable with x length and y width
    
    >>> is_hypotenuse(1, 2)
    6
    >>> is_hypotenuse(1, 2)
    20
    """

    return (x + y)*2

def triangle_permimeter(x: float, y: float, z: float) -> float:
    """Calculate perimeter of triangle with sides x, y, and z
    
    >>> triangle_permimeter(5, 2, 7)
    14
    >>> triangle_permimeter(1, 6, 3)
    10
    """

    return x + y + z

def area_triangle(x: float, y: float, z: float) -> float:
    """Calculate area of triangle given sides x, y, and z
    
    >>> area_triangle(3, 3, 4)
    10
    """

    s = triangle_permimeter(x, y, z) / 2
    return math.sqrt(s * (s - x) * (s - y) * (s - z))

def factorial(n: int) -> int:
    """Calculate and return factorial of n
    
    >>> factorial(5)
    120
    >>> factorial(12)
    479001600
    """
    result = 1

    for i in range (1, n + 1):
        result *= i
    
    return result

def calculate_slope(A: [float], B: [float]) -> float:
    """Calculate the distance between points A and B
    
    >>> calculate_slope([1, 2], [5, 6])
    1
    >>> calculate_slope([4, 5], [7, 12])
    2.33
    """

    if B[0] - A[0] == 0:
        return math.inf
    else:
        return (B[1] - A[1]) / (B[0] - A[0])

def distance(A: [float], B: [float]) -> float:
    """Calculate the distance between point A and B
    
    >>> distance([4, 5], [7, 12])
    7.62

    >>> distance([7, 3], [2, -19])
    22.56
    """

    return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

def is_absolute(x: float, y: float):
    """Determine if numbers x and y have the same absolute value
    
    >>> is_absolute(-3, 3)
    True
    >>> is_absolute(5, -2)
    False
    """

    return abs(x) == abs(y)

def maximum_minimum(a: float, b: float, x: float, y: float) -> float:
    """Determine the maximum values of the minimums between a, b, and x, y
    
    >>> maximum_minimum(1, 2, 3, 4)
    3
    >>> maximum_minimum(1, 2, 3, 4)
    6
    """

    return max(min(a, b), min(x, y))

def main():
    print(maximum_minimum(6, 12, 9, 2))

if __name__ == "__main__":
    main()