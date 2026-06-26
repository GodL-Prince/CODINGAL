import re
import random
from colorama import Fore, init

init(autoreset=True)

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


def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def provide_recommendations():

    while True:

        print(
            Fore.CYAN +
            "What type of destination are you interested in?"
        )
        print("(beaches, mountains, cities)")

        choice = normalize_input(input("> "))

        if choice not in destinations:
            print(
                Fore.RED +
                "Please choose beaches, mountains or cities."
            )
            continue

        suggestion = random.choice(destinations[choice])

        print(
            Fore.GREEN +
            f"🌍 How about visiting {suggestion}?"
        )

        feedback = normalize_input(
            input("Do you like this suggestion? (yes/no): ")
        )

        if feedback == "yes":
            print(
                Fore.YELLOW +
                "✨ Great! Have an amazing trip!"
            )
            break

        elif feedback == "no":
            print(
                Fore.RED +
                "Let's find another destination..."
            )

        else:
            print(
                Fore.RED +
                "Please answer yes or no."
            )


def packing_tips():

    destination = normalize_input(
        input(
            "Destination type (beaches/mountains/cities): "
        )
    )

    try:
        days = int(
            input(
                "How many days will your trip be? "
            )
        )
    except ValueError:
        print(
            Fore.RED +
            "Please enter a valid number."
        )
        return

    print(Fore.YELLOW + "\n📦 Packing Tips:")

    if destination == "beaches":
        print("- Sunscreen")
        print("- Sunglasses")
        print("- Swimwear")
        print("- Flip-flops")

    elif destination == "mountains":
        print("- Warm jackets")
        print("- Hiking boots")
        print("- Gloves")
        print("- Water bottle")

    elif destination == "cities":
        print("- Comfortable shoes")
        print("- Power bank")
        print("- Travel documents")
        print("- Casual clothing")

    else:
        print("- Basic travel essentials")

    if days > 7:
        print("- Extra clothes for long trip")

    print("- First-aid kit")


def tell_joke():
    print(Fore.BLUE + "😂 " + random.choice(jokes))


def show_help():
    print(Fore.YELLOW + "\nThings I can help you with:")
    print("• Recommend travel destinations")
    print("• Provide packing tips")
    print("• Tell travel-related jokes")
    print("• Help plan your next adventure")


def chat():

    print(
        Fore.MAGENTA +
        "✈️ Hello! I'm your Travel Assistant."
    )

    while True:

        print(Fore.CYAN + "\nOptions:")
        print("1. Get travel recommendations")
        print("2. Get packing tips")
        print("3. Tell me a joke")
        print("4. Help")
        print("5. Exit")

        choice = normalize_input(
            input("Please select an option (1-5): ")
        )

        if choice == "1":
            provide_recommendations()

        elif choice == "2":
            packing_tips()

        elif choice == "3":
            tell_joke()

        elif choice == "4":
            show_help()

        elif choice == "5":
            print(
                Fore.GREEN +
                "Thank you for using the Travel Assistant!"
            )
            break

        else:
            print(
                Fore.RED +
                "Invalid option. Please try again."
            )


if __name__ == "__main__":
    chat()