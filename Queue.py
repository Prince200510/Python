#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Prince Maurya
#
# Created:     10-02-2024
# Copyright:   (c) Prince Maurya 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Queue:
    arr = []
    element = 0
    def main(self):
        while True:
            switch_dict = {
                1:self.insert,
                2:self.delete,
                3:self.display,
                4:self.exit
            }
            print("==========Queue==========")
            print("press 1:Insertion")
            print("press 2:Deletion")
            print("press 3:Display")
            print("press 4:Exit")
            print("=========================")

            choice = int(input("Press any (1 - 3):"))

            if choice in switch_dict:
                if choice == 4:
                    exit()
                switch_dict[choice]()
            else:
                print("Invaild Option")

    def insert(self):
        element = int(input("Enter a total element :"))
        for i in range(0,element):
            value = int(input(f"Enter {i + 1} element :"))
            self.arr.append(value)

    def delete(self):
        if not self.arr:
            print("Queue is Empty")
            return

        value_delete = self.arr.pop(0)
        print(f"Element {value_delete} is deleted")

    def display(self):
        if not self.arr:
            print("Queue is Empty")
        for value in self.arr:
            print(value)

    def exit():
        pass

obj1 = Queue()
obj1.main()