from google.adk.agents import Agent


def create_itinerary_agent(output_key: str = "itinerary_result") -> Agent:
    return Agent(
        model="gemini-2.5-flash",
        mode="chat",
        disallow_transfer_to_parent=True,
        disallow_transfer_to_peers=True,
        name="itinerary_agent",
        output_key=output_key,
        description="...",
        instruction="""...""",
    )


itinerary_agent = create_itinerary_agent()
root_agent = itinerary_agent