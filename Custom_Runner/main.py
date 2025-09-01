from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio
from agents import RunConfig

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=client,
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)


agent = Agent(
    name = "First Agent",
    instructions="You are a helpful assistant. Answer questions to the best of your ability.",
    model=model 
)

async def main():
    prompt = input("Ask your question: ")
    result = await Runner.run(agent, prompt, run_config=config)
    print("\n🤖 Response:\n", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

                             

