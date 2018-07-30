def nextid(start):
    resletters = 'abcdefghijklmnopqrstuvwxyz'
    resindex = 0
    while True:
        yield str(start) + resletters[resindex]
        if resindex == 25:
            return
        else:
            resindex += 1

if __name__ == '__main__':
    reservation = nextid(99)
    for res_code in reservation:
        print(res_code)
