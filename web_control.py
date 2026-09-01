import webbrowser

def web_command(command):

    command = command.lower()

    if "youtube" in command and "open" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube, Boss."

    if "google" in command and "open" in command:
        webbrowser.open("https://google.com")
        return "Opening Google, Boss."

    if "chatgpt" in command and "open" in command:
        webbrowser.open("https://chatgpt.com")
        return "Opening ChatGPT, Boss."

    if "search youtube for" in command:

        query = command.replace(
            "search youtube for",
            ""
        ).strip()

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )

        return f"Searching YouTube for {query}, Boss."

    if "search google for" in command:

        query = command.replace(
            "search google for",
            ""
        ).strip()

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return f"Searching Google for {query}, Boss."

    return None