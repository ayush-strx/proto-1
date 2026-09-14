from assistant.command_handler import execute_command
import automation.system_control as os

def start():
    print("""
Type 'voice'  - Use voice input      
Type 'help'   - Show available commands     
Type 'clear'  - Clear terminal screen         
Type 'exit'   - Close kAI       
""")

    while True:
        command = input().lower()

        if command == "voice":
            import voice.stt as stt
            command = stt.listen().lower()

        if command == "exit":
            break

        if command == "clear":
            os.clear()

            start()
            break

        execute_command(command)