import automation.app_launcher as launch
import automation.browser_control as browse
from voice.tts import speak
from brain.router import route, chat_response
import agents.time_agent as time_agent
import agents.weather_agent as weather_agent
import agents.wikipedia_agent as wiki_agent


def execute_command(command):
    try:
        decision, value = route(command)

        if decision == "dynamic_open":
            speak(launch.find_and_open_app(value))

        elif decision == "open_google":
            speak("Opening Google.")
            browse.google()

        elif decision == "open_youtube":
            speak("Opening YouTube.")
            browse.youtube()

        elif decision == "search":
            speak(f"Searching Google for {value}.")
            browse.google_search(value)

        elif decision == "time_agent":
            speak(time_agent.get_time())

        elif decision == "date_agent":
            speak(time_agent.get_date())

        elif decision == "weather_agent":
            speak(weather_agent.get_weather(value))

        elif decision == "wikipedia_agent":
            response = wiki_agent.search_wikipedia(value)
            print(f"Ayu One: {response}")
            speak(response)

        else:
            response = chat_response(command)
            print(f"Ayu One: {response}")
            speak(response)

    except FileNotFoundError:
        speak("Sorry Sir!. I couldn't find that application.")

    except Exception as e:
        print(e)
        speak(f"Sorry Sir!. An unexpected error occurred: {e}")