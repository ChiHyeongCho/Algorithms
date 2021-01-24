

import re

text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"

regex = re.compile("에러 1033")

mo = regex.search(text)

if mo != None:
    print(mo.group())

text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber)

text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러\s\d+")
mc = regex.findall(text)
print(mc)
# 출력: ['에러 1122', '에러 1033']

text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."

regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group(1)
num = matchobj.group(2)
fullNum = matchobj.group()
print(areaCode, num)  # 032 232-3245

s = "Aaaaaaaaaaddfdaf"

for i in range(1, len(s)//2 + 1):

    relist = re.sub('(\w{%i})' %i, '\g<1> ', s).split()
    print(relist)


#Trie Class

class Node(object):

    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}
        self.length = 0

class Trie(object):

    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            curr_node.children[char] += 1
        curr_node.data = string

    def serach(self, prefix):

        curr_node = self.head
        count = 0
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]

            else:
                return 0

        return curr_node.length

