# SIGHT KIT
# This script opens, in Chrome, a web site kit you want to keep in sight for specific activities or projects.

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


PATH = "./sight_kit_addendum"
# SPECIFY BROWSERS AND MODE
browser_path_incog = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


# FILE DICTIONARY
# Show all kit files available in library directory.
files = os.listdir(PATH)
file_range = list(range(len(files)))
files = {str(x+1): files[x] for x in file_range}


def main(PATH, files):
    # USER INPUT on which file to use. Cancel if non-existent option is selected.
    try:
        url_file = PATH + "/" + files[input("\nEnter kit file number: ")]
    except:
        print("Invalid key. Exiting.\n")
        sys.exit()

    # EXTRACT URLS
    try:
        with open(url_file, "r") as url_file:
            all_urls = url_file.read().split("---incognito_mode:")
    except:
        print("Error. Invalid file.")

    urls_incog = all_urls[1].splitlines()
    urls = all_urls[0].splitlines()
    urls.remove("---standard_mode:")

    return urls_incog, urls



# MAIN FUNCTION
print(f"\n\nThere are {len(files)} files availabe:")
for x, y in files.items():
    print(" ", x, " ", y)

urls_incog, urls = main(PATH, files)


# PAIR BROWSER AND URL
browser_and_target = {
    browser_path_incog: urls_incog,
    browser_path: urls,
}


# OPEN SITES
# Pre-open Chrome. Opens start page tab, and also prevents non-responsiveness at startup.
os.startfile("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")

# OPEN SPECIFIED WEBPAGES
for browser, links in browser_and_target.items():
    webbrowser.get(browser)
    for url in links:
        webbrowser.get(browser).open(url)
print("\nDone!\n")