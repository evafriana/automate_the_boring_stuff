def div42by(devideBy):
    try:
        return 42 / devideBy
    except ZeroDivisionError:
        print('error: You tried to devide by zero')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


print('How many cats do you have.')
numCats = input()
try:
    if int(numCats) >=4:
        print('That is a lot of cats')
    else:
        print('That is not that many cast')
except ValueError:
    print('You did not enter a number')

