def print_multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i * j, end="\t")
        print()

# Example usage
n = 10
print_multiplication_table(n)