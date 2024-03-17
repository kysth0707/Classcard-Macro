arrkey = """
n
o
f
z
t
b
k
u
e
d
r
j
h
p
v
g
a
m
q
y
l
w
c
i
x
s
"""

arrkey = arrkey.replace('\n','').replace(' ','').lstrip().rstrip()
arrMaybe = "0123456789abcdefghijklmnopqrstuvwxyz"[:len(arrkey)]
arrDict = {}

for key, value in zip(arrkey, arrMaybe):
	print(key, ':', value)
	arrDict[key] = value

print("exit 로 탈출")
while True:
	a = input()
	if a == "exit":
		break

	for txt in a:
		d = arrDict.get(txt)
		print(d if d != None else txt, end='')
	print()
