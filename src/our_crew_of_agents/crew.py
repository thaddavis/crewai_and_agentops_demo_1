from crewai import Crew, Process, Agent
from crewai.project import CrewBase, agent, crew

@CrewBase
class OurCrewOfAgents():
	@agent
	def george_washington(self):
		return Agent(
			config=self.agents_config['george_washington'],
    	verbose=True
		)
	@agent
	def thomas_jefferson(self):
		return Agent(
			config=self.agents_config['thomas_jefferson'],
    	verbose=True
		)
	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=[],
			process=Process.sequential,
			verbose=True,
		)