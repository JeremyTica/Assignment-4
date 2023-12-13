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
                        resource_content = Resource_Manager().read_resource(resource_type.capitalize())
                        
                        for content in resource_content:
                            for info in content:
                                if info == "name":
                                    print("Name:", content[info])
                                elif info == "year":
                                    print("Year:", content[info])
                                elif info == "author" or info == "producer" or info == "studio":
                                    print(info.capitalize() + ":", content[info])
                                else:
                                    print("Available")
                            print()
                    else:
                        print("Invalid resource!")

                #! UPDATE/EDIT CHARACTERISTICS
                elif user_input == "3":
                    while True:
                        os.system("cls")
                        resource_options = Resource_Manager().update_resource()
                        for resources in resource_options:
                            print(resources)
                        print()
                        user_selection = input("Please select a collection of resources that are available:\n\n")
                        for resources in resource_options:
                            if resources == user_selection:
                                break
                            else:
                                print("Invalid option!")
                    resource_type = input("Please input the resource to be updated: ")
                    if resource_type.lower() == "guidebooks":
                        os.system("cls")
                    else:
                        os.system("cls")
                        print("Invalid resource!")

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

    def getName(self):
        return self.name
        
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
        
class Decoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        decoded_object =  Resource(
            obj.get("name"),
            obj.get("year"),
            obj.get("author"),
            obj.get("is_available")
        )
        return decoded_object

class Resource_Manager:
    def read_resource(self, resource):
        list_of_resources = []
        with open("library.json", "r") as f:
            data = json.load(f)

        for info in data[resource]:
            if info["is_available"] == True:
                list_of_resources.append(info)
        return list_of_resources

    def add_resource(self, resource):
        with open("library.json", "a") as f:
            json.dump(resource, f, cls=Encoder, indent=4)
            f.close()

    def update_resource(self):
        list_of_resources = []
        with open("library.json", "r") as f:
            data = json.load(f)

        for resources in data:
            list_of_resources.append(resources)
        return list_of_resources


    def delete_resource(self, resource, name):
        with open("library.json", "r") as f:
            data = json.load(f)

            count = 0
            for info in data[resource]:
                if info.get("name") == name:
                    data[resource].pop(count)
                    print(data[resource])
                count+=1



            
        

class Data_Persistence:
    def data_rewrite():
        pass

#! Program Execution
Program()