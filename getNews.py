from newsapi import NewsApiClient

newsApiOrgApiKey = open("newsApiOrgAPIKey.txt","r").read() # a text file containing your free API key from https://newsapi.org/
newsApiOrgSources = "the-guardian-uk,bbc-news,al-jazeera-english,independent" # the news sources the headlines are from
# format of sources: comma-separated string of source ids. See sources at: https://newsapi.org/docs/endpoints/sources

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