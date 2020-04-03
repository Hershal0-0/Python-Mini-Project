from questions import getQuestion

a,b = getQuestion()
print(b)
print(a)
print(a['question'])
print(a['options'])
print(a['answer'])
for i in a['options'].keys():
	print(i,a['options'][i])