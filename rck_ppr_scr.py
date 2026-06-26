import random

AIMOVES = ["rock", "paper", "scissors"]


def get_user_choice():
    while True:
        user_choice = input(
            "\nEnter your choice (rock, paper, scissors): "
        ).strip().lower()

        if user_choice in AIMOVES:
            return user_choice

        print(
            "❌ Invalid choice. Please enter rock, paper, or scissors."
        )


def get_ai_choice():
    return random.choice(AIMOVES)


def determine_winner(user_choice, ai_choice):

    if user_choice == ai_choice:
        return "tie"

    elif (
        (user_choice == "rock" and ai_choice == "scissors")
        or (user_choice == "paper" and ai_choice == "rock")
        or (user_choice == "scissors" and ai_choice == "paper")
    ):
        return "user"

    else:
        return "ai"


def display_result(user_choice, ai_choice, winner):

    print(f"\n🧑 You chose: {user_choice}")
    print(f"🤖 AI chose: {ai_choice}")

    if winner == "tie":
        print("🤝 It's a tie!")

    elif winner == "user":
        print("🎉 You win!")

    else:
        print("😎 AI wins!")


def play_game():

    user_score = 0
    ai_score = 0
    ties = 0

    print("🎮 Welcome to Rock Paper Scissors!")

    while True:

        user_choice = get_user_choice()
        ai_choice = get_ai_choice()

        winner = determine_winner(
            user_choice,
            ai_choice
        )

        display_result(
            user_choice,
            ai_choice,
            winner
        )

        if winner == "user":
            user_score += 1

        elif winner == "ai":
            ai_score += 1

        else:
            ties += 1

        print("\n📊 Scoreboard")
        print(f"You : {user_score}")
        print(f"AI  : {ai_score}")
        print(f"Ties: {ties}")

        play_again = input(
            "\nPlay another round? (yes/no): "
        ).strip().lower()

        while play_again not in ["yes", "no"]:
            play_again = input(
                "Please enter yes or no: "
            ).strip().lower()

        if play_again == "no":
            break

    print("\n🏁 Final Results")
    print(f"You : {user_score}")
    print(f"AI  : {ai_score}")
    print(f"Ties: {ties}")

    if user_score > ai_score:
        print("🏆 Congratulations! You won the match.")

    elif ai_score > user_score:
        print("🤖 AI wins the match.")

    else:
        print("🤝 Match Draw.")

    print("\nThanks for playing!")


if __name__ == "__main__":
    play_game()