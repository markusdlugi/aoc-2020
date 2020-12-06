from collections import namedtuple

lines = [line.strip() for line in open("input/06.txt")]

groups = []
sets = namedtuple("Sets", "any all")
questions = sets(any=set(), all=set())
for line in lines:
    if line == "":
        groups.append(questions)
        questions = sets(any=set(), all=set())
        continue
    if not questions.any:
        questions.all.update(set(list(line)))
    else:
        questions.all.intersection_update(set(list(line)))
    questions.any.update(set(list(line)))
groups.append(questions)

print(sum(len(questions.any) for questions in groups))
print(sum(len(questions.all) for questions in groups))
