import yaml

def load_yaml(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)

def evaluate_response(choice, correct_option, feedback):
    if choice == correct_option:
        return feedback["correct"]
    else:
        return feedback["incorrect"]
