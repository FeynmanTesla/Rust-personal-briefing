from newsapi import NewsApiClient

newsApiOrgApiKey = open("conf/newsApiOrgAPIKey.txt",
                        "r").read()  # a text file containing your free API key from https://newsapi.org/
newsApiOrgSources = open("conf/newsApiOrgSources.txt", "r").read()  # the news sources the headlines are from


# TODO: process the headlines from reading -> listening format
#           e.g. "S America" --> "South America", "<pound symbol>50bn" --> "50 billion pounds", etc

def get_news():
    newsapi = NewsApiClient(api_key=newsApiOrgApiKey)
    top_headlines = newsapi.get_top_headlines(sources=newsApiOrgSources)
    if top_headlines["status"] != "ok":
        return "I was unable to retrieve news headlines."

    articles = top_headlines["articles"]
    headlines = "Here are the news headlines."
    for article in articles:
        headlines += " " + article["title"]
        final_headline_char = article["title"][len(article["title"]) - 1]
        if (final_headline_char != "!" and final_headline_char != "." and final_headline_char != "?"
                and final_headline_char != ";"):
            headlines += "."
    return headlines
