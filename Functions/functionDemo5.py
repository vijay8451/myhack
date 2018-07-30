def printargs(*args, **kwargs):
    print("Positional Arguments ",args)
    print("Keyword Arguments ",kwargs)

    
if __name__ == '__main__':
    traveller1 = ('Passenger1', 'Pune',
                  350, 1000.00)

    traveller2 = {'name':'Passenger2','city':'Pune',
                  'distnace':350, 'cost':1000.00}

    printargs(traveller1)
    #printargs(*traveller1)
    #printargs(*traveller1, **traveller2)
    #printargs(traveller2)
    #printargs(**traveller2)
    #printargs(*traveller2)
    #printargs(name='passenger',)