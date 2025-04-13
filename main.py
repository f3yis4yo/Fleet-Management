"""
FUNCTIONS AND HELP FUNCTIONS 
"""

#MAIN LISTS FOR PROGRAM 
Fleet_veh_list = [] #List from 0 mainly for Fleet management
"""Fleet_veh_list([Veh_ID,Veh_Type,Veh_Capacity]) """
Shipment_list = []  #List from 0 mainly for Shipment management
"""Shipment_list([Shipment_ID, Origin_loc, Destination, Weight,Veh_ID.]) """
# Delivery_list = []
"""Initial variables"""
userOption = 0
#burned value for the validation test
test = [{"ID": "A123456789", "OLocation":"Sydney", "Dlocation":"Melbourne", "Weight":500, "IDVehiculo":"EXV25HJ"},
        {"ID": "A123456780", "OLocation":"Sydney", "Dlocation":"Melbourne", "Weight":500, "IDVehiculo":"EXV30HJ"}]

""" MENU'S DISPLAY """

def display_MM():
    # DISPLAY MM -> MAIN MENU
    print("\n===== MAIN MENU =====")
    print("----------------------- \n")
    print("1. FLEET MANAGEMENT")
    print("2. SHIPMENT MANAGEMENT")
    print("3. DELIVERY MANAGEMENT")
    print("4. QUIT\n")

def display_FM():
    #DISPLAY FM -> FLEET MANAGEMENT MENU
    print ("\n===FLEET MANAGEMENT MENU===== ")
    print ("---------------------------- \n")

    print ("1 ADD A VEHICLE ")
    print ("2 UPDATE VEHICLE INFORMATION")
    print ("3 REMOVE VEHICLE")
    print ("4 VIEW ALL VEHICLES")
    print ("5 QUIT \n")
    
def display_SM():
    #DISPLAY SHIPMENT MANAGEMENT MENU
    print ("\n===SHIPMENT MANAGEMENT MENU===== ")
    print ("---------------------------------- \n")

    print ("1 CREATE A NEW SHIPMENT ")
    print ("2 TRACK SHIPMENT")
    print ("3 VIEW ALL SHIPMENTS")
    print ("4 QUIT \n")

def menuShipment(userOption):
    if userOption == 1:
        createNewShipment()    
    if userOption == 2:
        trackShipment()  
    if userOption == 3:
        viewAllShipments()    

def display_DMS():
    while True:
        userOption = int(input("""This is the system Shipment Management
            1. Create a new shipment.
            2. Track a shipment.
            3. View all shipments.
            4. Quit shipment management.
            Please choose one option: """))
        if userOption == 4:
            return 4
        else:
            menuShipment(userOption)
    

"""HELP FUNCTIONS """
def find_by_id(Name_List,Name_ID):
    #LOOK FOR VEH_ID EXIST IN LIST
    for v in Name_List:
        if v[0]==Name_ID:
            return v
    return None

def is_unique_id(Name_List,Name_ID):
    #VEH_ID BE UNIQUE
    return all (v[0] != Name_ID for v in Name_List)

def is_positive_integer(val):
    #VALUE PROVIDED IS POSITIVE INTEGER THAT HOLDS FLOAT
    return val.replace(".","",1).isdigit() and float(val) > 0

"""MAIN FUNCTIONS OF FM """
def add_veh(Fleet_veh_list):
    #ADD NEW VEHICLE 
    print("\nPlease Follow the instructions and fill the requested data: ")
    
    Veh_ID = input("Enter the new Vehicle ID: ")
    Veh_Type = input("Enter the Vehicle Type: ")
    Veh_Capacity = input("Enter Vehicle capacity in KG: ")
    
    #Veh_capacity MUST BE A + INT THAT HOLDS DECIMALS -> HELP FUNC
    if is_positive_integer(Veh_Capacity):
        #Convert Veh_cap to integer with decimal
        Veh_Capacity = float(Veh_Capacity)
        
        # AND Veh_ID MUST BE UNIQUE IN  Fleet_veh_list
        if is_unique_id(Fleet_veh_list,Veh_ID):
            #ADD TO THE LIST
            Fleet_veh_list.append([Veh_ID,Veh_Type,Veh_Capacity])
               
            print("\nSUCCESSFUL:NEW VEHICLE HAS BEEN ADDED TO THE VEHICLE FLEET LIST\n")    
        else:
            print("\nERROR:VEHICLE ID MUST BE UNIQUE\n")  
    else: 
        print("\nERROR: VEHICLE CAPACITY IS NOT VALID, POSITIVE INTEGER REQUIRED\n")

