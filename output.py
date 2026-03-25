import json

def save_results(results):
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)