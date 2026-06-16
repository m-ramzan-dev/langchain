from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class Source(BaseModel):
    """Represents a source of information."""
    url:str = Field( description="The URL of the source")
    title:str = Field(description="The title of the source")
    snippet:str = Field(description="A brief snippet from the source")


class AgentResponse(BaseModel):
    """Represents the response from the agent."""
    answer: str = Field(description="The answer to the user's query")
    sources: list[Source] = Field(description="A list of sources used to generate the answer")

tavily_search_tool = TavilySearch(
    max_results=5,
    topic="general"
)
#llm = ChatOllama(model="gemma3:4b", temperature=0.0)
llm = ChatOllama(model="llama3.1:8b", temperature=0.0)
tools = [tavily_search_tool]
agent = create_agent(model=llm, tools=tools,response_format=AgentResponse)


def main():
    print("Hello from langchain!")
    try:
        response = agent.invoke({"messages": [HumanMessage(content="Find most recent jobs for AI Engineer on linkedin")]})
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    


if __name__ == "__main__":
    main()