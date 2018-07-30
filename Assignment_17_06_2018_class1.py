class Trip:
    def __init__(self, departCity=None, arriveCity=None,
                 departTime=None, departDay=None,
                 arriveTime=None, arriveDay=None):
        self.departCity = departCity
        self.arriveCity = arriveCity
        self.departTime = departTime
        self.departDay = departDay
        self.arriveTime = arriveTime
        self.arriveDay = arriveDay

    caribList = ['CUR', 'GCM']
    hawaiiList = ['HNL', 'ITO']

    def isRoundTrip(self):
        if self.arriveCity == self.departCity and self.departDay == self.arriveDay:
            return True
        else:
            return False

    def isCaribbean(self):
        if self.arriveCity in Trip.caribList:
            return True
        else:
            return False

    def isHawaiian(self):
        if self.arriveCity in Trip.hawaiiList:
            return True
        else:
            return False

    def isOverNight(self):
        if self.arriveDay != self.departDay:
            return True
        else:
            return False

    def isInterIsland(self):
        if self.arriveCity in Trip.hawaiiList and self.departCity in Trip.hawaiiList:
            return True
        else:
            return False




class Flight(Trip):
    def __init__(self,flightnum=-1,cost=0.0,code=0,departCity=None, arriveCity=None,departTime=None, departDay=None,arriveTime=None, arriveDay=None):
        self.flightnum = flightnum
        self.cost = cost
        self.code = code
        Trip.__init__(self,departCity=departCity,arriveCity=arriveCity,departDay=departDay,arriveDay=arriveDay,arriveTime=arriveTime,departTime=departTime)

    def discount(self):
        if super().isInterIsland() == True and super().isHawaiian() == True:
            return self.cost - self.cost/100*5
        elif super().isInterIsland() == True:
            return self.cost - self.cost/100*5
        elif super().isHawaiian() == True:
            return self.cost - self.cost/100*10
        elif super().isCaribbean() == True:
            return self.cost - self.cost/100*15
        else:
            return 'NOTFOUND'







if __name__ == '__main__':
    flight1 = Flight(flightnum=102, departCity="HNL", arriveCity="HKG",
                     departTime="4:00", departDay="Monday", arriveTime="8:00",
                     arriveDay="Monday", cost=99.95, code=4)
    flight2 = Flight(flightnum=204, departCity="HNL", arriveCity="ITO",
                     departTime="8:00", departDay="Monday", arriveTime="14:00",
                     arriveDay="Monday", cost=199.99, code=42)
    flight3 = Flight(flightnum=336, departCity="HKG", arriveCity="GCM",
                     departTime="12:00", departDay="Monday", arriveTime="20:00",
                     arriveDay="Monday", cost=299.99, code=44)
    flight4 = Flight(flightnum=660, departCity="CDG", arriveCity="GCM",
                     departTime="14:00", departDay="Monday", arriveTime="0:00",
                     arriveDay="Tuesday", cost=199.99, code=42)
    flight5 = Flight(flightnum=681, departCity="CDG", arriveCity="ITO",
                     departTime="6:00", departDay="Monday", arriveTime="11:00",
                     arriveDay="Monday", cost=209.89, code=41)
    flight6 = Flight(flightnum=753, departCity="LHR", arriveCity="HKG",
                     departTime="10:00", departDay="Monday", arriveTime="18:00",
                     arriveDay="Monday", cost=199.99, code=42)

    flightlist = [flight1,flight2,flight3,flight4,flight5,flight6]


    for n in flightlist:
        print("Before Discount: ",n.flightnum,"->",n.cost)
        print("After Discount: ",n.flightnum,"->",n.discount())
        print("#"*50)
