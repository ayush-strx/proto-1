import wikipedia

def search_wikipedia(query):
    if not query:
        return "Please specify what you want to know about."
    
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    
    except wikipedia.exceptions.DisambiguationError as e:
        options = ", ".join(e.options[:3])
        return f"That's a bit ambiguous. Did you mean: {options}?"
    
    except wikipedia.exceptions.PageError:
        return f"Sorry, I couldn't find anything about {query} on Wikipedia."
    
    except Exception:
        return "Sorry, something went wrong while searching Wikipedia."