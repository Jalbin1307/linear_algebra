def calc(n):
    sum = 0
    for i in range(n):
        sum += int(input())
    return sum

print("Input the number of values to be added => ")
count = int(input())
while count <= 0:
    print("The number must be greater than zero. =>")
    count = int(input())
print("Sum = ", calc(count))