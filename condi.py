with open('input.txt', 'r') as input:
	lines = input.readlines()
input.close()

t=[]
s = lines[0].split()
mode = lines[1].split()
print ('mode', mode[0])
print(type(mode[0]))
print (len(mode[0]))
print (mode[0]=='heat')


for i in s:
    t.append(int(i))

a=''

if mode[0] not in ('freeze', 'heat', 'auto', 'fan'):
	a=''
	print('a0 ', a)
elif mode[0] == 'freeze':
	a= str(min(t[0], t[1]))
	print('a1 ', a)
elif mode[0] == 'heat':
	a=str(max(t[0], t[1]))
	print('a2 ', a)
elif mode[0] == 'fan':
	a=str(t[0])
	print('a3 ', a)
elif mode[0] == 'auto':
	a=str(t[1])
	print('a4 ', a)

if abs(t[0]) > 50 or abs(t[1]) > 50 :
	a=''

print(a)
print(t)
print(mode)

with open('output.txt', 'w') as output:
	output.write(a)
	output.close()