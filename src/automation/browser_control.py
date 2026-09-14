import webbrowser

def google():
    webbrowser.open_new_tab("https://www.google.com")

def youtube():
    webbrowser.open_new_tab("https://youtube.com")

def google_search(query):
    search = f"https://www.google.com/search?q={query}"
    webbrowser.open(search)