import requests
class IRCTC:

    def __init__(self):
        user_input=input("""how would you like to procde?
        1. enter 1 to check live train status
        2.enter 2 to check pnr
        3.enter 3 to check train schedule""")

        if user_input=="1":
           self.live_status()
        elif user_input =="2":
            self.pnr()
        else:
            self.train_schedule()
   
   
    def pnr(self):
        pnr_no=input("enter the pnr no.")
        self.fetch_result(pnr_no)

    def fetch_result(self,pnr_no):
        data=requests.get("https://indianrailapi.com/api/v2/PNRCheck/apikey/9485fe667278d32f90d3337b8e025db0/PNRNumber/{}".format(pnr_no))
        data=data.json()
        print(data['Passangers'])
        
        
        for i in data['Passangers']:
            print(i['passanger'],"|",i["Booking_status"],"|",i["current_status"],"|")



   
    def live_status(self):
        train_no=input("enter the train no")
        year=input("enter the year")
        month=input("enter the month")
        day=input("enter the day")
        hello=year+month+day
        self.fetch_traindata(train_no,hello)
 
    

    def fetch_traindata(self,train_no,hello):
        data=requests.get("https://indianrailapi.com/api/v2/livetrainstatus/apikey/9485fe667278d32f90d3337b8e025db0/trainnumber/{}/date/{}".format(train_no,hello))    
        data=data.json()
        print(data['TrainRoute'])

        for i in data['TrainRoute']:
            print(i['StationName'],"|",i["ScheduleArrival"],"|",i["ActualArrival"],"|",i["ActualDeparture"],"pm")
    
    
    def train_schedule(self):
        train_no=input("enter the train no")
        self.fetch_data(train_no)

    def fetch_data(self,train_no):
        data=requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/9485fe667278d32f90d3337b8e025db0/TrainNumber/{}".format(train_no))
        data = data.json()

        print(data['Route'])

        for i in data['Route']:
            print(i['StationName'],"|",i["ArrivalTime"],"|",i["DepartureTime"],"|",i["Distance"],"kms")

obj = IRCTC()
