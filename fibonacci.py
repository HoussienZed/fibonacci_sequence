# prompting user to enter a number n
n = int(input("Enter a number: "))

starting_point = 0
next_point = 1

# printing fibonacci sequence
print(f"The first n fibonacci sequence is: {
      starting_point}, ", end="")

for i in range(n - 2):
    added_number = starting_point
    starting_point = next_point
    next_point += added_number
    print(f", {starting_point}", end="")
