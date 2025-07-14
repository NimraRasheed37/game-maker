import chainlit as cl
from agents import Runner
from agents.run import RunConfig
from config import model, external_client, gemini_config
from gamers.narrator_agent import narrator_agent
from gamers.monster_agent import monster_agent
from gamers.item_agent import item_agent

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message("🧙 Welcome, adventurer! Type anything to begin your journey… (or type 'end' to finish)").send()

@cl.on_message
async def handle(message: cl.Message):
    user_input = message.content.strip().lower()

    if user_input in ["end", "exit", "quit"]:
        await cl.Message("🏁 Your journey concludes here. Farewell, brave soul!").send()
        cl.user_session.set("history", [])  # Clear history
        return

    history = cl.user_session.get("history") or []
    history.append({"role": "user", "content": message.content})

    thinking = await cl.Message("🎲 The story unfolds…").send()

    try:
        result = await Runner.run(
            narrator_agent, 
            history,
            run_config = gemini_config
        )

        thinking.content = result.final_output
        await thinking.update()
        cl.user_session.set("history", result.to_input_list())

    except Exception as e:
        thinking.content = f"❌ Error: {e}"
        await thinking.update()
