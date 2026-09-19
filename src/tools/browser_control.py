import webbrowser

GOOGLE_TOOL_NAME = "open_google"
GOOGLE_TOOL_DESCRIPTION = "Opens the Google homepage in the browser."
GOOGLE_TOOL_PARAMETER = "none"

YOUTUBE_TOOL_NAME = "open_youtube"
YOUTUBE_TOOL_DESCRIPTION = "Opens the YouTube homepage in the browser."
YOUTUBE_TOOL_PARAMETER = "none"

SEARCH_TOOL_NAME = "search"
SEARCH_TOOL_DESCRIPTION = (
    "Searches a given query on Google and opens the search results in the browser. "
    "Use this when the user wants to search or look up something online."
)
SEARCH_TOOL_PARAMETER = "the search query"


def google():
    webbrowser.open_new_tab("https://www.google.com")


def youtube():
    webbrowser.open_new_tab("https://youtube.com")


def google_search(query):
    search = f"https://www.google.com/search?q={query}"
    webbrowser.open(search)