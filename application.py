# Assignment 4
# Jeremy Tica
# 2023-12-08
import os 

class Program:
    def __init__(self):
        def create_file():
            file_name = input("Please input file name: ")
            if os.path.exists(file_name):
                print("File already exists!")
            else:
                open(file_name, "x")
                print("File " + file_name + " has been created.")

        def read_file():
            file_name = input("Please input the filename to be read: ")
            if os.path.exists(file_name):
                file_name.read()
            else:
                print("File does not exist.")

        def update_file():
            file_name = input("Please input the filename to be updated: ")
            if  os.path.exists(file_name):
                open(file_name, "w")
            else:
                print("File does not exist.")

        def delete_file():
            file_name = input("Please input the filename to be removed: ")
            if os.path.exists(file_name):
                if file_name != "application.py" or file_name != "Assignment 4 Report.docx":
                    os.remove(file_name)
                else:
                    print("Cannot delete file.")
            else:
                print("File does not exist.")

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