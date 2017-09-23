import sys
text = sys.stdin.read ()
print (len(text))
text = text.replace (". ", ". \n" )
print(text)