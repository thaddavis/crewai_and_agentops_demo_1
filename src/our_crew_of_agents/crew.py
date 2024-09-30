from crewai import Crew, Process, Agent, Task
from crewai.project import CrewBase, agent, crew, task

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
	@task
	def write_declaration(self):
		return Task(
			config=self.tasks_config["write_declaration"],
		)
	@task
	def military_strategy(self):
		return Task(
			config=self.tasks_config["military_strategy"],
		)
	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)