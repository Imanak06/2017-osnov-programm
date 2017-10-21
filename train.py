import sys


lines = sys.stdin.readlines()

count = {}

words = {}

ww = {}

total = 0

for line in lines:

    if '\t' not in line:
        continue

    row = line.split('\t')
    tag = row[3]
    if tag == '_':
        continue
  
    if tag not in tag_count:
        count[tag] = 0
        
    count[tag] = count[tag] + 1   
    word = row[1]
    if word == '_':
        continue
    if word not in ww: 
        ww[word] = 0
        
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