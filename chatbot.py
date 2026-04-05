def chatbot(prompt):
        if prompt == "HELLO":
            print("👋 Hi there!")
        elif prompt == "HOW ARE YOU":
            print("☺️ I'm fine, thanks!")
        elif prompt == "NAME":
            print("🤖 My name is AlphaBot!")
        elif prompt == "HELP":
            print("❓ I can answer basic questions!")
        else:
            print("I didn't understand that!")
prompt=input("Enter prompt: ").upper()
while prompt !="BYE":
     chatbot(prompt)
     prompt=input("Enter prompt: ").upper()
print("👋 Goodbye!")
