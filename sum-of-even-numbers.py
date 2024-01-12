
target = int(input("Enter target number\n"))

even_sum = 0
for number in range(2, target + 1, 2):
    even_sum += number
print(even_sum)