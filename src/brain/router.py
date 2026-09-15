from brain.llm_engine import ask_llm

def route(command):
    prompt = f"""You are an intent classifier for a voice assistant. The command may be in English, Hindi, or Hinglish (mixed).

Reply in EXACTLY this format: category|value
"value" is the specific detail needed. If no value is needed, leave it empty after the pipe.

Categories and their value:
- dynamic_open -> value = app name to open
- open_google -> value = (empty)
- open_youtube -> value = (empty)
- search -> value = search query
- time_agent -> value = (empty)
- date_agent -> value = (empty)
- weather_agent -> value = city name
- wikipedia_agent -> value = topic/person name
- chat -> value = (empty) [use this for greetings, casual talk, questions about the assistant, thanks, or anything that isn't a specific task above]

Examples:
"chrome khol do" -> dynamic_open|chrome
"notepad khol" -> dynamic_open|notepad
"google kholo" -> open_google|
"youtube kholo" -> open_youtube|
"search python tutorials" -> search|python tutorials
"time kya hai" -> time_agent|
"aaj ki date kya hai" -> date_agent|
"mumbai ka weather batao" -> weather_agent|mumbai
"einstein ke baare mein batao" -> wikipedia_agent|einstein
"kaisa hai tu" -> chat|
"thank you" -> chat|
"tu kaun hai" -> chat|
"tera naam kya hai" -> chat|
"good morning" -> chat|

Command: "{command}"
Answer:"""

    result = ask_llm(prompt, max_tokens=30)

    if "|" in result:
        category, value = result.split("|", 1)
        return category.strip().lower(), value.strip()

    return "chat", ""


def chat_response(command):
    prompt = f"""You are Ayu One, a friendly voice assistant. Reply naturally and briefly (1-2 sentences) to the user's message. The user may write in English, Hindi, or Hinglish — reply in the same style/language they used.

User: {command}
Ayu One:"""

    return ask_llm(prompt, max_tokens=60)