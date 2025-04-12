userOption = 0
#burned value for the validation test
test = [{"ID": "A123456789", "OLocation":"Sydney", "Dlocation":"Melbourne", "Weight":500, "IDVehiculo":"EXV25HJ"},
        {"ID": "A123456780", "OLocation":"Sydney", "Dlocation":"Melbourne", "Weight":500, "IDVehiculo":"EXV30HJ"}]


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
    
    validData = True
    for i in test:
        if shiomentID != i['ID']:
            validData = False
            print('Error: Shipment ID Not Found')
            break #add break so the code dont keep searching after finding a match.
        if shiomentID == i['ID']:
            print("{:<15} {:<20} {:<30} {:<15} {:<15}".format("ID", "Origen Location", "Destination Location","Weight" ,"ID Vehiculo"))
            print("{:<15} {:<20} {:<30} {:<15} {:<15}".format(i["ID"], i["OLocation"], i["Dlocation"], i["Weight"], i["IDVehiculo"]))


#Function to View all shipments
def viewAllShipments():
    print("{:<15} {:<20} {:<30} {:<15} {:<15}".format("ID", "Origen Location", "Destination Location","Weight" ,"ID Vehiculo"))
    for i in test:
        print("{:<15} {:<20} {:<30} {:<15} {:<15}".format(i["ID"], i["OLocation"], i["Dlocation"], i["Weight"], i["IDVehiculo"]))
        

#Function to choose a menu
def menu(userOption):
    if userOption == 1:
        createNewShipment()    
    if userOption == 2:
        trackShipment()  
    if userOption == 3:
        viewAllShipments()


#Cycle to menu
while userOption != 4:
    userOption = int(input("""This is the system Shipment Management
        1. Create a new shipment.
        2. Track a shipment.
        3. View all shipments.
        4. Quit shipment management.
        Please choose one option: """))
    menu(userOption)