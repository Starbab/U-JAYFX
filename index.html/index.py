import datetime
import os 

DIARY_FILE = "diary . txt"

def add_entry():
    print("\n--- Add New Entry --")
    entry = input("write your entry:\n")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S")
    with open(DIARY_FILE, "a") as file:
        file.write(f"\n[{date}]\n{entry}\n{'-'*40}\n")
        print("Entry added successfully")
        
        def view_entries():
            print("\n--- All diary entries ---")
            if not os.path.exists(DIARY_FILE):
                 print("No entries yet.")
            return
        with open(DIARY_FILE, "r") as file:
            print(file.read())
            
        def search_entriesa():
            keyword = input("\nEnter keyword to search: ").lower()
        if not os.path.exists(DIARY_FILE):
            print("No entries to search.")
            return 
            found = False 
            with open(DIARY_FILE, "r") as file:
                entries = file.read().split('-'*40)
            for entry in entries:
             if keyword in entry.lower():
               print(entry.strip())
               print("-" *40)
               found = True
            if not found:
                print("No matching entries found.")
            def main():
             while true:
                 print("\n My diary app")
                 print("1. Add Entry")
                 print("2. view All Entries")
                 print("3. Search Entries")
                 print("4.Exit")
                 chioce = ("choose an option (1-4):")
                 if choice == '1':
                     add_entry()
                 elif choice == '2':
                     view_entries()
                 elif choice == '3':
                     search_entries()
                 elif choice == '4':
                     print("goodbye!")
                     break
                 else:
                    print("Invalid choice. please try again.")
            if  __name__ == "__main__":
                main()
                    