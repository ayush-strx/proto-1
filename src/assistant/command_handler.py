import automation.app_launcher as launch
import utils.time as get_time
import automation.browser_control as browse
from voice.tts import speak

def execute_command(command):
    try:
        if command == "open notepad":
            launch.open_notepad()
            speak("Notepad is ready.")

        elif command == "open calculator":
            launch.open_calculator()
            speak("Calculator is ready.")

        elif command == "open explorer":
            launch.open_explorer()
            speak("File Explorer is ready.")

        elif command == "open control panel":
            launch.open_control()
            speak("Control Panel is open.")

        elif command == "open task manager":
            launch.open_task()
            speak("Task Manager is open.")

        elif command == "open cmd":
            launch.open_cmd()
            speak("Command Prompt is ready.")

        elif command == "open snipping tool":
            launch.open_snip()
            speak("Snipping Tool is ready.")

        elif command == "open word":
            launch.open_word()
            speak("Microsoft Word is ready.")

        elif command == "open excel":
            launch.open_excel()
            speak("Microsoft Excel is ready.")

        elif command == "open powerpoint":
            launch.open_powerpoint()
            speak("Microsoft PowerPoint is ready.")

        elif command == "open paint":
            launch.open_paint()
            speak("Paint is ready.")

        elif command == "open chrome":
            launch.open_chrome()
            speak("Chrome is ready.")

        elif command == "tell me the date":
            speak(f"Today's date is {get_time.current_date()}.")

        elif command == "tell me the time":
            speak(f"The current time is {get_time.current_time()}.")

        elif command == "tell me the date and time":
            speak(f"It's {get_time.date_time()}.")

        elif command == "open google":
            speak("Opening Google.")
            browse.google()

        elif command == "open youtube":
            speak("Opening YouTube.")
            browse.youtube()

        elif command.startswith("search"):
            query = command.replace("search", "").strip()
            speak(f"Searching Google for {query}.")
            browse.google_search(query)

        else:
            speak(
                f"Sorry Sir. I didn't understand that command. "
                "Type 'help' to see available commands."
            )

    except FileNotFoundError:
        speak(f"Sorry Sir!. I couldn't find that application.")

    except Exception as e:
        speak(f"Sorry Sir!. An unexpected error occurred: {e}")