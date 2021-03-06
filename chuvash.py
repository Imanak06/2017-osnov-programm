import sys

chiw = sys.stdin.readlines()
	
cases = ['ăн','ĕн','нăн','нĕн','а','е','на','не','ра','ре','та','те','че',
'ран','рен','тан','тен','чен','па','пе','пала','пеле','сӑр','сӗр','шӑн','шĕн']
#  1л. -(ă)п/-(ĕ)п/-(ă)м/-(ĕ)м  2л. -ă/ -ĕ 3л. -ĕ 
#ед число: -0 ??? -(ă)н ? (во 2 лице) 
#мн. число: -(ă/ĕ)р (1 и 2 лицо) -ç(ĕ)
number = ['ăп','ĕп','ăм','ĕм','ăр','ĕр','ам','ем','ар','ер','ăн','ĕн','ĕ','тăр','тĕр','ç','чăр','чĕр','сем']

comperetive = ['рах','рех','тарах','терех']

time = ['нӑ','нӗ','кан','кен','ас','ес','ман','мас','мес','ме','мен','ççĕ']

frequency = ['кала','келе']

adverjectper = ['малла','мелле','лă','лĕ','сен','сессӗн','сан','сассӑн']

relative_adj = ['ла','ле']

abst = ['лăх', 'лĕх']

negative = ['м','ма']

verb_pre_future = ['тӑп','тӑн','ть','тпӑр','тӑр','ҫҫӗ','тӗп','тӗн','тпӗр','тӗр']

verb_past_perf = ['рӑм','рӑн','рӗ','рӑмӑр','рӑр','рӗҫ','рӗр']

verb_future = ['ӑп','ӑн','ӗ','ӑпӑр','ӑр','ӗҫ']

for z in chiw:
		
#remove white space from the beginning and eng of the line
	line = z.strip()
	if z.count('\t') != 9:
		print(line) 
		continue	
	
	#print('lalala',line.replace('\n','ba'))
	#print ('zazaza',z.replace('\n','ba'))
	
	line = z.strip().split('\t')
	if len(line[1]) < 3:
		print('\t'.join(line))
		continue
		
	lemma = line[1]
	# apply stemming rules here to lemma variable
	
	#lemma = "тĕпчевçĕсемшĕн"
	if lemma [-3:] in cases:
		lemma = lemma[:-3]

	if lemma [-2:] in cases:
		lemma = lemma[:-2]
	
	# lemma = "хатĕрĕсем"
	# lemma[-3:] =  'сем'
	# lemma[:-3]　= 'хатĕрĕ'
	if lemma[-3:] in number: 
		lemma = lemma[:-3]
	if lemma[-2:] in number: 
		lemma = lemma[:-2]
			
	# lemma = "массăллă"
	if lemma [-2:] in adverjectper:
		lemma = lemma[:-2]
	
	if lemma [-3:] in adverjectper:
		lemma = lemma[:-3]
				
	if lemma [-5:] in adverjectper:
		lemma = lemma[:-5]
		
			
	if lemma [-6:] in adverjectper:
		lemma = lemma[:-6]
			
		# lemma = "тухакан"
	if lemma [-3:] in time:
		lemma = lemma[:-3]
	
	if lemma [-2:] in time:
		lemma = lemma[:-2]
		
	if lemma [-3:] in comperetive:
		lemma = lemma[:-3]
	
	if lemma [-4:] in comperetive:
		lemma = lemma[:-4]	
		
	if lemma [-3:] in abst:
		lemma = lemma[:-3]
	
	if lemma [-4:] in frequency:
		lemma = lemma[:-4]
		
	if lemma [-2:] in relative_adj:
		lemma = lemma[:-2]
		
	if lemma [-2:] in negative:
		lemma = lemma[:-2]
		
	if lemma [-1:] in negative:
		lemma = lemma[:-1]		
		
	if lemma [-1:] in verb_pre_future:
		lemma = lemma[:-1]

	if lemma [-2:] in verb_pre_future:
		lemma = lemma[:-2]		

	if lemma [-3:] in verb_pre_future:
		lemma = lemma[:-3]
		
	if lemma [-4:] in verb_pre_future:
		lemma = lemma[:-4]
				
	if lemma [-2:] in verb_past_perf:
		lemma = lemma[:-2]
		
	if lemma [-3:] in verb_past_perf:
		lemma = lemma[:-3]
		
	if lemma [-5:] in verb_past_perf:
		lemma = lemma[:-5]
		
	if lemma [-1:] in verb_future:
		lemma = lemma[:-1]
		
	if lemma [-2:] in verb_future:
		lemma = lemma[:-2]
		
	if lemma [-4:] in verb_future:
		lemma = lemma[:-4]
		
	line[2] = lemma
	print('\t'.join(line))
	




