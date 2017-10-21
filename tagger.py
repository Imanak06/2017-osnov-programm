import sys

fd = open('train.output')
for line in  fd.readlines():
	line = line.strip('\n')
	line = line.split('\t')
	if int(row[1]) > count:
		print(line)
		count= int(line[1])
	print(line)
	
input = sys.stdin.readlines()

for line in input:
	if '\t' not in line:
		continue
	row = line.split('\t')
	x='X'
	row[3]=x
	
	
	print(row)
	
	