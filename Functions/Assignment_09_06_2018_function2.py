def flights_per_cities(*arg,**karg):
    '''
    This is to show the function for flights_per_cities
    :param arg:  string
    :param karg: Dictionary
    :return: String
    '''
    return print([key for key,value in karg.items() if value[0] == arg[0] and value[1] == arg[1]])







if __name__ == '__main__':
    flightdict = {
        '102': ['HNL', 'HKG', '4:00', 'Monday', '8:00', 'Monday', '99.95', 4],
        '132': ['HNL', 'HNL', '4:00', 'Monday', '8:00', 'Monday', '59.0', 2],
        '276': ['HKG', 'CDG', '15:00', 'Monday', '3:00', 'Tuesday', '233.99', 2],
        '303': ['HKG', 'ARN', '9:00', 'Monday', '16:00', 'Monday', '233.99', 2],
        '498': ['NRT', 'ITO', '14:00', 'Monday', '0:00', 'Tuesday', '159.99', 2],
        '390': ['HKG', 'CUR', '4:00', 'Thursday', '8:00', 'Thursday', '599.95', 3],
        '465': ['NRT', 'YYZ', '4:00', 'Thursday', '8:00', 'Thursday', '59.0', 3],
        '1305': ['ITO', 'ARN', '4:00', 'Thursday', '8:00', 'Thursday', '125.0', 2],
        '375': ['HKG', 'HNL', '6:00', 'Friday', '11:00', 'Friday', '299.99', 4],
        '444': ['NRT', 'LHR', '15:00', 'Friday', '3:00', 'Saturday', '125.0', 3],
        '1572': ['CUR', 'HNL', '4:00', 'Sunday', '8:00', 'Sunday', '125.0', 2]}

    #flights_per_cities('HNL','HKG',**flightdict)
    #flights_per_cities('HKG', 'HNL',**flightdict)
    flights_per_cities('NRT', 'ITO', **flightdict)
