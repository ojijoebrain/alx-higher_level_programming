#!/usr/bin/python3
""" Module 12-pascal_triangle.py """


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns  list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for j in range(len(tri) - 1):
            tmp.append(tri[j] + tri[j + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
