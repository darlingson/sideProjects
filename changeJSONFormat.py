import json

def convert_json(input_json):
    output_json = []
    for player in input_json:
        for match in input_json[player]:
            for goal in input_json[player][match]["goals"]:
                output_json.append({
                    "name": player,
                    "day": match,
                    "time": goal["time"],
                    "half": goal["half"]
                })
    return output_json

# Your input JSON data
input_json = json.loads('{"C. Nyondo":{...}}')  # replace with your actual JSON data

# Convert the JSON data
output_json = convert_json(input_json)

# Print the output
for item in output_json:
    print(item)