def update_veh(Fleet_veh_list):
    #UPDATE VEHICLE
    print("\nPlease Follow the instructions and fill the requested data: ")
    
    Update_ID = input("Enter the Vehicle ID of the Vehicle you want to Update:")
    #LOOK THE VALID Veh_ID IN Fleet_veh_list AND MATCHS -> HELP FUNC
    veh = find_by_id(Fleet_veh_list,Update_ID)
    
    if veh:
        #PROMPT USER FOR NEW VEHICLE INFO
        New_Veh_Type = input("What is the new Vehicle Type?: ")
        New_Veh_Cap = input("What is the new Vehicle Capacity?: ")
        #VALIDATE New_Veh_Cap POSITIVE INTEGER -> HELP FUNC
        if is_positive_integer(New_Veh_Cap):
            #UPDATE NEW INFO INTO LIST
            veh[1],veh[2] =  New_Veh_Type,float(New_Veh_Cap)
            print("\nSUCCESS: Vehicle information has been updated into List \n")
        else:
            print("\nERROR: VEHICLE CAPACITY IS NOT VALID, POSITIVE INTEGER REQUIRED\n")
    else:
        print("\nERROR: VEHICLE ID NOT FOUND ON THE DATA BASE\n") 

def remove_veh():
    #REMOVE VEHICLE FROM THE LIST 3
    print("\nPlease Follow the instructions and fill the requested data: ")
    
    Remove_ID = input("Enter the Vehicle ID of the Vehicle you want to remove: ")
    #LOOK THE VALID Veh_ID IN Fleet_veh_list AND MATCHS -> HELP FUNC
    veh = find_by_id(Fleet_veh_list,Remove_ID)
    
    if  veh:
        print("\nThe Following Vehicle will be remove from list:\n")
        print("-> Vehicle ID: ",veh[0])
        print("-> Vehicle Type: ",veh[1])
        print("-> Vehicle Capacity: ",veh[2])
        #ASK CONFIRMATION
        Confirm = input("\nARE YOU SURE YOU WANT TO REMOVE THIS VEHICLE? (YES/NO) : ")
        #remain upper case
        if Confirm.upper() == "YES":
            #REMOVE THE VEHICLE
            Fleet_veh_list.remove(veh) 
            print("\nSuccess: VEHICLE HAS BEEN REMOVED FROM THE VEHICLE FLEET LIST\n")    
        else:
            print("\nCANCELED: VEHICLE WAS NOT REMOVED FROM THE VEHICLE FLEET LIST\n")
    else:
        print("\nERROR: VEHICLE ID NOT FOUND ON THE DATA BASE\n")

#Function to Create a new Shipment
def createNewShipment():
    shiomentID = input("""Create a new Shipment
        Please writhe the information.
        Shipment ID: """)
    
    validData = True
    for i in test:
        if shiomentID == i['ID']:
            validData = False
            print('Error: Shipment ID is not unique')
            break #add break so the code dont keep searching after finding a match.

    if validData: # add this verification so the program only ask for the next inputs if the ID is valid.
        originLocation = input("Origen location: ")
        dlocation = input("Destination location: ")
        weight = int(input("Weight: "))
        if weight < 0:
            validData = False
            print('Error: Invalid Weight')
    if validData:   
        vehicleID = input("Vehicle ID: ")

        new_shipment = {
                "ID": shiomentID,
                "OLocation": originLocation,
                "Dlocation": dlocation,
                "Weight": weight,
                "IDVehiculo": vehicleID
        }
        test.append(new_shipment)

        
#Function to Create a new Shipment
def trackShipment():
    shiomentID = input("""Create a new Shipment
        Please writhe the information.
        Shipment ID: """)
    found = False 
    for i in test:
        print(i['ID'])
        if shiomentID == i['ID']:
            print("{:<15} {:<20} {:<30} {:<15} {:<15}".format("ID", "Origen Location", "Destination Location","Weight" ,"ID Vehiculo"))
            print("{:<15} {:<20} {:<30} {:<15} {:<15}".format(i["ID"], i["OLocation"], i["Dlocation"], i["Weight"], i["IDVehiculo"]))
            break
    if not found:
        print('Error: Shipment ID Not Found')


