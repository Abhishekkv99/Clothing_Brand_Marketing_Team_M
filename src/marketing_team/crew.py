from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class MarketingTeamCrew():
    """MarketingTeam crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self._cache = {}

    @agent
    def marketing_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['marketing_manager'],
            verbose=True,
            allow_delegation=True,
            memory=True
        )

    @agent
    def market_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['market_researcher'],
            tools=[SerperDevTool()],
            verbose=True,
            memory=True
        )

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator'],
            verbose=True,
            memory=True
        )

    @task
    def market_research_task(self) -> Task:
        if 'market_research_task' not in self._cache:
            self._cache['market_research_task'] = Task(
                config=self.tasks_config['market_research_task'],
            )
        return self._cache['market_research_task']

    @task
    def content_strategy_task(self) -> Task:
        if 'content_strategy_task' not in self._cache:
            self._cache['content_strategy_task'] = Task(
                config=self.tasks_config['content_strategy_task'],
                context=[self.market_research_task()]
            )
        return self._cache['content_strategy_task']

    @task
    def review_and_approval_task(self) -> Task:
        if 'review_and_approval_task' not in self._cache:
            self._cache['review_and_approval_task'] = Task(
                config=self.tasks_config['review_and_approval_task'],
                context=[self.market_research_task(), self.content_strategy_task()]
            )
        return self._cache['review_and_approval_task']

    @crew
    def crew(self) -> Crew:
        return Crew(
            # The manager_agent should not be in the agents list
            agents=[agent for agent in self.agents if agent.role != self.marketing_manager().role],
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=self.marketing_manager(),
            verbose=True,
            memory=True
        )
