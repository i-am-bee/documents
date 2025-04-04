
from agents import Agent, Runner

async def agent(input):
    agent = Agent(name="Assistant", instructions="You are a helpful assistant")

    result = await Runner.run(agent, f"Write a haiku about {input}")

    return result.final_output