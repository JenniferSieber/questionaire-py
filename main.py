"""
Hawaii Aloha Q & A 
Ask questions of the User.
If receive correct response, score + 1 
If incorrect - continue to next question (minus one down the road)
Return Score when Questionnaire is completed
"""

print()
print('Hawaii Question and Answer'.upper())
print('We ask a question, you input your response. \n Receive one point for each correct answer and spelling matters!')
print()

""" Provided lists passed as arguments. Utilize database later """
questions = [
            'How do you say hello in Hawaiian? ',
            'Which island is home to the city of Lahaina? ',
            'How many islands in the state of Hawaii? ',
            'What is the state flower for Hawaii? ',
            'How do you say goodbye in Hawaiian? '
]

answers = [
          'aloha', 
          'maui', 
          '137', 
          'yellow hibiscus', 
          'aloha' 
]


def question_score_user(q_list, a_list): 
    score = 0
    game_len = len(questions)
    for (idx, value) in enumerate(q_list) :
        q = value
        a = a_list[idx]
        print()
        print('Question ', idx + 1)
        user_inp = input(q).lower()
        
        if user_inp == a :
            score += 1
            print(user_inp, 'is correct answer.')
            print('Score: ', score)
            if idx + 1 == game_len :
                print()
                print('Complete! ')
                print('Final Score: ', score, '/', game_len)
                print()

        elif user_inp != a :
            print(user_inp, ' is incorrect answer.')
            if idx + 1 == game_len :
                print()
                print('Complete! ')
                print('Final Score: ', score, '/', game_len)
                print()
          
question_score_user(questions, answers)