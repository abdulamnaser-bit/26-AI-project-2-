import webbrowser
import requests
from ddgs import DDGS

# =========================
# GOOGLE SEARCH
# =========================

def google_search(command):

    query = (
        command.lower()
        .replace("search web for", "")
        .replace("search google for", "")
        .strip()
    )

    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )

    return f"Searching Google for {query}, Boss."


# =========================
# WIKIPEDIA
# =========================

def wiki_search(command):

    query = (
        command.lower()
        .replace("who is", "")
        .replace("what is", "")
        .replace("tell me about", "")
        .strip()
    )

    print("SEARCH QUERY =", query)

    if not query:
        return "Please tell me what you want to know, Boss."

    try:

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=1
                )
            )

        print("RESULTS =", results)

        if not results:
            return f"I couldn't find information about {query}, Boss."
        
        first = results[0]

        title = first.get("title", "")
        body = first.get("body", "")
        href = first.get("href", "")

        return f"{title}\n{body}"


    except Exception as e:

        print("SEARCH ERROR:", e)

        return f"I couldn't find information about {query}, Boss."

# =========================
# WEATHER
# =========================

def get_weather(city="Hyderabad"):

    try:

        url = (
            f"https://wttr.in/{city}?format="
            "%C+%t+Humidity:%h"
        )

        weather = requests.get(url).text

        return f"Weather in {city}: {weather}"

    except:

        return "Unable to fetch weather, Boss."


# =========================
# NEWS
# =========================

def get_news():

    try:

        rss = requests.get(
            "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
        ).text

        headlines = []

        for line in rss.split("<title>")[2:7]:

            title = line.split("</title>")[0]

            headlines.append(title)

        return "\n".join(headlines)

    except:

        return "Unable to fetch news, Boss."


# =========================
# STOCKS
# =========================

def stock_price(symbol):

    try:

        url = (
            f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        )

        data = requests.get(url).json()

        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]

        return f"{symbol.upper()} is trading at {price} USD."

    except:

        return "Unable to fetch stock price."


# =========================
# CRYPTO
# =========================

def crypto_price(coin):

    try:

        url = (
            f"https://api.coingecko.com/api/v3/simple/price"
            f"?ids={coin}&vs_currencies=usd"
        )

        data = requests.get(url).json()

        price = data[coin]["usd"]

        return f"{coin.title()} is {price} USD."

    except:

        return "Unable to fetch crypto price."


# =========================
# CURRENCY
# =========================

def convert_currency(amount):

    try:

        amount = float(amount)

        url = (
            "https://open.er-api.com/v6/latest/USD"
        )

        data = requests.get(url).json()

        rate = data["rates"]["INR"]

        result = amount * rate

        return f"{amount} USD equals {result:.2f} INR."

    except:

        return "Conversion failed, Boss."