import string

#def mycompany(name):
#    for n in name:
#        if n not in string.ascii_letters:
#            raise CompError("This is not correct company")
#
#    print(name)
#
#class CompError(Exception):
#    def __init__(self,code):
#        self.code = code




#if __name__ == '__main__':
#
#    try:
#        name = input("Enter you Company name:")
#
#        mycompany(name)
#    except CompError as e:
#        print("Error:",e)
#
#    finally:
#        print("Thank you!")

#def foo():
#    try:
#        return 1
#    finally:
#        return 2
#k = foo()
#print(k)



a = False
while not a:
    try:
        f_n = input("Enter file name")
        i_f = open(f_n, 'r')
    except:
        print("Input file not found")
