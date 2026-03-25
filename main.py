# My first AI Agent - Built from Scratch
# Loop: Think, Act, Observe, Repeat
#Fuction run_agent for the first query
def run_agent(task: str):
    print(f"\n Agent recieved task: {task}")
    print("-" * 51)

    step = 1
    last_result = None #track the last result
    #Run the while loop
    while True:
        print(f"\nStep {step}: Thinking....")

        # This is where the brain (LLM) will go
        # For now we'll simulate it
        action = think(task, last_result) #Passing last_result

        print(f"Step {step}: Agent decided to: {action['tool']}")

        # This is where tools will go

        result = act(action)
        last_result = result #save the result

        print(f"Step {step}: Result: {result}")

        # Check if agent is done
        if action['tool'] == 'finish':
            print(f"\nTask completed! Final answer: {result}")
            break

        step += 1

""" 
#Making run_agent2 - run_agent 4 into comments
#Function run_agent2 for the second query
def run_agent2(task: str):
    print(f"\nAgent recieved task: {task} ")
    print("-" * 47)

    step = 1
    last_result = None #track the last result
    #Run the while loop
    while True:
        print(f"\nStep {step}: Thinking....")

        action  = think(task, last_result)

        print(f"\nStep {step}: Agent decided to: {action['tool']}")
        result = act(action)
        last_result = result
        print(f"Step {step}: Result: {result}")

        # Check if agent is done
        if action['tool'] == 'finish':
            print(f"\nTask completed! Final answer: {result}")
            break

        step += 1

#Function run_agent3 for the third query
def run_agent3(task: str):
    print(f"\nAgent recieved task: {task}")
    print("-" * 54)

    step = 1
    last_result = None
    #Run the while loop
    while True:
        print(f"\nStep {step}: Thinking.....")
        action = think(task, last_result)

        print(f"\nStep {step}: Agent decided to: {action['tool']}")
        result = act(action)
        last_result = result
        print(f"Step{step}: Result: {result}")

        if action['tool'] == 'finish':
            print(f"\n Task is completed: Final answer: {result}")
            break

        step +=1

#Function run_agent4 for the fourth query
def run_agent4(task: str):
    print(f"\nAgent recieved task: {task}")
    print("-" * 56)

    step = 1
    last_result = None
    #Run the while loop
    while True:
        print(f"\nStep {step}: Thinking.....")
        action = think(task, last_result)

        print(f"\nstep {step}: Agent decided to: {action['tool']}")
        result = act(action)
        last_result = result
        print(f"Step{step}: Result: {result}")

        if action['tool'] == 'finish':
            print(f"\nTask is completed: Final answer: {result}")
            break

        step +=1
#Comment Ends
"""

def think(task: str, last_result: str = None) -> dict:

    #If we already have a search result , we're done
    if last_result:
        return{
            "tool": "finish",
            "input": last_result
        }

    # Simulate the LLM deciding what to do
    # For now we hardcore logic - later a real LLM will do this

    if "capital" in task.lower():
        return {
            "tool" : "search",
            "input" : task
        }
    elif "weather" in task.lower():
        return{
            "tool" : "weather",
            "input" : task
        }

    elif "food" in task.lower():
        return{
            "tool": "food",
            "input": task
        }

    elif "market" in task.lower():
        return{
            "tool" : "market",
            "input" : task
        }

    else:
        return {
            "tool": "finish",
            "input": "I dont know how to handle this taskl yet"
        }

def act(action:dict) -> str:
    #Execute whatever tool the agent decided to use

    if action['tool'] == 'search':
        return fake_search(action['input'])

    elif action['tool'] == 'weather':
        return fake_weather(action['input'])

    elif action['tool'] == 'food':
        return fake_food(action['input'])


    elif action['tool'] == 'finish':
        return action['input']

    elif action['tool'] == 'market':
        return fake_market(action['input'])

    else:
        return "Unknown tool!"


def fake_search(query: str) -> str:
    #Simulate a search result for now
    return f"Search result for '{query}': New Delhi is the capital of India."

def fake_weather(query2: str) -> str:
    #Simulate a search result for now
    return f"Search result for '{query2}': The weather is Rainy day with 98% chances of precipitation and wind speed 10KMPH."

def fake_food(query3: str) -> str:
    #Simulate a search result for now
    return f"Search result for  '{query3}': The famous food of Delhi is Chole Bhature."

def fake_market(query4: str) -> str:
    #Simulate a search result for now
    return f"Search result for '{query4}': The famous market of Delhi is Chandani Chowk."

run_agent("What is the capital of India?")
run_agent("What is the weather today?")
run_agent("What is the famous food of Delhi?")
run_agent("What is the famous market of Delhi?")