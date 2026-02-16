# fleet_manager.py
# Simple Python code using parallel lists and 10 functions,
# each invoked from a central main() loop.

# Parallel lists
names = []
ranks = []
divisions = []
ids = []

# 1) Seed sample data (optional helper to quickly populate lists)
def seed_data():
    sample_names = ["Picard", "Riker", "Data", "Worf"]
    sample_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    sample_divs  = ["Command", "Command", "Operations", "Security"]
    sample_ids   = ["NCC-1701-D-01", "NCC-1701-D-02", "NCC-1701-D-03", "NCC-1701-D-04"]
    names.extend(sample_names)
    ranks.extend(sample_ranks)
    divisions.extend(sample_divs)
    ids.extend(sample_ids)
    print("Seeded sample crew.\n")

# 2) Add crew member
def add_crew():
    print("\n--- ADD CREW ---")
    nm = input("Name: ").strip()
    rk = input("Rank: ").strip()
    dv = input("Division: ").strip()
    cid = input("ID: ").strip()

    if not (nm and rk and dv and cid):
        print("All fields are required.")
        return

    if cid in ids:
        print("ID already exists.")
        return

    names.append(nm)
    ranks.append(rk)
    divisions.append(dv)
    ids.append(cid)
    print("Crew member added.")

# 3) View crew
def view_crew():
    print("\n--- CREW MANIFEST ---")
    if not names:
        print("No crew recorded.")
        return
    for i in range(len(names)):
        print(f"{i+1}. {names[i]} | {ranks[i]} | {divisions[i]} | ID: {ids[i]}")

# 4) Search crew by name (exact match)
def search_by_name():
    print("\n--- SEARCH BY NAME ---")
    target = input("Name: ").strip()
    if target in names:
        i = names.index(target)
        print(f"FOUND: {names[i]} | {ranks[i]} | {divisions[i]} | ID: {ids[i]}")
    else:
        print("No match.")

# 5) Remove crew by ID
def remove_by_id():
    print("\n--- REMOVE BY ID ---")
    target = input("ID: ").strip()
    if target in ids:
        i = ids.index(target)
        print(f"Removing {names[i]}...")
        names.pop(i)
        ranks.pop(i)
        divisions.pop(i)
        ids.pop(i)
        print("Removed.")
    else:
        print("ID not found.")

# 6) Update rank by ID
def update_rank():
    print("\n--- UPDATE RANK ---")
    target = input("ID: ").strip()
    if target in ids:
        i = ids.index(target)
        new_rank = input("New rank: ").strip()
        if new_rank:
            ranks[i] = new_rank
            print("Rank updated.")
        else:
            print("No change made.")
    else:
        print("ID not found.")

# 7) Count by division
def count_by_division():
    print("\n--- COUNT BY DIVISION ---")
    dv = input("Division: ").strip()
    count = divisions.count(dv)
    print(f"{count} crew member(s) in {dv}.")

# 8) List unique divisions
def list_divisions():
    print("\n--- DIVISIONS ---")
    uniq = sorted(set(divisions))
    if not uniq:
        print("No divisions recorded.")
        return
    for d in uniq:
        print(f"- {d}")

# 9) Highest ranking officers (simple hierarchy)
def highest_ranking():
    print("\n--- HIGHEST RANKING OFFICERS ---")
    if not ranks:
        print("No crew recorded.")
        return
    hierarchy = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    present = [rk for rk in ranks if rk in hierarchy]
    if not present:
        print("No recognizable ranks found.")
        return
    best = min(present, key=lambda r: hierarchy.index(r))
    print(f"Highest rank present: {best}")
    for i, rk in enumerate(ranks):
        if rk == best:
            print(f"- {names[i]} (ID {ids[i]})")

# 10) Analytics summary
def analytics():
    print("\n--- ANALYTICS ---")
    total = len(names)
    print(f"Total crew: {total}")
    print(f"Unique ranks: {len(set(ranks))}")
    print(f"Unique divisions: {len(set(divisions))}")
    if total:
        # crew per division
        print("Crew per division:")
        for dv in sorted(set(divisions)):
            print(f"  {dv}: {divisions.count(dv)}")

def main():
    # Optional: auto-seed for quick testing; comment out if not desired.
    # seed_data()

    while True:
        print("\n===== FLEET COMMAND =====")
        print("1) Seed Sample Data")
        print("2) Add Crew")
        print("3) View Crew")
        print("4) Search by Name")
        print("5) Remove by ID")
        print("6) Update Rank by ID")
        print("7) Count by Division")
        print("8) List Divisions")
        print("9) Highest Ranking Officers")
        print("10) Analytics")
        print("11) Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            seed_data()
        elif choice == "2":
            add_crew()
        elif choice == "3":
            view_crew()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            remove_by_id()
        elif choice == "6":
            update_rank()
        elif choice == "7":
            count_by_division()
        elif choice == "8":
            list_divisions()
        elif choice == "9":
            highest_ranking()
        elif choice == "10":
            analytics()
        elif choice == "11":
            print("Shutting down.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
