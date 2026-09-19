import tools.app_launcher as launch
import tools.browser_control as browse
from voice.tts import speak
from llm.tool_selector import select_tool, chat_response
import tools.time_agent as time_agent
import tools.weather_agent as weather_agent
import tools.wikipedia_agent as wiki_agent


def execute_command(command):
    try:
        tool_name, param = select_tool(command)

        if tool_name == "dynamic_open":
            speak(launch.find_and_open_app(param))

        elif tool_name == "open_google":
            speak("Opening Google.")
            browse.google()

        elif tool_name == "open_youtube":
            speak("Opening YouTube.")
            browse.youtube()

        elif tool_name == "search":
            speak(f"Searching Google for {param}.")
            browse.google_search(param)

        elif tool_name == "time_agent":
            speak(time_agent.get_time())

        elif tool_name == "date_agent":
            speak(time_agent.get_date())

        elif tool_name == "weather_agent":
            speak(weather_agent.get_weather(param))

        elif tool_name == "wikipedia_agent":
            response = wiki_agent.search_wikipedia(param)
            print(f"Ayu One: {response}")
            speak(response)

        else:
            response = chat_response(command)
            print(f"Ayu One: {response}")
            speak(response)

    except FileNotFoundError:
        speak("Sorry, I couldn't find that application.")

    except Exception as e:
        print(e)
        speak("Sorry, an unexpected error occurred.")