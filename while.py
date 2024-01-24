result_break = []
for i in range(1, 10):
    if i == 5:
        break
    result_break.append(i)


count = 0
while True:
    print(count)
    count += 1
    if count >=6:
        break
print("if you love me.")


count = 5
while count < 12:
    print(count)
    count += 2
print("are u okay?")

count = 0
while count < 5:
    count += 1
    if count == 3 :
        continue 
    print(count)
print("kankanwo")




count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("you look so pretty")
