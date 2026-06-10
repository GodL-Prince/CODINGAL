name=str(input("What is your name?"))
print(f"Hello, {name}! Nice to meet you.")
feel=input("How are you feeling today?").lower()
if feel=="good":
    print("That's great to hear!")
elif feel=="bad":
    print("I'm sorry to hear that.") 
else:
    print("Thanks for sharing how you're feeling.")
hobby=input("What is your hobby?").lower()
print(f"That's awesome! {hobby} sounds interesting.")
if name=="Exit":
    print(f"Goodbye, {name}! It was nice talking to you. Take care!")
#END    