from agents import function_tool
import random

@function_tool
async def roll_dice(sides: int = 6) -> dict:
    """Rolls a dice with the given number of sides and returns the result."""
    result = random.randint(1, sides)
    return {"sides": sides, "result": result}
