import sys
import random

if len(sys.argv) != 4:
    print("params needed: x y density")
    sys.exit()

x = int(sys.argv[1])
y = int(sys.argv[2])
density = int(sys.argv[3])

output_filename = "plateau.txt"

with open(output_filename, "w") as output_file:
    output_file.write(f"{y}.xo\n")
    for i in range(y):
        for j in range(x):
            output_file.write('x' if random.randint(0, 2 * y) < density else '.')
        output_file.write("\n")

print(f"Output written to {output_filename}")
