#Function Definition
def print_one():
    '''
    Function block begins with the keyword def
    Followed by Function Name
    Parameter list (empty or any)
    then Colon
    Function block with indentation
    Optional DocString
    Then Function Statements
    and then optional return statement.
    :return: None
    '''
    num = 1
    print("The value of num is {}".format(num))


def print_two():
    """
    Another Function
    :return: None
    """
    num = 2
    print("The value of num is {}".format(num))

if __name__ == '__main__':
    """Main Method"""
    #Call Function
    print_one()
    print_two()
    #print_one
    #print(print_one)