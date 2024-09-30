from src.our_crew_of_agents.crew import OurCrewOfAgents
from dotenv import load_dotenv
load_dotenv()

print("Calling our crew of agents...")
OurCrewOfAgents().crew().kickoff()