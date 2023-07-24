#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      prince
#
# Created:     11-07-2023
# Copyright:   (c) prince 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random


class Train:
    def __init__(self):
        self.passengerdetails = []

    def mainpage(self):
        option = {
            1: self.admin,
            2: self.passengerlogin,
        }
        print("|---------Indian Railway---------|")
        print("|press 1. Admin Login            |")
        print("|press 2. Passenger Login        |")
        print("|--------------------------------|")

        choice = int(input("press 1/2: "))

        if choice in option:
            option[choice]()
        else:
            print("! Invalid option !")

    def admin(self):
        ID = int(input("Login ID: "))
        password = input("Password: ")
        if ID == 1001:
            if password =="prince":
                self.ticketpage()
            else:
                print("! Incorrect Password !")
                self.mainpage()
        elif ID == 1002:
            if password =="admin1":
                self.ticketpage()
            else:
                print("! Incorrect Password !")
                self.mainpage()
        elif ID == 1003:
            if password =="admin2":
                self.ticketpage()
            else:
                print("! Incorrect Password !")
                self.mainpage()
        elif ID == 1004:
            if password =="admin3":
                self.ticketpage()
            else:
                print("! Incorrect Password !")
                self.mainpage()
        else:
            print("! Incorrect Login ID !")
            self.mainpage()

    def ticketpage(self):
        print("|----------ADMIN LOGIN-----------|")
        print("|press 1. Ticket Booking         |")
        print("|press 2. Show Ticket            |")
        print("|press 3. Change Ticket Price    |")
        print("|press 4. Search Passenger       |")
        print("|press 5. Logout                 |")
        print("|--------------------------------|")
        option1 = {
            1: self.newticketbook,
            2: self.showticket,
            3: self.changeticketprice,
            4: self.searchpass,
            5: self.goback
        }
        self.passengerdetails = []
        while True:
            choice1 = int(input("press any 1 - 5 : "))
            if choice1 in option1:
                if choice1 == 6:
                    break
                option1[choice1]()
            else:
                print("Invalid choice!")

    def newticketbook(self):
        p=0
        total = 0
        print("|===========================Journey Details===========================|")
        print("|                        Station name and code                        |")
        print("|1.LTT - Mumbai                        11.New Delhi Railway Station   |")
        print("|2.CSMT - Mumbai                       12.Chennai                     |")
        print("|3.Bandar - Mumbai                     13.Kanpur Central              |")
        print("|4.Dadar - Mumbai                      14.Kalyan Junction - Mumbai    |")
        print("|5.Gorakapur                           15.Nagpur Railway Junction - MH|")
        print("|6.Jaunpur                             16.Luncknow Charbagh           |")
        print("|7.Prayagraj Junction                  17.Varanasi Junction           |")
        print("|8.Kolkata                             18.Patna Junction              |")
        print("|9.Bangalore                           19.Itrasi Junction             |")
        print("|10.Howrah Junction, Kolkata           20.Konkan Junction             |")
        print("|=====================================================================|")
        name = input("Enter the booker name or agent name                      : ")
        date = input("Enter the date or day of departure or arrival            : ")
        phone_number = input("Enter phone number                                       : ")

        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Note: Please enter a 10-digit phone number.")
            phone_number = input("Reenter phone number                                     : ")
        num_passengers = int(input("Enter the number of passengers                           : "))

        while num_passengers >5:
            print("At Timne one use can add only 5 passenger in a one ticket")
            num_passengers = int(input("Re - Enter the number of passengers                      : "))
        total = num_passengers * 1500
        source=None
        sources = input("From or Source, please enter the station code like 1/2/3 : ")
        if sources =="1":
            source = "LTT - Mumbai"
        elif sources =="2":
            source = "CSMT - Mumbai"
        elif sources =="3":
            source = "Bandar - Mumbai"
        elif sources =="4":
            source = "Dadar - Mumbai"
        elif sources =="5":
            source = "Gorakapur"
        elif sources =="6":
            source = "Jaunpur"
        elif sources =="7":
            source = "Prayagraj Junction"
        elif sources =="8":
            source = "Kolkata"
        elif sources =="9":
            source = "Bangalore"
        elif sources =="10":
            source = "Howrah Junction, Kolkata"
        elif sources =="11":
            source = "New Delhi Railway Station"
        elif sources =="12":
            source = "Chennai"
        elif sources =="13":
            source = "Kanpur Central"
        elif sources =="14":
            source = "Kalyan Junction - Mumbai"
        elif sources =="15":
            source = "Nagpur Railway Junction - MH"
        elif sources =="16":
            source = "Luncknow Charbagh"
        elif sources =="17":
            source = "Varanasi Junction"
        elif sources =="18":
            source = "Patna Junction"
        elif sources =="19":
            source = "Itrasi Junction"
        elif sources =="20":
            source = "Konkan Junction"
        else:
            print("Invaild Station code or Source code, Please Renter it")
            sources = input("From or Source, please enter the station code like 1/2/3 : ")
        destination = None
        destinations = input("To or Dest  , please enter the station code like 1/2/3   : ")
        if destinations =="1":
            destination = "LTT - Mumbai"
        elif destinations =="2":
            destination = "CSMT - Mumbai"
        elif destinations =="3":
            destination = "Bandar - Mumbai"
        elif destinations =="4":
            destination = "Dadar - Mumbai"
        elif destinations =="5":
            destination = "Gorakapur"
        elif destinations =="6":
            destination = "Jaunpur"
        elif destinations =="7":
            destination = "Prayagraj Junction"
        elif destinations =="8":
            destination = "Kolkata"
        elif destinations =="9":
            destination = "Bangalore"
        elif destinations =="10":
            destination = "Howrah Junction, Kolkata"
        elif destinations =="11":
            destination = "New Delhi Railway Station"
        elif destinations =="12":
            destination = "Chennai"
        elif destinations =="13":
            destination = "Kanpur Central"
        elif destinations =="14":
            destination = "Kalyan Junction - Mumbai"
        elif destinations =="15":
            destination = "Nagpur Railway Junction - MH"
        elif destinations =="16":
            destination = "Luncknow Charbagh  "
        elif destinations =="17":
            destination = "Varanasi Junction"
        elif destinations =="18":
            destination = "Patna Junction"
        elif destinations =="19":
            destination = "Itrasi Junction"
        elif destinations =="20":
            destination = "Konkan Junction"
        else:
            print("Invaild Station code or destination code, Please Renter it")
            destinations = input("From or Source, please enter the station code like 1/2/3 : ")
        pnrs = random.choice([9930, 9987, 6969, 7070, 1234,2345,2334,7865,3424,3247,8756,1223,7675,7643])
        print("PNR number auto-generated                                :", pnrs)
        pnr = input("Enter PNR which generated automatic                      : ")
        while int(pnr) != pnrs:
            print("Invaild pnr number entered please enter it correct pnr number from auto-generted")
            pnr = input("Reenter pnr number                                       : ")

        passengers = []
        for _ in range(num_passengers):
            p+=1
            passenger_name = input("Enter passenger "+ str(p) + " name                                   : ")
            passenger_age = int(input("Enter passenger age                                      : "))

            passenger = {
                "name": passenger_name,
                "age": passenger_age
            }
            passengers.append(passenger)

        passenger_detail = {
            "num_passengers":num_passengers,
            "pnr": pnr,
            "name": name,
            "date":date,
            "total":total,
            "phone_number": phone_number,
            "source": source,
            "destination": destination,
            "passengers": passengers
        }
        self.passengerdetails.append(passenger_detail)

        print("Ticket(s) booked successfully!")

    def showticket(self):
        search_passenger = input("Enter the PNR number: ")
        found_passenger = None
        for passenger_detail in self.passengerdetails:
            if passenger_detail["pnr"] == search_passenger:
                found_passenger = passenger_detail
                break

        if found_passenger:
            print("|==============================================================|")
            print("|     शुभ यात्रा       | PNR Number : ", found_passenger["pnr"])
            print("| HAPPY JOURNEY    | Train Number : xxxxx5                   ")
            print("|==============================================================|")
            print("|                   Indian Railway                ", found_passenger["date"])
            print("|--------------------------------------------------------------|")
            print("| Name         :", found_passenger["name"])
            print("| Phone Number :", found_passenger["phone_number"])
            print("|--------------------------------------------------------------|")
            print("|     Source                                                    ")
            print("| ",found_passenger["source"])
            print("|   Destination ")
            print("| ",found_passenger["destination"])
            print("|--------------------------------------------------------------|")
            print("| Passenger Name                     Age ")


            passengers = found_passenger["passengers"]
            for passenger in passengers:
                print("| {}                 {}".format(passenger["name"].ljust(18), str(passenger["age"]).ljust(3)))
            print("|--------------------------------------------------------------|")
            print("|                                    Price : 1500/-")
            print("|                                    Total : {} x 1500 = {}/-".format(found_passenger["num_passengers"], found_passenger["total"]))

            print("|==============================================================|")
        else:
            print("Passenger not found.")

    def changeticketprice(self):
        pass

    def searchpass(self):
        p=0
        search_passenger = input("Enter the PNR number: ")
        found_passenger = None
        for passenger_detail in self.passengerdetails:
            if passenger_detail["pnr"] == search_passenger:
                found_passenger = passenger_detail
                break

        if found_passenger:
            print("|====================Passenger Details====================|")
            print("PNR Number         :", found_passenger["pnr"])
            print("Name               :", found_passenger["name"])
            print("Phone Number       :", found_passenger["phone_number"])
            print("Date or departure  :",found_passenger["date"])
            print("Source             :", found_passenger["source"])
            print("Destination        :", found_passenger["destination"])

            passengers = found_passenger["passengers"]
            for passenger in passengers:
                p+=1
                print("Passenger "+str(p)+" Name   :", passenger["name"])
                print("Age                :", passenger["age"])
            print("|=========================================================|")
        else:
            print("Passenger not found.")

    def goback(self):
        logout = input("Confirm logout ? if yes then click y :")

        if logout=="y" or "Y":
            self.mainpage()

    def passengerlogin(self):
        print("welcome test")


object = Train()
object.mainpage()
