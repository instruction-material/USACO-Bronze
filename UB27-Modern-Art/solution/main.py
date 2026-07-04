# http://www.usaco.org/index.php?page=viewproblem2&cpid=737


def read_input():
    f = open("art.in")
    text = f.readlines()
    f.close()

    canvas = []
    for i in range(1, len(text)):
        canvas.append(text[i].strip())

    return canvas


# checks if a given color is in the canvas
def is_in_canvas(color):
    for i in range(0, len(canvas)):
        for j in range(0, len(canvas[0])):
            if color == canvas[i][j]:
                return True
    return False


# returns whether color1 is found inside the rectangle of color2
def color_in_rect(color1, color2):
    # find boundaries of color2
    min_row = len(canvas)
    max_row = 0
    min_col = len(canvas[0])
    max_col = 0
    for i in range(0, len(canvas)):
        for j in range(0, len(canvas[0])):
            if canvas[i][j] == color2:
                if i < min_row:
                    min_row = i
                if i > max_row:
                    max_row = i
                if j < min_col:
                    min_col = j
                if j > max_col:
                    max_col = j

    # check if color1 is found inside color2
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if color1 == canvas[i][j]:
                return True
    return False


def main(canvas):
    # check each color and see if it is on top of any other rectangles.
    # if it is, then it cannot have been drawn first.

    num_possible = 0
    for color in range(1, 10):
        color = str(color)
        if is_in_canvas(color):
            could_be_first = True
            for color2 in range(1, 10):
                color2 = str(color2)
                if color2 != color:
                    if color_in_rect(color, color2):
                        could_be_first = False
            if could_be_first:
                num_possible += 1
    return num_possible


def write_output(num_possible):
    f = open("art.out", "w")
    f.write(str(num_possible) + "\n")
    f.close()


canvas = read_input()
num_possible = main(canvas)
write_output(num_possible)
