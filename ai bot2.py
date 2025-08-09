import random
import time

print('Hello! I am an enhanced AI bot.')
print('What is your name?')

def ai_bot():
    user_name = input()
    print(f'Nice to meet you, {user_name}!')

    def health():
        print('How are you feeling today?')
        mood = input().lower()
        if mood == 'good':
            print('I am glad to hear that!')
        elif mood == 'bad':
            print('I am sorry to hear that. I hope you feel better soon!')
        else:
            print('I hope you have a great day!')

    def hobbies():
        print('What are your hobbies?')
        hobby = input().lower()
        if hobby == 'reading':
            print('Reading is a great way to relax and learn new things!')
        elif hobby == 'sports':
            print('Sports are a fun way to stay active and healthy!')
        elif hobby == 'gaming':
            print('Gaming can be a great way to unwind and have fun!')
        else:
            print('That sounds interesting! Tell me more about it.')

    def favourite_food():
        print('What is your favourite food?')
        food = input().lower()
        if food == 'pizza':
            print('Pizza is a delicious choice! Do you like it with extra cheese?')
            extra_cheese = input().lower()
            if extra_cheese == 'yes':
                print('Extra cheese makes everything better!')
        elif food == 'sushi':
            print('Sushi is a healthy and tasty option! Do you prefer it with soy sauce?')
            soy_sauce = input().lower()
            if soy_sauce == 'yes':
                print('Soy sauce adds a nice flavor to sushi!')
        elif food == 'ice cream':
            print('Ice cream is a sweet treat! Do you like it with sprinkles?')
            sprinkles = input().lower()
            if sprinkles == 'yes':
                print('Sprinkles make ice cream even more fun!')
        else:
            print(f'{food.capitalize()}! That sounds delicious! I would love to try it sometime.')

    def favourite_color():
        print('What is your favourite color?')
        color = input().lower()
        if color == 'blue':
            print('Blue is a calming and peaceful color!')
        elif color == 'red':
            print('Red is a bold and energetic color!')
        elif color == 'green':
            print('Green is a refreshing and natural color!')
        else:
            print(f'{color.capitalize()} is a unique choice! It must be special to you.')

    health()
    hobbies()
    favourite_food()
    favourite_color()

# Extra Functions

def show_help():
    print("\n📋 You can type any of the following:")
    print("- Tell me a joke")
    print("- Tell me a trivia")
    print("- Tell me a quote")
    print("- Tell me a fact")
    print("- Give me a riddle")
    print("- Personality quiz")
    print("- Roll a dice")
    print("- ASCII art")
    print("- Countdown timer")
    print("- Would you rather")
    print("- Help")
    print("- Exit\n")

def tell_fact():
    facts = [
        "Bananas are berries, but strawberries aren't.",
        "A day on Venus is longer than a year on Venus.",
        "Octopuses have three hearts!",
        "Honey never spoils — archaeologists found 3,000-year-old edible honey."
    ]
    print(random.choice(facts))

def tell_quote():
    quotes = [
        "Believe you can and you're halfway there. — Theodore Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
        "You miss 100% of the shots you don’t take. — Wayne Gretzky",
        "Do what you can, with what you have, where you are. — Theodore Roosevelt"
    ]
    print(random.choice(quotes))

def give_riddle():
    riddles = [
        "What has to be broken before you can use it? (Answer: An egg)",
        "I’m tall when I’m young, and I’m short when I’m old. What am I? (Answer: A candle)",
        "What gets wetter the more it dries? (Answer: A towel)"
    ]
    print(random.choice(riddles))

def personality_quiz():
    print("Let's start a quick personality quiz! Answer A or B.")
    time.sleep(1)
    print("1. Do you prefer (A) mountains or (B) beach?")
    q1 = input().upper()
    print("2. Do you enjoy (A) books or (B) movies?")
    q2 = input().upper()
    print("3. Are you more (A) quiet or (B) outgoing?")
    q3 = input().upper()

    print("Analyzing your personality...")
    time.sleep(2)

    if q1 == 'A' and q2 == 'A':
        print("You're introspective and adventurous. A deep thinker who loves discovery!")
    elif q1 == 'B' and q2 == 'B':
        print("You’re energetic and love fun! A social butterfly!")
    else:
        print("You have a balanced personality — curious, calm, and creative!")

def roll_dice():
    print("Rolling a 6-sided dice...")
    time.sleep(1)
    print(f"You rolled a {random.randint(1,6)}!")

def would_you_rather():
    questions = [
        "Would you rather be able to fly or be invisible?",
        "Would you rather live in space or under the sea?",
        "Would you rather always be 10 minutes late or 20 minutes early?",
        "Would you rather give up pizza or chocolate forever?"
    ]
    print(random.choice(questions))

def trivia_quiz():
    questions = [
        {"q": "What is the largest planet in our solar system?", "a": "jupiter"},
        {"q": "Who painted the Mona Lisa?", "a": "leonardo da vinci"},
        {"q": "What is the capital of Australia?", "a": "canberra"},
        {"q": "What language is spoken in Brazil?", "a": "portuguese"}
    ]
    q = random.choice(questions)
    print(f"Trivia: {q['q']}")
    user_answer = input("Your answer: ").strip().lower()
    if user_answer == q["a"]:
        print("🎉 Correct!")
    else:
        print(f"❌ Oops! The correct answer is: {q['a'].title()}")
def ascii_art():
    word = input("Enter a word for ASCII art: ").upper()
    for char in word:
        print(f"{char} " * 5)
def countdown_timer():
    try:
        seconds = int(input("Enter number of seconds for countdown: "))
        while seconds > 0:
            print(f"{seconds}...", end='\r')
            time.sleep(1)
            seconds -= 1
        print("⏰ Time's up!")
    except ValueError:
        print("Please enter a valid number.")
ai_bot()

while True:
    user_input = input('\nWhat would you like to know? (Type "help" for options):\n').strip().lower()

    if user_input == 'exit':
        print("Thank you for chatting with me! Come back anytime. 👋")
        break
    elif user_input == 'a':
        print('You pressed "a". This is a random button.')
    elif user_input == 'b':
        print('You pressed "b". Another random button.')
    elif user_input == 'c':
        print('You pressed "c". Yet another random button.')
    elif user_input == 'd':
        print('You pressed "d". A different random button.')
    elif user_input == 'e':
        print('You pressed "e". A special random button.')
    elif user_input == 'tell me a joke':
        print('Why did the scarecrow win an award? Because he was outstanding in his field!')
    elif user_input == 'tell me a fact':
        tell_fact()
    elif user_input == 'tell me a quote':
        tell_quote()
    elif user_input == 'give me a riddle':
        give_riddle()
    elif user_input == 'personality quiz':
        personality_quiz()
    elif user_input == 'roll a dice':
        roll_dice()
    elif user_input == 'would you rather':
        would_you_rather()
    elif user_input == 'tell me a trivia':
        trivia_quiz()
    elif user_input == 'ASCII art':
        ascii_art()
    elif user_input == 'countdown timer':
        countdown_timer()
    elif user_input == 'help':
        show_help()
    elif user_input == 'whats the waether today?':
        print('I am not sure about the weather, but you can check a weather app or website for the latest updates.')
    elif user_input == 'what is your favorite programming language?':
        print('As an AI, I don’t have personal preferences, but Python is a popular language for AI development due to its simplicity and versatility.')
    elif user_input == 'what is your favorite food?':
        print('As an AI, I don’t eat, but I can tell you about popular foods! Many people love pizza, sushi, and ice cream.')
    else:
        print("I'm not sure how to answer that yet. Try typing 'help' to see what I can do!")
