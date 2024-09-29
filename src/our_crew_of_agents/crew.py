from crewai import Crew, Process
from crewai.project import CrewBase, agent, crew

@CrewBase
class OurCrewOfAgents():
	@agent
	def george_washington(self):
		return Agent()
	@agent
	def thomas_jefferson(self):
		return Agent()
	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=[],
			process=Process.sequential,
			verbose=True,
		)