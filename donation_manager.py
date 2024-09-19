class Donation:
    def __init__(self, item_name, quantity, donor_name):
        self.item_name = item_name
        self.quantity = quantity
        self.donor_name = donor_name

class DonationManager:
    def __init__(self):
        self.donations = []

    def add_donation(self, item_name, quantity, donor_name):
        donation = Donation(item_name, quantity, donor_name)
        self.donations.append(donation)
        print(f"Donation of {quantity} {item_name}(s) from {donor_name} added successfully!")

    def list_donations(self):
        if not self.donations:
            print("No donations recorded.")
            return
        print("List of Donations:")
        for donation in self.donations:
            print(f"- {donation.quantity} {donation.item_name}(s) from {donation.donor_name}")

def main():
    manager = DonationManager()

    while True:
        print("\nWelcome to the Donation Management System")
        print("1. Add Donation")
        print("2. List Donations")
        print("3. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            donor_name = input("Enter the donor's name: ")
            manager.add_donation(item_name, quantity, donor_name)
        elif choice == '2':
            manager.list_donations()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()












git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/donation_manager.git
git push -u origin main
