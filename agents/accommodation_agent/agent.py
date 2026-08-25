from google.adk.agents import Agent


def create_accommodation_agent(output_key: str = "accommodation_result") -> Agent:
    return Agent(
        model="gemini-2.5-flash",
        mode="chat",
        disallow_transfer_to_parent=True,
        disallow_transfer_to_peers=True,
        name="accommodation_agent",
        output_key=output_key,
        description="...",
        instruction="""...""",
    )


accommodation_agent = create_accommodation_agent()
root_agent = accommodation_agent