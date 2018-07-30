def addone(num, handle):
    '''
    call by reference example
    :param num: Immutable
    :param handle: Mutable
    :return: None
    '''
    new_handle = handle.copy()
    new_handle.append('one')
    num += 1
    print(num, new_handle)


if __name__ == '__main__':
    # Mutable and Immutable Arguments
    count = 0
    list1 = ['two']
    addone(count,list1)
    print(count,list1)
