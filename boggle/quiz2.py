import difflib


def save_questions(question):
    lines = []
    with open('questions2.txt', 'a') as f:
        for q in question:
            q += "\n"
            f.write(q)
            lines.append(q.strip())
    return lines


def input_questions():
    question = raw_input('Enter your quiz question: ')
    answer = raw_input('Enter the answer: ')
    question = [question, answer]
    return question


def add_question():
    question = input_questions()
    return save_questions(question)


def get_questions():
    with open('questions2.txt') as f:
        lines = f.readlines()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]


def ask_questions(questions):
    score = 0
    total = len(questions)
    for question, answer in questions:
        guess = raw_input(question)
        guess = guess.lower()
        answer = answer.lower()
        for i in range(2): # give 3 tries
            difference = difflib.SequenceMatcher(None, guess, answer).ratio() # compare two strings
            # calculate acceptable percentage difference based on string length
            no_chars_diff = 2
            differential = float(len(answer) - no_chars_diff) / float(len(answer))
            if difference < differential:
                print 'That\'s wrong. Try again'
                guess = raw_input(question)
            if difference >= differential:
                score += 1
                break
    return 'You got %s out of %s questions right' % (score, total)


def run_quiz():
    questions = get_questions()
    return ask_questions(questions)


print run_quiz()
