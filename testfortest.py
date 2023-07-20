# Make a thing that tests itself. 

# Request characteristic and the return will be a students name. 

# get user input. 

# Compare input to options in a dictionary I guess. 

students = {
    'the best':'Sonne',
    'schmitty':'Seth',
    'questions':'Diego'
}

class GuessWho:
    def inputTest():
        # Make sure we're using a dictionary
        if str(type(students)) == "<class 'dict'>":
            print('Dict Good: 1/4')
        else:
            print('Not dictionary')

        if students['questions'] == 'Diego':
            print('Retrieval Good: 2/4')
        else:
            print('Dictionary not working')
            print(students)

    def ask(studentDict):
        # Make sure input is string
        userAttr = input("Describe the camper: ")
        if str(type(userAttr)) == "<class 'str'>":
            print('String Good: 3/4')
        else:
            print('Input not string')
        # Make suure input is a key in dict. 
        if userAttr in studentDict:
            print('Dict contains Key: 4/4')
            print(students[userAttr])
        else:
            print('attribute not in dictionary')


GuessWho.inputTest()
while True:
    GuessWho.ask(students)






