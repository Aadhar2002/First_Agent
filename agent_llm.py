#Import groq
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
#Initialise the Groq client with your API key
client = Groq(api_key=os.getenv("GROQ_API_KEY")) #Put your api key here

#Write the llm_think function
def llm_think(task: str, last_result: str =None)->  dict:

    if last_result:
        return {"tool": "finish", "input": last_result}

    #Ask the LLM what tool to use
    prompt = f"""You are an AI agent. Give a task, decide which tool to use
Available Tools: search, weather, food, market, finish

Task: {task}

Reply with ONLY the tool name. Nothing else."""

    response = client.chat.completions.create(
        model= "llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    tool = response.choices[0].message.content.strip().lower()
    return {"tool": tool, "input": task}

def llm_act(action: dict) -> str:
    #LLM generates the real answer!
    prompt = f"Answer this question in one sentence: {action['input']}"

    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
def run_agent(task:str):
    print(f"\nAgent recived task:{task}")
    print("-" * 51)

    step = 1
    last_result = None
    #Run while loop
    while True:
        print(f"\nStep {step}: Thinking.....")
        action = llm_think(task, last_result)
        print(f"\nStep {step}: Agent decided to:  {action['tool']}")

        #Simple tool execution
        if action['tool'] == 'finish':
            print(f"\nTask Complete! Final Answer: {last_result}")
            break
        else:
            last_result = llm_act(action)

        print(f"Step {step}: Result: {last_result}")

        step +=1

run_agent("What is the capital France?")
run_agent("What is the famous food of Delhi?")
run_agent("Who Intvented the telephone?") #A new question which was not hardcoded earlier