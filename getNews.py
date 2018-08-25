from newsapi import NewsApiClient

newsApiOrgApiKey = open("newsApiOrgAPIKey.txt","r").read() # a text file containing your free API key from https://newsapi.org/
newsApiOrgSources = open("newsApiOrgSources.txt","r").read() # the news sources the headlines are from

# TODO: process the headlines from reading -> listening format
#           e.g. "S America" --> "South America", "<pound symbol>50bn" --> "50 billion pounds", etc

def getNews():
    newsapi = NewsApiClient(api_key=newsApiOrgApiKey)
    top_headlines = newsapi.get_top_headlines(sources=newsApiOrgSources)
    if (top_headlines["status"] != "ok"): return "I was unable to retrieve news headlines."

    articles = top_headlines["articles"]
    headlines = "Here are the news headlines."
    for article in articles:
        headlines += " " + article["title"]
        finalHeadlineChar = article["title"][len(article["title"]) - 1]
        if (finalHeadlineChar != "!" and finalHeadlineChar != "." and finalHeadlineChar != "?" and finalHeadlineChar != ";"): headlines += "."
    return headlines