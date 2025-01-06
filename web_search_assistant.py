#Web Search Assistant

import datetime
import random
import webbrowser

# Set up our assistant's responses
assistant_name = "Rachelle"
greetings = [
    f"Hello! I'm {assistant_name}, how can I help you?",
    f"Hi there! {assistant_name} at your service.",
    f"Greetings! What can I do for you today?"
]
goodbye_responses = [
    "Goodbye! Have a great day.",
    "See you later! Take care.",
    "Bye! Hope I was helpful."
]

# Start the program
print("Web Search Assistant Simulation!")
print("Type your commands (or 'exit' to quit)")

# Main loop
while True:
    try:
        # Get user input
        user_input = input("\n> ").strip()
        command = user_input.lower()

        # Process commands
        if command in ['quit', 'exit', 'bye'] or any(word in command for word in ["bye", "goodbye", "exit"]):
            print(random.choice(goodbye_responses))
            break

        elif any(greeting in command for greeting in ["hello", "hi", "hey"]):
            print(random.choice(greetings))

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"The current time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            print(f"Today's date is {current_date}")

        elif "search" in command:
            query = command.split("search")[1].strip()
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            print(f"Searching the web for: {query}")

        else:
            print("I'm sorry, I didn't understand that command. Could you please repeat?")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again.")