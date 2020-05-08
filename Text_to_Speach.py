from gtts import gTTS
import os

fh = open("bangla-lang.txt", "r")
myText = fh.read().replace("\n", " ")
language = 'bn'
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
fh.close()
os.system("start output.mp3")