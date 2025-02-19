from pydantic import BaseModel

class Agent(BaseModel):
    role: str
    description: str
    backstory: str

fruit_classifier = Agent(
    role="Fruit Classifier",
    description="Classifies whether the fruit is ripe or not.",
    backstory="This agent uses a model to evaluate fruit ripeness based on images."
)

ripeness_decider = Agent(
    role="Ripeness Decider",
    description="Decides whether the fruit is ripe or not.",
    backstory="This agent evaluates the classification result and determines harvest readiness."
)

farmer_notifier = Agent(
    role="Farmer Notifier",
    description="Sends an alert if the fruit is ripe.",
    backstory="This agent alerts farmers about the readiness of the fruit."
)
