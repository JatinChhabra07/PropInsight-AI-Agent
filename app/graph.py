from typing import TypedDict, List, Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from app.agents import financial_node, tools_list
from langgraph.prebuilt import ToolNode, tools_condition

class AgentState(TypedDict):
    messages:Annotated[List, add_messages]

workflow = StateGraph(AgentState)

workflow.add_node("financial_agent", financial_node)
workflow.add_node("tools", ToolNode(tools_list))
workflow.add_edge(START, "financial_agent")
workflow.add_conditional_edges(
    "financial_agent",
    tools_condition,
)
workflow.add_edge("tools", "financial_agent")

app = workflow.compile()
