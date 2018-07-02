import sys

def TOH(n):
	n = int(n)
	a = [100]
	for i in range(0,n):
		a.append(n-i)
	b = [100]
	c = [100]
	while(len(c) != n+1):
		if n%2 == 0:
			if a[-1] < b[-1]:
				b.append(a.pop())
				print("0 1")
			elif a[-1] > b[-1]:
				a.append(b.pop())
				print("1 0")
			else:
				continue
			if a[-1] < c[-1]:
				c.append(a.pop())
				print("0 2")
			elif a[-1] > c[-1]:
				a.append(c.pop())
				print("2 0")
			else:
				continue
			if b[-1] < c[-1]:
				c.append(b.pop())
				print("1 2")
			elif b[-1] > c[-1]:
				b.append(c.pop())
				print("2 1")
			else:
				continue
		else:
			if a[-1] < c[-1]:
				c.append(a.pop())
				print("0 2")
			elif a[-1] > c[-1]:
				a.append(c.pop())
				print("2 0")
			else:
				continue
			if a[-1] < b[-1]:
				b.append(a.pop())
				print("0 1")
			elif a[-1] > b[-1]:
				a.append(b.pop())
				print("1 0")
			else:
				continue
			if b[-1] < c[-1]:
				c.append(b.pop())
				print("1 2")
			elif b[-1] > c[-1]:
				b.append(c.pop())
				print("2 1")
			else:
				continue
	

if __name__ == "__main__":
    TOH(int(sys.argv[1]))