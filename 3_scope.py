def spam():
    global eggs
    eggs = 99
    print(eggs)

eggs = 42
spam()
print(eggs)