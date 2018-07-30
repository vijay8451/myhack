def printargs(*args,**kwargs):
    print("Positional Arguments ", args)
    print("Keyword Arguments ",kwargs)


if __name__ == '__main__':
    printargs('Pune',350,1000.00,1,2,3)
    #printargs(place='pune',distance=350,price=1000.00)
    #printargs('Passenger1',place='pune',distance=350,price=1000.00)
    #printargs(place='pune',distance=350,
    #          price=1000.0,'passenger2')
    #Positional Arguments is followed by keyword arguments
