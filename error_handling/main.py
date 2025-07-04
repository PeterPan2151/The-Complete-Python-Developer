while True:
    try:
        age = int(input('What is your age? '))
        print(age)
    except ValueError:
        print('Please enter a number')
    else:
        break
