from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from dotenv import load_dotenv

load_dotenv();

@tool
def search(query : str) -> str:
    """
    tool that searches over internet
    args:
        query : the query to search for
    Returns:
        the search result
    """
    print(f"searching for {query}")
    return "tokyo weather is sunny"

llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

tools=[search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("hello workd")
    result = agent.invoke({"messages":HumanMessage(content="what is the weather in tokyo")})
    print(result)
 
# i'll become so good that everyone will see me
if __name__ == "__main__":
    main()
