import sys 

vocab = sys.stdin.readlines()

table = {}

table['а'] = 'a'
table['ă'] = 'ə'
table['б'] = 'b'
table['в'] = 'ʋ'
table['г'] = 'ɡ'
table['д'] = 'd'
table['е'] = 'ɛ'
table['ё'] = 'jo'
table['ӗ'] = 'ɘ'
table['ж'] = 'ʐ'
table['з'] = 'z'
table['и'] = 'i'
table['й'] = 'j'
table['к'] = 'k'
table['л'] = 'l'
table['м'] = 'm'
table['н'] = 'n'
table['о'] = 'o'
table['п'] = 'p'
table['р'] = 'r'
table['с'] = 's'
table['ç'] = 'ɕ'
table['т'] = 't'
table['у'] = 'u'
table['ӳ'] = 'y'
table['ф'] = 'f'
table['х'] = 'χ'
table['ц'] = 'ts'
table['ч'] = 'ʨ'
table['ш'] = 'ʂ'
table['щ'] = 'ɕː'
table['ы'] = 'ɯ'
table['ь'] = 'ʲ'
table['э'] = 'e'
table['ю'] = 'ju'
table['я'] = 'ja'

table['А'] = 'a'
table['Ӑ'] = 'ə'
table['Б'] = 'b'
table['В'] = 'ʋ'
table['Г'] = 'ɡ'
table['Д'] = 'd'
table['Е'] = 'ɛ'
table['Ё'] = 'jo'
table['Ӗ'] = 'ɘ'
table['Ж'] = 'ʐ'
table['З'] = 'z'
table['И'] = 'i'
table['Й'] = 'j'
table['К'] = 'k'
table['Л'] = 'l'
table['М'] = 'm'
table['Н'] = 'n'
table['О'] = 'o'
table['П'] = 'p'
table['Р'] = 'r'
table['С'] = 's'
table['Ҫ'] = 'ɕ'
table['Т'] = 't'
table['У'] = 'u'
table['Ӳ'] = 'y'
table['Ф'] = 'f'
table['Х'] = 'χ'
table['Ц'] = 'ts'
table['Ч'] = 'ʨ'
table['Ш'] = 'ʂ'
table['Щ'] = 'ɕː'
table['Ы'] = 'ɯ'
table['Ь'] = 'ʲ'
table['Э'] = 'e'
table['Ю'] = 'ju'
table['Я'] = 'ja'

for a in vocab:
	a = a.strip()
	if a.count('\t') != 9:
		print(a)
		continue
	line = a.split('\t')
	form = line[1]
	
	for trans in table:
			form = form.replace(trans,table[trans])

	line[9] = form
	
	print('\t'.join(line))


			
