import sys
import random

if len(sys.argv) < 4 or len(sys.argv[3]) < 5:
    print("params needed: height width characters")
else:
    height, width, chars, gates = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
    entry = random.randint(2, width - 3)
    entry2 = random.randint(2, width - 3)
    entry3 = random.randint(2, height - 3)

    output_filename = "maze.txt"
    with open(output_filename, "w") as output_file:
        output_file.write(f"{height}x{width}{sys.argv[3]}\n")
        for y in range(height):
            for x in range(width):
                if y == 0 and x == entry:
                    output_file.write(chars[4])
                elif y == height - 1 and x == entry2:
                    output_file.write(chars[3])
                elif 1 <= y <= height - 2 and 1 <= x <= width - 2 and random.randint(0, 99) > 20:
                    output_file.write(chars[1])
                elif y == entry3 and x == width - 1:
                    output_file.write(chars[4])
                else:
                    output_file.write(chars[0])
            output_file.write("\n")

print("good !")