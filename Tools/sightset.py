# This script opens a set of web pages contained in a separate files for quick access.

# MODULES
import os
import webbrowser

path = "./sightset_addendum"

# files = os.listdir(path)
files = os.listdir(path)
file_range = list(range(len(files)))
files = {x+1: files[x] for x in file_range}

for x, y in files.items():
    print(x, y)


# # SPECIFY URLS
# url_file = open("sightset_addendum.txt", "r")
# all_urls = url_file.read().split("---incognito_mode:")
# url_file.close

# urls_inc = all_urls[1].splitlines()
# urls = all_urls[0].splitlines()
# urls.remove("---standard_mode:")


# # SPECIFY BROWSERS AND MODE
# browser_path_inc = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
# browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


# # PAIR BROWSER AND URL
# browser_and_target = {
#     browser_path_inc: urls_inc,
#     browser_path: urls,
# }


# # OPEN SITES

# for browser, links in browser_and_target.items():
#     # webbrowser.get(browser)
#     for url in links:
#         webbrowser.get(browser).open(url)