#Positional Parameters
def printposit(depart, arrive):
    '''
    positional parameters functionalty demo
    :param depart: String
    :param arrive: String
    :return: None
    '''
    print("depart and arrive by position: {} {}".
          format(depart,arrive))

if __name__ == '__main__':
    #printposit('Pune','Mumbai')
    printposit('Mumbai','Pune')
