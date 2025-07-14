from agents import Agent, handoff
from config import model
from gamers.item_agent import item_agent
from utils.orchestrator import orchestrator_handoff
from tools.roll_dice import roll_dice


monster_agent = Agent(
    name = "MonsterAgent",
    instructions = """ 
    You are the Monster Agent in charge of all combat scenarios.

    Responsibilities:
    * Narrate exciting and vivid battle scenes.
    * Ask the player to roll a dice using the roll_dice() tool.
    * Use the dice result to decide if the player:
    - Wins the fight,
    - Loses and takes damage,
    - Escapes or must fight again.
    * If the player wins, reward them with loot and hand off to ItemAgent.
    * If the fight continues or they lose, narrate consequences and hand off back to NarratorAgent.

    Tools you can use:
    🎲 roll_dice()

    Goal:
    Keep combat thrilling and connected to the main adventure flow.
    """,
    tools = [roll_dice],
    model = model,
    handoffs=[
        handoff(agent=item_agent, on_handoff=orchestrator_handoff(item_agent))
    ]

)
