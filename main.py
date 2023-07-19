def find_modulo_of_large_number(A, B):
    number = 0
    for digit in A:
        number = number * 10 + digit
        number = number % B
    return number
A = list(map(int, input("Enter the elements of A1 (space-separated): ").split()))
B = int(input("Enter the value of B1: "))
output1 = find_modulo_of_large_number(A, B)
print("Output 1:", output1)
