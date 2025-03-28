import os
import yaml
import threading
import time
from utils import evaluate_response, load_yaml

class IncidentSimulator:
    def __init__(self):
        self.scenarios = []

    def load_scenarios(self, folder="scenarios"):
        for file in os.listdir(folder):
            if file.endswith(".yml"):
                scenario = load_yaml(os.path.join(folder, file))
                self.scenarios.append(scenario)

    def run(self):
        for scenario in self.scenarios:
            print(f"\n🚨 Incident: {scenario['title']}")
            print(scenario["description"])
            print("You have 30 seconds to respond.\n")
            for idx, opt in enumerate(scenario["options"]):
                print(f"{idx + 1}. {opt}")
            
            timer = threading.Timer(30.0, lambda: print("\n⏰ Time's up!"))
            timer.start()

            try:
                choice = int(input("\nYour response (1-4): "))
                timer.cancel()
                feedback = evaluate_response(choice, scenario["correct_option"], scenario["feedback"])
                print(f"\n✅ Feedback: {feedback}")
            except:
                print("❌ Invalid input or timeout.")
