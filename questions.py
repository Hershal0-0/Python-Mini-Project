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
	{
	'question' : 'What is value of postfix expression 542*+3-?',
	'options' : {'a' : 10 , 'b' : 29 , 'c' : 15 , 'd' : 12},
	'answer' : 'a'
	},
	{
	'question' : 'What is not a prime number?',
	'options' : {'a' : 329 , 'b' : 669 , 'c' : 571 , 'd' : 129},
	'answer' : 'c'
	},
	{
	'question' : 'Suppose a C program has floating constant 1.414, whats the best way to convert this as "float" data type?',
	'options' : {'a' : '(float)1.414' , 'b' : 'float(1.414)' , 'c' : '1.414f or 1.414F', 'd' : 'None of the above'},
	'answer' : 'c'
	},
	{
	'question' : 'What is the value of expression 2**2**3**1',
	'options' : {'a' : 64 , 'b' : 256 , 'c' : 24 , 'd' : 'None of the above'},
	'answer' : 'b'
	},
	{
	'question' : 'In python,what is the value of round(12.5) - round(11.5)?',
	'options' : {'a' : 0 , 'b' : 2 , 'c' : 1 , 'd' : 'Error'},
	'answer' : 'c'
	},
	{
	'question' : "What is output for −raining'. find('z') ?",
	'options' : {'a' : '-1' , 'b' : 'TypeError' , 'c' : "''" , 'd' : 'Not Found'},
	'answer' : 'a'
	},
	{
	'question' : 'What command is used to insert 6 in a list ‘‘L’’ at 3rd position ?',
	'options' : {'a' : 'L.insert(2,5)' , 'b' : 'L.insert(3,6)' , 'c' : 'L.add(3,6)' , 'd' : 'L.append(2,6)'},
	'answer' : 'a'
	},
	{
	'question' : 'All keyworkds in Python are in:',
	'options' : {'a' : 'Uppercase' , 'b' : 'Lowercase' , 'c' : 'Capitalized' , 'd' : 'None of the above'},
	'answer' : 'd'
	},
	{
	'question' : 'Which operator has the highest precedance in python?',
	'options' : {'a' : 'Multiplication', 'b' : 'Exponential' , 'c' : 'Parantheses' , 'd' : 'Integer division'},
	'answer' : 'c'
	},
	{
	'question' : 'What is return type of id function?',
	'options' : {'a' : 'int' , 'b' : 'float' , 'c' : 'bool' , 'd' : 'dict'},
	'answer' : 'a'
	},		
	{
	'question' : 'Select the reserve keyword in python:',
	'options' : {'a' : 'else' , 'b' : 'lambda' , 'c' : 'raise' , 'd' : 'All of the above'},
	'answer' : 'd'
	},	
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},	
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},	
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},	
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},	
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
	{
	'question' : 'What is not a perfect square?',
	'options' : {'a' : 9 , 'b' : 20 , 'c' : 625 , 'd' : 25},
	'answer' : 'b'
	},
]

data = questions_data

def getQuestion():
	global data
	if(len(data) < 1):
		data = questions_data
	question = random.choice(data)
	data.pop(data.index(question))
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