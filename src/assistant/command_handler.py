import automation.app_launcher as launch
import automation.browser_control as browse
from voice.tts import speak
from brain.router import route
import agents.time_agent as time_agent
import agents.weather_agent as weather_agent
import agents.wikipedia_agent as wiki_agent

def execute_command(command):
    try:
        decision = route(command)

        if decision == "dynamic_open":
            app_name = command.replace("open", "").strip()
            speak(launch.find_and_open_app(app_name))

        elif decision == "open_google":
            speak("Opening Google.")
            browse.google()

        elif decision == "open_youtube":
            speak("Opening YouTube.")
            browse.youtube()

        elif decision == "search":
            query = command.replace("search", "").strip()
            speak(f"Searching Google for {query}.")
            browse.google_search(query)

        elif decision == "time_agent":
            speak(time_agent.get_time())

        elif decision == "date_agent":
            speak(time_agent.get_date())

        elif decision == "weather_agent":
            city = command.replace("weather in", "").replace("weather", "").strip()
            speak(weather_agent.get_weather(city))

        elif decision == "wikipedia_agent":
            query = command.replace("tell me about", "").replace("who is", "").replace("what is", "").strip()
            response = wiki_agent.search_wikipedia(query)
            print(response)
            speak(response)
        else:
            speak(
                f"Sorry Sir. I didn't understand that command. "
                "Type 'help' to see available commands."
            )

    except FileNotFoundError:
        speak(f"Sorry Sir!. I couldn't find that application.")

    except Exception as e:
        print(e)
        speak(f"Sorry Sir!. An unexpected error occurred: {e}")
    