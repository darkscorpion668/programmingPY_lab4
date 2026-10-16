"""Exercise 1: display the two requested number series."""

# Write your solution below.

for a in range(10):
    for b in range(10):
        print("{a},{b}", end= " ")
    print()

for a in range(0, 100, 10):
    for b in range(10):
        print(a + b, end=" ")
    print()

