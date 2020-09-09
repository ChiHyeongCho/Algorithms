
import re

string = input()

moFrist = re.findall(":-\)", string)
moSecond = re.findall(":-\(", string)

moFristLen = len(moFrist)
moSecondLen = len(moSecond)

if moFristLen == 0 and moSecondLen == 0:
    print("none")

elif moFristLen > moSecondLen:
    print("happy")

elif moFristLen < moSecondLen:
    print("sad")

else:
    print("unsure")