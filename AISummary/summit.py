# Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from gtts import gTTS
import os
import pygame

# NLP
from summarizer import nltk_summarizer

# Scraper
from mediawiki import MediaWiki
from bs4 import BeautifulSoup
from urllib.request import urlopen

wikipedia = MediaWiki()
pygame.init()

'''############### WINDOW CREATION ###############'''

window = Tk()
window.title("Summ-it By Stephen Ouellette")
window.geometry('680x650')

# Styling the Window
style = ttk.Style()
style.theme_create("TabStyle", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
    "TNotebook.Tab": {"configure": {"padding": [20, 20]}, }})

style.theme_use("TabStyle")

# Window Tabs
tabs = ttk.Notebook(window, width=200, height=200)

# Create Tab and then Add the tab to the notebook...
tabOne = ttk.Frame(tabs)
tabTwo = ttk.Frame(tabs)
tabThree = ttk.Frame(tabs)

tabs.add(tabOne, text='Summ-it Text')
tabs.add(tabTwo, text='Summ-it File')
tabs.add(tabThree, text='Summ-it WikiScrape')

# Labels
tabs.pack(expand=True, fill=tk.BOTH)

'''############### FUNCTIONS ###############'''


# Summarize function
def SummarizeText():
    textIn = str(inputEntryBoxTabOne.get('1.0', tk.END))
    textOut = nltk_summarizer(textIn)
    result = '\nSummary:{}'.format(textOut)
    outputEntryBoxTabOne.insert(tk.END, result)


def SummarizeFile():
    textIn = str(inputEntryBoxTabTwo.get('1.0', tk.END))
    textOut = nltk_summarizer(textIn)
    result = '\nSummary:{}'.format(textOut)
    outputEntryBoxTabTwo.insert(tk.END, result)


# Clear Input
def ClearEntryText():
    inputEntryBoxTabOne.delete('1.0', END)


def ClearEntryFile():
    inputEntryBoxTabTwo.delete('1.0', END)


def ClearEntryURL():
    inputEntryBoxTabThree.delete('1.0', END)
    outputContentTabThree.delete('1.0', END)
    pageTitle.set('')
    outputSummaryTabThree.delete('1.0', END)


# Clear Output
def ClearOutputText():
    outputEntryBoxTabOne.delete('1.0', END)


def ClearOutputFile():
    outputEntryBoxTabTwo.delete('1.0', END)


# Open a file
def OpenFile():
    fileOne = tkinter.filedialog.askopenfilename(
        filetypes=(("Text Files", ".txt"), ("All files", "*")))
    readText = open(fileOne, 'rt', encoding='utf-8').read()
    inputEntryBoxTabTwo.insert(tk.END, readText)


# Get text from URL
def GetTextFromURL():
    textIn = str(inputEntryBoxTabThree.get('1.0', tk.END))
    inputEntryBoxTabThree.delete('1.0', END)
    page = wikipedia.page(textIn)
    textOut = page.summarize()
    pageTitle.set(page.title)
    outputContentTabThree.insert(tk.END, page.content)
    outputSummaryTabThree.insert(tk.END, textOut)
    tts = gTTS(text=outputSummaryTabThree.get('1.0', tk.END), lang='en')
    tts.save('Summary.mp3')

def SpeakIt():
    pygame.mixer.music.load('Summary.mp3')
    pygame.mixer.music.play(1)

def PauseIt():
    global pauseBool
    if pauseBool == True:
        pygame.mixer.music.unpause()
        pauseSpeechButton.config(text='Pause')
        pauseBool = False
    else:
        pygame.mixer.music.pause()
        pauseSpeechButton.config(text='Resume')
        pauseBool = True

def StopIt():
    pygame.mixer.music.stop()
    


'''############### HOME TAB ###############'''

titleLabel = Label(tabOne, text='Paste your text to Summarize', padx=5, pady=5)
titleLabel.config(font=("Courier", 14))
titleLabel.grid(column=0, row=0, columnspan=3, rowspan=2)

# Entry Boxes
inputEntryBoxTabOne = ScrolledText(tabOne, height=10)
outputEntryBoxTabOne = ScrolledText(tabOne, height=10)

inputEntryBoxTabOne.grid(column=0, row=3, columnspan=3, padx=10)
outputEntryBoxTabOne.grid(column=0, row=8, columnspan=3, padx=10)

# Buttons
resetInputButton = Button(tabOne, text='Reset Input',
                          command=ClearEntryText, width=12, bg='red', fg='black')
