from google.adk.agents import Agent


def create_transportation_agent(output_key: str = "transportation_result") -> Agent:
    return Agent(
        model="gemini-2.5-flash",
        mode="chat",
        disallow_transfer_to_parent=True,
        disallow_transfer_to_peers=True,
        name="transportation_agent",
        output_key=output_key,
        description="...",
        instruction="""...""",
    )


transportation_agent = create_transportation_agent()
root_agent = transportation_agent