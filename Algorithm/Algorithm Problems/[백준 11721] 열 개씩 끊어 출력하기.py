

string = input()
number = 0

for i in string:

    number += 1

    if number == 11:
        print()
        print(i, end = "")
        number = 1

    else:
        print(i, end = "")
