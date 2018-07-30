class Trip:
    '''This is Class1'''
    def __init__(self,departcity=None,arrivecity=None,departtime=0,departday=None,arrivetime=0,arriveday=None):
        self.departcity = departcity
        self.arrivecity = arrivecity
        self.departtime =  departtime
        self.arrivetime = arrivetime
        self.departday = departday
        self.arriveday = arriveday

    caribList = ['GCM', 'CUR']
    hawaiiList = ['ITO', 'HNL']


    def is_round_trip(self):
        if self.departcity == self.arrivecity:
            return 'round trip'
        else:
            return 'not round trip'



if __name__ == '__main__':
    depCity = 'CUR'
    arrCity = 'HNL'
    depTime = '12:00'
    depDay = 'Sunday'
    arrTime = '20:00'
    arrDay = 'Sunday'

    mytrip1=Trip(depCity,arrCity,depTime,depDay,arrTime,arrDay)
#    print(mytrip1.departday)

    myTrip2 = Trip(departcity=depCity,arrivecity=arrCity)

    print(Trip.caribList)
    print(myTrip2.is_round_trip())

