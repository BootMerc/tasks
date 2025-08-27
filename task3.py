# 1

# def multiplication_table():
#         num = int(input("Enter a number: "))
#         print(f"\nMultiplication Table for {num}:\n")
#         for i in range(1, 11):
#             print(f"{num} x {i} = {num * i}")
# multiplication_table()


#2

# def prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print("Twin primes les than 1000\n")
# for i in range(2, 1000):
#     if prime(i) and prime(i + 2) and i + 2 < 1000:
#         print(f"{i}, {i + 2}")


#3

# def prime_factors(n):
#     print(f"Prime factors of {n} are:")
#     for i in range(2, n + 1):
#         while n % i == 0:
#             print(i)
#             n = n // i
# number = int(input("Enter a number: "))
# prime_factors(number)

#4

# def decimal_to_binary(decimal_num):
#     binary = ""
#     while decimal_num > 0:
#         binary = str(decimal_num % 2) + binary
#         decimal_num = decimal_num // 2
#     return binary
# number = int(input("Enter a decimal number: "))
# result = decimal_to_binary(number)
# print(f"Binary: {result}")

#5

def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"\nPerfect numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if is_perfect(num):
        print(num)

