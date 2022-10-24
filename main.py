# Import the libraries
import tkinter as tk
import re


# Make the window
win = tk.Tk()
win.title("Word repeat notifier")


def StartSearch():
    """
    The whole meat of this program.
    Counts the words and sentences,
    and displays the repeated words
    and their occurrences.
    """

    # Declare variables 

    # | the content of the text box 
    # | (there's always a "\n" at the end of the text and I don't like that.)
    # | (remove extra spaces at the end of text, to prevent them from )
    # V (.lower() for easier handling of the text) 
    text = textBox.get("0.0", "end").rstrip("\n").rstrip(" ").lower()
    words = [] # list of all the words
    temp = "" # temporary variable that helps with 
    sentences = 0 # counts the total sentences

    # find all words
    words = re.findall("\w+", text, re.I)
    for i in re.findall("\w+-\w+", text, re.I):
        words.append(i)
        words.remove(i[0:i.find("-")])
        words.remove(i[i.find("-")+1:len(i)])
    word_count = len(words)

    # find all sentences
    sentences = len(re.findall(r"\w+\.|\w+\!|\w\?|\w\:", text))
    # find all repeated words and order them into a dictionary
    repeated_words = {}
    for i in words:
        if i not in repeated_words:
            temp = re.findall(fr"\b{i}\b", str(words))
            if len(temp) != 1:
                repeated_words[i] = len(temp)

    repeated_words = dict(sorted(repeated_words.items(), key=lambda x:x[1], reverse=True))      

    totalWordsLabel["text"] = f"Total words: {word_count}\nTotal sentences: {sentences}"


    repeatedWordsListbox.delete(0, "end")
    for i in repeated_words:
        repeatedWordsListbox.insert("end", f"{i}: {repeated_words[i]}\n")

    if repeatedWordsListbox.get("end") == "":
        totalWordsLabel["text"] += "\n\nYay! No repeated words!"
    


statsFrame = tk.Frame(win)
baseFrame = tk.Frame(win)
repeatedWordsFrame =  tk.Frame(win)

textBox = tk.Text(baseFrame, height=5, width=50, wrap="word")
startButton = tk.Button(baseFrame, text="Start!", command=lambda:StartSearch())
totalWordsLabel = tk.Label(statsFrame)
repeatedWordsScrollbar=tk.Scrollbar(repeatedWordsFrame, orient="vertical")
repeatedWordsListbox = tk.Listbox(repeatedWordsFrame, yscrollcommand=repeatedWordsScrollbar.set)

repeatedWordsScrollbar.config(command=repeatedWordsListbox.yview)

baseFrame.grid(row=0, column=0)
statsFrame.grid(row=1, column=0)
repeatedWordsFrame.grid(row=2, column=0)
textBox.grid(row=0, column=0)
startButton.grid(row=0, column=1)
totalWordsLabel.grid(row=1, column=0, sticky="w")
repeatedWordsListbox.pack(side="left", fill="both")
repeatedWordsScrollbar.pack(side="right", fill="both")

win.mainloop()