#Function to View all shipments
def viewAllShipments():
    print("{:<15} {:<20} {:<30} {:<15} {:<15}".format("ID", "Origen Location", "Destination Location","Weight" ,"ID Vehiculo"))
    for i in test:
        print("{:<15} {:<20} {:<30} {:<15} {:<15}".format(i["ID"], i["OLocation"], i["Dlocation"], i["Weight"], i["IDVehiculo"]))
      

def view_veh():
    #DISPLAY A TABULAR LIST OF Fleet_veh_list
    print("\n =========== VEHICLES FLEET LIST ==============")
    print("-------------------------------------------------")
    print("{:<15} {:<15} {:<15}".format("ID", "TYPE", "CAPACITY"))
    print("-------------------------------------------------")
    
    for veh in Fleet_veh_list:
        print("{:<15} {:<15} {:<15}".format(veh[0], veh[1], veh[2]))
        
#MAIN LOOP MENU
while True:
    #DISPLAY MAIN MENU
    display_MM()

    # GET USER CHOICE
    choice = input("PLEASE SELECT AN OPTION FROM THE MAIN MENU (1-4): \n")

    # CHECK IF INPUT IS VALID
    if choice.isdigit():
        choice = int(choice)

        # MAIN MENU FLEET MANAGEMENT MENU
        if choice == 1:
            

            #CONTINUALLY PROMPT
            while True:
                #DISPLAR FLEET MANAGEMET MENU
                display_FM()
                #PROMPT USER TO SELECT A FUNCTION FROM THE MENU
                FM_option = input("PLEASE SELECT AN OPTION FROM FLEET MANAGEMENT MENU  (1-5): \n")

                #QUIT PROGRAM 5
                if FM_option == '5' :
                    print("\nEXITING FLEET MANAGEMENT MENU\n")
                    break
                #ADD NEW VEHICLE 1
                elif FM_option == '1':
                    add_veh(Fleet_veh_list)
                    continue
                #UPDATE VEHICLE FROM THE LIST 2
                elif FM_option == '2':
                    update_veh(Fleet_veh_list)
                    continue
                #REMOVE VEHICLE FROM THE LIST 3
                elif FM_option == '3':
                    remove_veh()
                    continue
                #VIEW ALL VEHICLES 4 
                elif FM_option == '4':
                     view_veh()
                     break
                #DISPLAY INVALID OPTION
                else:
                    print("\nERROR:PLEASE SELECT AN OPTION FROM FLEET MANAGEMENT MENU (1-5)\n")
                
        
        #MAIN MENU SHIPMENT MANAGEMENT      
        elif choice == 2:
            returnData =  display_DMS()
            if returnData == 4:
                #DISPLAY MAIN MENU
                display_MM()

        #MAIN MENU DELIVERY MANAGEMENT
        elif choice == 3:
            
            while True:
                
                #DISPLAY MAIN MENU
                display_DM()

                #PROPMT USER TO SELECT OPTION
                DM_option = int(input("PLEASE SELECT AN OPTION FROM THE  DELIVERY MANAGEMENT MENU (1-3): \n"))
                
                #QUIT PROGRAM 3
                if DM_option == 3 :
                    print("\nEXITING DELIVERY MANAGEMENT MENU\n")
                    break
                
                #MARK SHIPMENT DELIVERY 1
                elif DM_option == 1:
                    print("\n -> MARK SHIPMENT DELIVERY FUNCTION\n")
                    continue
                
                #VIEW DELIVERY STATUS  2
                elif DM_option == 2:
                    print("\n -> VIEW DELIVERY STATUS FUNCTION\n")
                    continue

        #MAIN MENU QUIT ENTIRE PROGRAM
        elif choice == 4:
            print("\nEXITING THE APP. GOODBYE!")
            break  

        else:
            print("ERROR:PLEASE SELECT AN OPTION FROM MAIN MENU (1-4\n")
            continue

    else:
        print("\nERROR:TYPE NOT SUPPORTED, PLEASE SELECT AN OPTION FROM MAIN MENU (1-4)\n")
        continue"""
FUNCTIONS AND HELP FUNCTIONS 
"""

