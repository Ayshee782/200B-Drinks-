# Input number of drinks
n = int(input())

# Input percentage of orange juice in each drink
percentages = list(map(int, input().split()))

# Calculate average percentage
average = sum(percentages) / n

# Print result with 12 decimal places
print(f"{average:.12f}")
