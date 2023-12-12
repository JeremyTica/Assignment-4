# Assignment 4
# Jeremy Tica
# 2023-12-08
import os #! Import operating system for organization, relative directory, etc. 
import json #! Import json for the .json extension

class Program:
    """_summary_
    Primary class and instance
    Used to administer user interaction
    """
    def __init__(self):
        resource = Resource() #! Create an instance of the resource object/class

        def showMainMenu():
            """_summary_
            Display the main menu the user will use to
            interact with to modify or create files
            """
            library = open('library.json')
            data = json.load(library)
            
            while True:
                os.system("cls")
                user_input = input("Welcome to the Programming Library System\n\n[1] Create\n[2] Read\n[3] Update\n[4] Delete\n\n") 
                if user_input == "1":
                    file_name = input("Please input file name: ")
                    print(resource.create_file(file_name))
                elif user_input == "2":
                    file_name = input("Please input the filename to be read: ")
                    print(resource.read_file(file_name))
                elif user_input == "3":
                    file_name = input("Please input the filename to be updated: ")
                    if resource.check_file() == True:
                        resource.update_file(file_name)
                    else:
                        print(file_name)
                elif user_input == "4":
                    file_name = input("Please input the filename to be removed: ")
                    resource.delete_file()
                else:
                    print("Invalid option")  
                    
        def run(): 
            showMainMenu() #! Display the main menu
        
        run()

class Resource:
    """_summary_
    Class responsible for the operations of file collection, management, etc.
    """
    def create_file(self, file_name):
        """_summary_

        Args:
            file_name (str): the file name and extension

        Returns:
            str: returns a statement on whether the file already exists or has been successfully created
        """
        if os.path.exists(file_name):
            return "File already exists!"
        else:
            open(file_name, "x")
            return "File " + file_name + " has been created."

    def read_file(self, file_name):
        """_summary_

        Args:
            file_name (str): the file name and extension

        Returns:
            str: Returns a statement declaring that the desired file does not exist
        """
        if os.path.exists(file_name):
            file_name.read()
        else:
            return "File does not exist."

    def check_file(self, file_name):
        """_summary_
        Primarily for updating files to check
        whether or not the desired file exists
        Args:
            file_name (str): the file name and extension

        Returns:
            bool: returns True declaring that the file exists
            or
            str:  returns the statement declaring that the file does not exist
        """
        if  os.path.exists(file_name):
            return True
        else:
            return "File does not exist."
        
    def update_file(self, file_name):
        file_name.write()
        open(file_name, "w")

    def delete_file(self, file_name):
        if os.path.exists(file_name):
            if file_name != "application.py" or file_name != "Assignment 4 Report.docx" or file_name != "library.json":
                os.remove(file_name)
            else:
                return "Cannot delete file."
        else:
            return "File does not exist."

#! Program Execution
Program()