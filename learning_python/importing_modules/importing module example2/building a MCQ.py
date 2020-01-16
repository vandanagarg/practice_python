#building a MCQ
#we need to make a class that going to store the type of questions we want to prompt and the corresponding answers for them
# first we made a class or a question module and import it
#next we will make an array of questions/ and prepare or question prompt structure
#next we have make a function that would run the test array, will put up questions and see if they got the answer right

from question import Question

question_prompts = [
    "What color are apples?\n (a)Red/Green \n (b) Purple \n (c) Orange \n\n",
    "What color are Bananas?\n (a)Teal \n (b) Magenta \n (c) Yellow \n\n",
    "What color are strawberries?\n (a)Yellow \n (b) Red \n (c) Blue \n\n",
]

questions =[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):  # here we want to ask a list of question objects to user/ so we need to loop through all the questions that we need to ask user
#we need to check what user answers and if it is right and we need to keep a track of user points
    score = 0
    for question in questions:  #for each question object inside this questions array we want to do something
        answer = input(question.prompt)  # so we want to ask question nd store its answer
        if answer == question.answer:  #here we are checking if the answer given by user is correct
            score += 1  # if correct increase the score
    print("You got "+ str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)


