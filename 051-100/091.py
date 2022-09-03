# returns the square of the distance between two points (x1, y1) and (x2, y2)
def sqr_distance(x1, y1, x2, y2):
    return (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)


# returns True if triangle that is joined to the origin is a right triangle
def is_right_triangle(x1, y1, x2, y2):
    # get squares of sides of triangle
    sides = sorted([sqr_distance(x1, y1, x2, y2), sqr_distance(x1, y1, 0, 0), 
        sqr_distance(0, 0, x2, y2)])

    # assign side length variables
    (a, b, c) = sides

    if a + b == c:
        if a != 0 and b != 0 and c != 0: # check if any points are equal to origin
            return True
    return False


# declare variables
limit = 50
rightTriangles = 0

# main loop
for x1 in range(limit+1):
    for x2 in range(limit+1):
        for y1 in range(limit+1):
            for y2 in range(limit+1):
                # check that we are not double counting triangles
                if y2 - x2 > y1 - x1 and is_right_triangle(x1, x2, y1, y2):
                    rightTriangles += 1

# print result
print(f"Number of right triangles that can be formed: {rightTriangles}")
