# ADDED: File handling is provided; the geometric calculation remains a task.
INPUT_PATH = "square.in"
OUTPUT_PATH = "square.out"


def minimum_square_area(rectangles):
    # TODO: Find the left, right, bottom and top bounds of both rectangles.
    # TODO: Choose a square side that covers both width and height.
    # TODO: Return the square's area, rather than its side or perimeter.
    raise NotImplementedError("Complete the enclosing-square calculation.")


def main():
    with open(INPUT_PATH, encoding="utf-8") as source:
        rectangles = [tuple(map(int, line.split())) for line in source]

    area = minimum_square_area(rectangles)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as output:
        output.write(str(area) + "\n")


if __name__ == "__main__":
    main()
