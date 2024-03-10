# A Python Side Salad

This is a repository for a little challenge for myself. Sometimes there are those small little annoyances popping up while working with projects or managing files or information that halts the progress. If I find it likely that I'll run into the same issue again, I'll try to create a Python script to solve the issue or speed up the process. 

Sometimes the time saved is minuscule, or there are softwares or tools online that can do the same thing. Well, the points of importance of this activity is, in order: play, practice, practicality. Perhaps something useful comes out of it, but at least I get to reiterate and sharpen my knowledge and skill with Python.



## Current Salad Content 

### Image processing tool
[*image_processing.py*](https://github.com/elmwall/PythonSalad/blob/main/Tools/image_processing.py)

This is a tool to either crop a series of images in a folder, or convert them to PNG or JPEG format. It then saves the modified images in a new subfolder.

#### Motivation
It often happens one has a series of screenshots or other images, but only part of them are necessary. Instead of adjusting them individually, this script can crop all of them using pixel coordinates.

There are also times when there's a sets of images, and one wants to convert all of them, e.g. to .jpeg to save space. The script can perform this on a batch of images within a folder.

#### Outcome
- I will actually have great use of this tool. Yes, there are softwares that can do the same thing, but both my need and the script is simple enough that I'll be motivating to use it over looking for other solutions. 
- There's a drawback, that one has to determine the pixels for cropping, although it's only needed once. Therefore it's most useful for a batch of images.
- Perhaps somewhat overly sophisticated for the functions needed, but it was valuable practice in structuring a script and using functions and classes. It also makes it easier for me to add more functions later on.



### Word count
[*word_count.py*](https://github.com/elmwall/PythonSalad/blob/main/Tools/word_count.py)

This script is for counting lines, words, and characters in a text file.

#### Motivation

Just a silly thing, while working with some text I found myself lacking a word count function. In software which felt like they really should have such. Yes, there are plenty of tools online, but it annoyed me to paste things into yet another software or page, so I made one myself.

#### Outcome
- It's easy enough to use that I'll probably use it again, unless I'm working in word processors which actually already has a built-in one.