#MAIN LISTS FOR PROGRAM 
Fleet_veh_list = [] #List from 0 mainly for Fleet management
"""Fleet_veh_list([Veh_ID,Veh_Type,Veh_Capacity]) """
Shipment_list = []  #List from 0 mainly for Shipment management
"""Shipment_list([Shipment_ID, Origin_loc, Destination, Weight,Veh_ID.]) """
# Delivery_list = []

""" MENU'S DISPLAY """

def display_MM():
    # DISPLAY MM -> MAIN MENU
    print("\n===== MAIN MENU =====")
    print("----------------------- \n")
    print("1. FLEET MANAGEMENT")
    print("2. SHIPMENT MANAGEMENT")
    print("3. DELIVERY MANAGEMENT")
    print("4. QUIT\n")

def display_FM():
    #DISPLAY FM -> FLEET MANAGEMENT MENU
    print ("\n===FLEET MANAGEMENT MENU===== ")
    print ("---------------------------- \n")

    print ("1 ADD A VEHICLE ")
    print ("2 UPDATE VEHICLE INFORMATION")
    print ("3 REMOVE VEHICLE")
    print ("4 VIEW ALL VEHICLES")
    print ("5 QUIT \n")
    
def display_SM():
    #DISPLAY SHIPMENT MANAGEMENT MENU
    print ("\n===SHIPMENT MANAGEMENT MENU===== ")
    print ("---------------------------------- \n")

    print ("1 CREATE A NEW SHIPMENT ")
    print ("2 TRACK SHIPMENT")
    print ("3 VIEW ALL SHIPMENTS")
    print ("4 QUIT \n")
    

def display_DM():
    #DISPLAY DELIVERY MANAGEMENT MENU
    print ("\n===DELIVERY MANAGEMENT MENU===== ")
    print ("---------------------------------- \n")

    print ("1 RECORD DELIVERY FOR A SHIPMENT ")
    print ("2 VIEW DELIVERY STATUS FOR A SHIPMENT")
    print ("3 QUIT \n")
    

"""HELP FUNCTIONS """
def find_by_id(Name_List,Name_ID):
    #LOOK FOR VEH_ID EXIST IN LIST
    for v in Name_List:
        if v[0]==Name_ID:
            return v
    return None

def is_unique_id(Name_List,Name_ID):
    #VEH_ID BE UNIQUE
    return all (v[0] != Name_ID for v in Name_List)

def is_positive_integer(val):
    #VALUE PROVIDED IS POSITIVE INTEGER THAT HOLDS FLOAT
    return val.replace(".","",1).isdigit() and float(val) > 0

"""MAIN FUNCTIONS OF FM """
def add_veh(Fleet_veh_list):
    #ADD NEW VEHICLE 
    print("\nPlease Follow the instructions and fill the requested data: ")
    
    Veh_ID = input("Enter the new Vehicle ID: ")
    Veh_Type = input("Enter the Vehicle Type: ")
    Veh_Capacity = input("Enter Vehicle capacity in KG: ")
    
    #Veh_capacity MUST BE A + INT THAT HOLDS DECIMALS -> HELP FUNC
    if is_positive_integer(Veh_Capacity):
        #Convert Veh_cap to integer with decimal
        Veh_Capacity = float(Veh_Capacity)
        
        # AND Veh_ID MUST BE UNIQUE IN  Fleet_veh_list
        if is_unique_id(Fleet_veh_list,Veh_ID):
            #ADD TO THE LIST
            Fleet_veh_list.append([Veh_ID,Veh_Type,Veh_Capacity])
               
            print("\nSUCCESSFUL:NEW VEHICLE HAS BEEN ADDED TO THE VEHICLE FLEET LIST\n")    
        else:
            print("\nERROR:VEHICLE ID MUST BE UNIQUE\n")  
    else: 
        print("\nERROR: VEHICLE CAPACITY IS NOT VALID, POSITIVE INTEGER REQUIRED\n")

