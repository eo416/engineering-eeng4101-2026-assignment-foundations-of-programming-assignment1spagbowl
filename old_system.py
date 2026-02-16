n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

# active = True (not used)

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    # Initialize crew lists
    names = []
    ranks = []
    divisions = []
    
    # Fixed loading loop with increment
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        # Fixed comparison operator (== instead of =)
        if opt == "1":  
            print("Current Crew List:")
            # Fixed looping through actual list length
            for i in range(len(names)):
                print(f"{names[i]} - {ranks[i]} ({divisions[i]})")
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
            # Append to all three lists
            names.append(new_name)
            ranks.append(new_rank)
            divisions.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
            # Handle name not found
            if rem in names:
                idx = names.index(rem)
                names.pop(idx)
                ranks.pop(idx)
                divisions.pop(idx)
                print("Removed.")
            else:
                print("Crew member not found!")
                
        elif opt == "4":
            print("Analyzing...")
            count = 0
            # Fixed condition syntax
            for rank in ranks:
                if rank == "Captain" or rank == "Commander": 
                    count += 1
            # Convert count to string for concatenation
            print("High ranking officers: " + str(count)) 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid option.")
        
        # Database status check
        if names:
            print("Database has entries.")
        else:
            print("Database empty.")
        
        # Simplified fuel simulation
        fuel = 100
        print("Idling...")
        
        print("End of cycle.")
run_system_monolith()
