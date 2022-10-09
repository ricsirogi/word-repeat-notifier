# Import the libraries
import tkinter as tk

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
    text = textBox.get("0.0", "end") # the content of the text box
    words = [] # list of all the words
    temp = "" # temporary variable that helps with 
    isSpace = False # temporary variable, that helps with preventing registering double spaces as one word
    wordCounter = 0 # counts the total wordsd
    sentenceCounter = 0 # counts the total sentences

    # Loops thorough every character of the text
    for counter, i in enumerate(text):
        if i != " ":
            temp += i
            isSpace = False
        else:
            if not isSpace:
                words.append(temp.lower())
                temp = ""
                isSpace = True
                wordCounter += 1
        if counter == len(text)-1:
            words.append(temp)
            temp = ""
        if i == "." or i == "?" or i == "!":
            if text[counter+1] == " " or text[counter+1] != "." and not text[counter+1].isnumeric():
                sentenceCounter += 1
    words[len(words)-1] = words[len(words)-1].rstrip()
    totalWordsLabel["text"] = f"Total words: {wordCounter}\nTotal sentences: {sentenceCounter}"

    repeatedWords = {}
    for i in words:
        try:
            repeatedWords[i] = repeatedWords.get(i) + 1
        except:
            repeatedWords[i] = 1
    
    toRemove = []
    for i in repeatedWords:
        if repeatedWords.get(i) == 1:
            toRemove.append(i)
    
    for i in toRemove:
        repeatedWords.pop(i)

    oRepeatedWords = dict(sorted(repeatedWords.items(), key=lambda x:x[1], reverse=True))

    for i in oRepeatedWords:
        repeatedWordsLabel["text"] += f"{i}: {oRepeatedWords[i]}\n"

textBox = tk.Text(win, height=3, width=50)
startButton = tk.Button(win, text="Start!", command=lambda:StartSearch())
totalWordsLabel = tk.Label(win)
repeatedWordsLabel = tk.Label(win)

textBox.grid(row=0, column=0)
startButton.grid(row=0, column=1)
totalWordsLabel.grid(row=1, column=0, sticky="w")
repeatedWordsLabel.grid(row=2, column=0, sticky="w")

win.mainloop()