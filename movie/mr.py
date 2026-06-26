import os
import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# ==========================
# DATASET LOADING
# ==========================

possible_paths = [
    "imdb_top_1000.csv",
    "../imdb_top_1000.csv",
    "./imdb_top_1000.csv"
]

df = pd.read_csv("imdb_top_1000.csv")



# ==========================
# GENRES
# ==========================

genres = sorted(
    {
        g.strip()
        for genre_list in df["Genre"].dropna().str.split(", ")
        for g in genre_list
    }
)

# ==========================
# FUNCTIONS
# ==========================

def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)


def senti(p):
    if p > 0:
        return "Positive 😊"
    elif p < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"


def get_genre():

    print(Fore.CYAN + "\nAvailable Genres:\n")

    for i, g in enumerate(genres, start=1):
        print(f"{i}. {g}")

    while True:

        choice = input(
            Fore.YELLOW +
            "\nEnter genre number or name: "
        ).strip()

        if choice.isdigit():

            idx = int(choice)

            if 1 <= idx <= len(genres):
                return genres[idx - 1]

        for g in genres:
            if choice.lower() == g.lower():
                return g

        print(
            Fore.RED +
            "Invalid input. Try again."
        )


def get_rating():

    while True:

        value = input(
            Fore.YELLOW +
            "Enter minimum IMDb rating (7.6-9.3) or 'skip': "
        ).strip().lower()

        if value == "skip":
            return None

        try:

            rating = float(value)

            if 7.6 <= rating <= 9.3:
                return rating

            print(
                Fore.RED +
                "Rating out of range."
            )

        except ValueError:

            print(
                Fore.RED +
                "Invalid input."
            )


def recommend(
    genre=None,
    mood="neutral",
    rating=None,
    n=5
):

    filtered = df.copy()

    # Genre filter
    if genre:

        filtered = filtered[
            filtered["Genre"].str.contains(
                genre,
                case=False,
                na=False
            )
        ]

    # Rating filter
    if rating is not None:

        filtered = filtered[
            filtered["IMDB_Rating"] >= rating
        ]

    if filtered.empty:
        return "No suitable movie recommendations found."

    filtered = filtered.sample(
        frac=1
    ).reset_index(drop=True)

    recs = []

    for _, row in filtered.iterrows():

        overview = str(row["Overview"])

        polarity = TextBlob(
            overview
        ).sentiment.polarity

        # Mood matching

        if mood == "positive" and polarity <= 0:
            continue

        if mood == "negative" and polarity >= 0:
            continue

        recs.append(
            (
                row["Series_Title"],
                row["IMDB_Rating"],
                row["Genre"],
                polarity
            )
        )

        if len(recs) >= n:
            break

    if not recs:
        return "No suitable movie recommendations found."

    return recs


def show(recs, name):

    print(
        Fore.MAGENTA +
        f"\n🍿 Movie Recommendations for {name}\n"
    )

    for i, (
        title,
        rating,
        genre,
        polarity
    ) in enumerate(recs, start=1):

        print(
            Fore.GREEN +
            f"{i}. 🎥 {title}"
        )

        print(
            f"   ⭐ IMDb Rating: {rating}"
        )

        print(
            f"   🎭 Genre: {genre}"
        )

        print(
            f"   😊 Sentiment: "
            f"{senti(polarity)} "
            f"(Polarity: {polarity:.2f})"
        )

        print("-" * 40)


# ==========================
# MAIN PROGRAM
# ==========================

print(Fore.CYAN + "=" * 50)
print(Fore.MAGENTA + "🎬 AI MOVIE RECOMMENDER 🎬")
print(Fore.CYAN + "=" * 50)

name = input(
    Fore.GREEN +
    "\nEnter your name: "
).strip()

if not name:
    name = "Movie Lover"

print(
    Fore.CYAN +
    f"\n🔍 Analyzing preferences for {name}"
)

genre = get_genre()

mood = input(
    Fore.YELLOW +
    "\nHow are you feeling today? "
    "(positive/negative/neutral): "
).strip().lower()

if mood not in [
    "positive",
    "negative",
    "neutral"
]:
    mood = "neutral"

print(
    Fore.CYAN +
    "\nAnalyzing mood",
    end=""
)

dots()

mood_polarity = TextBlob(
    mood
).sentiment.polarity

print(
    f"\nMood Analysis: "
    f"{senti(mood_polarity)} "
    f"(Polarity: {mood_polarity:.2f})"
)

rating = get_rating()

while True:

    print(
        Fore.CYAN +
        f"\nFinding movies for {name}",
        end=""
    )

    dots()
    print()

    recommendations = recommend(
        genre=genre,
        mood=mood,
        rating=rating,
        n=5
    )

    if isinstance(
        recommendations,
        str
    ):

        print(
            Fore.RED +
            recommendations
        )

    else:

        show(
            recommendations,
            name
        )

    again = input(
        Fore.YELLOW +
        "\nWould you like more recommendations? (yes/no): "
    ).strip().lower()

    if again != "yes":

        print(
            Fore.GREEN +
            "\n🍿 Enjoy your movies!"
        )

        break