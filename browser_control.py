import webbrowser
import urllib.parse

def google_search(query):

    search = urllib.parse.quote(query)

    webbrowser.open(
        f"https://www.google.com/search?q={search}"
    )

    return f"Searching Google for {query}, Boss."

def youtube_search(query):

    url = (
        "https://www.youtube.com/results?"
        f"search_query={query}"
    )

    webbrowser.open(url)

    return f"Searching YouTube for {query}, Boss."