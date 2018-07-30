def discount(price,disc):
    '''
    THis is to check the Dsicount as per argument
    :param price: int
    :param disc: int
    :return: discounted price
    '''
    #print(price)
    return price - (price * disc)

def discount_printer(*arg,**karg):
    '''
    to make a list of price and discount
    :param arg: list
    :param targ:
    :return:Flot
    '''
    #print(arg)
    #return [for price,disc in zip(arg[0],arg[1])
    return [discount(price,disc) for price,disc in zip(arg[0],arg[1])]












if __name__ == '__main__':
    pricelist = [100, 299, 399.95]
    disclist = [0.05, 0.15, 0.10]


    #discount(price=100,disc=0.05)
    result1,result2,result3 = discount_printer(pricelist,disclist)
    print(result1)

