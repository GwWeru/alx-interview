#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]*(i + 1)
        if i > 1:
            _row = triangle[i - 1]
            for a in range(i - 1):
                row[a] = _row[a - 1]+_row[a]
        triangle.append(row)
    return triangle
x = pascal_triangle(5)
for y in (x):
    print(y)
