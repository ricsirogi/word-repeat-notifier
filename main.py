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

    # | the content of the text box 
    # | (there's always a "\n" at the end of the text and I don't like that.)
    # | (remove extra spaces at the end of text, to prevent them from )
    # V (.lower() for easier handling of the text) 
    text = textBox.get("0.0", "end").rstrip("\n").rstrip(" ").lower()
    words = [] # list of all the words
    temp = "" # temporary variable that helps with 
    isSpace = False # temporary variable, that helps with preventing registering double spaces as one word
    wordCounter = 1 # counts the total word  (there's plus one, because the wor counter doesn't count the last word)
    sentenceCounter = 0 # counts the total sentences
    endOfSentenceCharacters = [".", "?", "!"]

    # Loops thorough every character of the text
    for counter, i in enumerate(text):
        if i != " " and i != "\n":
            if i != "\n" and i not in endOfSentenceCharacters:
                temp += i
            isSpace = False
        else:
            if not isSpace:
                words.append(temp)
                temp = ""
                wordCounter += 1
                isSpace = True
                
        if counter == len(text)-1:
            words.append(temp)
            temp = ""
        if i in endOfSentenceCharacters:
            try:
                if text[counter+1] == " " or text[counter+1] != "." and not text[counter+1].isnumeric():
                    sentenceCounter += 1
            except IndexError:
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

    repeatedWordsListbox.delete(0, "end")
    for i in oRepeatedWords:
        repeatedWordsListbox.insert("end", f"{i}: {oRepeatedWords[i]}\n")

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
