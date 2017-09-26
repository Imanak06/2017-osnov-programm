import sys
text = sys.stdin.readlines()
e=1
for line in text:
	print()
	line = line.replace("."," .").replace(".", " .") 
	token = line.strip().split(' ')
	orders = 1 
	print("# sent_id =",e)
	print("# text =", line.strip()) 
	for t in token:
		print("%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_" % (orders, t))
		orders = orders + 1
	e=e+1
	print()
	