with open('input.txt', 'r') as input:
	lines = input.readlines()
input.close()

t=[]
s = lines[0].split()
mode = lines[1]	
print ('mode', mode)

for i in s:
    t.append(int(i))
if mode not in ('freeze', 'heat', 'auto', 'fan'):
	a=''
	print('a0 ', a)
elif mode == 'freeze':
	a= str(min(t[0], t[1]))
	print('a1 ', a)
elif mode == 'heat':
	a=str(max(t[0], t[1]))
	print('a2 ', a)
elif mode == 'fan':
	a=str(t[0])
	print('a3 ', a)
elif mode == 'auto':
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