def update_veh(Fleet_veh_list):
    #UPDATE VEHICLE
    print("\nPlease Follow the instructions and fill the requested data: ")
    
    Update_ID = input("Enter the Vehicle ID of the Vehicle you want to Update:")
    #LOOK THE VALID Veh_ID IN Fleet_veh_list AND MATCHS -> HELP FUNC
    veh = find_by_id(Fleet_veh_list,Update_ID)
    
    if veh:
        #PROMPT USER FOR NEW VEHICLE INFO
        New_Veh_Type = input("What is the new Vehicle Type?: ")
        New_Veh_Cap = input("What is the new Vehicle Capacity?: ")
        #VALIDATE New_Veh_Cap POSITIVE INTEGER -> HELP FUNC
        if is_positive_integer(New_Veh_Cap):
            #UPDATE NEW INFO INTO LIST
            veh[1],veh[2] =  New_Veh_Type,float(New_Veh_Cap)
            print("\nSUCCESS: Vehicle information has been updated into List \n")
        else:
            print("\nERROR: VEHICLE CAPACITY IS NOT VALID, POSITIVE INTEGER REQUIRED\n")
    else:
        print("\nERROR: VEHICLE ID NOT FOUND ON THE DATA BASE\n") 

def remove_veh():
    #REMOVE VEHICLE FROM THE LIST 3
    print("\nPlease Follow the instructions and fill the requested data: ")
    
    Remove_ID = input("Enter the Vehicle ID of the Vehicle you want to remove: ")
    #LOOK THE VALID Veh_ID IN Fleet_veh_list AND MATCHS -> HELP FUNC
    veh = find_by_id(Fleet_veh_list,Remove_ID)
    
    if  veh:
        print("\nThe Following Vehicle will be remove from list:\n")
        print("-> Vehicle ID: ",veh[0])
        print("-> Vehicle Type: ",veh[1])
        print("-> Vehicle Capacity: ",veh[2])
        #ASK CONFIRMATION
        Confirm = input("\nARE YOU SURE YOU WANT TO REMOVE THIS VEHICLE? (YES/NO) : ")
        #remain upper case
        if Confirm.upper() == "YES":
            #REMOVE THE VEHICLE
            Fleet_veh_list.remove(veh) 
            print("\nSuccess: VEHICLE HAS BEEN REMOVED FROM THE VEHICLE FLEET LIST\n")    
        else:
            print("\nCANCELED: VEHICLE WAS NOT REMOVED FROM THE VEHICLE FLEET LIST\n")
    else:
        print("\nERROR: VEHICLE ID NOT FOUND ON THE DATA BASE\n")

def view_veh():
    #DISPLAY A TABULAR LIST OF Fleet_veh_list
    print("\n =========== VEHICLES FLEET LIST ==============")
    print("-------------------------------------------------")
    print("{:<15} {:<15} {:<15}".format("ID", "TYPE", "CAPACITY"))
    print("-------------------------------------------------")
    
    for veh in Fleet_veh_list:
        print("{:<15} {:<15} {:<15}".format(veh[0], veh[1], veh[2]))
        
