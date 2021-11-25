import sys

number_of_steps = sys.argv[1]

for i in range(number_of_steps):
    if i == 0:
        continue
    if i > 0:
        print((number_of_steps - i) * " " + i * "#")
print(number_of_steps * "#")

