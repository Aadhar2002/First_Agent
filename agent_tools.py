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
    print(f"URL being called: {url}")

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


def run_agent(task:str):
    print(f"\nAgent recived task:{task}")
    print("-" * 51)

    step = 1
    last_result = None
    #Run while loop
    while True:
        #Add this check at the top of the loop
        if step > 3:
            print(f"\n Task complete! Final Answer: {last_result}")
            break

        print(f"\nStep {step}: Thinking.....")
       #LLM decides which tool to use
        prompt = f"""You are an AI agent with access to tools.
        You MUST use a tool before finishing.
        Available Tools: search, weather, food, market, finish

        Task: {task}
        
        Rules:
        - If task is a question about a person fact: use search
        - If task involves number or math: use calculate
        -Do NOT use finish on the first step
        
        Reply with ONLY the tool name. Nothing else."""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        tool = response.choices[0].message.content.strip().lower()
        print(f"\nStep {step}: Agent decided to: {tool}")

        #Simple tool execution
        if tool == 'finish':
            print(f"\nTask Complete! Final Answer: {last_result}")
            break
        elif tool == 'search':
            #Extract just the search term
            search_prompt = f"Extract only the main subject/name to search from this question, nothing else: {task}"
            search_response = client.chat.completions.create(
                model = "llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": search_prompt}]
            )
            search_term = search_response.choices[0].message.content.strip()
            print(f"Searching for: {search_term}")
            last_result = search(search_term)

        elif tool == 'calculate':
            #Ask LLM to extract just the math expression
            math_prompt = f"Extract only the math expression from this task, nothing else: {task}"
            math_response = client.chat.completions.create(
                model= "llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": math_prompt}]
            )
            expression = math_response.choices[0].message.content.strip()
            last_result = calculate(expression)

        print(f"Step {step}: Result: {last_result}")

        if last_result and 'Error' not in last_result:
            print(f"\n Task Completed! Final Answer!: {last_result}")
            break

        step +=1

run_agent("Who is Alaxander Graham Bell?")
run_agent("What is 2547 divided by 3")
