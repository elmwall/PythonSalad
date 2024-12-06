import json


def load_profiles():
    with open("./sight_kit_addendum/profiles.json", "r") as f:
        return json.load(f)

def load_activities():
    with open("./sight_kit_addendum/resources.json", "r") as f:
        return json.load(f)


profiles = load_profiles().get("profiles")
activities = load_activities().get("resources")

profile_options = {str(x+1): profiles[x].get("name") for x in range(len(profiles))}
print(profile_options)
# for p in profiles:


# print(profiles)