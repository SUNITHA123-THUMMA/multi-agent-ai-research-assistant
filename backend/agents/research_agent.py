from tools.web_search import search_web

def research_topic(topic):

    results = search_web(topic)

    combined_text = ""

    for r in results:
        combined_text += r + "\n"

    return combined_text