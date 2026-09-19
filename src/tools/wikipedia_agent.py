import wikipedia

TOOL_NAME = "wikipedia_agent"
TOOL_DESCRIPTION = (
    "Looks up information on Wikipedia. "
    "Use this ONLY when the user EXPLICITLY asks to search, check, or look up "
    "something specifically on Wikipedia (e.g., user says the word 'wikipedia' or 'wiki'). "
    "Do NOT use this for general questions, even factual ones, unless the user "
    "explicitly mentions Wikipedia by name."
)
TOOL_PARAMETER = "the specific topic to look up on Wikipedia"


def search_wikipedia(query):
    if not query:
        return "Please specify what you want to know about."

    try:
        summary = wikipedia.summary(query, sentences=4)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        options = ", ".join(e.options[:3])
        return f"That's a bit ambiguous. Did you mean: {options}?"
    except wikipedia.exceptions.PageError:
        return f"Sorry, I couldn't find anything about {query} on Wikipedia."
    except Exception:
        return "Sorry, something went wrong while searching Wikipedia."