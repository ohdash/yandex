with open('input.txt', 'r') as input:
	lines = input.readlines()
input.close()

t=[]
s = lines[0].split()
mode = lines[1]	

for i in s:
    t.append(int(i))

if mode not in ('freeze', 'heat', 'auto', 'fan'):
	a=''
elif mode == 'freeze':
	a= str(min(t[0], t[1]))
elif mode == 'heat':
	a=str(max(t[0], t[1]))
elif mode == 'fan':
	a=str(t[0])
elif mode == 'auto':
	a=str(t[1])

if abs(t[0]) > 50 or abs(t[1]) > 50 :
	a=''

with open('output.txt', 'w') as output:
	output.write(a)
	output.close()