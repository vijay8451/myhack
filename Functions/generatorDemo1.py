def gen_next_day(today):
    wk = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    while True:
        yield wk[today]
        if today == 6:
            today = 0
        else:
            today += 1

if __name__ == '__main__':
    days = gen_next_day(5)
    #print(days) # Generator object will be returned

    #print(days.__next__()) #'Fri' will be returned
    #print(days.__next__()) #'Sat' will be returned
    #print(days.__next__()) #'Sun' will be returned
    #print(days.__next__())  # 'Mon' will be returned
    for day in days:
        print(day)