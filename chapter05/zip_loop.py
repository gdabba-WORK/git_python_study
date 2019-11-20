names = ['James', 'Robert', 'Lisa', 'Mary']

scores = [95, 96, 97, 94]

for k in range(len(names)):
    print(names[k], scores[k])

print()
for name, score in zip(names, scores):
    print(name, score)

