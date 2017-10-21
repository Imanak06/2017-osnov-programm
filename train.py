import sys


lines = sys.stdin.readlines()

count = {}

words = {}

ww = {}

total = 0
#each of lines of input 
for line in lines:
# if no tab ignore and continue
	if '\t' not in line:
		continue
#split line after tab
	row = line.split('\t')
	print(row)
#put tag on 4th row
	tag = row[3]
#if there there is no tag, ignore
	if tag == '_':
		continue
#if tag not find in tag print 0 
	if tag not in count:
		count[tag] = 0
		count[tag] = count[tag] + 1
#put word on 2nd row
	word = row[1]
# if there are no word ????
	if word == '_':
		continue
# if there are no word in ww put 0 but what is +1?
	if word not in ww: 
		ww[word] = 0
#why ww[word]is 0 and at the same time ww[word]= ww[word]+1???
		ww[word] = ww[word] + 1
		words[word] = {}

	if tag not in words[word]:
		words[word][tag] = 0

	words[word][tag] = words[word][tag] + 1
	total = total + 1

print()


for tag in count:
    freq = count[tag]/total
    print(tag, count[tag], freq)


for word in words:
    for tag in words[word]:
        freq = words[word][tag]/ww[word]
        print('%.2f\t%d\t%s\t%s' % (freq, words[word][tag], tag, word))