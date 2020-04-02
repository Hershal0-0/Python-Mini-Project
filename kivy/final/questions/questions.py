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
	return random.choice(questions_data)
"""
def checkForQuiz():
	question = getQuestion();
	print(question.get('question'))
	if(input("Enter the correct option : ") == question.get('answer')):
		print('correct')
	else:
		print("Incorrect")

"""
#checkForQuiz()

