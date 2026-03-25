#Import Libraries
from groq import  Groq
from dotenv import load_dotenv
import  os
import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()

client = Groq(api_key= os.getenv("GROQ_API_KEY"))

#Real Tools
def search(query: str) -> str:
    #using Wikipedia API - completely free, no key needed!
    query = query.replace(" ", "_")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "MyAgent/1.0 (learning project)"}
        )
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read())
        return data.get("extract", "No result found")[:500]
    except Exception as e:
        return f"Error: {str(e)}"

def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return f"{expression} = {result}"
    except:
        return f"Could not calculater: {expression}"




#Test the tools directly first
print(search("Alexander Graham Bell"))
print(calculate("15+27"))


