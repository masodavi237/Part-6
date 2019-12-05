count = 1
def new_ex(count):
    print()
    print()
    print('(%0.0f)' % count)




# To print 8 stars, one at a time on a single line:
for i in range(0,6):
    print(' * ', end=' ')

new_ex(count)
# To print a 6 X 6 grid of '*'
for i in range(0,6):
    for j in range(6):
        print(' * ', end=' ')
    print()

new_ex(count)
count += 1
# end='' ends the output where it is and adds the character in the ''
i = 0
print(i, end=" ")
i = 1
print(i, end=" ")

new_ex(count)
count += 1
# Print 10, 5 then 20 * using for loops
for j in range(10):
    print(' * ', end='')
print()
for j in range(5):
    print(' * ', end='')
print()
for k in range(20):
    print(' * ', end='')

new_ex(count)
count += 1
# Print a 10 X 10 rectangle
for i in range(10):
    for j in range(10):
        print(' * ', end='')
    print()

new_ex(count)
count += 1
# Print 5 X 10 rectangle
for i in range(10):
    for j in range(5):
        print(' * ', end='')
    print()

new_ex(count)
count += 1
# print a 20 X 5 rectangle
for i in range(5):
    for j in range(20):
        print(' * ', end='')
    print()

new_ex(count)
count += 1
# print 10 lines of 0 through 9 as a string
for i in range(10):
    for j in range(0,10):
        print(j, end=' ')
    print()

new_ex(count)
count += 1
# print 10 of each number 0 through 9
for i in range(10):
    for j in range(10):
        print(i, end=' ')
    print()

new_ex(count)
count += 1
# print each number but add another one each line
for row in range(10):
    for column in range(row + 1):
        print(column, end=" ")
    # Print a blank line
    # to move to the next row
    print()

new_ex(count)
count += 1
for row in range(11, 0, -1):
    for column in range(11 - row):
        print('  ', end='')
    for column in range(row - 1):
        print(column, end=' ')
    print()

new_ex(count)
count += 1
# 10 x 10 grid ofn row X column
for row in range(1, 10):
    for column in range(1, 10):
        print(row * column, '  ', end='')
        if row * column < 10:
            print(' ', end='')
    print()

new_ex(count)
count += 1
#pyramid of numbers
for i in range(10):
    for l in range(16 - (2 * i)):
        print(' ', end='')
    for k in range(i + 1):
        if k != 0:
            print(k, end=' ')
    for j in range(i+1):
        if j != 0:
            print(j, end=" ")

    print()