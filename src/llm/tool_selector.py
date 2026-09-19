from llm.llm_engine import ask_llm
import tools.time_agent as time_agent
import tools.weather_agent as weather_agent
import tools.wikipedia_agent as wiki_agent
import tools.app_launcher as launch
import tools.browser_control as browse

TOOLS = [
    (time_agent.TIME_TOOL_NAME, time_agent.TIME_TOOL_DESCRIPTION, time_agent.TIME_TOOL_PARAMETER),
    (time_agent.DATE_TOOL_NAME, time_agent.DATE_TOOL_DESCRIPTION, time_agent.DATE_TOOL_PARAMETER),
    (weather_agent.TOOL_NAME, weather_agent.TOOL_DESCRIPTION, weather_agent.TOOL_PARAMETER),
    (wiki_agent.TOOL_NAME, wiki_agent.TOOL_DESCRIPTION, wiki_agent.TOOL_PARAMETER),
    (launch.TOOL_NAME, launch.TOOL_DESCRIPTION, launch.TOOL_PARAMETER),
    (browse.GOOGLE_TOOL_NAME, browse.GOOGLE_TOOL_DESCRIPTION, browse.GOOGLE_TOOL_PARAMETER),
    (browse.YOUTUBE_TOOL_NAME, browse.YOUTUBE_TOOL_DESCRIPTION, browse.YOUTUBE_TOOL_PARAMETER),
    (browse.SEARCH_TOOL_NAME, browse.SEARCH_TOOL_DESCRIPTION, browse.SEARCH_TOOL_PARAMETER),
]


def build_tools_description():
    lines = []
    for name, desc, param in TOOLS:
        lines.append(f"- {name}: {desc} (parameter: {param})")
    return "\n".join(lines)


def select_tool(command):
    tools_text = build_tools_description()

    prompt = f"""You are a function-calling assistant. Based on the user's request (which may be in English, Hindi, or Hinglish), decide which ONE tool below is most appropriate, and extract the required parameter from the request if needed.

Available tools:
{tools_text}

If NO tool matches the request, respond with exactly: no_tool|

Respond in EXACTLY this format: tool_name|parameter

User request: "{command}"
Response:"""

    result = ask_llm(prompt, max_tokens=200)
    print(f"[DEBUG] LLM raw output: {result}")

    if "|" in result:
        tool_name, param = result.split("|", 1)
        tool_name = tool_name.strip().lower()
        param = param.strip()

        if param.lower() in ["none", "empty", "n/a", "null"]:
            param = ""

        return tool_name, param

    return "no_tool", ""


def chat_response(command):
    prompt = f"""You are a helpful voice assistant. Respond naturally and helpfully in the same language style the user used.

IMPORTANT RULES:
1. Always write your response using ONLY the Roman/English alphabet (Latin script), even when responding in Hindi. Never use Devanagari or any non-Latin script.
2. Answer from your own knowledge. If you genuinely don't know something, or it's about very recent events/things you weren't trained on, honestly say you don't have information about it — do not guess or make things up.
3. If the user asks to learn, understand, or get an explanation about something, give a clear, conversational explanation in 3-5 sentences.

User: {command}
Assistant:"""

    return ask_llm(prompt, max_tokens=250)