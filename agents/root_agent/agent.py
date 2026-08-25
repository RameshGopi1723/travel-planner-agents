from google.adk.agents import Agent, ParallelAgent, SequentialAgent
try:
    from ..accommodation_agent.agent import create_accommodation_agent
    from ..budget_agent.agent import create_budget_agent
    from ..destination_agent.agent import create_destination_agent
    from ..itinerary_agent.agent import create_itinerary_agent
    from ..transportation_agent.agent import create_transportation_agent
except ImportError:
    from agents.accommodation_agent.agent import create_accommodation_agent
    from agents.budget_agent.agent import create_budget_agent
    from agents.destination_agent.agent import create_destination_agent
    from agents.itinerary_agent.agent import create_itinerary_agent
    from agents.transportation_agent.agent import create_transportation_agent


MODEL = "gemini-2.5-flash"


final_plan_agent = Agent(
    model=MODEL,
    mode="chat",
    output_key="final_travel_plan",
    name="final_plan_agent",
    description="Consolidates all specialist findings into the final travel plan.",
    instruction="""
You are the Final Travel Plan Specialist. Consolidate the specialist findings
below into one consistent, actionable response for the traveler.

Destination findings:
{destination_result}

Itinerary findings:
{itinerary_result}

Accommodation findings:
{accommodation_result}

Transportation findings:
{transportation_result}

Budget findings:
{budget_result}

Return the final plan with: trip snapshot and assumptions, recommended
destination, day-by-day itinerary, accommodation shortlist, transportation plan,
budget breakdown, savings options, booking checklist, and risks to verify. Resolve
inconsistencies using the original request and clearly label estimates. Do not
mention internal agents or workflow steps.
""",
)


planning_parallel = ParallelAgent(
    name="itinerary_and_accommodation",
    description="Creates itinerary and accommodation recommendations after destination selection.",
    sub_agents=[
        create_itinerary_agent(),
        create_accommodation_agent(),
    ],
)


root_agent = SequentialAgent(
    name="root_agent",
    description="Coordinates specialist travel agents and produces one complete travel plan.",
    sub_agents=[
        create_destination_agent(),
        planning_parallel,
        create_transportation_agent(),
        create_budget_agent(),
        final_plan_agent,
    ],
)