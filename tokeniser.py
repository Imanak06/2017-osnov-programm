import sys
text = sys.stdin.readlines()
e=1

for line in text:
	line = line.replace("."," .").replace(".", " .") 
	token = line.strip().split(' ')
	line = line.strip(' ')
	if line == '':
		continue
	orders = 1 
	print("# sent_id =",e)
	print("# text =", line.strip()) 
	for t in token:
		if t.strip() == '':
			continue
	
		print("%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_" % (orders, t))
		orders = orders + 1
	e=e+1

print()
