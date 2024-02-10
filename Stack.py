#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Prince Maurya
#
# Created:     10-02-2024
# Copyright:   (c) Prince Maurya 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Stack:
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
            print("==========Stack==========")
            print("press 1:Insertion")
            print("press 2:Deletion")
            print("press 3:Display")
            print("press 4:Exit")
            print("=========================")

            choice = int(input("Press any (1-4) :"))

            if choice in switch_dict:
                if choice == 4:
                    break
                switch_dict[choice]()
            else:
                print("Invaild Option")

    def insert(self):
        element = int(input("Enter a length of stack :"))

        for i in range(0,element):
            value = int(input(f"Enter a {i + 1} in stack :"))
            self.arr.append(value)
    def delete(self):
        if not self.arr:
            print("Stack is empty")
        else:
            delete_element = self.arr.pop()
            print(f"Delete element from stack :{delete_element}")
    def display(self):
        if not self.arr:
            print("Stack is empty")
        else:
            print("Stack elements:", end=" ")
            print(*self.arr, sep=" ")
    def exit(self):
        pass
obj = Stack()
obj.main()