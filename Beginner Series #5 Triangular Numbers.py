"""
Beginner Series #5 Triangular Numbers
Triangular number is the amount of points that can fill equilateral triangle.

Example: the number 6 is a triangular number because all sides of a triangle has the same amount of points.

Hint!
T(n) = n * (n + 1) / 2,
n - is the size of one side.
T(n) - is the triangular number.
"""

def is_triangular(t):
    return ((1+8*t)**0.5).is_integer()