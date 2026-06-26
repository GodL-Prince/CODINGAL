#name the file as main.py , uncomment the imports and basic functions, complete  the code by writing remainig functions 

import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Destination & joke data
destinations = {
  "beaches": ["Bali", "Maldives", "Phuket"],
     "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
     "cities": ["Tokyo", "Paris", "New York"]
 }
jokes = [
     "Why don't programmers like nature? Too many bugs!",
     "Why did the computer go to the doctor? Because it had a virus!",
     "Why do travelers always feel warm? Because of all their hot spots!"
 ]

 # Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
     return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def provide_recommendations():
        print(Fore.CYAN + "What type of destination are you interested in? (beaches, mountains, cities)")
        choice = normalize_input(input())
        if choice in destinations:
            suggestion = random.choice(destinations[choice])
            print(Fore.GREEN + f"How about visiting {suggestion}?")
            print("Do you like this suggestion? (yes/no)")
            feedback = normalize_input(input())
            if feedback == "yes":
                print(Fore.YELLOW + "Great! I hope you have an amazing trip!")
            else:
                print(Fore.RED + "No worries, let's try again.")
                provide_recommendations()  # Recursive call for new suggestions
        else:
            print(Fore.RED + "Sorry, I didn't understand that. Please choose from beaches, mountains, or cities.")
            provide_recommendations()  # Recursive call for valid input
 # Offer packing tips based on user’s destination and duration

 # Tell a random joke

 # Display help menu

# Main chat loop
def chat():
    print(Fore.MAGENTA + "Hello! I'm your travel assistant. How can I help you today?")
    while True:
        print(Fore.CYAN + "\nOptions:")
        print("1. Get travel recommendations")
        print("2. Get packing tips")
        print("3. Tell me a joke")
        print("4. Help")
        print("5. Exit")
        choice = normalize_input(input("Please select an option (1-5): "))
        if choice == "1":
            provide_recommendations()
        elif choice == "2":
            pass  # Implement packing tips logic
        elif choice == "3":
            print(Fore.BLUE + random.choice(jokes))
        elif choice == "4":
            print(Fore.YELLOW + "Here are some things I can help you with:")
            print("- Recommend destinations based on your interests")
            print("- Provide packing tips for your trip")
            print("- Share interesting jokes")
        elif choice == "5":
            print(Fore.GREEN + "Thank you for using the travel assistant. Have a great day!")
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")

# Run the chatbot
if __name__ == "__main__":
    chat()
