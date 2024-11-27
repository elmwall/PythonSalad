# SITE KIT
# This script opens a kit of web sites (in Chrome) and softwares you need for specific activities or projects. 

# Keep a directory named "sight_kit_addendum" in the same folder as the script. Use separate .txt files for your different web kits.
# In the text file, paste all relevant web pages, separate them by line breaks, ordered depending on the mode you want to use.

# Use the following format:
# ---standard_mode:
# YOUR.urls
# ---incognito_mode:
# YOURincognito.urls



# MODULES
import os
import sys
import webbrowser


# DIRECTORIES
KITS_PATH = "./sight_kit_addendum"
BROWSER_PATH_INCOG = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
BROWSER_PATH = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


# REGISTER all kit files available in kit directory.
files = os.listdir(KITS_PATH)
file_range = list(range(len(files)))
files = {str(x+1): files[x] for x in file_range}


# FUNCTION for processing kit entries into categories.
def main(PATH, files_list):

    # USER INPUT on which file to use. Cancel if non-existent option is selected.
    try:
        url_file = PATH + "/" + files_list[input("\nEnter kit file number: ")]
    except:
        print("Invalid key. Exiting.\n")
        sys.exit()

    # EXTRACT URLS
    try:
        with open(url_file, "r") as url_file:
            all_urls = url_file.read().replace("---standard_mode---", "").split("---softwares---")
            software_urls = all_urls[1]
            web_urls = all_urls[0].split("---incognito_mode---")
    except:
        print("Error. Invalid file.")

    incog_urls = list(filter(None, web_urls[1].splitlines()))
    standard_urls = list(filter(None, web_urls[0].splitlines()))
    software_urls = list(filter(None, software_urls.splitlines()))

    return incog_urls, standard_urls, software_urls



# MAIN FUNCTION

# - COLLECT INFO FOR OPERATION
print(f"\n\nThere are {len(files)} files availabe:")
for number, file in files.items():
    print(" ", number, " ", file)

web_incog, web_standard, softwares = main(KITS_PATH, files)

# Pair browser and URL
browser_and_target = {
    BROWSER_PATH_INCOG: web_incog,
    BROWSER_PATH: web_standard,
}



# - CONDUCT OPERATION
# OPEN SOFTWARES
for url in softwares:
    try:
        os.startfile(url)
    except:
        print(f"\nError! Executable could not be accessed from: {url}")

# BROWSER
# Pre-open Chrome. Opens start page tab, and also prevents non-responsiveness due to slow startup.
os.startfile("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
# TO DO: ADD DELAY HERE

# OPEN SITES 
for browser, links in browser_and_target.items():
    webbrowser.get(browser)
    for url in links:
        webbrowser.get(browser).open(url)

print("\nDone!\n")

