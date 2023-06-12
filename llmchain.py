# pip install google-search-results


# pip install google-search-results

import os
os.environ["SERPAPI_API_KEY"] = "9ad62748493b99abe25d62d2b3a1b898c5a08f263a2769aa5a84ae70ece3d21e"
os.environ["OPENAI_API_KEY"] = "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"


from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

# First, let's load the language model we're going to use to control the agent.
llm = OpenAI(temperature=0)

# Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
tools = load_tools(["serpapi", "llm-math"], llm=llm)


# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Now let's test it out!
agent.run("What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?")