def sum_call(a,b):
    if a > 0 and b > 0:
        return a+b
    else:
        pass
def div_call(a,b):
    if a > 0 and b > 0:
        return a/b
    else:
        pass
def mult_call(a,b):
    if a > 0 and b > 0:
        return a*b
    else:
        pass
def sub_call(a,b):
    if a > 0 and b > 0:
        return a-b
    else:
        pass
def main(first_value=0,second_value=0):

    # Sum
    print("Sum of {} + {} is: {}".format(first_value,second_value,sum_call(first_value,second_value)))
    # Division
    print("Division of {} / {} is: {}".format(first_value,second_value,div_call(first_value,second_value)))
    # Multiplication
    print("Multiplication of {} * {} is: {}".format(first_value,second_value,mult_call(first_value,second_value)))
    # Subtraction
    print("Subtraction of {} - {} is: {}".format(first_value,second_value,sub_call(first_value,second_value)))


if __name__ == '__main__':
    main(100,200)
