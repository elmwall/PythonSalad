import json
from resources.tm_method import format, searchable, prompts

RESOURCE_PATH = "./resources"
FILES = ["/tm.json", "/ch.json", "/em.json"]

# Collect and review resources
def load_resource(file):
    with open(RESOURCE_PATH + file, "r") as f:
        return json.load(f)

# Viewing party content correctly
def viewer(party_list):
    for entry in party_list:
        print("_" * 40)
        # Print title
        print(f"\n{entry.get("title").upper()}\n")
        for subject, info in entry.items():
            # For list entries, print bullet list
            output = str()
            if subject not in ["title"]:
                if isinstance(info, list) or isinstance(info, set):
                    n = 10
                    space = " "
                    for d in info:
                        fill = n - len(d)
                    #     print(f" - {d}")
                        output += space*fill + str(d).capitalize()
                    fillx = n - len(subject)
                    print(f"{subject.capitalize()}:{space*fillx}{output}")
                # For dictionary entries, print bullet list with separation of items
                elif isinstance(info, dict):
                    print(f"{subject.capitalize()}:")
                    for x, y in info.items():
                        print(f" - {x}:", f"{y}")
                    print()
                else:
                    print(f"{subject.capitalize()}:", str(info))
        print()
        # for x in entry["notes"]:
        #     print(x)
        # for title, note in entry["notes"]:
        #     print(f"{title}: {note}")


# Print party documentation
def explanation():
    print(f"  {"TITLE":<12}{"DESCRIPTION":<20}\n", "-"*50)
    for key in format.keys():
        print(f"  {key:<12}{format[key]:<20}")
    # n = 10
    # space = " "
    # # print("  TITLE     ", "DESCRIPTION\n", "-" * 40)
    # for key in format.keys():
    #     fill = n - len(key)
    #     print(f"  {key}" + space*fill, format[key])


def table(data):
    pass

# Search party for keywords within entries
def search_resource(party):
    findings = list()

    # Print guide for searching
    print(f"Searchable categories:")
    for numeral, title in searchable.items():
        print(f"  {numeral}: {title}")

    # Select search subject
    # Loop requesting valid entry for search subject
    verified = False
    while not verified:
        selection = input("Enter numeral: ")
        if selection in searchable.keys():
            subject = searchable[selection]
            print(f"Selected: {subject}")
            verified = True
        else:
            print("Invalid selection! Please try again.")

    # Request keyword and search within selected subject
    search_for = input(f"\n{prompts[subject]}")
    
    for entry in party:
        if isinstance(entry[subject], list):
            if any(search_for.lower() in item.lower() for item in entry[subject]):
                findings.append(entry)
            else:
                print("No records found.")
        elif isinstance(entry[subject], str):
            if search_for.lower() in entry[subject].lower():
                findings.append(entry)
            else:
                print("No records found.")
        elif isinstance(entry[subject], dict):
            if any(search_for.lower() in item.lower() for item in entry[subject].keys()):
                findings.append(entry)
                details = {key: value for key, value in entry[subject].items() if search_for.lower() in key.lower()}
                # print(f"Hits for {search_for}:")
                
                for x, y in details.items():
                    print(f" - {x} as {y} in '{entry["title"]}'")
                # for key, value in entry[subject].items():
                #     print(key, value)
                # detail = {key: value for key, value in entry[subject].items() if search_for in value}
                # print(detail)
                # for key, value in entry[subject].items() if search_for in value:
                #     print(f"{entry["title"]}: {value} as {key}")

    return findings

def character_analysis(data_list):
    # for x in data_list:
    #     x["test"] = "hej"
    # return data_list
    registered_ability = list()
    
    for party in data_list:
        character_abilities = dict()

        characters = list()
        effects = list()
        abilities = set()
        multiples = set()

        for member in party["members"].keys():
            characters.append(member)
        character_abilities[party["title"]] = characters
        for character in character_data:
            if character["name"] in characters:
                if character["ability"] in abilities:
                    multiples.add(character["ability"])
                abilities.add(character["ability"])
        character_abilities["ability"] = abilities
        character_abilities["duplet"] = multiples
        party["abilities"] = abilities
        party["duplets"] = multiples
        for entry in ability_data:
        
            if entry["type"] == "effect":

                if all(item.lower() in (n.lower() for n in abilities) for item in entry["relevance"]):
                    effects.append(entry["name"])
        character_abilities["effects"] = effects
        registered_ability.append(character_abilities)
    # print(data_list)

    # registered_ability = list()
    
    # for x in data_list:
    #     character_abilities = dict()

    #     characters = list()
    #     effects = list()
    #     abilities = set()
    #     duplet = list()

    #     for y in x["members"].keys():
    #         characters.append(y)
    #     character_abilities[x["title"]] = characters
    #     for z in character_data:
    #         if z["name"] in characters:
    #             if z["ability"] in abilities:
    #                 duplet.append(z["ability"])
    #             abilities.add(z["ability"])
    #     character_abilities["ability"] = abilities
    #     character_abilities["duplet"] = duplet
    #     for m in ability_data:
        
    #         if m["type"] == "effect":

    #             if all(item.lower() in (n.lower() for n in abilities) for item in m["relevance"]):
    #                 effects.append(m["name"])
    #     character_abilities["effects"] = effects
    #     registered_ability.append(character_abilities)
    # print(registered_ability)




party = load_resource("/tm.json")["tm"]
character_data = load_resource("/ch.json")["ch"]
ability_data = load_resource("/em.json")["em"]
explanation()
# print(party)
findings = search_resource(party)
# print(findings)

character_analysis(findings)
viewer(findings)

# test = add_em(findings)
# print(test)
# print_resource(party[0])