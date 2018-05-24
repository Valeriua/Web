print("Task 1")

text = input()

while "." in text:
    print(text.capitalize())
    break
else:
    print(text.capitalize()+".")

print(" ")
print("Task 2")

number = int(input("Enter number: "))

if number % 3 and number % 5:
    print(number)
elif number % 3:
    print("Only 5")
elif number % 5:
    print("Only 3")
else:
    print("Two ways possible")


print(" ")
print("Task 3")

text = input()
lst = ""

for i in text:
    if i.istitle():
        lst += i
    else:
        continue
print(lst)
