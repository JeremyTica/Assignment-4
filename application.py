# Assignment 4
# Jeremy Tica
# 2023-12-08
import os 

class Program:
    def __init__(self):
        def create_file():
            file_name = input("Please input file name: ")
            open(file_name, "x")
            print("File " + file_name + " has been created.")

        def read_file():
            pass

        def update_file():
            pass

        def delete_file():
            pass

        def run():
            while True:
                os.system("cls")
                user_input = input("Welcome to the Programming Library System\n\n[1] Create\n[2] Read\n[3] Update\n[4] Delete\n\n") 
                if user_input == "1":
                    create_file()
                elif user_input == "2":
                    read_file()
                elif user_input == "3":
                    update_file()
                elif user_input == "4":
                    delete_file()
                else:
                    print("Invalid option")  
        
            
        run()

#! Program Execution
Program()