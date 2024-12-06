import json
from resources.tm_method import format, searchable, prompts

RESOURCE_PATH = "./resources"
FILES = ["/tm.json", "/ch.json", "/em.json"]

# Collect and review resources
def load_resource(file):
    with open(RESOURCE_PATH + file, "r") as f:
        return json.load(f)
    
def print_resource(dictionary):
    pass
    # print(f"\n  TEAM: {dictionary.get("title").upper()}\n")
    # print(f"  Rating: {}\n")


def explanation():
    n = 10
    sp = " "
    print("  TITLE     ", "DESCRIPTION\n-------------------------------------------------------")
    for key in format.keys():
        fill = n - len(key)
        print(f"  {key}" + sp*fill, format[key])


def search_resource(resource):
    print(f"Searchable categories:")
    for numeral, title in searchable.items():
        print(f"  {numeral}: {title}")
    verified = False
    while not verified:
        selection = input("Enter numeral: ")
        if selection in searchable.keys():
            subject = searchable[selection]
            print(f"Selected: {subject}")
            verified = True
        else:
            print("Invalid selection! Please try again.")
    # if searchable[selection] == "h-score":
    #     for r in resource:
    #         if input(prompts["h-score"]) in r.get("h-score"):
    #             print(r)
    #         else:
    #             print("No records found.")
    # else:
    for entry in resource:
        # print(r.get(key))
        search_for = input(prompts[subject])
        if isinstance(entry[subject], list):
            if any(search_for.lower() in item.lower() for item in entry[subject]):
                print(entry)
            else:
                print("No records found.")
        elif isinstance(entry[subject], str):
            if search_for.lower() in entry[subject].lower():
                print(entry)
    # for r in resource:
    #     if isinstance(r[selection], str):
    #         if tag.lower() in r[selection].lower():
    #             print(r)
    #     if isinstance(r[selection], list):
    #         if any(tag.lower() == item.lower() for item in r[selection]):
    #             print(r)
    
    
    # for r in resource:
    #     print(f"  {r[selection]}")
    # verified = False
    # while not verified:
    #     tag = input("Enter keyword: ")
    #     if tag in format.keys():
    #         verified = True
    # for r in resource:
    #     if isinstance(r[selection], str):
    #         if tag.lower() in r[selection].lower():
    #             print(r)
    #     if isinstance(r[selection], list):
    #         if any(tag.lower() == item.lower() for item in r[selection]):
    #             print(r)


resource = load_resource("/tm.json")["tm"]
char = load_resource("/ch.json")["ch"]
elem = load_resource("/em.json")["em"]
explanation()
# print(resource)
search_resource(resource)



# print_resource(resource[0])