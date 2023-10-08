# Day 2: Rock Paper Scissors

# X is Rock, Y is Paper, Z is scissors
points = {"X": 1, "Y": 2, "Z": 3}
lose, draw, win = 0, 3, 6
# what we should play to win
win_move = {"A": "Y", "B": "Z", "C": "X"}
# what we should play to lose
lose_move = {"A": "Z", "B": "X", "C": "Y"}


def score(a, b):
    if b == win_move[a]:
        return points[b] + win
    elif b == lose_move[a]:
        return points[b] + lose
    else:
        return points[b] + draw


file = open("2.in", "r")
lines = file.read().splitlines()

total = 0
for line in lines:
    total += score(*line.split())

print(total)

# Correct answer: 12855

# Part Two

# A is Rock, B is Paper, C is scissors
points = {"A": 1, "B": 2, "C": 3}
# X is lose, Y is draw, Z is win
condition = {"X": 0, "Y": 3, "Z": 6}
# what we should play to win
win_move = {"A": "B", "B": "C", "C": "A"}
# what we should play to lose
lose_move = {"A": "C", "B": "A", "C": "B"}


def score(a, b):
    match b:
        case "X":
            return points[lose_move[a]] + condition[b]
        case "Y":
            return points[a] + condition[b]
        case _:
            return points[win_move[a]] + condition[b]


file = open("2.in", "r")
lines = file.read().splitlines()

total = 0
for line in lines:
    total += score(*line.split())

print(total)

# Correct answer: 13726
