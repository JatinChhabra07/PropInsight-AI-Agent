from langchain_groq import ChatGroq
from langchain_core.tools import tool
from app.tools import calculate_rent_rolls
from dotenv import load_dotenv


load_dotenv()

llm = ChatGroq(
    model= "llama-3.3-70b-versatile",
    temperature=0
)

@tool
def financial_tool(file_path:str):
    "Calculates total income and occupancy from a rent roll Excel file"
    return calculate_rent_rolls(file_path)

financial_agent = llm.bind_tools([financial_tool])

def financial_node(state):
    messages = state['messages']

    response = financial_agent.invoke(messages)

    return {"messages": [response]}


tools_list = [financial_tool]
    