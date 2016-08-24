from tkinter import *
import piglatinmaker

def make_textbox(userinput, pig_latin_word):
	textbox = Tk()
	textbox.title("Pig Latin Maker")
	textbox.geometry("450x300+200+200")

	text = StringVar()
	text.set(userinput + " is " + pig_latin_word + " in pig latin.")
	text1 = Label(textbox, textvariable=text, height=4)
	text1.pack()

	textbox.mainloop()

def main():
	userinput = raw_input("What is a word you would like to see in pig latin? ")
	pig_latin_word = piglatinmaker.pig_latin(userinput)
	make_textbox(userinput, pig_latin_word)

if __name__ == '__main__':
	main()