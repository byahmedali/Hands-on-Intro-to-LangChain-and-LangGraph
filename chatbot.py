import chainlit as cl
import asyncio
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from dotenv import load_dotenv

# Load .evn
load_dotenv()

# Initialize the LLM
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {"messages": response}


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


# Add a config thread
config = {"configurable": {"thread_id": "abc123"}}


@cl.on_message
async def handle_message(message: cl.Message):
    # Convert user input to HumanMessage
    user_message = HumanMessage(content=message.content)
    # Invoke the app with the correct message format
    # response = app.invoke({"messages": [user_message]}, config)
    # content = response["messages"][-1].content

    msg = cl.Message(content="")
    await msg.send()
    
    for chunk, metadata in app.stream({"messages": [user_message]},
                                      config,
                                      stream_mode="messages"):
        if isinstance(chunk, AIMessage):  # Filter to just model responses
            # Stream the token
            await msg.stream_token(chunk.content)
            await asyncio.sleep(0.015)
    
    # Remove the typing cursor after streaming is complete
    await msg.send()