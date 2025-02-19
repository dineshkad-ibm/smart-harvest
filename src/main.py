from agent import fruit_classifier, ripeness_decider, farmer_notifier
from task import task1, task2, task3
from crew import Crew

if __name__ == "__main__":
    image_path = "assets/apple.jpeg"
    crew = Crew(agents=[fruit_classifier, ripeness_decider, farmer_notifier], tasks=[task1, task2, task3])
    
    try:
        result = crew.kickoff(inputs={"image_path": image_path})
        print(result)
    except Exception as ex:
        print("An error occurred:", str(ex))
