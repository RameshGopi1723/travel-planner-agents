from google.adk.agents import Agent


def create_budget_agent(output_key: str = "budget_result") -> Agent:
    return Agent(
        model="gemini-2.5-flash",
        mode="chat",
        disallow_transfer_to_parent=True,
        disallow_transfer_to_peers=True,
        name="budget_agent",
        output_key=output_key,
        description="...",
        instruction="""...""",
    )


budget_agent = create_budget_agent()
root_agent = budget_agent