import os
import pygame
from time import sleep

lettersContainers="letters/"
lettersFileExtension=".bmp"
letters=[]
for i in os.listdir(lettersContainers):
    letters.insert(0,{})
    letters[0]["fileName"]=i[:-4]

heightMult=5
for i in range(len(letters)):
    tempFN=f"{lettersContainers}{letters[i]['fileName']}{lettersFileExtension}"
    letters[i]["image"]=pygame.image.load(tempFN)
    letters[i]["width"]=letters[i]["image"].get_width()
    letters[i]["height"]=letters[i]["image"].get_height()
    letters[i]["image"]=pygame.transform.scale(letters[i]["image"],(int(letters[i]["width"]*heightMult),int(letters[i]["height"]*heightMult)))
    letters[i]["width"]=letters[i]["image"].get_width()
    letters[i]["height"]=letters[i]["image"].get_height()

EndTopLetters="wrov"

inp=input(":")
words=inp.split()
for i in range(len(words)):
    words[i]=words[i]+" "

letterHeight=heightMult*35
lines=5
screenWidth=1500
screenHeight=letterHeight*lines
caption="Cursive Writer"

pygame.init()
screen=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption(caption)
screen.fill((255,255,255))


def saveWord():
    global foundLetter
    genWord.append({})
    genWord[-1]["image"]=j["image"]
    genWord[-1]["width"]=j["width"]
    foundLetter=True


curX=10
line=0

for word in words:
    genWord=[]
    prevTB="b"

    for i in range(len(word)-1):
        foundLetter=False

        for j in letters:

            if foundLetter!=True:

                if word[i].islower():

                    if word[i] in EndTopLetters:

                        if f"{prevTB}{word[i]}t"==j["fileName"][0:3]:
                            saveWord()
                            prevTB="t"

                    else:

                        if f"{prevTB}{word[i]}"==j["fileName"][0:2]:
                            saveWord()
                            prevTB="b"
                else:

                    if word[i]=="/":
                        if j["fileName"][:5]=="slash":
                            saveWord()
                            prevTB="b"

                    elif word[i]==".":
                        if j["fileName"][:3]=="dot":
                            saveWord()
                            prevTB="b"

                    elif word[i]==j["fileName"][0:1]:
                            saveWord()
                            prevTB="b"
        if foundLetter==False:
            if word[i] in EndTopLetters:
                print(f"Missing: {prevTB}{word[i]}t")
            else:
                print(f"Missing: {prevTB}{word[i]}b")

    totWordWidth=0
    for i in genWord:
        totWordWidth+=i["width"]
    if totWordWidth+curX>screenWidth:
        line+=1
        curX=10
    for i in genWord:
        screen.blit(i["image"],(curX,line*letterHeight))
        curX+=i["width"]
        pygame.display.update()
        sleep(0.2)
    curX+=10*heightMult


pygame.image.save(screen, "screenshot.jpg")

while True:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

        #if event.type==pygame.KEYDOWN:
        #    if event.key == pygame.K_EQUALS: