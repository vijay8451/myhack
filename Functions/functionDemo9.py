def area(radius):
    global pi
   # pi = pi + 1
   # print(pi*radius**2)
    pi = radius + 1
    print('Local',pi)


if __name__ == '__main__':
    pi = 3
    area([pi])
    print("Global pi is: ",pi)
