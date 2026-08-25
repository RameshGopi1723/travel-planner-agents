# Travel Planner Multi-Agent System

A Google Agent Development Kit (ADK) travel planner made of five independent specialist agents and one master workflow agent.

## Architecture

The specialists are independently runnable and are also used as separate child instances by the master workflow.

```text
User
 |
 v
root_agent (SequentialAgent)
 |
 +-- destination_agent
 |
 +-- itinerary_and_accommodation (ParallelAgent)
 |   +-- itinerary_agent
 |   +-- accommodation_agent
 |
 +-- transportation_agent
 |
 +-- budget_agent
 |
 +-- final_plan_agent
 |
 v
Final Travel Plan
```

### Workflow order

1. `destination_agent` recommends destinations.
2. `itinerary_agent` and `accommodation_agent` run in parallel.
3. `transportation_agent` creates the intercity and local transportation plan.
4. `budget_agent` estimates the complete trip cost.
5. `final_plan_agent` consolidates the findings into one final travel plan.

The ADK graph displays the agent hierarchy. Use the Events or Traces panel to see the runtime execution order.

## Project structure

```text
Travel Planner/
├── agents/
│   ├── root_agent/
│   ├── destination_agent/
│   ├── itinerary_agent/
│   ├── accommodation_agent/
│   ├── transportation_agent/
│   └── budget_agent/
├── .env
└── .venv/
```

Each agent folder contains an `agent.py` and `__init__.py`. Every standalone specialist exports `root_agent`, as required by the ADK CLI. The master uses factory functions to create separate child instances, so standalone agents do not inherit the master agent's parent relationship.

## Requirements


The project currently uses:

```text
gemini-2.5-flash
```

## Configuration

Create or update `.env` in the project root:

```env
GOOGLE_API_KEY="your-google-api-key"
```

Keep the API key private. Do not commit `.env` to source control.

## Installation

If the virtual environment already exists:

```bash
cd "/Users/gopinathr/Travel Planner"
source .venv/bin/activate
```

If ADK is not installed yet:

```bash
pip install google-adk
```

## Run the complete workflow in the browser

Start the ADK development web server from the project root:

```bash
cd "/Users/gopinathr/Travel Planner"
source .venv/bin/activate
adk web agents --port 8001
```

Open this address in a browser:

```text
http://127.0.0.1:8001
```

Select `root_agent`, click **New Session**, and send a request such as:

```text
Plan a complete 7-day trip to Tokyo for two people traveling from New York in October. Our total budget is $3,500. We enjoy local food, Japanese culture, museums, neighborhoods, and light nature activities. We prefer a relaxed pace and accommodation near public transportation.
```

Stop the server with `Ctrl+C`.

## Run an individual agent

Every specialist can also run independently from the terminal:

```bash
adk run agents/destination_agent
adk run agents/itinerary_agent
adk run agents/accommodation_agent
adk run agents/transportation_agent
adk run agents/budget_agent
```

Run the complete master workflow from the terminal:

```bash
adk run agents/root_agent
```

A single prompt can be supplied directly:

```bash
adk run agents/transportation_agent "Plan transportation from New York to Tokyo for two people and compare flights, travel time, and approximate costs."
```

## Example specialist prompts

### Destination

```text
Recommend three destinations for a 7-day trip from New York for two people. We enjoy beaches, local food, culture, and warm weather. Our total budget is $3,000.
```

### Itinerary

```text
Create a relaxed 5-day itinerary for Tokyo focused on food, temples, museums, neighborhoods, and nearby nature. Group nearby places together and include estimated travel times.
```

### Accommodation

```text
Recommend three accommodation options or accommodation types in Tokyo for two people staying 7 nights with a budget of about $150 per night. Prefer safe central areas near public transportation.
```

### Transportation

```text
Plan transportation from New York to Tokyo for two people. Compare flights by approximate cost, travel time, and number of stops. Also recommend local transportation in Tokyo.
```

### Budget

```text
Estimate the total cost of a 7-day Tokyo trip for two people traveling from New York. Include flights, accommodation, food, local transportation, activities, insurance, and a 10% contingency.
```

## Validation

Compile all agent modules:

```bash
PYTHONPATH=agents .venv/bin/python -m py_compile agents/*/agent.py
```

Verify the master workflow structure:

```bash
PYTHONPATH=agents .venv/bin/python -c 'from root_agent.agent import root_agent; print(root_agent.name); print([agent.name for agent in root_agent.sub_agents])'
```

Expected child stages:

```text
root_agent
['destination_agent', 'itinerary_and_accommodation', 'transportation_agent', 'budget_agent', 'final_plan_agent']
```

## Troubleshooting

### `Agent 'my_agent' not found`

`my_agent` was the old project name. Start the server with the current directory:

```bash
adk web agents --port 8001
```

Then open a fresh browser tab at `http://127.0.0.1:8001`, select `root_agent`, and click **New Session**.

### `Context variable not found`

Specialist agents are designed to work independently. If this error appears, restart the ADK server and create a new session. Do not reuse a session created by an older version of the workflow.

### `MODEL_RETURNED_NO_CONTENT`

Stop any old ADK server process, start a fresh one, and create a new session. The final plan agent uses `mode="chat"` so it returns normal response text rather than relying on the task-mode `finish_task` flow.

### Import errors when testing manually

The root agent is loaded by ADK with `agents` as the module path. For direct Python checks, use:

```bash
PYTHONPATH=agents .venv/bin/python -c 'from root_agent.agent import root_agent; print(root_agent.name)'
```
