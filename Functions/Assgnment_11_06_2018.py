def mycount(X,Y):
    mylist=[]
    for i in range(0,X-1+1):
        mychildlist=[]
        for j in range(0,Y-1+1):
            mychildlist.append(i*j)
        mylist.append(mychildlist)

    return mylist





if __name__ == '__main__':

#    mycount= lambda X,Y: [i=0,1.., X-1; j=0,1,…Y-1]
#    A,B = input('Enter the numbers:')
#    print(mycount(int(A),int(B)))
     print(mycount(3,5))

