import random

quiz = {
    "Which planet is known as the Red Planet?": {
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "b"
    },

    "Which language is mainly used to build web pages?": {
        "options": ["Python", "Java", "HTML", "C++"],
        "answer": "c"
    },

    "What does CPU stand for?": {
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Control Power Unit",
            "Central Program User"
        ],
        "answer": "a"
    },

    "Which animal is known as the King of the Jungle?": {
        "options": ["Tiger", "Lion", "Elephant", "Bear"],
        "answer": "b"
    },

    "What is the largest ocean on Earth?": {
        "options": [
            "Atlantic Ocean",
            "Indian Ocean",
            "Pacific Ocean",
            "Arctic Ocean"
        ],
        "answer": "c"
    },

    "Who created the Python programming language?": {
        "options": [
            "Guido van Rossum",
            "Elon Musk",
            "Bill Gates",
            "Mark Zuckerberg"
        ],
        "answer": "a"
    },

    "What is the capital city of Nigeria?": {
        "options": ["Lagos", "Kano", "Abuja", "Kaduna"],
        "answer": "c"
    },

    "Which device is used to store data permanently?": {
        "options": ["RAM", "Hard Drive", "CPU", "Keyboard"],
        "answer": "b"
    },

    "How many continents are there in the world?": {
        "options": ["5", "6", "7", "8"],
        "answer": "c"
    },

    "Which programming language is known for data science and AI?": {
        "options": ["Python", "HTML", "CSS", "SQL"],
        "answer": "a"
    },

    "Which country won the 2022 FIFA World Cup?": {
        "options": ["Brazil", "Argentina", "France", "Germany"],
        "answer": "b"
    },

    "What is the largest planet in our solar system?": {
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "c"
    },

    "Which organ pumps blood around the human body?": {
        "options": ["Brain", "Lungs", "Heart", "Kidney"],
        "answer": "c"
    },

    "What does HTML stand for?": {
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyper Transfer Main Language",
            "Home Tool Markup Language"
        ],
        "answer": "a"
    },

    "Which company developed Android?": {
        "options": ["Apple", "Google", "Microsoft", "Samsung"],
        "answer": "b"
    },

    "What is the fastest land animal?": {
        "options": ["Lion", "Horse", "Cheetah", "Tiger"],
        "answer": "c"
    },

    "Which symbol is used for comments in Python?": {
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "b"
    },

    "What is the chemical symbol for water?": {
        "options": ["O2", "CO2", "H2O", "NaCl"],
        "answer": "c"
    },

    "Which planet is closest to the Sun?": {
        "options": ["Venus", "Earth", "Mercury", "Mars"],
        "answer": "c"
    },
    
    "Who is currently the richest man in the world?": {
    "options": [
        "Elon Musk",
        "Jeff Bezos",
        "Mark Zuckerberg",
        "Bernard Arnault"],
    "answer": "a"
    },

    "Which data structure stores items in key-value pairs in Python?": {
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "c"
    }
}


def quiz_game():
    score = 0
    questions = list(quiz.items())

    random.shuffle(questions)

    for number, (question, data) in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {question}")

        letters = ["a", "b", "c", "d"]

        for letter, option in zip(letters, data["options"]):
            print(f"{letter.upper()}. {option}")

        user = input("Your answer (A/B/C/D): ").lower()

        if user == data["answer"]:
            print("Correct! ✅")
            score += 1
        else:
            correct_index = letters.index(data["answer"])
            print("Wrong! ❌ The answer is", data["options"][correct_index])

    print("\nQuiz Completed 🎮")
    print(f"Your final score: {score}/{len(quiz)}")

    if score == 0:
        print("Don't give up! Keep learning and try again 💪")
    elif score <= 10:
        print("Good attempt! Keep practicing 🚀")
    elif score == len(quiz):
        print("Perfect score! You are a quiz master 🏆")
    else:
        print("Great job! Keep improving 🎉")


print("Welcome to NovaByte Quiz Game 🎮")
quiz_game()