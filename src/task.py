from pydantic import BaseModel
from agent import fruit_classifier, ripeness_decider, farmer_notifier, Agent

class Task(BaseModel):
    description: str
    agent: Agent

task1 = Task(description="Classify the fruit and check if it's ripe", agent=fruit_classifier)
task2 = Task(description="Decide whether the fruit is ready for harvest", agent=ripeness_decider)
task3 = Task(description="Send an alert if the fruit is ripe", agent=farmer_notifier)
