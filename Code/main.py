import csv
import os
from prettytable import PrettyTable

VOTER_DATABASE = "users.csv"
VOTES_DATABASE = "votes.csv"

ADMIN_PASSWORD = "admin123"  # Simple password for admin access

def load_users():
    """Load the user database (voters) from a CSV file."""
    users = {}
    if os.path.exists(VOTER_DATABASE):
        with open(VOTER_DATABASE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # Ensure the row has the expected number of columns
                if len(row) >= 2:
                    voter_id, name = row
                    users[voter_id] = name
    else:
        print("No user database found!")
    return users

def save_vote(voter_id, vote):
    """Save a vote to the CSV file."""
    with open(VOTES_DATABASE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([voter_id, vote])

def load_votes():
    """Load votes from the CSV file."""
    votes = []
    if os.path.exists(VOTES_DATABASE):
        with open(VOTES_DATABASE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # Ensure the row has the expected number of columns
                if len(row) >= 2:
                    votes.append({"voter_id": row[0], "vote": row[1]})
    return votes

def cast_vote(voter_id, vote):
    """Cast a vote."""
    users = load_users()
    if voter_id not in users:
        print("Invalid voter ID.")
        return
    
    votes = load_votes()
    
    if voter_id in [v["voter_id"] for v in votes]:
        print("This voter has already voted.")
        return
    
    save_vote(voter_id, vote)
    print("Vote successfully cast.")

def tally_votes():
    """Tally the votes and print them in a tabular format."""
    votes = load_votes()

    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["Voter ID", "Vote"]

    for v in votes:
        table.add_row([v["voter_id"], v["vote"]])

    print("\nVote Tally:")
    print(table)

def admin_login():
    """Authenticate admin to allow vote tallying."""
    password = input("Enter admin password: ")
    if password == ADMIN_PASSWORD:
        tally_votes()
    else:
        print("Invalid password.")

def main():
    while True:
        print("\nElectronic Voting System")
        print("1. Cast Vote")
        print("2. Admin Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            voter_id = input("Enter your Voter ID: ")
            vote = input("Enter your vote (candidate name): ")
            cast_vote(voter_id, vote)
        elif choice == "2":
            admin_login()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()