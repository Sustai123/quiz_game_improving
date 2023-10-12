#! /usr/bin/python3
def check_question(level, question, answer):
    count = 0
    while count < 3:
        print(f'Please read the question of level {level}.')
        print(question)
        user_answer = input(f"Please input the answer of level {level}: ")
        count += 1

        if user_answer == answer:
            print("Correct!")
            break

        if count == 3:
            print('Sorry, wrong time is over 3. Exiting the game.')
            exit(0)

        choice = input('Wrong! Please input 1 to try again or input 2 to exit: ')
        if choice == '2':
            exit(0)

container_1 = [['1+1=?'], ['2']]
container_2 = [['What is the capital of Finland?'], ['Helsinki']]
container_3 = [['876*820=?'], ['718320']]

check_question(1, container_1[0][0], container_1[1][0])
check_question(2, container_2[0][0], container_2[1][0])
check_question(3, container_3[0][0], container_3[1][0])

