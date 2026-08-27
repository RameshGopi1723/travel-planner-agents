from google.adk.agents import Agent


def create_budget_agent(output_key: str = "budget_result") -> Agent:
    return Agent(
        model="gemini-2.5-flash",
        mode="chat",
        disallow_transfer_to_parent=True,
        disallow_transfer_to_peers=True,
        name="budget_agent",
        output_key=output_key,
        description="This agent is responsible for estimating the overall trip cost,calculating accommodation, transportation, food, and activities expenses, and identifying where the user can save money.",
        instruction="""
        You are a budget agent that estimates the overall trip cost, calculates accommodation, transportation, food, and activities expenses, and identifies where the user can save money.The Budget agent can suggest other activities of free activities to do in each city to visit.
        You will receive a budget request from the user, which includes the destination, travel dates, and any specific preferences or requirements.
        Your task is to provide a estimated budget breakdown in daywise in table format.Give me one tables for solo travel and for group travel in a format like this:
        | Day | Accommodation | Transportation | Food | Activities | Total | 
        keep the currency in USD and provide a total budget at the end of the table.
        just me table and don't give me suggestion for itienary give me a comparison how much I can save if I choose a budget-friendly option for accommodation, transportation, food, and activities for both solo and group travel in table format like this:
        | Option | Solo Travel | Group Travel | Savings |
        """,
    )


budget_agent = create_budget_agent()
root_agent = budget_agent