import sys

def TOH(n,a=0,b=1,c=2):
	n = int(n)
	if n > 0:
		TOH(n-1,a,c,b)
		print(a,c)
		TOH(n-1,b,a,c)

if __name__ == '__main__':
	TOH(sys.argv[1])