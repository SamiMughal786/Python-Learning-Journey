# For loops statement
name="sami ullah"
for i in name:
    print(i)


colors=["Red","Blue","Green","Yellow"]
for color in colors:
    print(color)
    for i in color:
     print(i)

# Example 1: Default range usage
# Syntax: range(stop)
# Starts from 0 by default, stops before 5 (exclusive)
for s in range(5):
    print(s)  # Output: 0 1 2 3 4

# Example 2: Specifying start and stop values
# Syntax: range(start, stop)
# Starts from 10, goes up to 19 (20 is exclusive), adds 1 to each value before printing
for s in range(10, 20):
    print(s + 1)  # Output: 11 12 13 14 15 16 17 18 19 20

# Example 3: Specifying start, stop, and step values
# Syntax: range(start, stop, step)
# Starts from 1, stops before 20, increments by 3
for x in range(1, 20, 3):
    print(x)  # Output: 1 4 7 10 13 16 19


