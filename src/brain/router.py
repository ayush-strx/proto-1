def route(command):
    command = command.lower()
    
    if command.startswith("open "):
        if "google" in command:
            return "open_google"
        elif "youtube" in command:
            return "open_youtube"
        else:
            return "dynamic_open"
        
    elif command.startswith("search"):
        return "search"
    
    elif "time" in command:
        return "time_agent"
    
    elif "date" in command:
        return "date_agent"
    
    elif "weather" in command:
        return "weather_agent"

    elif command.startswith("tell me about") or command.startswith("who is") or command.startswith("what is"):
        return "wikipedia_agent"
    
    else:
        return "unknown"