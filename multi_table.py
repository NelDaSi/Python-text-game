# for i in range(1, 11):
#   line = ""
#   for j in range(1, 11):
#       line = line + str(i * j) + " "
#   print(line)

letters = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']
for i, letter in enumerate(letters):
    if i % 3 == 0:
        print(letter)
