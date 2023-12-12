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

        def showMainMenu():
            """_summary_
            Display the main menu the user will use to
            interact with to modify or create resources within the library.json
            """
            while True:
                choosing = False
                user_input = input("Welcome to the Programming Library System\n\n[1] Create\n[2] Read\n[3] Update\n[4] Delete\n\n") 
                os.system("cls")

                #! WRITE
                if user_input == "1":
                    choosing = True
                    while choosing:
                        resource_type = input("What resource will you be adding to the library:\n\nGuidebooks\nMovies\nGames\n\n")
                        if resource_type.lower() == "guidebooks":
                            resource_name = input("Please input the name of the guidebook: ")
                            resource_year = input("Please input year of publication: ")
                            resource_author = input("Please input author of the guidebook: ")
                            new_resource = Resource(resource_name, resource_year, resource_author, "author")
                            Resource_Manager().add_resource(new_resource)
                            break
                        elif resource_type.lower() == "movies":
                            resource_name = input("Please input the name of the guidebook: ")
                            resource_year = input("Please input year of publication: ")
                            resource_author = input("Please input author of the guidebook: ")
                            new_resource = Resource(resource_name, resource_year, resource_author, "producer")
                            Resource_Manager().add_resource(new_resource)
                            break
                        elif resource_type.lower() == "games":
                            resource_name = input("Please input the name of the guidebook: ")
                            resource_year = input("Please input year of publication: ")
                            resource_author = input("Please input author of the guidebook: ")
                            new_resource = Resource(resource_name, resource_year, resource_author, "author")
                            Resource_Manager().add_resource(new_resource)
                            break
                        else:
                            os.system("cls")
                            print("Invalid resource!")

                #! READ 
                elif user_input == "2":
                    resource_type = input("Please choose which resources to view:\n\nGuidebooks\nMovies\nGames\n\n")
                    os.system("cls")
                    if resource_type.lower() == "guidebooks" or resource_type.lower() == "movies" or resource_type.lower() == "games":
                        Resource_Manager().read_resource(resource_type.capitalize())
                    else:
                        print("Invalid resource!")

                #! UPDATE/EDIT CHARACTERISTICS
                elif user_input == "3":
                    file_name = input("Please input the filename to be updated: ")
                    if resource.check_file(file_name) == True:
                        file_content = input("Please input what you would like to add the to the file: ")
                        resource.update_file(file_name, file_content)
                        os.system("cls")
                    else:
                        os.system("cls")
                        print("File does not exist.")

                #! DELETE
                elif user_input == "4":
                    resource_type = input("Please choose which resources to view:\n\nGuidebooks\nMovies\nGames\n\n")
                    name_of_resource = input("Please input the name of the resource: ")
                    if resource_type.lower() == "guidebooks" or resource_type.lower() == "movies" or resource_type.lower() == "games":
                        Resource_Manager().delete_resource(resource_type.capitalize(), name_of_resource)
                    else:
                        print("Invalid resource!")
                    
        def run(): 
            os.system("cls")
            showMainMenu() #! Display the main menu
        
        run()

class Resource:
    def __init__(self, name, year, creator, creator_type):
        self.name = name
        self.year = year
        self.creator = creator
        self.creator_type = creator_type
        self.is_available = True
        
class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Resource):
            return {
            "name" : obj.name,
            "year" : obj.year,
            obj.creator_type : obj.creator,
            "is_available" : obj.is_available
            }
        else:
            return super().default(obj)

class Resource_Manager:
    def read_resource(self, resource):
        with open("library.json", "r") as f:
            data = json.load(f)

        for info in data[resource]:
            if info["is_available"] == True:
                print(info)

    def add_resource(self, resource):
        with open("library.json", "w") as f:
            json.dump(resource, f, cls=Encoder, indent=4)

    def delete_resource(self, resource, name):
        with open("library.json", "r") as f:
            data = json.load(f)

            for info in data[resource]:
                if name == info["name"]:
                    data[resource].pop(1)


            
        

class Data_Persistence:
    pass

#! Program Execution
Program()