submitButton = Button(tabOne, text='Summarize',
                      command=SummarizeText, width=12, bg='blue', fg='#fff')
resetOutputButton = Button(tabOne, text='Reset Output',
                           command=ClearOutputText, width=12, bg='red', fg='black')

resetInputButton.grid(row=4, column=2, pady=10, padx=10)
submitButton.grid(row=5, column=1, pady=10, padx=10)
resetOutputButton.grid(row=9, column=2, pady=10, padx=10)

'''############### FILE TAB ###############'''

titleLabel = Label(tabTwo, text='Open file to Summarize', padx=5, pady=5)
titleLabel.config(font=("Courier", 14))
titleLabel.grid(column=0, row=0, columnspan=3, rowspan=2)

# Entry Boxes
inputEntryBoxTabTwo = ScrolledText(tabTwo, height=10)
outputEntryBoxTabTwo = ScrolledText(tabTwo, height=10)

inputEntryBoxTabTwo.grid(column=0, row=3, columnspan=3, padx=10)
outputEntryBoxTabTwo.grid(column=0, row=8, columnspan=3, padx=10)
outputEntryBoxTabTwo.config(state=NORMAL)

# Buttons
openFileButton = Button(tabTwo, text='Open File',
                        command=OpenFile, width=12, bg='#25d366', fg='#fff')
resetInputButton = Button(tabTwo, text='Reset Input',
                          command=ClearEntryFile, width=12, bg='red', fg='black')
submitButton = Button(tabTwo, text='Summarize',
                      command=SummarizeFile, width=12, bg='blue', fg='#fff')
resetOutputButton = Button(tabTwo, text='Reset Output',
                           command=ClearOutputFile, width=12, bg='red', fg='black')

openFileButton.grid(row=4, column=0, pady=10, padx=10)
resetInputButton.grid(row=4, column=2, pady=10, padx=10)
submitButton.grid(row=5, column=1, pady=10, padx=10)
resetOutputButton.grid(row=9, column=2, pady=10, padx=10)

'''############### URL TAB ###############'''

titleLabel = Label(tabThree, text='Please enter something to search for', padx=5, pady=5)
titleLabel.config(font=("Courier", 14))
titleLabel.grid(column=0, row=0, columnspan=3, rowspan=2)

pageTitle = StringVar()
pageLabel = Label(tabThree, textvariable=pageTitle, padx=5, pady=5, fg='red')
pageLabel.config(font=("Courier", 12))
pageLabel.grid(column=1, row=6)

contentLabel = Label(tabThree, text="Content Of Wiki", padx=5, pady=5)
contentLabel.config(font=("Courier", 10))
contentLabel.grid(column=0, columnspan=3, row=8)

summaryLabel = Label(tabThree, text="Summary of Text", padx=5, pady=5)
summaryLabel.config(font=("Courier", 10))
summaryLabel.grid(column=0, columnspan=3, row=10)

# Entry Boxes
inputEntryBoxTabThree = Text(tabThree, height=1)
outputContentTabThree = ScrolledText(tabThree, height=10)
outputSummaryTabThree = ScrolledText(tabThree, height=10)

inputEntryBoxTabThree.grid(column=0, row=3, columnspan=3, padx=10)
outputContentTabThree.grid(column=0, row=9, columnspan=3, padx=10)
outputSummaryTabThree.grid(column=0, row=11, columnspan=3, padx=10)

outputSummaryTabThree.config(state=NORMAL)

# Boolean used for tracking playback
pauseBool = False

# Buttons
getTextFromURLButton = Button(tabThree, text='Search Wikipedia', command=GetTextFromURL, width=12, bg='#25d366', fg='#fff')
resetInputButton = Button(tabThree, text='Clear Text', command=ClearEntryURL, width=12, bg='red', fg='black')
textToSpeechButton = Button(tabThree, text='SpeakIt', command=SpeakIt, width=4, bg='#25d366', fg='#fff')
pauseSpeechButton = Button(tabThree, text='Pause', command=PauseIt, width=4, bg='blue', fg='white')
stopSpeechButton = Button(tabThree, text='Stop', command=StopIt, width=4, bg='red', fg='black')


getTextFromURLButton.grid(row=5, column=0, pady=10, padx=10)
resetInputButton.grid(row=5, column=2, pady=10, padx=10)
textToSpeechButton.grid(row=12, column=0)
pauseSpeechButton.grid(row=12, column=1)
stopSpeechButton.grid(row=12, column=2)

window.mainloop()
