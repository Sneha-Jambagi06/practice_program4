import sys
numbers = list(map(int, sys.argv[1:]))
even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Total numbers: {len(numbers)}")
print(f"Even count: {even}")
print(f"Odd count: {odd}")
