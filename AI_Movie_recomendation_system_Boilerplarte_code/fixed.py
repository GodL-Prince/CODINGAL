import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

# Init colors
init(autoreset=True)

# Load CSV (same error output)
try: df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found."); raise SystemExit

# Unique genres
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    """Prints ... with delay (AI thinking effect)."""
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)

def senti(p):
    """Polarity -> label."""
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    """Filter by genre/rating, shuffle, analyze Overview polarity, return n (title, polarity) or message."""
    # 1) Start: d = df
    d=df
    # 2) If genre: filter Genre contains (case-insensitive)
    if genre: d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: d = d[d["IMDB_Rating"] >= rating]
    if d.empty:
      print ("empty")
      return "No suitable movie recommendations found."
    # 3) If rating not None: filter IMDB_Rating >= rating
    # 4) If empty: return "No suitable movie recommendations found."
    # 5) Shuffle: sample(frac=1).reset_index(drop=True)
    d = d.sample(frac=1).reset_index(drop=True)
    # 6) need_nonneg = bool(mood)
    need_nonneg = bool(mood)
    # 7) Loop rows:    
    #    - skip missing Overview
    #    - pol = TextBlob(overview).sentiment.polarity
    #    - if not need_nonneg or pol >= 0: append (Series_Title, pol)
    #    - stop at n
    recs = []
    for _, row in d.iterrows():
        overview = row.get("Overview", "")
        if pd.isna(overview) or not overview.strip():
            continue
        pol = TextBlob(overview).sentiment.polarity
        if not need_nonneg or pol >= 0:
            recs.append((row["Series_Title"], pol))
        if len(recs) >= n:
            break
    print(recs)    
    # 8) Return list else same message
    return recs if recs else "No suitable movie recommendations found."
    pass

def show(recs, name):
    """Print in same format: header + numbered 🎥 lines with polarity + senti()."""
    # Print: "\n🍿 AI-Analyzed Movie Recommendations for {name}:"
    print(f"\n🍿 AI-Analyzed Movie Recommendations for {name}:")
    # Loop enumerate(recs, 1) and print:
    # "{i}. 🎥 {title} (Polarity: {p:.2f}, {senti(p)})"
    for i, (title, p) in enumerate(recs, 1):
        print(f"{i}. 🎥 {title} (Polarity: {p:.2f}, {senti(p)})")
        
    pass

def get_genre():
    print(Fore.GREEN + "Available Genres: ", end="")
    for i, g in enumerate(genres, 1): print(f"{Fore.CYAN}{i}. {g}")
    print()
    while True:
        x = input(Fore.YELLOW + "Enter genre number or name: ").strip()
        if x.isdigit() and 1 <= int(x) <= len(genres): return genres[int(x) - 1]
        x = x.title()
        if x in genres: return x
        print(Fore.RED + "Invalid input. Try again.\n")

def get_rating():
    """Ask rating or 'skip' (repeat until valid)."""
    # Prompt must match exactly
    prompt = "Enter minimum IMDb rating (7.6-9.3) or 'skip': "
    # If skip -> None
    input_rating = input(prompt).strip().lower()
    # Else float in 7.6..9.3
    while True:
        if input_rating == "skip":
            return None
        try:
            rating = float(input_rating)
            if 7.6 <= rating <= 9.3:
                return rating
            else:
                print("Rating out of range. Try again.\n")
        except ValueError:
            print("Invalid input. Try again.\n")
        input_rating = input(prompt).strip().lower()
    # Out of range -> "Rating out of range. Try again.\n"
    # Bad float -> "Invalid input. Try again.\n"
    pass

# MAIN (students write)
print("Welcome to the Movie Recommender! 🎬")
# 1) Print welcome + ask name + greet
name = input("Please enter your name: ").strip()
# 2) Print 🔍 line
print(f"🔍 Analyzing movies for {name}...")
# 3) genre = get_genre(); mood input
genre = get_genre()
print(genre)
mood = input("How are you feeling today? (positive/negative/neutral): ").strip().lower()
# 4) Print "Analyzing mood" + dots(); compute mood polarity + print mood line
print("Analyzing mood", end="")
# 5) rating = get_rating()
rating = get_rating()
# 6) Print "Finding movies for {name}" + dots()
mood_polarity = TextBlob(mood).sentiment.polarity
# 7) recs = recommend(...); if str print red else show()
print(f"Finding movies for {name}", end="")
# 8) Loop ask "Would you like more recommendations? (yes/no):"
recs=recommend(genre=genre, mood=mood, rating=rating, n=5)
if isinstance(recs, str):
    print(Fore.RED + recs)
#    - no -> print enjoy line + break
#    - yes -> recommend again + show
#    - else -> invalid choice line