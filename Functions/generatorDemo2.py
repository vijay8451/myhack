# return statement will terminate the generator function

def gen_next_day(today):
    wk = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    while True:
        yield wk[today]
        if today == 6:
#            return
             print()
        else:
            today += 1

if __name__ == '__main__':
    days = gen_next_day(5)
    print(days) #Gnerator object will be returned

    for day in days:
        print(day) ## day.__next__()
