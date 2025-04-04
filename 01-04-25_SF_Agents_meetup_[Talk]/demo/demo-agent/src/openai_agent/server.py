import asyncio

from acp.server.highlevel import Server, Context
from beeai_sdk.providers.agent import run_agent_provider
from beeai_sdk.schemas.metadata import UiDefinition, UiType
from beeai_sdk.schemas.text import TextInput, TextOutput

from agents import Agent, Runner

async def run():
    server = Server("openai-agent")

    @server.agent(
        name="openai-agent",
        description="OpenAI Agent to showcase beeai platform extension",
        input=TextInput,
        output=TextOutput,
        ui=UiDefinition(
            type=UiType.hands_off, userGreeting="Write a haiku poem about:"
        ),
    )
    async def openai_agent_example(input: TextInput, ctx: Context) -> TextOutput:

        agent = Agent(name="Assistant", instructions="You are a helpful assistant")
        result = await Runner.run(agent, f"Write a haiku about {input}")

        return TextOutput(text=result.final_output)
    
    await run_agent_provider(server)


def main():
    asyncio.run(run())
