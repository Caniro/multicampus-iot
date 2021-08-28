score = [88, 95, 70, 100, 99, 88, 78, 50]
score.remove(100)
print(score)
del(score[2])
print(score)
score[1:4] = []
print(score)

if (1000 in score):
    score.remove(1000)
