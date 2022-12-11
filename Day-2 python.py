# prime number has only 2 factor for eg- 2,3,5,7,11
# composite 4,6,8,9,10,12
print("Welcome :)\n")
x = int(input(">>>Enter the lower no: \n"))
y = int(input(">>>Enter the upper no: \n"))
s = 0
g = 0
if x > y:
    c = input("The lower limit cannot be more than the upper limit \nIf you wish to interchange the values type 'Yes' else 'No': ")

    if c == "yes":
        temp = y
        y = x
        x = temp
for i in range(x, y + 1):
    a = i
    c = 0
    for j in range(2, a):
        if a % j == 0:
            c = 1
            s += 1
            print(f"{a} is Composite.")
            break
    if c == 0:
        print(f"{a} is Prime.")
        g += 1
if c == "no":
    pass
else:
    print(f"\nThere are total of {g} prime numbers, and {s} composite numbers in the given range.")
