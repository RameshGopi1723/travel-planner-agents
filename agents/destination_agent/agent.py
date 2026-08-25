from google.adk.agents import Agent


def create_destination_agent(output_key: str = "destination_result") -> Agent:
    return Agent(
        model="gemini-2.5-flash",
        mode="chat",
        disallow_transfer_to_parent=True,
        disallow_transfer_to_peers=True,
        name="destination_agent",
        output_key=output_key,
        description="...",
        instruction="""...""",
    )


destination_agent = create_destination_agent()
root_agent = destination_agent