from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

tavily_search_tool = TavilySearch(
    max_results=5,
    topic="general"
)
#llm = ChatOllama(model="gemma3:4b", temperature=0.0)
llm = ChatOllama(model="llama3.1:8b", temperature=0.0)
tools = [tavily_search_tool]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain!")
    try:
        response = agent.invoke({"messages": [HumanMessage(content="Find most recent jobs for 'Flutter Developer' on upwork")]})
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    


if __name__ == "__main__":
    main()