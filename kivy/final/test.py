from questions.questions import getQuestion

def checkForQuiz():
	print("HERE")
	question = getQuestion();
	print(question.get('question'))
	if(input("Enter the correct option : ") == question.get('answer')):
		print('correct')
	else:
		print("Incorrect")

checkForQuiz()