#MAIN LOOP MENU
while True:
    #DISPLAY MAIN MENU
    display_MM()

    # GET USER CHOICE
    choice = input("PLEASE SELECT AN OPTION FROM THE MAIN MENU (1-4): \n")

    # CHECK IF INPUT IS VALID
    if choice.isdigit():
        choice = int(choice)

        # MAIN MENU FLEET MANAGEMENT MENU
        if choice == 1:
            

            #CONTINUALLY PROMPT
            while True:
                #DISPLAR FLEET MANAGEMET MENU
                display_FM()
                #PROMPT USER TO SELECT A FUNCTION FROM THE MENU
                FM_option = input("PLEASE SELECT AN OPTION FROM FLEET MANAGEMENT MENU  (1-5): \n")

                #QUIT PROGRAM 5
                if FM_option == '5' :
                    print("\nEXITING FLEET MANAGEMENT MENU\n")
                    break
                #ADD NEW VEHICLE 1
                elif FM_option == '1':
                    add_veh(Fleet_veh_list)
                    continue
                #UPDATE VEHICLE FROM THE LIST 2
                elif FM_option == '2':
                    update_veh(Fleet_veh_list)
                    continue
                #REMOVE VEHICLE FROM THE LIST 3
                elif FM_option == '3':
                    remove_veh()
                    continue
                #VIEW ALL VEHICLES 4 
                elif FM_option == '4':
                     view_veh()
                     break
                #DISPLAY INVALID OPTION
                else:
                    print("\nERROR:PLEASE SELECT AN OPTION FROM FLEET MANAGEMENT MENU (1-5)\n")
                
        
        #MAIN MENU SHIPMENT MANAGEMENT      
        elif choice == 2:
            while True:
                
                #DISPLAY MAIN MENU
                display_SM()
                
                #PROMPT USER TO SELECT OPTION
                SM_option = int(input("Please select an option from SHIPMENT MANAGEMENT MENU (1-4): \n"))
                
                #QUIT PROGRAM 4
                if SM_option == 4 :
                    print("\nExiting Shipment Management Menu\n")
                    break
                
                #ADD NEW SHIPMENT 1 // DRAFT CREATING RELATION TO FLEET LIST TO SHOW VEH_ID AVAILABLES
                elif SM_option == 1:
                    
                    print("\n -> ADD NEW SHIPMENT FUNCTION\n")
                    print("\nPlease Follow the instructions and fill the requested data: ")
                    
                    Shipment_ID = input("Enter the new Shipment ID: ")
                    Orig_Location = input("Enter the Origin location for shipment: ")
                    Dest_Loc = input("Enter the Destination location for shipment: ")
                    Shipment_Weight = input("Enter Shipment Weight: ")
                    
                    #SHIPMENT ID UNIQUE -> HELP FUNC
                    if is_unique_id(Shipment_list,Shipment_ID):
                        #SHIP_WIGHT POSITIVE INTEGER
                        if is_positive_integer(Shipment_Weight):
                            #Convert Shipment_Weight to integer with decimal
                            Shipment_Weight = float(Shipment_Weight)
                            
                            #DISPLAY TABULAR CURRENT FLEET VEHICLE LIST
                            view_veh()
                            
                            #PROMPT USER TO ENTER VEH_ID FROM TABLE
                            Veh_ID_Searched = input("\nEnter the Existing Vehicle ID: \n")
                            veh = find_by_id(Fleet_veh_list,Veh_ID_Searched)
                            
                            #VALIDATE VEHICLE ID EXITS -> HELP FUNC
                            if veh:
                                new_shipment = [Shipment_ID,Orig_Location,Dest_Loc,Shipment_Weight,Veh_ID_Searched]
                                #ADD TO THE LIST
                                Shipment_list.append(new_shipment)
                                print("\nSUCCESSFUL: New Shipment has been added to the Shipment List\n")
                                print("Shipment current list:",Shipment_list ) #verify that list is being saved
                                
                                
                                continue
                            
                            else:
                                print("\nERROR: VEHICLE ID NOT FOUND ON THE DATA BASE\n")
                        else:
                            print("\nERROR: Shipment Weight Invalid, must be a positive numeric value\n")
                            continue
                    else:
                        print("\nERROR: VEHICLE ID MUST BE UNIQUE\n")
                        continue  
        
                #TRACK A SHIPMENT 2
                elif SM_option == 2:
                    print("\n -> TRACK SHIPMENT FUNCTION\n")
                    continue
                
                #VIEW ALL SHIPMENTS 3
                elif SM_option == 3:
                    print("\n -> VIEW SHIPMENT FUNCTION\n")
                    continue
                    

        #MAIN MENU DELIVERY MANAGEMENT
        elif choice == 3:
            
            while True:
                
                #DISPLAY MAIN MENU
                display_DM()
                
                #PROPMT USER TO SELECT OPTION
                DM_option = int(input("PLEASE SELECT AN OPTION FROM THE  DELIVERY MANAGEMENT MENU (1-3): \n"))
                
                #QUIT PROGRAM 3
                if DM_option == 3 :
                    print("\nEXITING DELIVERY MANAGEMENT MENU\n")
                    break
                
                #MARK SHIPMENT DELIVERY 1
                elif DM_option == 1:
                    print("\n -> MARK SHIPMENT DELIVERY FUNCTION\n")
                    continue
                
                #VIEW DELIVERY STATUS  2
                elif DM_option == 2:
                    print("\n -> VIEW DELIVERY STATUS FUNCTION\n")
                    continue

        #MAIN MENU QUIT ENTIRE PROGRAM
        elif choice == 4:
            print("\nEXITING THE APP. GOODBYE!")
            break  

        else:
            print("ERROR:PLEASE SELECT AN OPTION FROM MAIN MENU (1-4\n")
            continue

    else:
        print("\nERROR:TYPE NOT SUPPORTED, PLEASE SELECT AN OPTION FROM MAIN MENU (1-4)\n")
        continue