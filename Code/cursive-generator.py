import os
from time import sleep
import sys
import pygame

def importImage(fileN):
    image = pygame.image.load(fileN)
    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image,(int(width*heightMult),int(height*heightMult)))
    width = image.get_width()
    height = image.get_height()
    return image, width, height


heightMult = 1
lettersContainers = "letters/"
lettersFileExtension = ".bmp"
letters = {}
for i in os.listdir(lettersContainers):
    if i[:-7] not in letters:
        letters[i[:-7]] = {}

    letters[i[:-7]][i[-7:-4]]={}
    letters[i[:-7]][i[-7:-4]]['image'], letters[i[:-7]][i[-7:-4]]['width'], letters[i[:-7]][i[-7:-4]]['height'] = importImage(f"{lettersContainers}{i}")



EndTopLetters="wrov"

inp=input(":")
words=inp.split()
for i in range(len(words)):
    words[i]=words[i]+" "

letterHeight=heightMult*35
lines=6
screenWidth=300*heightMult
screenHeight=letterHeight*lines
caption="Cursive Writer"

pygame.init()
screen=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption(caption)
screen.fill((255,255,255))


def saveWord():
    genWord.append(letters[j])
    global foundLetter
    foundLetter=True


curX=10
line=0
curPic = 0

for word in words:
    genWord=[]
    prevTB="b"

    for ltrN in range(len(word)-1): #for letter
        ltr = word[ltrN]
        foundLetter=False


        for j in letters:

            if foundLetter!=True:

                if ltr.islower():

                    if ltr in EndTopLetters:

                        if f"{prevTB}{ltr}t"==j[0:3]:
                            saveWord()
                            prevTB="t"

                    else:

                        if f"{prevTB}{ltr}"==j[0:2]:
                            saveWord()
                            prevTB="b"
                else:

                    if ltr=="/":
                        if j[:5]=="slash":
                            saveWord()
                            prevTB="b"

                    elif ltr==".":
                        if j[:3]=="dot":
                            saveWord()
                            prevTB="b"

                    elif ltr=="!":
                        if j[:3]=="exclaim":
                            saveWord()
                            prevTB="b"

                    elif ltr==j[0:1]:
                            saveWord()
                            prevTB="b"
        if foundLetter==False:
            if ltr == '^':
                line += 1.5
                curX=10
            elif ltr in EndTopLetters:
                print(f"Missing: {prevTB}{ltr}t")
            else:
                print(f"Missing: {prevTB}{ltr}b")

    #display
    totWordWidth = 0
    for i in genWord:
        totWordWidth += i['000']['width']
    if totWordWidth+curX>screenWidth:
        line+=1
        curX=10
    for ch in genWord:
        for px in range(len(ch)):
            px = f"{px:03}"
            screen.blit(ch[px]["image"],(curX,line*letterHeight))
            pygame.display.update()
            pygame.image.save(screen, f"saves/{curPic:05}.jpg")
            curPic += 1
            sleep(0.01)
        curX+=ch['000']["width"]
    curX+=10*heightMult

while True:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        #if event.type==pygame.KEYDOWN:
        #    if event.key == pygame.K_EQUALS: