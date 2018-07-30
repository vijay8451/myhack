def func1(): #enclosing function
    #print(var)
    var = 'enclosing'
    print(var)
    def func2(): # local function
        var = 'local'
        print(var)
    func2()

    
if __name__ == '__main__':
    '''Main Function'''
    var = 'global'
    print(var)
    func1()
    
