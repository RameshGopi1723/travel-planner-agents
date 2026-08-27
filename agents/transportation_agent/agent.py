from google.adk.agents import Agent


def create_transportation_agent(output_key: str = "transportation_result") -> Agent:
    return Agent(
        model="gemini-2.5-flash",
        mode="chat",
        disallow_transfer_to_parent=True,
        disallow_transfer_to_peers=True,
        name="transportation_agent",
        output_key=output_key,
        description="""We are planning a trip to new zealand . What are the available modes of transportation and what is their cost ?What are famous places to visit in new zealand ? what is the required duration of days to cover all these must visit tourist spots ?what is the best time to travel to new zealand and what are the different available modes of local transport ? what is the best season to travel to new zealand ?what is the visa required to travel to new zealand as a tourist ? what are the required documents for those ?""",
        instruction="""...""",
    )


transportation_agent = create_transportation_agent()
root_agent = transportation_agent
