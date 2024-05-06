"""
Hawaii Aloha Q & A 
Ask user if they want to play, if so:
Ask questions of the user about Hawaii.
If receive correct answer, score + 1 
If incorrect - continue to next question (minus one down the road)
Return final score at end of questionnaire game
"""

print()
print('🏝️    Hawaii Question and Answer Game   🏝️'.upper())
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

play = input('Do you want to Play? yes or no? ').lower()

if play != 'yes' :
    print('Ok, maybe we play another time.  🙃')
    quit()
if play == 'yes' : 
    print("Let's Play! 😃")

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
            print(user_inp, 'is correct answer. 🤩')
            print('Score: ', score)
            if idx + 1 == game_len :
                print()
                print('Complete! ')
                if score < 3 : 
                    print(' 🧐 Final Score: ', score, '/', game_len, ' = ', str((score/game_len)*100) + '%  🏝️')
                else :
                    print(' 🤩 Final Score: ', score, '/', game_len, ' = ', str((score/game_len)*100) + '%  🏝️')
                print()

        elif user_inp != a :
            print(user_inp, ' is incorrect answer. 😕')
            if idx + 1 == game_len :
                print()
                print('Complete! ')
                if score < 3 : 
                    print(' 🧐  Final Score: ', score, '/', game_len, ' = ', str((score/game_len)*100) + '%  🏝️')
                else :
                    print('🤩  Final Score: ', score, '/', game_len, ' = ', str((score/game_len)*100) + '%  🏝️')
                print()
          
question_score_user(questions, answers)
