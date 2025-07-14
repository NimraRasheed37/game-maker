from agents import Agent
from agents import RunContextWrapper
import chainlit as cl 

def orchestrator_handoff(agent: Agent):
    async def _ob_handoff(ctx: RunContextWrapper[None]):
        await cl.message(
            content = f"Handing off to '{agent.name}'..."
        ).send()
        
        cl.user_session.set("agent", agent)
        return _on_handoff