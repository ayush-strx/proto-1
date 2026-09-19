from assistant.executor import execute_command
import tools.system_control as system

WELCOME_MESSAGE = """
========================================
   Ayu One - Personal Voice Assistant
========================================
Type 'voice'  - Use voice input      
Type 'help'   - Show available commands     
Type 'clear'  - Clear terminal screen         
Type 'exit'   - Close Ayu One
========================================
"""


def start():
    print(WELCOME_MESSAGE)

    while True:
        command = input("\nYou: ").strip()

        if not command:
            continue

        if command.lower() == "voice":
            print("Listening...")
            import voice.stt as stt
            command = stt.listen()
            if not command:
                print("Ayu One: Sorry, I didn't catch that. Please try again.")
                continue
            print(f"You said: {command}")

        if command.lower() == "exit":
            print("Ayu One: Goodbye!")
            break

        if command.lower() == "clear":
            system.clear()
            print(WELCOME_MESSAGE)
            continue

        if command.lower() == "help":
            print(WELCOME_MESSAGE)
            continue

        execute_command(command)