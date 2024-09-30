from dotenv import load_dotenv
load_dotenv()
from src.our_crew_of_agents.crew import OurCrewOfAgents
import os
import agentops

agentops.init(os.getenv("AGENTOPS_API_KEY"))

print("Calling our crew of agents...")
OurCrewOfAgents().crew().kickoff()