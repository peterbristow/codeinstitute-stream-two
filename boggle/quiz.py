import sys

# f = open('questions.txt', 'r')
# lines = f.readlines()
# f.close()
# print lines


# with open('questions.txt', 'r') as f:
#     lines = f.readlines()
# print lines


# with open('questions.txt') as f:
#     for line in f:
#         print line


# def get_questions():
#     questions, answers = [], []
#     with open('questions.txt') as f:
#         for i, line in enumerate(f):
#             answers.append(line.strip()) if i % 2 else questions.append(line)
#     return zip(questions, answers)


def get_questions():
    with open('questionss.txt') as f:
        lines = f.readlines()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]


try:
    questions = get_questions()
except IOError as e:
    print 'Error reading questions file: %s' % e
    sys.exit()
except IndexError:
    print 'Error: All questions in the questions file must have answers.'
    sys.exit()
score = 0
total = len(questions)
for question, answer in questions:
    guess = raw_input(question)
    if guess == answer:
        score += 1
print 'You got %s out of %s questions right' % (score, total)