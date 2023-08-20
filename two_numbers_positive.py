def positive_numbers(a, b, c):
    count = 0
    for number in [a, b, c]:
        if number > 0:
            count += 1
    return count == 2

a = int(input("First Number is: "))
b = int(input("Second Number is: "))
c = int(input("Third Number is: "))

print(positive_numbers(a, b, c))