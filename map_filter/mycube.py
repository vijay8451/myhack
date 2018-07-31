def mycube(x):
    return x**x

if __name__ == '__main__':
    """Return the list of cube"""
    print(list(map(mycube, range(1,10))))
