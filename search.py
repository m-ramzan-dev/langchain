from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent


@tool
def search(query: str) -> str:
    """
    Search for information about a given query.
    Args:        query (str): The search query.
    Returns:        str: The search results.
    """
    return "Multan weather is sunny with a high of 30°C and a low of 20°C. No precipitation expected."


#llm = ChatOllama(model="gemma3:4b", temperature=0.0)
llm = ChatOllama(model="llama3.1:8b", temperature=0.0)
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain!")
    try:
        response = agent.invoke({"messages": [HumanMessage(content="What's the weather like in Multan?")]})
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    


if __name__ == "__main__":
    main()