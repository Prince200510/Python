#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      prince
#
# Created:     08-06-2023
# Copyright:   (c) prince 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Bank Management System

class AmountExcpetion(Exception):
    pass

class Bank:
    def __init__(self):
        self.accounts = []

    def mainpage(self):
        option = {
            1: self.admin,
            2: self.customerlogin
        }

        print("|---------INDIA POST PAYMENT BANK---------|")
        print("|press 1. Admin Login                     |")
        print("|press 2. Customer Login                  |")
        print("|-----------------------------------------|")

        choice = int(input("press 1/2: "))

        if choice in option:
            option[choice]()
        else:
            print("! Invalid option !")

    def admin(self):
        ID = int(input("Login ID: "))
        password = input("Password: ")

        if ID == 1001:
            if password == "prince":
                self.accdetail()
            else:
                print("! Incorrect Password !")
                self.mainpage()
        else:
            print("! Incorrect Login ID !")
            self.mainpage()

    def accdetail(self):
        option1 = {
            1: self.newacc,
            2: self.deposit,
            3: self.withdraw,
            4: self.searchacc,
            5: self.goback
        }
        self.accounts = []
        while True:
            print("|---------ADMIN LOGIN---------|")
            print("|press 1. New Account Opening |")
            print("|press 2. Deposit             |")
            print("|press 3. Withdraw            |")
            print("|press 4. Search Account      |")
            print("|press 5. Go Back             |")
            print("|-----------------------------|")

            choice1 = int(input("press any 1 - 5 : "))

            if choice1 in option1:
                if choice1 == 5:
                    break
                option1[choice1]()
            else:
                print("Invalid choice!")

    def newacc(self):
        a = int(input("Enter how many new accounts to create: "))
        for i in range(a):
            print("Note: Account number size should be equal to 4 digits")
            accnumber = input("Enter new account number: ")
            if len(accnumber) != 4 or not accnumber.isdigit():
                print("Note: Please enter only 4 digit account number and validate account number")
                accnumber = input("Reenter a new account number: ")
            else:
                pass
            name = str(input("Enter account holder name: "))
            if len(name) > 32:
                print("Note: Account holder name should be up to 32 characters.")
                name = str(input("Reenter account holder name: "))
            else:
                pass
            phone_number = input("Enter phone number: ")
            if len(phone_number) != 10 or not phone_number.isdigit():
                print("Note: Please enter only 10 digit phone number and validate phone number")
                phone_number = input("Reenter a phone number: ")
            else:
                pass
            balance = float(input("Enter opening balance: "))
            if balance < 100.00:
                print("Note: Opening balance should be more than 100.00 rs")
                balance = float(input("Reenter opening balance: "))
            else:
                pass
            print("New account created successfully")
            account = {
                "accnumber": accnumber,
                "name": name,
                "phone_number": phone_number,
                "balance": balance
            }
            self.accounts.append(account)

    def deposit(self):
        searchaccnumber = input("Enter the account number to deposit into: ")
        found_account = None
        for account in self.accounts:
            if account["accnumber"] == searchaccnumber:
                found_account = account
                break

        if found_account:
            print("|------------Account Details:------------|")
            print("Account Number     :", found_account["accnumber"])
            print("Account Holder Name:", found_account["name"])
            print("Phone Number       :", found_account["phone_number"])
            print("Current Balance    :", found_account["balance"])
            print("|----------------------------------------|")
            depositbalance = float(input("Enter balance: "))
            print("|------------Account Updated Details:------------|")
            print("Account Number     :", found_account["accnumber"])
            print("Account Holder Name:", found_account["name"])
            print("Phone Number       :", found_account["phone_number"])
            print("Old Balance        :", found_account["balance"])
            balance = found_account["balance"] + depositbalance
            found_account["balance"] = balance
            print("New Balance        :", balance)
            print("|------------------------------------------------|")

        else:
            print("Account not found!")

    def withdraw(self):
        searchaccnumber = input("Enter the account number to withdraw from: ")
        found_account = None
        for account in self.accounts:
            if account["accnumber"] == searchaccnumber:
                found_account = account
                break

        if found_account:
            print("|------------Account Details:------------|")
            print("Account Number     :", found_account["accnumber"])
            print("Account Holder Name:", found_account["name"])
            print("Phone Number       :", found_account["phone_number"])
            print("Current Balance    :", found_account["balance"])
            print("|----------------------------------------|")
            withdrawbalance = float(input("Enter balance: "))
            print("|------------Account Updated Details:------------|")
            print("Account Number     :", found_account["accnumber"])
            print("Account Holder Name:", found_account["name"])
            print("Phone Number       :", found_account["phone_number"])
            print("Old Balance        :", found_account["balance"])
            balance = found_account["balance"]

            if balance >= withdrawbalance:
                balance -= withdrawbalance
                found_account["balance"] = balance
                print("New Balance        :", balance)
                print("|------------------------------------------------|")
            else:
                print("Insufficient Balance!")

        else:
            print("Account not found!")

    def searchacc(self):
        searchaccnumber = input("Enter the account number to search: ")
        found_account = None
        for account in self.accounts:
            if account["accnumber"] == searchaccnumber:
                found_account = account
                break

        if found_account:
            print("|------------Account Details:------------|")
            print("|Account Number     :", found_account["accnumber"])
            print("|Account Holder Name:", found_account["name"])
            print("|Phone Number       :", found_account["phone_number"])
            print("|Balance            :", found_account["balance"])
            print("|----------------------------------------|")
        else:
            print("Account not found!")

    def goback(self):
        self.mainpage()

    def customerlogin(self):
        accsrcnumber = input("Enter the account number: ")
        found_account = None
        for account in self.accounts:
            if account["accnumber"] == accsrcnumber:
                found_account = account
                break
        if found_account:
            print("|------------Account Details:------------|")
            print("|Account Number     :", found_account["accnumber"])
            print("|Account Holder Name:", found_account["name"])
            print("|Phone Number       :", found_account["phone_number"])
            print("|Balance            :", found_account["balance"])
            print("|----------------------------------------|")
        else:
            print("Account not found!")

object1 = Bank()
object1.mainpage()
