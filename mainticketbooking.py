from pathlib import Path
import random
import string
import json
from pathlib import Path
import pyttsx3

class Booking:
    # dataa='Bank.py'
    database = 'temp.json'
    show = [{"showno":1,"userinfo":[{"seatstatus":"Available"} for _ in range(50)] } ,
            {"showno":2,"userinfo":[{"seatstatus":"Available"} for _ in range(50)]} ,
            {"showno":3,"userinfo":[{"seatstatus":"Available"} for _ in range(50)]}]
    # try:
    #     if Path(database).exists():
    #         with open(database) as fs:
    #           show = json.loads(fs.read())
    #     else:
    #        print("no such file exist: ")
    # except Exception as err:
    #     print(f"exception occured due to {err}")
    # # a=show[0]["userinfo"][0]["seatstatus"] ="bookedd"
    # # print(a)
           
    @staticmethod
    def __ticketidgenerate():
        # show = int(input("Enter your show time eg:1,2,3  "))
        
            alpha=random.choices("A") 
            num=random.choices(string.digits,k=2) 
            id= alpha+num 
            return "".join(id)
        

    def transaction(self):
        print("press 1 to choose UPI method: ")
        print("press 2 to NetBanking method: ")
        
        res =int(input("please choose any option from above : "))
        try:
            paymt = int(input("Pay 500rs to book this ticket...  "))
        except Exception as err:
            print(f"exception occured due to {err}")
        if (paymt>=500):
            if res==1:
                 a =input("please enter your UPI id: ")
            
            elif res==2:
                a =input("please enter your Debit card number:  ")
                a=  input("enter your Debit card PIN : ")
        
            else:
                print("please choose right option from above: ")
        
            print("\n\nPayment sucessfully:-  ")
            num = random.randint(10900,99999)
            print("your transaction id is : TXN"+str(num))  
               
        else:
            print("please check you amount.. \ntry again. ")
            self.transaction()
       


        
    
    @staticmethod
    def __update():
        if Path(Booking.database).exists():
            with open(Booking.database,"w") as fs:
                fs.write(json.dumps(Booking.show))
        

    @staticmethod
    def __shedule():
        print(f"  x------SHOW TIMMING-------x\n")
        print(f"[First show: 9:00 am to 12:00 pm ]\n[Second show: 1:00 pm to 4:00 pm ]\n[Third show: 6:00 pm to 9:00 pm ]\n")
        res =int(input(print("Press 1 to book ticket in 1st show\nPress 2 to book ticket in 2nd show\nPress 3 to book ticket in 3rd show")))
        return res
  
    
    @staticmethod
    def __movie():
        print("1. KGF\n2. Dilwale\n3. 3 IDIOT\n4. Marjavaa")
        res=input(print("Enter any movie name from above: "))
        print(res)
        return res

    def bookticket(self):
        engine = pyttsx3.init()
        engine.setProperty('rate',150)
        voice=engine.getProperty('voices')
        engine.setProperty('voices',voice[1].id)
        engine.say(''' Hello   You   have   entered   1 !,
                   now   you   can   book   your   ticket .,
                    enter your correct detalis below
        
         ''')
        engine.runAndWait()
        #Showtime = self.__shedule()   
        self.printseats()
        data ={
            "Showtime" : self.__shedule(),
            "moviename":self.__movie(),
            "Name" :input("enter your name: "),
            "Age" :int(input("enter Your age: ")),  
            "Seatno" :int(input("enter seat no that is empty : ")),
            "TicketId" : self.__ticketidgenerate()
        }
        
        if (Booking.show[data["Showtime"]-1]['userinfo'][data["Seatno"]-1]["seatstatus"] == "Available"):
            Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["seatstatus"] ="x--Booked--X"
            Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["Name"] = data["Name"]
            Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["Age"]= data["Age"]
            Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["Seatno"]= data["Seatno"]
            Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["TicketId"]= data["TicketId"]
            Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["showslot"]= data["Showtime"]
            Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["moviename"]= data["moviename"]
            if data["Showtime"]== 1:
                Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["Showtime"]=" 09 :00 am  to 12:00 pm "
            elif data["Showtime"] == 2:
                Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["Showtime"] ="01 :00 pm  to 04:00 pm"
            else:
                Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["Showtime"] ="06 :00 pm  to 09:00 pm"
            
            if(Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["Age"]>14 and Booking.show[data["Showtime"]-1]["userinfo"][data["Seatno"]-1]["Age"] <60) :
                self.transaction()
                print("Processing...")
                engine = pyttsx3.init()
                engine.setProperty('rate',150)
                voice=engine.getProperty('voices')
                engine.setProperty('voices',voice[1].id)
                engine.say(''' Congratulations your ticket has been booked
        
                 ''')
                engine.runAndWait()
               
                print("--x--YOUR TUCKET IS BOOKED SUCESSFULLY--x--")
                for i in data:
                    if i == "Showtime":
                        if data["Showtime"]== 1:
                            print("Your Slot is booked in 09 :00 am  to 12:00 pm ")
                        elif data["Showtime"] == 2:
                            print("Your Slot is booked in 01 :00 pm  to 04:00 pm ")
                        else:
                            print("Your Slot is booked in 06 :00 pm  to 09:00 pm ")
                    else: 
                       print(f"{i}  :-  {data[i]}")
                self.__update()
            else:
                print("Your Age is not eligible for show: ")
        else:
            print(" Sorry this   ticket is allready booked !  for the perticular slot..")


    def CancleTicket(self):
        res = input(print("please Enter D to Cancle Your ticket "))
        if(res=='d' or res=='D'):
            showno = int(input(print("please enter your show time 1 ,2 or 3")))
            seatno = int(input(print("please enter your seat no :")))

            Booking.show[showno-1]["userinfo"][seatno-1]["seatstatus"] ="Available"
            Booking.show[showno-1]["userinfo"][seatno-1]["Name"] =""
            Booking.show[showno-1]["userinfo"][seatno-1]["Age"]= ""
            Booking.show[showno-1]["userinfo"][seatno-1]["Seatno"]= ""
            Booking.show[showno-1]["userinfo"][seatno-1]["TicketId"]= ""
            Booking.show[showno-1]["userinfo"][seatno-1]["showtime"]= ""
            print("Ticket Canclled Sucessfully: ")
            self.__update()
        else:
            print("Thanks for your response\nyour ticket is not cancelled !")

    @staticmethod
    def printseats():
        index=0
        inv=1
        res=  int(input("Enter slot number (1,2,3)  to see available seats in perticular slot: "))

        if res == 1:
           for i  in Booking.show[res-1]["userinfo"]:
               if (Booking.show[res-1]["userinfo"][index]["seatstatus"] == "Available"):
                   print(f"{index+1}:-{Booking.show[res-1]["userinfo"][index]["seatstatus"]} ",end='')
                   index+=1
                   if index == 10*(inv):
                       inv+=1
                       print("\n")
               else:
                   index+=1

        elif res == 2:
           for i  in Booking.show[res-1]["userinfo"]:
               if (Booking.show[res-1]["userinfo"][index]["seatstatus"] == "Available"):
                   print(f"{index+1}:-{Booking.show[res-1]["userinfo"][index]["seatstatus"]}  ",end='')
                   index+=1
                   if index == 10*(inv):
                       inv+=1
                       print("\n")
               else:
                   index+=1

        elif res == 3:
           for i  in Booking.show[res-1]["userinfo"]:
               if (Booking.show[res-1]["userinfo"][index]["seatstatus"] == "Available"):
                   print(f"{index+1}:-{Booking.show[res-1]["userinfo"][index]["seatstatus"]}  ",end='')
                   index+=1
                   if index == 10*(inv):
                       inv+=1
                       print("\n")
                  
                   
               else:
                   index+=1
        else:
            print("please enter correct slot time: ")
               



a = Booking()
while(True):
  print("Press 1 to Book ticket: ")
  print("Press 2 to Cancle ticket: ")
  print("Press 3 to see available ticket: ")
  print("Press 4 to exit : ")

  res=  int(input(print("please tell your response: ")))
  if res==1:
      a.bookticket()
  if res==2:
      a.CancleTicket()
  if res==3:
      a.printseats()
  if res ==4 :
      break







