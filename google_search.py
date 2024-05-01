from langchain_google_community import GoogleSearchAPIWrapper
import os 

os.environ.get("GOOGLE_CSE_ID")
os.environ.get("GOOGLE_API_KEY")

search = GoogleSearchAPIWrapper()

def generate_urls_from_query(query:str, amount:int = 1) -> list[str]:
    results = search.results(query, amount)
    urls = [url.get("link") for url in results]
    return urls 
        
if __name__ == '__main__':
    print(generate_urls_from_query("software developer jobs", 10))