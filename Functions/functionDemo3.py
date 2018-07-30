def printkey(depart, arrive):
    '''
    KeyWord Parameters Functionality or Positional depending on
    how you are making a call
    :param depart: String
    :param arrive: String
    :return: None
    '''
    print("Depart and Arrive by Keyword: {} {}"
          .format(depart,arrive))

def printdef(depart='Pune',arrive ='Mumbai'):
    '''
    Default Parameters Implementation
    :param depart: String
    :param arrive: String
    :return: None
    '''
    print('depart and arrive defaults: {} {}'.format(depart,arrive))
    
if __name__ == '__main__':
    # Function call determines keyword or positional parameters
    #printkey('Pune','Mumbai')
    #printkey(arrive='Mumbai', depart='Pune')
    #printkey(depart='Pune', arrive='Mumbai')
    #printkey()
    printdef()
    #printdef(depart='Nagpur')
    #printdef(depart='Nagpur', arrive = 'kochi')
