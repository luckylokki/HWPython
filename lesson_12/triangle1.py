row = int(input('Enter number of rows required: '))

def triangle(size):
    for i in range(size):
        for j in range(size - i):
            print(' ', end='')  # printing space required and staying in same line

        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # printing new line
triangle(row)