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

    def is_over_night(self):
        if self.departday != self.arriveday:
            return True

    def is_hawaiian(self):
        if self.arrivecity in Trip.hawaiiList:
            return True

    def is_caribbean(self):
        if self.arrivecity in Trip.caribList:
            return True

    def is_interisland(self):
        if self.arrivecity and self.departcity in Trip.hawaiiList:
            return true




if __name__ == '__main__':
    trip1 = Trip(departcity="HNL", arrivecity="ITO", departtime="8:00", departday="Monday",
                 arrivetime="14:00", arriveday="Monday")
    trip2 = Trip(departcity="HKG", arrivecity="HNL", departtime="6:00", departday="Monday",
                 arrivetime="11:00", arriveday="Monday")
    trip3 = Trip(departcity="CDG", arrivecity="GCM", departtime="12:00", departday="Monday",
                 arrivetime="20:00", arriveday="Monday")
    trip4 = Trip(departcity="ARN", arrivecity="CDG", departtime="17:00", departday="Tuesday",
                 arrivetime="7:00", arriveday="Wednesday")

    #print(trip4.departcity)
    tripList = [trip1, trip2, trip3, trip4]


    def printTrip(t):
        print('Trip from', t.departcity, 'to', t.arriveity)
        print('Departs at', t.departtime, 'on', t.departday)
        print('Arrives at', t.arrivetime, 'on', t.arriveday)
    print(trip1)
