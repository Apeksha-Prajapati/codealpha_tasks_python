from datetime import datetime

user_name = ""
last_topic = ""

def current_time():
    return datetime.now().strftime("%I:%M %p")

def current_date():
    return datetime.now().strftime("%d-%m-%Y")

def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Sorry, I can't calculate that."

def chatbot_reply(user_input):
    global user_name, last_topic
    text = user_input.lower()

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey", "namaste"]):
        last_topic = "greeting"
        return "Hello 😊 How can I help you today?"

    # Name memory
    if "my name is" in text:
        user_name = user_input.split("is")[-1].strip()
        last_topic = "name"
        return f"Nice to meet you, {user_name}!"

    if "what is my name" in text:
        return f"Your name is {user_name}." if user_name else "You haven't told me your name yet."

    # Mood detection
    if any(word in text for word in ["sad", "upset", "tired"]):
        last_topic = "mood"
        return "I'm sorry to hear that 😔 Everything will be okay."

    if any(word in text for word in ["happy", "good", "great"]):
        last_topic = "mood"
        return "That's nice to hear 😊 Keep smiling!"

    # Time & Date
    if "time" in text:
        last_topic = "time"
        return f"Current time is {current_time()}"

    if "date" in text:
        last_topic = "date"
        return f"Today's date is {current_date()}"

    # Math calculation
    if text.startswith("calculate"):
        last_topic = "math"
        expression = text.replace("calculate", "").strip()
        return f"Result: {calculate(expression)}"

    # Small talk
    if "how are you" in text:
        return "I'm doing great! Thanks for asking 😊"

    if "thank" in text:
        return "You're welcome 🙌"

    # Help
    if "help" in text:
        return (
            "You can try:\n"
            "- hello\n"
            "- my name is ...\n"
            "- what is my name\n"
            "- time / date\n"
            "- calculate 5+3\n"
            "- I am sad / happy\n"
            "- bye"
        )

    # Exit
    if any(word in text for word in ["bye", "exit", "quit"]):
        return "Goodbye 👋 Take care!"

    # Context-based fallback
    if last_topic == "greeting":
        return "Tell me how can I help you 🙂"

    return "Sorry, I didn't understand that. Type 'help' to see commands."

def main():
    print("🤖 Ultra-Advanced Python Chatbot")
    print("Type 'help' for commands | 'bye' to exit\n")

    while True:
        user_input = input("You: ")
        reply = chatbot_reply(user_input)
        print("Bot:", reply)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break

main()
