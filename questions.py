import random

questions_data = [
	{
	'question' : 'What year it is today?',
	'options' : {'a' : 2009 , 'b' : 2002 , 'c' : 2015 , 'd' : 2020},
	'answer' : 'd'
	},
	{
	'question' : 'What is cube of 9?',
	'options' : {'a' : 729 , 'b' : 1000 , 'c' : 2132 , 'd' : 2020},
	'answer' : 'a'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},

]

def getQuestion():
	question = random.choice(questions_data)
	return question
	#,questions_data.index(question)


"""
options = []
value = "No"
question = "What year it is today?"
for i in questions_data:
	if question in i.values():
		value = "YES"
		for j in i['options'].values():
			options.append(j)

print(options)
print(value)"""