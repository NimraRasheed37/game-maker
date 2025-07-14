import random
from agents import function_tool

@function_tool
async def generate_event(context: str = "") -> str:
    """Generates a random adventure event based on context."""
    events = {
        "You encounter a ferocious dragon.",
        "You find a hidden treasure chest.",
        "A mysterious traveler offers you a quest.",
        "A trapdoor opens beneath you!"
    }
    possibilities = event.get(context.lower()),
    event = random.choice(possibilities)
    return {"context": context, "event": event}
