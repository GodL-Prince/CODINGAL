import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init(autoreset=True)

print(f"{Fore.CYAN}🕵️ Welcome to Sentiment Spy! 🔍{Style.RESET_ALL}")

user_name = input(
    f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}"
).strip()

if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!{Style.RESET_ALL}")

print(
    f"{Fore.CYAN}Type a sentence and I will analyze its sentiment using TextBlob."
)

print(
    f"Type {Fore.YELLOW}'history'{Fore.CYAN}, "
    f"{Fore.YELLOW}'reset'{Fore.CYAN}, or "
    f"{Fore.YELLOW}'exit'{Fore.CYAN} to quit."
    f"{Style.RESET_ALL}\n"
)

while True:

    user_input = input(
        f"{Fore.GREEN}>> {Style.RESET_ALL}"
    ).strip()

    if not user_input:
        print(
            f"{Fore.RED}Please enter some text or a valid command."
            f"{Style.RESET_ALL}"
        )
        continue

    if user_input.lower() == "exit":
        print(
            f"\n{Fore.BLUE}👋 Exiting Sentiment Spy."
            f" Farewell, Agent {user_name}! 🔍"
            f"{Style.RESET_ALL}"
        )
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()

        print(
            f"{Fore.CYAN}🗑️ All conversation history cleared!"
            f"{Style.RESET_ALL}"
        )
        continue

    elif user_input.lower() == "history":

        if not conversation_history:
            print(
                f"{Fore.YELLOW}No conversation history yet."
                f"{Style.RESET_ALL}"
            )

        else:
            print(
                f"\n{Fore.CYAN}📜 Conversation History:"
                f"{Style.RESET_ALL}"
            )

            for idx, (
                text,
                polarity,
                sentiment_type
            ) in enumerate(conversation_history, start=1):

                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"

                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"

                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(
                    f"{idx}. {color}{emoji} {text} "
                    f"(Polarity: {polarity:.2f}, "
                    f"{sentiment_type})"
                    f"{Style.RESET_ALL}"
                )

        continue

    analysis = TextBlob(user_input)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"

    elif polarity < 0:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"

    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append(
        (
            user_input,
            polarity,
            sentiment_type
        )
    )

    print(
        f"{color}{emoji} Sentiment Analysis Result:"
        f"{Style.RESET_ALL}"
    )

    print(
        f"{color}Polarity Score: {polarity:.2f}"
        f"{Style.RESET_ALL}"
    )

    print(
        f"{color}Sentiment Type: {sentiment_type}"
        f"{Style.RESET_ALL}\n"
    )