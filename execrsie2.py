#!/usr/bin/python

questions = [
    [ 
        {"question": "What is 123 + 321?", "answer": "444"},
        {"question": "What is the largest continet?", "answer": "Asia"},
    ],
    [  
        {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
        {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
    ],
    [   
        {"question": "Who is known as the 'Father of Computer Science?","answer": "Alan Turing"},
        {"question": "What is the largest mammal?", "answer": "Blue Whale"},
    ],
]

current_level = 0
grade = 2  
max_attempts= 3

while current_level < len(questions):
    print(f"Level {current_level + 1}:")

    score = 0
    for question in questions[current_level]:
        attempts = 0
        while attempts < max_attempts:
            user_answer = input(question["question"] + " ")

            if user_answer.lower() == question["answer"].lower():
                print("Correct!\n")
                score += 1
                break
            else:
                attempts += 1
                print(f"Wrong! Attempts left: {max_attempts- attempts}")

        if attempts == max_attempts:
            print("Game over!")
            exit()

    if score >= grade:
        print(f"You passed Level {current_level + 1}.\n")
        current_level += 1
    else:
        retry = input("Fail. Do you want to retry? (yes/no) ").lower()
        if retry != 'yes':
            print("Game over!")
            break

print(f"Your final grade is {score}/{len(questions) * grade}.")
