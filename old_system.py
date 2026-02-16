n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True
# active = True not an assignment
active == True

def run_system_monolith():
    print("BOOTING SYSTEM...")
@@ -28,64 +29,65 @@
        if opt = "1":  
            print("Current Crew List:")

            for i in range(10):
            # for i in range(10): Looping to 10 causes IndexError.
                for i in range(len(n)):
                print(n[i] + " - " + r[i]) 

        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")


            n.append(new_name)
            print("Crew member added.")

        elif opt == "3":
            rem = input("Name to remove: ")

            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")

        elif opt == "4":
            print("Analyzing...")
            count = 0

            for rank in r:
                if rank == "Captain" or "Commander": 
                    count = count + 1
            print("High ranking officers: " + count) 

        elif opt == "5":
            print("Shutting down.")
            break

        else:
            print("Invalid.")


        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")


        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")


        fuel = 100
        consumption = 0
        while fuel > 0:

            print("Idling...")
            break 

        print("End of cycle.")

run_system_monolith
