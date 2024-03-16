

# Grid Based Transport Game
import pygame,sys,random,math,datetime,pickle,OpenGL
from pygame.locals import*
from datetime import timedelta
pygame.init()

infoObject=pygame.display.Info()
screen=pygame.display.set_mode((1600,900),FULLSCREEN)
pygame.display.set_caption("Transporticular")
clock=pygame.time.Clock()
pygame.mouse.set_cursor(*pygame.cursors.tri_left)

##Images

icon_img=pygame.image.load("data/icon.png").convert_alpha()
pygame.display.set_icon(icon_img)


grass_img=pygame.image.load("data/grass.jpg").convert()
desert_img=pygame.image.load("data/desert.jpg").convert()

factory_img=pygame.image.load("data/factory.jpg").convert()
refinery_img=pygame.image.load("data/refinery.jpg").convert()


fade_img=pygame.image.load("data/fade.png").convert_alpha()
##Menu items
roadSelect_img=pygame.image.load("data/roadSelect.png").convert_alpha()
baySelect_img=pygame.image.load("data/baySelect.jpg").convert()
trainSelect_img=pygame.image.load("data/trainSelect.jpg").convert()
stationSelect_img=pygame.image.load("data/stationSelect.jpg").convert()
airportSelect_img=pygame.image.load("data/airportSelect.jpg").convert()
deleteSelect_img=pygame.image.load("data/deleteSelect.jpg").convert()
fullscreenSelect_img=pygame.image.load("data/fullscreenSelect.jpg").convert()
companySelect_img=pygame.image.load("data/companySelect.jpg").convert()
financeSelect_img=pygame.image.load("data/financeSelect.jpg").convert()
routesSelect_img=pygame.image.load("data/routesSelect.png").convert_alpha()
pauseSelect_img=pygame.image.load("data/pause.png").convert_alpha()
speed1Select_img=pygame.image.load("data/speed1.jpg").convert()
speed2Select_img=pygame.image.load("data/speed2.jpg").convert()
speed3Select_img=pygame.image.load("data/speed3.jpg").convert()
menuSelect_img=pygame.image.load("data/menuSelect.png").convert_alpha()

grain_img=pygame.image.load("data/grain.png").convert_alpha()##Factory images
livestock_img=pygame.image.load("data/livestock.png").convert_alpha()
forestry_img=pygame.image.load("data/forestry.png").convert_alpha()
iron_img=pygame.image.load("data/iron.png").convert_alpha()
coal_img=pygame.image.load("data/coal.png").convert_alpha()
oil_img=pygame.image.load("data/oil.png").convert_alpha()
grainPiece_img=pygame.image.load("data/grainPiece.png").convert_alpha()

########Window images
windowExit_img=pygame.image.load("data/windowExit.jpg").convert()





########

town_img=pygame.image.load("data/town.jpg").convert()
townPiece_img=pygame.image.load("data/townPiece.png").convert_alpha()


tree_img=pygame.image.load("data/tree.png").convert_alpha()
water_img=pygame.image.load("data/water.jpg").convert()

station_img=pygame.image.load("data/station.png").convert_alpha()
airport_img=pygame.image.load("data/airport.png").convert_alpha()

driverUp_img=pygame.image.load("data/driverUp.png").convert_alpha()##Lorries
driverDown_img=pygame.transform.rotate(driverUp_img,180)
driverLeft_img=pygame.transform.rotate(driverUp_img,90)
driverRight_img=pygame.transform.rotate(driverUp_img,-90)

bay_img=pygame.image.load("data/bay.jpg").convert()##Bays
bay3_img=pygame.image.load("data/bay3.jpg").convert()
bay2_img=pygame.image.load("data/bay2.jpg").convert()
bay1_img=pygame.image.load("data/bay1.jpg").convert()

lorryUp_img=pygame.image.load("data/lorryUp.png").convert_alpha()##Lorries
lorryDown_img=pygame.transform.rotate(lorryUp_img,180)
lorryLeft_img=pygame.transform.rotate(lorryUp_img,90)
lorryRight_img=pygame.transform.rotate(lorryUp_img,-90)

busUp_img=pygame.image.load("data/busUp.png").convert_alpha()##Buses
busDown_img=pygame.transform.rotate(busUp_img,180)
busLeft_img=pygame.transform.rotate(busUp_img,90)
busRight_img=pygame.transform.rotate(busUp_img,-90)



##Train pieces
trainPiece_img=pygame.image.load("data/trainPiece.jpg").convert()
trainUp_img=pygame.image.load("data/trainUp.png").convert_alpha()
trainHorizontal_img=pygame.transform.rotate(trainUp_img,90)

trainRB_img=pygame.image.load("data/trainRB.png").convert_alpha()
trainLB_img=pygame.transform.rotate(trainRB_img,-90)
trainRA_img=pygame.transform.rotate(trainRB_img,90)
trainLA_img=pygame.transform.rotate(trainRB_img,180)

trainRAB_img=pygame.image.load("data/trainRAB.png").convert_alpha()
trainLAB_img=pygame.transform.rotate(trainRAB_img,180)
trainRLA_img=pygame.transform.rotate(trainRAB_img,90)
trainRLB_img=pygame.transform.rotate(trainRAB_img,270)

##Plane
plane_img=pygame.image.load("data/plane.png").convert_alpha()

##All kinds of roads
roadUp_img=pygame.image.load("data/roadUp.png").convert_alpha()
roadHorizontal_img=pygame.transform.rotate(roadUp_img,90)

roadRB_img=pygame.image.load("data/roadRB.png").convert_alpha()
roadLB_img=pygame.transform.rotate(roadRB_img,-90)
roadRA_img=pygame.transform.rotate(roadRB_img,90)
roadLA_img=pygame.transform.rotate(roadRB_img,180)

roadRAB_img=pygame.image.load("data/roadRAB.png").convert_alpha()
roadLAB_img=pygame.transform.rotate(roadRAB_img,180)
roadRLA_img=pygame.transform.rotate(roadRAB_img,90)
roadRLB_img=pygame.transform.rotate(roadRAB_img,270)

##Sound effects and abience################
pygame.mixer.music.load("data/ambient.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

lorryRoute_sound=pygame.mixer.Sound("data/lorryRoute.wav")
trainRoute_sound=pygame.mixer.Sound("data/trainRoute.wav")
planeRoute_sound=pygame.mixer.Sound("data/planeRoute.wav")
click_sound=pygame.mixer.Sound("data/click.wav")
build_sound=pygame.mixer.Sound("data/build.wav")
alert_sound=pygame.mixer.Sound("data/alert.wav")
destroy_sound=pygame.mixer.Sound("data/destroy.wav")

###Main menu images
menuBackground_img=pygame.image.load("data/menuImage.jpg").convert()
menuBar_img=pygame.image.load("data/menuBar.png").convert_alpha()
menuBox_img=pygame.image.load("data/menuBox.jpg").convert()
grassDemo_img=pygame.image.load("data/grassDemo.jpg").convert()
desertDemo_img=pygame.image.load("data/desertDemo.jpg").convert()
title_img=pygame.image.load("data/title.png").convert_alpha()

###Window images
add_img=pygame.image.load("data/add.jpg").convert()
subtract_img=pygame.image.load("data/subtract.jpg").convert()

###########





###########################################


##font
bigfont= pygame.font.Font('data/BigBOBY-Rounded.otf', 50)
font= pygame.font.Font('data/BigBOBY-Rounded.otf', 20)
smallfont= pygame.font.Font('data/BigBOBY-Rounded.otf', 15)


townNames=["Tunstead",
"Westwend ",
"Acomb",
"Farnworth",
"Travercraig",
"Garmsby",
"Eanverness",
"Bamburgh",
"Armskirk",
"Duncaster",
"Alryne",
"Cleethorpes",
"Drumnadrochit",
"Braedon",
"Kamouraska",
"Hartlepool",
"Garrigill",
"Bradfordshire",
"Inverness",
"Snake's Canyon"]

industryList=[["Coal Mine","coal"],
              ["Grain Farm","grain"],
              ["Livestock Farm","livestock"],
              ["Iron Mine","iron"],
              ["Oil Well","oil"],
              ["Forestry","wood"]
              ]
refineList=[["Sawmill","wood","  ","wood goods"],
            ["Food Processor","livestock","grain","food goods"],
            ["Steel Mill","iron","  ","steel"],
            ["Factory","steel","  ","metal goods"],
            ["Oil Refinery","oil","  ","plastic goods"],
            ["Power Plant","coal","  ","none"]]


    


#Main Variables
screenx,screeny=0,0
mousex,mousey=0,0
clicked=False
xChange,yChange=0,0
scrollMenuSpeed=40
buildItem="Road"
buildList=[]
lorryList=[]
trainList=[]
planeList=[]
windowList=[]
risingTextList=[]
payTimer=0
feed=["","","","",""]
extraInfo=False
fullscreen=False
mouseDown=False
gameSpeed=1
profit=0
goodsList=["wood goods",
           "food goods",
           "metal goods",
           "plastic goods"]
monthReset=False
lastMonthList=[]
currentMonthList=[]

showSaves=False
lastProfit=0
lastExpenditure=0
lastTax=0
showUI=True
mainMenu=True
prevSpeed=1


currentProfit=0
currentExpenditure=0
currentTax=0

loan=0

totalwood=0
totalmetal=0
totalfood=0
totalplastic=0

influence=0
forProposal=0
againstProposal=0
proposal=""
currentLaw="Nothing"
averageRespect=0

##Developer settings##########
version=8

companyName="Company Name"
cash=5
numberOfTowns=20
numberOfFactories=70
numberOfRefineries=50
numberOfTrees=150
numberOfRivers=1
desert=False

roadCost=50
trackCost=100
bayCost=200
stationCost=2000
airportCost=4000
deleteCost=20
fundCost=5000
respectCost=1000

lorryTax=5
trainTax=25
planeTax=40

growthPerPassengerTrain=20
growthPerCargoTrain=10
growthPerBus=2##Not applicable
growthPerLorry=5##Not applicable

planeSpeed=10
townStartMin=200
townStartMax=2000

scrollSpeed=20
date = datetime.datetime(2000, 1, 1)
interest=0.5

totalPrice=3.9

metalPrice=0.9
plasticPrice=0.9
foodPrice=0.9
woodPrice=0.9
busPrice=0.5
coalPrice=1




#######################

#With towns, each month they have capacity which resests at the end, if full gain pop and respect, if empty loose respect


influence=0
forProposal=0
againstProposal=0
proposal=""
currentLaw="Nothing"
averageRespect=0




previousCash=cash
class SaveClass:
    def __init__(self):
        self.payTimer=payTimer
        self.lastMonthList=lastMonthList
        self.currentMonthList=currentMonthList
        self.loan=loan
        self.lastProfit=lastProfit
        self.lastExpenditure=lastExpenditure
        self.lastTax=lastTax
        self.currentProfit=currentProfit
        self.currentExpenditure=currentExpenditure
        self.currentTax=currentTax
        self.cash=cash
        self.date=date
        self.metalPrice=metalPrice
        self.plasticPrice=plasticPrice
        self.foodPrice=foodPrice
        self.woodPrice=woodPrice
        self.busPrice=busPrice
        self.coalPrice=coalPrice
        self.lorryList=lorryList
        self.trainList=trainList
        self.planeList=planeList
        self.tileList=tileList
        self.desert=desert
        self.totalwood=totalwood
        self.totalmetal=totalmetal
        self.totalfood=totalfood
        self.totalplastic=totalplastic
        self.influence=influence
        self.forProposal=forProposal
        self.againstProposal=againstProposal
        self.proposal=proposal
        self.currentLaw=currentLaw
        self.averageRespect=averageRespect
        self.companyName=companyName
    def setVariables(self):
        global companyName,influence,forProposal,againstProposal,proposal,currentLaw,averageRespect,payTimer,totalwood,totalfood,totalmetal,totalplastic,desert,lastMonthList,currentMonthList,loan,lastProfit,lastExpenditure,lastTax,currentProfit,currentExpenditure,currentTax,cash,date,metalPrice,plasticPrice,foodPrice,woodPrice,busPrice,coalPrice,lorryList,trainList,planeList,tileList
        payTimer=self.payTimer
        lastMonthList=self.lastMonthList
        currentMonthList=self.currentMonthList
        loan=self.loan
        lastProfit=self.lastProfit
        lastExpenditure=self.lastExpenditure
        lastTax=self.lastTax
        currentProfit=self.currentProfit
        currentExpenditure=self.currentExpenditure
        currentTax=self.currentTax
        cash=self.cash
        date=self.date
        metalPrice=self.metalPrice
        plasticPrice=self.plasticPrice
        foodPrice=self.foodPrice
        woodPrice=self.woodPrice
        busPrice=self.busPrice
        coalPrice=self.coalPrice
        lorryList=self.lorryList
        trainList=self.trainList
        planeList=self.planeList
        tileList=self.tileList
        desert=self.desert
        totalwood=self.totalwood
        totalmetal=self.totalmetal
        totalplastic=self.totalplastic
        totalfood=self.totalfood
        influence=self.influence
        forProposal=self.forProposal
        againstProposal=self.againstProposal
        proposal=self.proposal
        currentLaw=self.currentLaw
        companyName=self.companyName

class Tile:
    def __init__(self,xNumber,yNumber):
        self.xNumber=xNumber
        self.yNumber=yNumber
        self.item=None
        self.img=None
        self.capacity=random.randint(50,300)
        self.value=self.capacity
        self.rate=self.capacity/2000
        self.name=""
        self.holding=""
        self.used=False
        self.milestone=0
        
    def addPiece(self,piece):
        distance=2+round_down(self.value/1000,1)
        placed=False
        while placed==False:
            piecex=self.xNumber+random.randint(-distance,distance)
            piecey=self.yNumber+random.randint(-distance,distance)
            try:
                if tileList[piecex+piecey*200].item==None:
                    if piece=="townPiece":
                        tileList[piecex+piecey*200].item="townPiece"
                        placed=True
                    elif piece=="Factory":
                        tileList[piecex+piecey*200].item="Factory"
                        placed=True
                        factoryNum=random.randint(0,5)
                        tileList[piecex+piecey*200].name=industryList[factoryNum][0]
                        tileList[piecex+piecey*200].produce=industryList[factoryNum][1]
                    elif piece=="Refinery":
                        tileList[piecex+piecey*200].item="Refinery"
                        placed=True
                        refineryNum=random.randint(0,5)
                        tileList[piecex+piecey*200].name=refineList[refineryNum][0]
                        tileList[piecex+piecey*200].intakeList=[refineList[refineryNum][1],refineList[refineryNum][2]]
                        tileList[piecex+piecey*200].produce=refineList[refineryNum][3]
                        tileList[piecex+piecey*200].rate=0
            except:
                pass

    def draw(self):
        if self.item!=None:
            if self.item=="Town":
                screen.blit(town_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                valueText=smallfont.render(str( self.name+" ("+str(round(self.value))+")"),False,self.colour)
                screen.blit(valueText,(screenx+(self.xNumber*20)-30,screeny+(self.yNumber*20)-40))
                if self.value>self.milestone+100:
                    self.addPiece("townPiece")
                    feed.append(self.name+" has grown!")
                    self.milestone+=100
                    self.busLimit=round(self.value/1000)
                            
            elif self.item=="Factory":##Change this and just assign an image at the start
                if self.name=="Grain Farm":
                    screen.blit(grain_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif self.name=="Livestock Farm":
                    screen.blit(livestock_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif self.name=="Forestry":
                    screen.blit(forestry_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif self.name=="Iron Mine":
                    screen.blit(iron_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif self.name=="Coal Mine":
                    screen.blit(coal_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif self.name=="Oil Well":
                    screen.blit(oil_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))    


                self.increase()
                valueText=font.render(str(self.name+" ("+str(round(self.value))+")"),False,(0,0,0))
                screen.blit(valueText,(screenx+(self.xNumber*20)-50,screeny+(self.yNumber*20)-20))


            elif self.item=="Refinery":
                if self.name=="Steel Mill" or self.name=="Sawmill" or self.name=="Food Processor":
                    screen.blit(factory_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                else:
                    screen.blit(refinery_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))

                self.increase()
                valueText=font.render(str(self.name+" ("+str(round(self.value))+")"),False,(0,0,0))
                screen.blit(valueText,(screenx+(self.xNumber*20)-50,screeny+(self.yNumber*20)-20))

                
                
            elif self.item=="Road":
                above=tileList[self.xNumber+self.yNumber*200-200].item
                below=tileList[self.xNumber+self.yNumber*200+200].item
                right=tileList[self.xNumber+1+self.yNumber*200].item
                left=tileList[self.xNumber-1+self.yNumber*200].item
                accept=["Road","Factory","Town","Refinery","Airport"]
                
                if left not in accept and right not in accept:##Drawing road in correct orientation
                    screen.blit(roadUp_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                if above not in accept and below not in accept:
                    screen.blit(roadHorizontal_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                    
                elif right in accept and left in accept and above in accept and below in accept:
                    screen.blit(roadUp_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                    screen.blit(roadHorizontal_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))

                elif right in accept and above in accept and below in accept:
                    screen.blit(roadRAB_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif left in accept and above in accept and below in accept:
                    screen.blit(roadLAB_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif right in accept and left in accept and above in accept:
                    screen.blit(roadRLA_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif right in accept and left in accept and below in accept:
                    screen.blit(roadRLB_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))

                    
                elif right in accept and below in accept:
                    screen.blit(roadRB_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif left in accept and below in accept:
                    screen.blit(roadLB_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif right in accept and above in accept:
                    screen.blit(roadRA_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif left in accept and above in accept:
                    screen.blit(roadLA_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))

            elif self.item=="Track":
                above=tileList[self.xNumber+self.yNumber*200-200].item
                below=tileList[self.xNumber+self.yNumber*200+200].item
                right=tileList[self.xNumber+1+self.yNumber*200].item
                left=tileList[self.xNumber-1+self.yNumber*200].item
                accept=["Track","Factory","Town","Refinery","Airport"]
                
                if left not in accept and right not in accept:##Drawing road in correct orientation
                    screen.blit(trainUp_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                if above not in accept and below not in accept:
                    screen.blit(trainHorizontal_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                    
                elif right in accept and left in accept and above in accept and below in accept:
                    screen.blit(trainUp_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                    screen.blit(trainHorizontal_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))

                elif right in accept and above in accept and below in accept:
                    screen.blit(trainRAB_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif left in accept and above in accept and below in accept:
                    screen.blit(trainLAB_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif right in accept and left in accept and above in accept:
                    screen.blit(trainRLA_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif right in accept and left in accept and below in accept:
                    screen.blit(trainRLB_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))

                    
                elif right in accept and below in accept:
                    screen.blit(trainRB_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif left in accept and below in accept:
                    screen.blit(trainLB_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif right in accept and above in accept:
                    screen.blit(trainRA_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif left in accept and above in accept:
                    screen.blit(trainLA_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))

            elif self.item=="Bay":
                if self.value==3:
                    screen.blit(bay3_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif self.value==2:
                    screen.blit(bay2_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                elif self.value==1:
                    screen.blit(bay1_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                else: 
                    screen.blit(bay_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
            elif self.item=="Station":
                screen.blit(station_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
            elif self.item=="Airport":
                screen.blit(airport_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                
                valueText=font.render(str(self.holding+" ("+str(round(self.value))+")"),False,(0,0,0))
                screen.blit(valueText,(screenx+(self.xNumber*20)-70,screeny+(self.yNumber*20)-20))
                
            elif self.item=="Tree":
                screen.blit(tree_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
            elif self.item=="Water":
                screen.blit(water_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
            elif self.item=="townPiece":
                screen.blit(townPiece_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
            elif self.item=="Grain":
                screen.blit(grainPiece_img,(screenx+(self.xNumber*20),screeny+(self.yNumber*20)))
                
    def increase(self):
        if self.value<self.capacity:##Adds to factories
            self.value+=self.rate*gameSpeed



class Lorry:## Vehicle moves on road
    def __init__(self,path):
        self.path=path
        self.x=path[0][0]*20
        self.y=path[0][1]*20
        self.item=0
        self.carrying=0
        self.product=""
        self.bus=False
        self.bay=0


    def move(self):
        global cash,currentProfit
        if self.bus==False:
            if self.path[self.item][0]<self.path[self.item+1][0]:
                self.x+=1*gameSpeed
                screen.blit(lorryRight_img,((screenx+self.x+2),(screeny+self.y-4)))##Drawing lorry in correct direction
            elif self.path[self.item][0]>self.path[self.item+1][0]:
                self.x-=1*gameSpeed
                screen.blit(lorryLeft_img,((screenx+self.x+2),(screeny+self.y+4)))
            elif self.path[self.item][1]<self.path[self.item+1][1]:
                self.y+=1*gameSpeed
                screen.blit(lorryDown_img,((screenx+self.x+4),(screeny+self.y+2)))
            elif self.path[self.item][1]>self.path[self.item+1][1]:
                self.y-=1*gameSpeed
                screen.blit(lorryUp_img,((screenx+self.x-4),(screeny+self.y+2)))
        else:
            if self.path[self.item][0]<self.path[self.item+1][0]:
                self.x+=1*gameSpeed
                screen.blit(busRight_img,((screenx+self.x+2),(screeny+self.y-4)))##Drawing lorry in correct direction
            elif self.path[self.item][0]>self.path[self.item+1][0]:
                self.x-=1*gameSpeed
                screen.blit(busLeft_img,((screenx+self.x+2),(screeny+self.y+4)))
            elif self.path[self.item][1]<self.path[self.item+1][1]:
                self.y+=1*gameSpeed
                screen.blit(busDown_img,((screenx+self.x+4),(screeny+self.y+2)))
            elif self.path[self.item][1]>self.path[self.item+1][1]:
                self.y-=1*gameSpeed
                screen.blit(busUp_img,((screenx+self.x-4),(screeny+self.y+2)))
    
            
        if ((self.x/20),(self.y/20))==self.path[self.item+1]:
            self.item+=1

        if extraInfo==True:
            valueText=smallfont.render(str(self.product+" ("+str(round(self.carrying))+")"),False,(200,200,0))
            screen.blit(valueText,((screenx+self.x+2)+20,(screeny+self.y+2)))
            
        #####Load of complicated stuff for changing direction and controlling flow of goods
        if self.item==len(self.path)-1:
            obj=tileList[self.path[self.item][0]+self.path[self.item][1]*200]
            
            if obj.item=="Town" and self.product in goodsList:
                if self.product=="wood goods" and currentLaw!="Ban Wood Goods":
                    if obj.usedWoodGoods<obj.woodGoods-20:
                        cash+=self.carrying*woodPrice
                        currentProfit+=self.carrying*woodPrice
                        obj.usedWoodGoods+=self.carrying
                        self.carrying=0
                    else:
                        cash+=(obj.woodGoods-obj.usedWoodGoods)*woodPrice
                        currentProfit+=(obj.woodGoods-obj.usedWoodGoods)*woodPrice
                        obj.usedWoodGoods=obj.woodGoods
                        self.carrying-=obj.woodGoods-obj.usedWoodGoods
                elif self.product=="metal goods" and currentLaw!="Ban Metal Goods":
                    if obj.usedMetalGoods<obj.metalGoods-20:
                        cash+=self.carrying*metalPrice
                        currentProfit+=self.carrying*metalPrice
                        obj.usedMetalGoods+=self.carrying
                        self.carrying=0
                    else:
                        cash+=(obj.metalGoods-obj.usedMetalGoods)*metalPrice
                        currentProfit+=(obj.metalGoods-obj.usedMetalGoods)*metalPrice
                        obj.usedMetalGoods=obj.metalGoods
                        self.carrying-=obj.metalGoods-obj.usedMetalGoods
                elif self.product=="plastic goods" and currentLaw!="Ban Plastic Goods":
                    if obj.usedPlasticGoods<obj.plasticGoods-20:
                        cash+=self.carrying*plasticPrice
                        currentProfit+=self.carrying*plasticPrice
                        obj.usedPlasticGoods+=self.carrying
                        self.carrying=0
                    else:
                        cash+=(obj.plasticGoods-obj.usedPlasticGoods)*plasticPrice
                        currentProfit+=(obj.plasticGoods-obj.usedPlasticGoods)*plasticPrice
                        obj.usedPlasticGoods=obj.plasticGoods
                        self.carrying-=obj.plasticGoods-obj.usedPlasticGoods
                elif self.product=="food goods" and currentLaw!="Ban Food Goods":
                    if obj.usedFoodGoods<obj.foodGoods-20:
                        cash+=self.carrying*foodPrice
                        currentProfit+=self.carrying*foodPrice
                        obj.usedFoodGoods+=self.carrying
                        self.carrying=0
                    else:
                        cash+=(obj.foodGoods-obj.usedFoodGoods)*foodPrice
                        currentProfit+=(obj.foodGoods-obj.usedFoodGoods)*foodPrice
                        obj.usedFoodGoods=obj.foodGoods
                        self.carrying-=obj.foodGoods-obj.usedFoodGoods

                     

            elif obj.item=="Town" and self.product=="people":
                obj.value+=self.carrying+growthPerBus
                cash+=self.carrying*busPrice
                currentProfit+=self.carrying*busPrice
                self.carrying=0
                newVal=random.randint(5,30)
                self.carrying=newVal
                obj.value-=newVal

            elif obj.item=="Airport":
                if self.product=="":
                    self.product=obj.holding
                elif self.carrying>0 or self.product!=obj.holding:
                    obj.holding=self.product
                    obj.value+=self.carrying
                    self.carrying=0
                    obj.holding=self.product
                else:
                    self.product=obj.holding
                    if obj.value>=20:
                        self.carrying=20
                        obj.value-=20
                    else:
                        self.carrying=obj.value
                        obj.value=0
                        
            elif obj.item=="Factory" and self.carrying==0:
                if self.product==obj.produce:
                    if obj.value>=20:
                        self.carrying=20
                        obj.value-=20
                    else:
                        temp=round(obj.value)
                        self.carrying=temp
                        obj.value-=temp
            elif obj.item=="Refinery":
                if self.carrying>0:
                    if self.product in obj.intakeList:
                        if obj.produce=="none":
                            cash+=self.carrying
                            currentProfit+=self.carrying
                        else:
                            obj.value+=self.carrying
                            cash+=round(self.carrying/2)
                            currentProfit+=round(self.carrying/2)
                        self.carrying=0
                else:
                    if self.product==obj.produce:
                        if obj.value>=20:
                            self.carrying=20
                            obj.value-=20
                        else:
                            temp=round(obj.value)
                            self.carrying=temp
                            obj.value-=temp                    

                
            self.path=self.path[::-1]
            self.item=0


class Train:## Vehicle moves on road
    def __init__(self,path):
        self.path=path
        self.x=path[0][0]*20
        self.y=path[0][1]*20
        self.item=0
        self.carrying=0
        self.station=0
        self.product=""
        self.bus=False
        self.history=[]
        for i in range(40):
            self.history.append((self.x,self.y))

    def move(self):
        global cash,currentProfit
        if self.path[self.item][0]<self.path[self.item+1][0]:
            self.x+=5*gameSpeed
            screen.blit(driverRight_img,((screenx+self.x),(screeny+self.y)))##Drawing lorry in correct direction
        elif self.path[self.item][0]>self.path[self.item+1][0]:
            self.x-=5*gameSpeed
            screen.blit(driverLeft_img,((screenx+self.x),(screeny+self.y)))
        elif self.path[self.item][1]<self.path[self.item+1][1]:
            self.y+=5*gameSpeed
            screen.blit(driverDown_img,((screenx+self.x),(screeny+self.y)))
        elif self.path[self.item][1]>self.path[self.item+1][1]:
            self.y-=5*gameSpeed
            screen.blit(driverUp_img,((screenx+self.x),(screeny+self.y)))


        if gameSpeed==0:
            for box in range(6):
                screen.blit(trainPiece_img,(screenx+self.history[(-(box+1))*round(4/prevSpeed)][0]+2,screeny+self.history[(-(box+1))*round(4/prevSpeed)][1]+2))
        else:
            
            for box in range(6):
                screen.blit(trainPiece_img,(screenx+self.history[(-(box+1))*round(4/gameSpeed)][0]+2,screeny+self.history[(-(box+1))*round(4/gameSpeed)][1]+2))
            self.history.append((self.x,self.y))  

        if len(self.history)>50:
            self.history.pop(0)

            
        if ((self.x/20),(self.y/20))==self.path[self.item+1]:
            self.item+=1

        if extraInfo==True:
            valueText=smallfont.render(str(self.product+" ("+str(round(self.carrying))+")"),False,(255,0,0))
            screen.blit(valueText,((screenx+self.x+2)+20,(screeny+self.y+2)))
            
        #####Load of complicated stuff for changing direction and controlling flow of goods
        if self.item==len(self.path)-1:
            obj=tileList[self.path[self.item][0]+self.path[self.item][1]*200]
            
            if obj.item=="Town" and self.product in goodsList:
                if self.product=="wood goods" and currentLaw!="Ban Wood Goods":
                    if obj.usedWoodGoods<obj.woodGoods-20:
                        cash+=self.carrying*woodPrice
                        currentProfit+=self.carrying*woodPrice
                        obj.usedWoodGoods+=self.carrying
                        self.carrying=0
                    else:
                        cash+=(obj.woodGoods-obj.usedWoodGoods)*woodPrice
                        currentProfit+=(obj.woodGoods-obj.usedWoodGoods)*woodPrice
                        obj.usedWoodGoods=obj.woodGoods
                        self.carrying-=obj.woodGoods-obj.usedWoodGoods
                elif self.product=="metal goods" and currentLaw!="Ban Metal Goods":
                    if obj.usedMetalGoods<obj.metalGoods-20:
                        cash+=self.carrying*metalPrice
                        currentProfit+=self.carrying*metalPrice
                        obj.usedMetalGoods+=self.carrying
                        self.carrying=0
                    else:
                        cash+=(obj.metalGoods-obj.usedMetalGoods)*metalPrice
                        currentProfit+=(obj.metalGoods-obj.usedMetalGoods)*metalPrice
                        obj.usedMetalGoods=obj.metalGoods
                        self.carrying-=obj.metalGoods-obj.usedMetalGoods
                elif self.product=="plastic goods" and currentLaw!="Ban Plastic Goods":
                    if obj.usedPlasticGoods<obj.plasticGoods-20:
                        cash+=self.carrying*plasticPrice
                        currentProfit+=self.carrying*plasticPrice
                        obj.usedPlasticGoods+=self.carrying
                        self.carrying=0
                    else:
                        cash+=(obj.plasticGoods-obj.usedPlasticGoods)*plasticPrice
                        currentProfit+=(obj.plasticGoods-obj.usedPlasticGoods)*plasticPrice
                        obj.usedPlasticGoods=obj.plasticGoods
                        self.carrying-=obj.plasticGoods-obj.usedPlasticGoods
                elif self.product=="food goods" and currentLaw!="Ban Food Goods":
                    if obj.usedFoodGoods<obj.foodGoods-20:
                        cash+=self.carrying*foodPrice
                        currentProfit+=self.carrying*foodPrice
                        obj.usedFoodGoods+=self.carrying
                        self.carrying=0
                    else:
                        cash+=(obj.foodGoods-obj.usedFoodGoods)*foodPrice
                        currentProfit+=(obj.foodGoods-obj.usedFoodGoods)*foodPrice
                        obj.usedFoodGoods=obj.foodGoods
                        self.carrying-=obj.foodGoods-obj.usedFoodGoods

                    
            elif obj.item=="Town" and self.product=="people":
                obj.value+=self.carrying+growthPerBus
                cash+=self.carrying*busPrice
                currentProfit+=self.carrying*busPrice
                self.carrying=0
                newVal=random.randint(20,100)
                self.carrying=newVal
                obj.value-=newVal
                
            elif obj.item=="Airport":
                if self.product=="":
                    self.product=obj.holding
                elif self.carrying>0 or self.product!=obj.holding:
                    obj.holding=self.product
                    obj.value+=self.carrying
                    self.carrying=0
                    obj.holding=self.product
                else:
                    self.product=obj.holding
                    if obj.value>=100:
                        self.carrying=100
                        obj.value-=100
                    else:
                        self.carrying=obj.value
                        obj.value=0
                        
            elif obj.item=="Factory" and self.carrying==0:
                if self.product==obj.produce:
                    if obj.value>=100:
                        self.carrying=100
                        obj.value-=100
                    else:
                        temp=round(obj.value)
                        self.carrying=temp
                        obj.value-=temp
            elif obj.item=="Refinery":
                if self.carrying>0:
                    if self.product in obj.intakeList:
                        if obj.produce=="none" and currentLaw!="Ban Coal":
                            cash+=self.carrying
                            currentProfit+=self.carrying
                        else:
                            obj.value+=self.carrying
                            cash+=round(self.carrying/2)
                            currentProfit+=round(self.carrying/2)
                        self.carrying=0
                else:
                    if self.product==obj.produce:
                        if obj.value>=100:
                            self.carrying=100
                            obj.value-=100
                        else:
                            temp=round(obj.value)
                            self.carrying=temp
                            obj.value-=temp                    

                
            self.path=self.path[::-1]
            self.item=0

class Plane:## Plane, no pathfinding or roads
    def __init__(self,start,end):
        self.x=start[0]*20
        self.y=start[1]*20
        self.item=0
        self.carrying=0
        self.product=tileList[start[0]+start[1]*200].holding
        self.bus=False
        self.targetx=end[0]*20
        self.targety=end[1]*20
        self.pickupx=self.x
        self.pickupy=self.y
        self.dropx=self.targetx
        self.dropy=self.targety



    def move(self):
        global cash

        flyAngle=math.atan2(self.targety-self.y,self.targetx-self.x)

        self.x+=math.cos(flyAngle)*planeSpeed*gameSpeed
        self.y+=math.sin(flyAngle)*planeSpeed*gameSpeed
        planeROT_img=pygame.transform.rotate(plane_img,-math.degrees(flyAngle)-90)
        screen.blit(planeROT_img,((screenx+self.x),(screeny+self.y)))##Drawing plane in correct direction





        if extraInfo==True:
            valueText=smallfont.render(str(self.product+" ("+str(round(self.carrying))+")"),False,(0,0,255))
            screen.blit(valueText,((screenx+self.x+2)+20,(screeny+self.y+2)))
            
        #####Load of complicated stuff for changing direction and controlling flow of goods
        if collide(self.x+10,self.y+10,self.targetx-20,self.targety-20,60,60):


            self.x=self.targetx
            self.y=self.targety
            obj=tileList[int(self.x/20)+int(self.y/20)*200]
            if self.x==self.pickupx and self.y==self.pickupy:
                if obj.value>50:
                    self.carrying+=50
                    obj.value-=50
                    self.product=obj.holding
                else:
                    self.carrying+=obj.value
                    obj.value=0
                    self.product=obj.holding
            else:
                obj.value+=self.carrying
                obj.holding=self.product
                self.carrying=0
                              

            if self.targetx==self.pickupx and self.targety==self.pickupy:
                self.targetx=self.dropx
                self.targety=self.dropy
            else:
                self.targetx=self.pickupx
                self.targety=self.pickupy

            #self.x-=math.cos(flyAngle)*10
            #self.y-=math.sin(flyAngle)*10


class MenuItem:
    def __init__(self,x,y,image,item,cost):
        self.image=image
        self.item=item
        self.x=x
        self.y=y
        self.cost=cost
    def draw(self):
        global buildItem,fullscreen,screen,gameSpeed,mainMenu,prevSpeed
        screen.blit(self.image,(self.x,self.y))
        if collide(mousex,mousey,self.x,self.y,40,40):
            
            pygame.draw.rect(screen,(200,200,200),(self.x,self.y,40,40),2)
            costText=font.render(str(self.cost),False,(0,0,0))
            screen.blit(costText,(self.x+5,self.y-20))
            
            if clicked==True:
                if self.item=="Fullscreen":
                    if fullscreen==False:
                        screen=pygame.display.set_mode((1600,900),FULLSCREEN)
                        fullscreen=True
                    else:
                        screen=pygame.display.set_mode((1600,900))
                        fullscreen=False
                elif self.item=="speed1":
                    feed.append("Speed X1")
                    gameSpeed=1
                    for i in lorryList:
                        i.x=i.path[i.item][0]*20
                        i.y=i.path[i.item][1]*20
                    for i in trainList:
                        i.x=i.path[i.item][0]*20
                        i.y=i.path[i.item][1]*20
                        
                elif self.item=="speed2":
                    feed.append("Speed X2")
                    gameSpeed=2
                    for i in lorryList:
                        i.x=i.path[i.item][0]*20
                        i.y=i.path[i.item][1]*20
                    for i in trainList:
                        i.x=i.path[i.item][0]*20
                        i.y=i.path[i.item][1]*20                
                elif self.item=="speed3":
                    feed.append("Speed X4")
                    gameSpeed=4
                    for i in lorryList:
                        i.x=i.path[i.item][0]*20
                        i.y=i.path[i.item][1]*20
                    for i in trainList:
                        i.x=i.path[i.item][0]*20
                        i.y=i.path[i.item][1]*20
                elif self.item=="Pause":
                    feed.append("Paused")
                    prevSpeed=gameSpeed
                    gameSpeed=0
                elif self.item=="Routes":
                    windowList.append(RouteWindow(100,100,400,600))
                elif self.item=="Finance":
                    windowList.append(FinanceWindow(20,300,700,500))
                elif self.item=="Company":
                    windowList.append(CompanyWindow(900,100,540,300))
                elif self.item=="Menu":
                    windowList.append(OptionsWindow(500,200,600,300))
                buildItem=self.item
                
#320 so middle is 800 left is 640
##Setting up menu items:
menuList=[MenuItem(600,860,roadSelect_img,"Road",roadCost),
          MenuItem(640,860,baySelect_img,"Bay",bayCost),
          MenuItem(680,860,trainSelect_img,"Track",trackCost),
          MenuItem(720,860,stationSelect_img,"Station",stationCost),
          MenuItem(760,860,airportSelect_img,"Airport",airportCost),
          MenuItem(800,860,deleteSelect_img,"Delete",deleteCost),
          MenuItem(840,860,companySelect_img,"Company","Company"),
          MenuItem(880,860,financeSelect_img,"Finance","Finance"),
          MenuItem(920,860,routesSelect_img,"Routes","Routes"),
          MenuItem(1400,860,pauseSelect_img,"Pause","Pause"),
          MenuItem(1440,860,speed1Select_img,"speed1","X1"),
          MenuItem(1480,860,speed2Select_img,"speed2","X2"),
          MenuItem(1520,860,speed3Select_img,"speed3","X4"),
          MenuItem(1560,860,fullscreenSelect_img,"Fullscreen","[   ]"),
          MenuItem(1560,0,menuSelect_img,"Menu","")]


class RisingText:
    def __init__(self,x,y,text):
        self.x=x-20
        self.y=y-40
        self.text=text
        self.time=15
        self.startScreenx=screenx
        self.startScreeny=screeny
    def draw(self,risingNumber):
        riseText=font.render(str(self.text),False,(200,200,0))
        screen.blit(riseText,(self.x+(screenx-self.startScreenx),self.y+(screeny-self.startScreeny)))        
        self.y-=2
        self.time-=1
        if self.time<=0:
            risingTextList.pop(risingNumber)

class Window:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.scroll=0
        self.moving=False
        self.grow=0
    def draw(self):
        if self.grow<1:
            pygame.draw.rect(screen,(0,0,0),(self.x+(self.width/2)*(1-self.grow),self.y+(self.height/2)*(1-self.grow),self.width*self.grow,self.height*self.grow),0)
            self.grow+=0.2
        else:
            pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height),0)
            pygame.draw.rect(screen,(30,30,30),(self.x,self.y,self.width,self.height),2)
            pygame.draw.line(screen,(30,30,30),(self.x,self.y+20),(self.x+self.width,self.y+20),1)
            screen.blit(windowExit_img,(self.x+self.width-18,self.y+2))
    def move(self,windowCount):
        global clicked
        if clicked==True and collide(mousex,mousey,self.x+self.width-20,self.y,20,20):
            windowList.pop(windowCount)
            clicked=False
        elif mouseDown==True and collide(mousex,mousey,self.x,self.y,self.width,20) or self.moving==True:
            self.moving=True
            self.x=mousex-self.xDist
            self.y=mousey-self.yDist
        else:
            self.xDist=mousex-self.x
            self.yDist=mousey-self.y
        if mouseDown==False:
            self.moving=False
    def checkMouseOver(self):
        if collide(mousex,mousey,self.x,self.y,self.width,self.height)==True:
            return True
        return False
    def checkScroll(self,amount):
        if collide(mousex,mousey,self.x,self.y,self.width,self.height)==True:
            self.scroll+=amount



            
class RouteWindow(Window):
    def content(self):
        titleText=font.render("Routes",False,(255,255,255))
        screen.blit(titleText,(self.x+self.width/2-40,self.y+1))
        routeCount=0
        for route in lorryList:
            try:
                if tileList[route.path[0][0]+route.path[0][1]*200].produce==route.product:
                    start=tileList[route.path[0][0]+route.path[0][1]*200].name
                    end=tileList[route.path[-1][0]+route.path[-1][1]*200].name##Get correct direction of the lorry route, list is constantly flipped 0_0

                else:
                    start=tileList[route.path[-1][0]+route.path[-1][1]*200].name
                    end=tileList[route.path[0][0]+route.path[0][1]*200].name
                    
                if self.y+22+routeCount*20+self.scroll<self.y+self.height-20 and self.y+22+routeCount*20+self.scroll>self.y+20:
                    routeText=font.render(str(start+" > "+end),False,(255,255,255))
                    screen.blit(routeText,(self.x+5,self.y+22+routeCount*20+self.scroll))
                    screen.blit(windowExit_img,(self.x+300,self.y+22+routeCount*20+self.scroll))
                    if collide(mousex,mousey,self.x+300,self.y+22+routeCount*20+self.scroll,20,20) and clicked==True:
                        tileList[route.bay].value+=1
                        lorryList.remove(route)

                routeCount+=1
            except:
                pass
        for route in trainList:
            try:
                if tileList[route.path[0][0]+route.path[0][1]*200].produce==route.product:
                    start=tileList[route.path[0][0]+route.path[0][1]*200].name
                    end=tileList[route.path[-1][0]+route.path[-1][1]*200].name##Get correct direction of the lorry route, list is constantly flipped 0_0

                else:
                    start=tileList[route.path[-1][0]+route.path[-1][1]*200].name
                    end=tileList[route.path[0][0]+route.path[0][1]*200].name
                    
                if self.y+22+routeCount*20+self.scroll<self.y+self.height-20 and self.y+22+routeCount*20+self.scroll>self.y+20:    
                    routeText=font.render(str(start+" > "+end),False,(255,255,255))
                    screen.blit(routeText,(self.x+5,self.y+22+routeCount*20+self.scroll))
                    screen.blit(windowExit_img,(self.x+300,self.y+22+routeCount*20+self.scroll))
                    if collide(mousex,mousey,self.x+300,self.y+22+routeCount*20+self.scroll,20,20) and clicked==True:
                        tileList[route.station].value+=1
                        trainList.remove(route)

                routeCount+=1
            except:
                pass
class TownWindow(Window):
    def __init__(self,x,y,width,height,tileNumber):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.tileNumber=int(tileNumber)
        self.scroll=0
        self.moving=False
        self.grow=0
    def content(self):
        global cash,tileList,currentExpenditure
        titleText=font.render(str(tileList[self.tileNumber].name),False,(255,255,255))
        screen.blit(titleText,(self.x+5,self.y+1))

        woodText=smallfont.render("Wooden Goods: "+str(tileList[self.tileNumber].usedWoodGoods)+"/"+str(tileList[self.tileNumber].woodGoods),True,(200,0,0))
        screen.blit(woodText,(self.x+5,self.y+25))

        metalText=smallfont.render("Metal Goods: "+str(tileList[self.tileNumber].usedMetalGoods)+"/"+str(tileList[self.tileNumber].metalGoods),True,(255,255,255))
        screen.blit(metalText,(self.x+5,self.y+45))

        plasticText=smallfont.render("Plastic Goods: "+str(tileList[self.tileNumber].usedPlasticGoods)+"/"+str(tileList[self.tileNumber].plasticGoods),True,(200,0,0))
        screen.blit(plasticText,(self.x+5,self.y+65)) 

        foodText=smallfont.render("Food Goods: "+str(tileList[self.tileNumber].usedFoodGoods)+"/"+str(tileList[self.tileNumber].foodGoods),True,(255,255,255))
        screen.blit(foodText,(self.x+5,self.y+85))

        habText=smallfont.render(str(tileList[self.tileNumber].value)+" habitants",True,(200,200,0))
        screen.blit(habText,(self.x+5,self.y+110))

        respectText=smallfont.render("Respect is "+str(tileList[self.tileNumber].respect)+"/100",True,(200,200,0))
        screen.blit(respectText,(self.x+5,self.y+150))

        busText=smallfont.render("Buses "+str(tileList[self.tileNumber].usedBuses)+"/"+str(tileList[self.tileNumber].busLimit),True,(255,255,255))
        screen.blit(busText,(self.x+220,self.y+25))

        resText=smallfont.render("Bribe $"+str(respectCost),True,(255,255,255))
        screen.blit(resText,(self.x+160,self.y+150))
        pygame.draw.rect(screen,(50,50,50),(self.x+156,self.y+146,140,20),2)
        if collide(mousex,mousey,self.x+156,self.y+146,138,20) and cash>=respectCost and tileList[self.tileNumber].respect<100 and clicked==True:
            cash-=respectCost
            tileList[self.tileNumber].respect+=10


        factoryText=smallfont.render("Fund Factory",True,(255,255,255))
        screen.blit(factoryText,(self.x+10,self.y+180))
        pygame.draw.rect(screen,(50,50,50),(self.x+8,self.y+180-4,130,20),2)
        if collide(mousex,mousey,self.x+8,self.y+180-4,130,20) and cash>=fundCost and tileList[self.tileNumber].respect>40 and clicked==True:
            cash-=fundCost
            currentExpenditure+=fundCost
            tileList[self.tileNumber].addPiece("Factory")

        refineryText=smallfont.render("Fund Refinery",True,(255,255,255))
        screen.blit(refineryText,(self.x+160,self.y+180))
        pygame.draw.rect(screen,(50,50,50),(self.x+160-4,self.y+180-4,130+8,20),2)
        if collide(mousex,mousey,self.x+160-4,self.y+180-4,130+8,20) and cash>=fundCost and tileList[self.tileNumber].respect>40 and clicked==True:
            cash-=fundCost
            currentExpenditure+=fundCost
            tileList[self.tileNumber].addPiece("Refinery")

class FactoryWindow(Window):
    def __init__(self,x,y,width,height,tileNumber):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.tileNumber=int(tileNumber)
        self.scroll=0
        self.moving=False
        self.grow=0
    def content(self):
        titleText=font.render(str(tileList[self.tileNumber].name),False,(255,255,255))
        screen.blit(titleText,(self.x+5,self.y+1))

        if tileList[self.tileNumber].item=="Factory":
            infoText=font.render("Produces "+str(round(tileList[self.tileNumber].rate*600))+" "+str(tileList[self.tileNumber].produce)+" per day",True,(255,255,255))
            screen.blit(infoText,(self.x+5,self.y+30))
            infoText=font.render("Holding "+str(round(tileList[self.tileNumber].value))+" / "+str(round(tileList[self.tileNumber].capacity)),True,(255,0,0))
            screen.blit(infoText,(self.x+5,self.y+60))
        else:
            infoText=font.render("Produces "+str(tileList[self.tileNumber].produce)+" from "+str(tileList[self.tileNumber].intakeList[0])+" "+str(tileList[self.tileNumber].intakeList[1]),True,(255,255,255))
            screen.blit(infoText,(self.x+5,self.y+30))
            infoText=font.render("Holding "+str(round(tileList[self.tileNumber].value)),True,(255,0,0))
            screen.blit(infoText,(self.x+5,self.y+60))

class OptionsWindow(Window):
    def content(self):
        global mainMenu
        titleText=font.render("Options",False,(255,255,255))
        screen.blit(titleText,(self.x+self.width/2-40,self.y+1))

        saveText=font.render("Save Game",False,(255,255,255))
        screen.blit(saveText,(self.x+20,self.y+24))
        
        for i in range(6):
            screen.blit(menuBox_img,(self.x+20,self.y+50+i*40))####Save files stuff
            if collide(mousex,mousey,self.x+20,self.y+50+i*40,120,30):
                text=font.render("Save "+str(i+1),True,(255,0,0))
                if clicked==True:
                    saveFile(i)
            else:
                text=font.render("Save "+str(i+1),True,(255,255,255))
            screen.blit(text,(self.x+30,self.y+55+i*40))
        pygame.draw.line(screen,(30,30,30),(self.x+150,self.y+20),(self.x+150,self.y+self.height),2)

        ###Exit buttons
        screen.blit(menuBox_img,(self.x+220,self.y+250))
        screen.blit(menuBox_img,(self.x+400,self.y+250))
        if collide(mousex,mousey,self.x+220,self.y+250,120,30):
            exitText=font.render("Exit to Menu",False,(255,0,0))
            if clicked==True:
                mainMenu=True
        else:
            exitText=font.render("Exit to Menu",False,(255,255,255))
        screen.blit(exitText,(self.x+228,self.y+256))

        if collide(mousex,mousey,self.x+400,self.y+250,120,30):
            deskText=font.render("To Desktop",False,(255,0,0))
            if clicked==True:
                pygame.quit()
                sys.exit()
                
        else:
            deskText=font.render("To Desktop",False,(255,255,255))
        screen.blit(deskText,(self.x+410,self.y+256))

class CompanyWindow(Window):
    def content(self):
        global forProposal,againstProposal,influence
        titleText=font.render("Company Information",False,(255,255,255))
        screen.blit(titleText,(self.x+160,self.y+1))

        titleText=font.render(companyName,False,(255,255,255))
        screen.blit(titleText,(self.x+10,self.y+30))
        pygame.draw.line(screen,(30,30,30),(self.x,self.y+55),(self.x+self.width,self.y+55),1)
        pygame.draw.line(screen,(30,30,30),(self.x,self.y+165),(self.x+self.width,self.y+165),1)
        titleText=font.render("Vehicles",False,(255,255,255))
        screen.blit(titleText,(self.x+10,self.y+60))
        titleText=font.render(str(len(lorryList))+" lorries",False,(255,255,0))
        screen.blit(titleText,(self.x+10,self.y+80))
        titleText=font.render(str(len(trainList))+" trains",False,(255,255,0))
        screen.blit(titleText,(self.x+10,self.y+100))
        titleText=font.render(str(len(planeList))+" planes",False,(255,255,0))
        screen.blit(titleText,(self.x+10,self.y+120))


        titleText=font.render("Products (last month)",False,(255,255,255))
        screen.blit(titleText,(self.x+150,self.y+60))
        titleText=font.render(str(round(totalwood))+" wood",False,(255,255,0))
        screen.blit(titleText,(self.x+150,self.y+80))
        titleText=font.render(str(round(totalmetal))+" metal",False,(255,255,0))
        screen.blit(titleText,(self.x+150,self.y+100))
        titleText=font.render(str(round(totalplastic))+" plastic",False,(255,255,0))
        screen.blit(titleText,(self.x+150,self.y+120))
        titleText=font.render(str(round(totalfood))+" food",False,(255,255,0))
        screen.blit(titleText,(self.x+150,self.y+140))

        titleText=font.render("Average Respect",False,(255,255,255))
        screen.blit(titleText,(self.x+350,self.y+110))
        titleText=font.render(str(averageRespect)+"/100",False,(255,255,0))
        screen.blit(titleText,(self.x+350,self.y+140))        
        
        ######Proposals
        titleText=font.render(str(round(round_down(influence,1)))+" influence points",False,(255,255,255))
        screen.blit(titleText,(self.x+10,self.y+170))


        titleText=font.render("Current Law: "+str(currentLaw),False,(255,255,255))
        screen.blit(titleText,(self.x+10,self.y+190))
        
        titleText=font.render("For             Against",False,(255,255,255))
        screen.blit(titleText,(self.x+50,self.y+230))
        titleText=font.render(str(round(forProposal)),False,(255,0,0))
        screen.blit(titleText,(self.x+50,self.y+250))
        titleText=font.render(str(round(againstProposal)),False,(255,0,0))
        screen.blit(titleText,(self.x+160,self.y+250))

        screen.blit(add_img,(self.x+55,self.y+270))
        if collide(mousex,mousey,self.x+55,self.y+270,20,20) and clicked==True:
            forProposal+=round_down(influence,1)
            influence=0
        screen.blit(add_img,(self.x+165,self.y+270))
        if collide(mousex,mousey,self.x+165,self.y+270,20,20) and clicked==True:
            againstProposal+=round_down(influence,1)
            influence=0
            
        titleText=font.render("Proposal: "+str(proposal),False,(255,255,255))
        screen.blit(titleText,(self.x+250,self.y+240))
            
        
class FinanceWindow(Window):
    def content(self):
        ####Graphs#####################################################
        global loan,cash
        titleText=font.render("Finance",False,(255,255,255))
        screen.blit(titleText,(self.x+self.width/2-40,self.y+1))
        pygame.draw.rect(screen,(100,100,100),(self.x+10,self.y+30,330,200),0)
        width=330/(len(lastMonthList)+1)
        for i in range(len(lastMonthList)):
            if i<len(lastMonthList)-1:
                pygame.draw.line(screen,(255,0,0),(self.x+10+i*width,self.y+230-(lastMonthList[i]/max(lastMonthList))*200),(self.x+10+(i+1)*width,self.y+230-(lastMonthList[i+1]/max(lastMonthList))*200),2)
                
        prevText=font.render("Previous Month",False,(255,255,255))
        screen.blit(prevText,(self.x+110,self.y+233))
        
        prevText=font.render("Income",False,(255,255,255))
        screen.blit(prevText,(self.x+10,self.y+250))
        prevText=font.render(str(round(lastProfit)),False,(0,255,0))
        screen.blit(prevText,(self.x+200,self.y+250))
        prevText=font.render("Expenditure",False,(255,255,255))
        screen.blit(prevText,(self.x+10,self.y+270))
        prevText=font.render(str(round(lastExpenditure)),False,(255,0,0))
        screen.blit(prevText,(self.x+200,self.y+270))
        prevText=font.render("Tax",False,(255,255,255))
        screen.blit(prevText,(self.x+10,self.y+290))
        prevText=font.render(str(round(lastTax)),False,(255,0,0))
        screen.blit(prevText,(self.x+200,self.y+290))
        prevText=font.render("Profit",False,(255,255,255))
        screen.blit(prevText,(self.x+10,self.y+310))

        colour=(255,0,0)
        if lastProfit-lastTax-lastExpenditure>0:
            colour=(0,255,0)
        prevText=font.render(str(round(lastProfit-lastTax-lastExpenditure)),False,colour)
        screen.blit(prevText,(self.x+200,self.y+310))
        
        pygame.draw.rect(screen,(100,100,100),(self.x+360,self.y+30,330,200),0)
        width=330/len(currentMonthList)
        for i in range(len(currentMonthList)):
            if i<len(currentMonthList)-1:
                pygame.draw.line(screen,(255,0,0),(self.x+360+i*width,self.y+230-(currentMonthList[i]/max(currentMonthList))*200),(self.x+360+(i+1)*width,self.y+230-(currentMonthList[i+1]/max(currentMonthList)*200)),2)

        currentText=font.render("Current Month",False,(255,255,255))
        screen.blit(currentText,(self.x+460,self.y+233))

        prevText=font.render("Income",False,(255,255,255))
        screen.blit(prevText,(self.x+360,self.y+250))
        prevText=font.render(str(round(currentProfit)),False,(0,255,0))
        screen.blit(prevText,(self.x+550,self.y+250))
        prevText=font.render("Expenditure",False,(255,255,255))
        screen.blit(prevText,(self.x+360,self.y+270))
        prevText=font.render(str(round(currentExpenditure)),False,(255,0,0))
        screen.blit(prevText,(self.x+550,self.y+270))
        prevText=font.render("Tax",False,(255,255,255))
        screen.blit(prevText,(self.x+360,self.y+290))
        prevText=font.render(str(round(currentTax)),False,(255,0,0))
        screen.blit(prevText,(self.x+550,self.y+290))
        prevText=font.render("Profit",False,(255,255,255))
        screen.blit(prevText,(self.x+360,self.y+310))
        colour=(255,0,0)
        if currentProfit-currentTax-currentExpenditure>0:
            colour=(0,255,0)
        prevText=font.render(str(round(currentProfit-currentTax-currentExpenditure)),False,colour)
        screen.blit(prevText,(self.x+550,self.y+310))


        
        ############################################################
        pygame.draw.line(screen,(30,30,30),(self.x,self.y+340),(self.x+700,self.y+340),2)
        loanText=font.render("Loan       $"+str(loan),True,(255,255,255))
        intText=font.render("Interest is "+str(interest)+"%"+" per day",True,(255,255,255))
        screen.blit(intText,(self.x+10,self.y+380))


        
        screen.blit(loanText,(self.x+10,self.y+350))
        screen.blit(add_img,(self.x+60,self.y+350))
        if collide(mousex,mousey,self.x+60,self.y+350,20,20) and clicked==True and loan<10000:
            loan+=1000
            cash+=1000
        screen.blit(subtract_img,(self.x+loanText.get_width()+20,self.y+350))
        if collide(mousex,mousey,self.x+loanText.get_width()+20,self.y+350,20,20) and clicked==True:
            if loan>1000 and cash>1000:
                loan-=1000
                cash-=1000
            else:
                if cash>=loan:
                    cash-=loan
                    loan=0
        #Net worth
        netWorth=len(lorryList)*80+len(trainList)*2000+len(planeList)*4000+cash-loan
        intText=font.render("Net Worth $"+str(round(netWorth)),True,(255,255,255))
        screen.blit(intText,(self.x+300,self.y+480))

        ##Prices
        priceText=font.render("Prices",True,(255,255,255))
        screen.blit(priceText,(self.x+550,self.y+350))    
        priceText=font.render("Wood  $"+"%.2f"%woodPrice,True,(200,200,200))
        screen.blit(priceText,(self.x+550,self.y+370))        
        priceText=font.render("Metal  $"+"%.2f"%metalPrice,True,(200,200,200))
        screen.blit(priceText,(self.x+550,self.y+390))
        priceText=font.render("Plastic  $"+"%.2f"%plasticPrice,True,(200,200,200))
        screen.blit(priceText,(self.x+550,self.y+410))
        priceText=font.render("Food  $"+"%.2f"%foodPrice,True,(200,200,200))
        screen.blit(priceText,(self.x+550,self.y+430))
        priceText=font.render("Bus  $"+"%.2f"%busPrice,True,(200,200,200))
        screen.blit(priceText,(self.x+550,self.y+450))
        priceText=font.render("Coal  $"+"%.2f"%coalPrice,True,(200,200,200))
        screen.blit(priceText,(self.x+550,self.y+470))
                    

class Node:
    def __init__(self,parent=None, position=None):
        self.parent=parent
        self.position=position
        self.g=0
        self.h=0
        self.f=0
    def __eq__(self,other):
        return self.position==other.position

def round_multiple(x, base=5):
    return base * round(x/base)
            
def round_down(num,divisor):
    return num-(num%divisor)

def round_up(num,divisor):
    return divisor*(round_down(num/divisor,1)+1)

def collide(checkx,checky,x,y,w,h):
    if checkx>x and checkx<x+w and checky>y and checky<y+h:
        return True
    else:
        return False

####SETUP################################################################

tileList=[]
for y in range(200):
    for x in range(200):
        tileList.append(Tile(x,y))

##Creating rivers

for i in range(numberOfRivers):
    sides=["l","r","t","b"]
    startSide=random.choice(["t","b"])
    if startSide=="l":
        startTile=random.randint(0,199)*200
        sides.remove("l") 
    elif startSide=="r":
        startTile=random.randint(0,199)*200+199
        sides.remove("r") 
    elif startSide=="t":
        startTile=random.randint(0,199)
        sides.remove("t") 
    elif startSide=="b":
        startTile=40000-random.randint(0,199)
        sides.remove("b") 
        
    while True:
        try:
            tileList[startTile].item="Water"
            direction=random.choice(sides)
            if direction=="r":
                startTile=startTile+1
            elif direction=="l":
                startTile=startTile-1           
            elif direction=="t":
                startTile=startTile-200
            elif direction=="b":
                startTile=startTile+200
        except:
            break;






        
##setting up towns, factories and refineries
for i in range(numberOfTowns):
    place=random.randint(1000,39000)
    if tileList[place].item==None:
        tileList[place].item="Town"
        tileList[place].capacity=100000
        tileList[place].value=random.randint(townStartMin,townStartMax)
        tileList[place].rate=0
        tileList[place].name=townNames[i]
        for i in range(round(tileList[place].value/80)):
            tileList[place].addPiece("townPiece")
        tileList[place].produce="people"
        tileList[place].colour=(random.randint(100,255),random.randint(100,255),random.randint(100,200))
        tileList[place].milestone=round_up(tileList[place].value,100)

        ##Setting up delivery limits
        tileList[place].metalGoods=round(tileList[place].value)+random.randint(-200,200)
        tileList[place].woodGoods=round(tileList[place].value)+random.randint(-200,200)
        tileList[place].plasticGoods=round(tileList[place].value)+random.randint(-200,200)
        tileList[place].foodGoods=round(tileList[place].value)+random.randint(-200,200)
        tileList[place].usedMetalGoods=0
        tileList[place].usedWoodGoods=0
        tileList[place].usedPlasticGoods=0
        tileList[place].usedFoodGoods=0
        tileList[place].respect=0
        tileList[place].busLimit=round(tileList[place].value/1000)
        tileList[place].usedBuses=0

for i in range(numberOfFactories):
    place=random.randint(1,40000)
    if tileList[place].item==None:
        tileList[place].item="Factory"
        factoryNum=random.randint(0,5)
        tileList[place].name=industryList[factoryNum][0]
        tileList[place].produce=industryList[factoryNum][1]
        if tileList[place].name=="Grain Farm":
            xPos=place-round_down(place,200)-3
            yPos=round_down(place/200,1)-3
            for y in range(7):
                for x in range(7):
                    try:
                        if tileList[int((xPos+x)+((yPos+y)*200))].item==None:
                            tileList[int((xPos+x)+((yPos+y)*200))].item="Grain"
                    except:
                        pass
        elif tileList[place].name=="Forestry":
            xPos=place-round_down(place,200)-3
            yPos=round_down(place/200,1)-3
            for y in range(7):
                for x in range(7):
                    try:
                        if tileList[int((xPos+x)+((yPos+y)*200))].item==None:
                            tileList[int((xPos+x)+((yPos+y)*200))].item="Tree"
                    except:                    
                        pass
    
for i in range(numberOfRefineries):
    place=random.randint(1,40000)
    refineryNum=random.randint(0,5)
    if tileList[place].item==None:
        tileList[place].item="Refinery"
        tileList[place].name=refineList[refineryNum][0]
        tileList[place].intakeList=[refineList[refineryNum][1],refineList[refineryNum][2]]
        tileList[place].produce=refineList[refineryNum][3]
        tileList[place].rate=0
    
    
for i in range(numberOfTrees):
    place=random.randint(1,40000)
    try:
        if tileList[place].item==None:
            tileList[place].item="Tree"
    except:
        pass
#########################################################################################   


def findPath(buildList,material):##A* pathfinding which is abit glitchy
    if material=="Bay":
        material="Road"
    elif material=="Station":
        material="Track"

    pos1=(int(buildList[1]-round_down(buildList[1]/200,1)*200),int(round_down(buildList[1]/200,1)))
    pos2=(int(buildList[2]-round_down(buildList[2]/200,1)*200),int(round_down(buildList[2]/200,1)))
    start_node=Node(None,pos1)
    start_node.g=start_node.h=start_node.f=0

    end_node=Node(None,pos2)
    end_node.g=end_node.h=end_node.f=0
    
    open_list=[]
    closed_list=[]
    open_list.append(start_node)
    tries=0
    while len(open_list)>0:
        current_node=open_list[0]
        current_index=0
        for index, item in enumerate(open_list):
            if item.f<current_node.f:
                current_node=item
                current_index=index
                
        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node==end_node:
            path=[]
            current=current_node
            while current is not None:
                path.append(current.position)
                current=current.parent
            feed.append("Route Created")
            return path[::-1]

        children=[]
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
      
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] > (200 - 1) or node_position[0] < 0 or node_position[1] > (200 -1) or node_position[1] < 0:
                continue

            if tileList[node_position[0]+node_position[1]*200].item != material and tileList[node_position[0]+node_position[1]*200].item != "Airport" and tileList[node_position[0]+node_position[1]*200].item != "Refinery" and tileList[node_position[0]+node_position[1]*200].item != "Town" and tileList[node_position[0]+node_position[1]*200].item != "Factory":
                continue
            

            new_node=Node(current_node,node_position)

            children.append(new_node)

        for child in children:

            for closed_child in closed_list:
                if child==closed_child:
                    continue
            child.g=current_node.g+1
            child.h=((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f=child.g+child.h

            for open_node in open_list:
                if child==open_node and child.g > open_node.g:
                    continue

            open_list.append(child)
        tries+=1
        if tries>2000:
            feed.append("No valid Route")
            return None

def payments():##Takes money per vehicles owned
    global payTimer,cash,date,profit,previousCash,currentTax,loan
    payTimer+=1
    if gameSpeed!=0:
        if payTimer>=(600/gameSpeed):
            cash-=len(lorryList)*lorryTax
            cash-=len(trainList)*trainTax
            cash-=len(planeList)*planeTax
            currentTax+=(len(planeList)*planeTax)+(len(trainList)*trainTax)+(len(lorryList)*lorryTax)
            payTimer=0
            date+=timedelta(days=1)
            profit=cash-previousCash
            previousCash=cash
            loan+=round(loan*(interest*0.01))



proposalList=["Ban Wood Goods",
              "Ban Metal Goods",
              "Ban Plastic Goods",
              "Ban Food Goods",
              "Ban Coal",
              "Double Selling Prices",
              "Half Selling Prices",
              ]
    

def setPrices():
    global woodPrice,metalPrice,plasticPrice,foodPrice, totalwood,totalmetal,totalplastic,totalfood,influence,forProposal,againstProposal,proposal,currentLaw,averageRespect
    ##Setting costs of goods
    totalwood=0.000001
    totalmetal=0.000001
    totalplastic=0.000001
    totalfood=0.000001
    towns=0
    totalrespect=0
    for i in tileList:
        if i.item=="Town":
            totalwood+=i.usedWoodGoods
            totalmetal+=i.usedMetalGoods
            totalplastic+=i.usedPlasticGoods
            totalfood+=i.usedFoodGoods
            towns+=1
            totalrespect+=i.respect
    total=totalwood+totalmetal+totalplastic+totalfood
    inverseTotal=(total/totalwood)+(total/totalmetal)+(total/totalplastic)+(total/totalfood)
    if total!=0:
        woodPrice=round_up((total/totalwood)/inverseTotal*totalPrice,0.2)
        metalPrice=round_up((total/totalmetal)/inverseTotal*totalPrice,0.2)
        plasticPrice=round_up((total/totalplastic)/inverseTotal*totalPrice,0.2)
        foodPrice=round_up((total/totalfood)/inverseTotal*totalPrice,0.2)

    averageRespect=round(totalrespect/towns)
    influence=(total/1000)+(totalrespect/towns)
    if forProposal>againstProposal:
        currentLaw=proposal
    forProposal=random.randint(1,1000-int(influence))
    againstProposal=1000-forProposal-round(influence)
    proposal=random.choice(proposalList)

    if currentLaw=="Double Selling Prices":
        woodPrice=woodPrice*2
        metalPrice=metalPrice*2
        plasticPrice=plasticPrice*2
        foodPrice=foodPrice*2
    elif currentLaw=="Half Selling Prices":
        woodPrice=round_up(woodPrice*0.5,0.2)
        metalPrice=round_up(metalPrice*0.5,0.2)
        plasticPrice=round_up(plasticPrice*0.5,0.2)
        foodPrice=round_up(foodPrice*0.5,0.2)
        
        

def showWindows():
    windowCount=0
    for i in windowList:
        i.draw()
        if i.grow>=1:
            i.content()
            i.move(windowCount)
        windowCount+=1

def drawRisingText():
    risingNumber=0
    for i in risingTextList:
        i.draw(risingNumber)
        risingNumber+=1

def mouseOverWindow():
    for i in windowList:
        if i.checkMouseOver()==True:
            return True
    return False


def resetDeliveries():
    for i in tileList:
        if i.item=="Town":
            if i.woodGoods==i.usedWoodGoods:
                i.value+=round(i.woodGoods/5)
                if i.respect<100:
                    i.respect+=10
            elif i.usedWoodGoods>0:
                i.respect+=1
            else:
                if i.respect>0:
                    i.respect-=1                
            if i.metalGoods==i.usedMetalGoods:
                i.value+=round(i.metalGoods/5)
                if i.respect<100:
                    i.respect+=10
            elif i.usedMetalGoods>0:
                i.respect+=1
            else:
                if i.respect>0:
                    i.respect-=1 
            if i.plasticGoods==i.usedPlasticGoods:
                i.value+=round(i.plasticGoods/5)
                if i.respect<100:
                    i.respect+=10
            elif i.usedPlasticGoods>0:
                i.respect+=1
            else:
                if i.respect>0:
                    i.respect-=1 
            if i.foodGoods==i.usedFoodGoods:
                i.value+=round(i.foodGoods/5)
                if i.respect<100:
                    i.respect+=10
            elif i.usedFoodGoods>0:
                i.respect+=1
            else:
                if i.respect>0:
                    i.respect-=1 

            i.woodGoods=round(i.value)+random.randint(-200,200)
            i.metalGoods=round(i.value)+random.randint(-200,200)
            i.plasticGoods=round(i.value)+random.randint(-200,200)
            i.foodGoods=round(i.value)+random.randint(-200,200)

                
            i.usedWoodGoods=0
            i.usedMetalGoods=0
            i.usedPlasticGoods=0
            i.usedFoodGoods=0
        

def drawItems():
    for i in tileList:
        i.draw()


def drawVehicles():
    for i in lorryList:
        i.move()
    for t in trainList:
        t.move()
    for p in planeList:
        p.move()

def drawMenuBar():
    screen.blit(fade_img,(0,870))
    for i in menuList:
        i.draw()

def drawui():
    if buildItem=="Delete":
        pygame.draw.rect(screen,(255,255,0),(round_down(mousex,20),round_down(mousey,20),20,20),3)
    elif len(buildList)==0:
        pygame.draw.rect(screen,(0,0,0),(round_down(mousex,20),round_down(mousey,20),20,20),2)
    elif len(buildList)==1:
        pygame.draw.rect(screen,(0,0,255),(round_down(mousex,20),round_down(mousey,20),20,20),3)
        startText=font.render(str("Start"),True,(0,0,255))
        screen.blit(startText,(round_down(mousex,20),round_down(mousey,20)-20))
    elif len(buildList)==2:
        pygame.draw.rect(screen,(255,0,0),(round_down(mousex,20),round_down(mousey,20),20,20),3)
        endText=font.render(str("End"),True,(255,0,0))
        screen.blit(endText,(round_down(mousex,20),round_down(mousey,20)-20))
    
    if clicked==True or mouseDown==True:
        pygame.draw.rect(screen,(255,255,255),(round_down(mousex,20),round_down(mousey,20),20,20),4)
        
    profitText=font.render("$"+str(round(profit)),True,(255,255,255))
    rect = pygame.Surface((profitText.get_width()+16,30), pygame.SRCALPHA, 32)
    rect.fill((0, 0, 0, 150))
    screen.blit(rect, (500-8-profitText.get_width()/2,0))
    screen.blit(profitText,(500-profitText.get_width()/2,8))

    cashText=font.render(str("$"+str(round(cash))),True,(200,200,0))
    rect2 = pygame.Surface((cashText.get_width()+16,30), pygame.SRCALPHA, 32)
    rect2.fill((0, 0, 0, 150))
    screen.blit(rect2, (800-cashText.get_width()/2-8,0))
    screen.blit(cashText,(800-cashText.get_width()/2,8))

    dateText=font.render(str(date.strftime("%d")+" "+date.strftime("%B")+" "+date.strftime("%Y")),True,(255,255,255))
    rect = pygame.Surface((228,30), pygame.SRCALPHA, 32)
    rect.fill((0, 0, 0, 150))
    screen.blit(rect, (996,0))
    screen.blit(dateText,(1000,8))


    if extraInfo==True:
        fpsText=font.render(str(round(clock.get_fps(),1)),True,(0,0,0))
        screen.blit(fpsText,(200,10))  
        

def drawFeed():
    for note in range(5):
        if len(feed)%2==0:
            if note%2==0:
                noteColour=(255,255,255)##Feed creation
            else:
                noteColour=(0,0,0)
        else:
            if note%2==0:
                noteColour=(255,255,255)
            else:
                noteColour=(0,0,0)
        noteText=font.render(str(feed[-(note+1)]),True,noteColour)
        screen.blit(noteText,(5,800-(note)*20))   




def build():
    global tileList,buildList,lorryList,cash,planeList,clicked,currentExpenditure
    itemNumber=(round_down(mousex-screenx,20)/20)+(round_down(mousey-screeny,20)/20)*200
    

        
    if tileList[int(itemNumber)].item==None:
        pygame.mixer.stop()
        build_sound.play()
        if buildItem=="Road" and cash>=roadCost:
            cash-=roadCost
            currentExpenditure+=roadCost
            tileList[int(itemNumber)].item=buildItem##Placing new item
            risingTextList.append(RisingText(mousex,mousey,"-$"+str(roadCost)))
        elif buildItem=="Track" and cash>=trackCost:
            cash-=trackCost
            currentExpenditure+=trackCost
            tileList[int(itemNumber)].item=buildItem##Placing new item
            risingTextList.append(RisingText(mousex,mousey,"-$"+str(trackCost)))
        elif buildItem=="Bay" and cash>=bayCost:
            cash-=bayCost
            currentExpenditure+=bayCost
            tileList[int(itemNumber)].item=buildItem
            tileList[int(itemNumber)].value=3
            tileList[int(itemNumber)].rate=0
            risingTextList.append(RisingText(mousex,mousey,"-$"+str(bayCost)))            
        elif buildItem=="Station" and cash>=stationCost:
            cash-=stationCost
            currentExpenditure+=stationCost
            tileList[int(itemNumber)].item=buildItem
            tileList[int(itemNumber)].value=1
            tileList[int(itemNumber)].rate=0
            risingTextList.append(RisingText(mousex,mousey,"-$"+str(stationCost)))
        elif buildItem=="Airport" and cash>=airportCost and clicked==True:
            cash-=airportCost
            currentExpenditure+=airportCost
            tileList[int(itemNumber)].item=buildItem
            tileList[int(itemNumber)].value=0
            tileList[int(itemNumber)].rate=0
            tileList[int(itemNumber)+1].item="air"
            tileList[int(itemNumber)+200].item="air"
            tileList[int(itemNumber)+201].item="air"
            risingTextList.append(RisingText(mousex,mousey,"-$"+str(airportCost)))



       
    elif buildItem=="Delete" and cash>=20 and clicked==True:
        if tileList[int(itemNumber)].item=="Bay":
            removeList=[]
            for item in lorryList:
                if round(item.bay)==round(itemNumber):
                    removeList.append(item)
            for i in removeList:
                lorryList.remove(i)
                    
        elif tileList[int(itemNumber)].item=="Station":
            for item in trainList:
                if int(item.station)==int(itemNumber):
                    trainList.remove(item)
        elif tileList[int(itemNumber)].item=="Town":
            feed.append("You can't do that")
            return
        tileList[int(itemNumber)].item=None
        tileList[int(itemNumber)].value=0
        tileList[int(itemNumber)].rate=0
        risingTextList.append(RisingText(mousex,mousey,"-$"+str(deleteCost)))
        cash-=20
        currentExpenditure+=20
        destroy_sound.play()
            
    elif tileList[int(itemNumber)].item=="Bay" and len(buildList)==0 and tileList[int(itemNumber)].value>0 and clicked==True:
        buildList.append(int(itemNumber))
        
    elif tileList[int(itemNumber)].item=="Station" and len(buildList)==0 and tileList[int(itemNumber)].value>0 and clicked==True:
        buildList.append(int(itemNumber))
        
    elif tileList[int(itemNumber)].item=="Airport" and len(buildList)==0 and tileList[int(itemNumber)].used==False and clicked==True:
        buildList.append(int(itemNumber))
        
    elif tileList[int(itemNumber)].item=="Town" and len(buildList)>0 and clicked==True:##Creating lorry route
        buildList.append(int(itemNumber))
                                                        
    elif tileList[int(itemNumber)].item=="Factory" and len(buildList)>0 and clicked==True:
        buildList.append(int(itemNumber))

    elif tileList[int(itemNumber)].item=="Refinery" and len(buildList)>0 and clicked==True:
        buildList.append(int(itemNumber))
        
    elif tileList[int(itemNumber)].item=="Airport" and len(buildList)>0 and clicked==True:
        buildList.append(int(itemNumber))

    elif tileList[int(itemNumber)].item=="Town" and clicked==True:
        windowList.append(TownWindow(600,350,300,200,itemNumber))

    elif tileList[int(itemNumber)].item=="Factory" and clicked==True:
        windowList.append(FactoryWindow(400,350,300,100,itemNumber))

    elif tileList[int(itemNumber)].item=="Refinery" and clicked==True:
        windowList.append(FactoryWindow(400,350,400,100,itemNumber))

   
    if len(buildList)>=3:
        if buildList[1]==buildList[2]:
            buildList=[] 
        elif tileList[buildList[0]].item=="Airport":
            if tileList[buildList[1]].item!="Airport" or tileList[buildList[2]].item!="Airport":
                buildList=[]
                return
            tileList[buildList[1]].used=True
            tileList[buildList[2]].used=True
            planeList.append(Plane((tileList[buildList[1]].xNumber,tileList[buildList[1]].yNumber),(tileList[buildList[2]].xNumber,tileList[buildList[2]].yNumber)))
            planeRoute_sound.play()

        else:
            path=findPath(buildList,tileList[buildList[0]].item)
            if path!=None:
                if tileList[buildList[0]].item=="Bay":
                    lorryList.append(Lorry(path))
                    if tileList[buildList[1]].item=="Town" and tileList[buildList[2]].item=="Town":##creating buses
                        if tileList[buildList[1]].busLimit>tileList[buildList[1]].usedBuses and tileList[buildList[2]].busLimit>tileList[buildList[2]].usedBuses:
                            tileList[buildList[1]].usedBuses+=1
                            tileList[buildList[2]].usedBuses+=1
                            lorryList[-1].bus=True
                        else:
                            lorryList.pop(-1)
                            buildList=[]
                            return
                    tileList[buildList[0]].value-=1
                    lorryList[-1].bay=buildList[0]
                    if tileList[buildList[1]].item=="Airport":
                        lorryList[-1].product=tileList[buildList[1]].holding
                    else:
                        lorryList[-1].product=tileList[buildList[1]].produce

                    lorryRoute_sound.play()
                        
                elif tileList[buildList[0]].item=="Station":
                    trainList.append(Train(path))
                    if tileList[buildList[1]].item=="Town" and tileList[buildList[2]].item=="Town":##creating buses
                        if tileList[buildList[1]].busLimit>tileList[buildList[1]].usedBuses and tileList[buildList[2]].busLimit>tileList[buildList[2]].usedBuses:
                            tileList[buildList[1]].usedBuses+=1
                            tileList[buildList[2]].usedBuses+=1
                            trainList[-1].bus=True
                        else:
                            trainList.pop(-1)
                            buildList=[]
                            return
                    tileList[buildList[0]].value-=1
                    trainList[-1].product=tileList[buildList[1]].produce
                    trainList[-1].station=buildList[0]

                    trainRoute_sound.play()


                
        buildList=[]
def drawBackground():##Places all grass
    if desert==True:
        for x in range(7):
            for y in range(7):
                screen.blit(desert_img,(screenx+x*640,screeny+y*640))
    else:
        for x in range(7):
            for y in range(7):
                screen.blit(grass_img,(screenx+x*640,screeny+y*640))

def drawMenuBackground():
    screen.blit(menuBackground_img,(0,0))
    versionText=font.render("Version: "+str(version),True,(0,0,0))
    screen.blit(versionText,(0,0))

def drawMenuItems():
    global mainMenu,showSaves
    screen.blit(title_img,(60,340))
    screen.blit(menuBox_img,(980,140))
    screen.blit(menuBox_img,(980,180))
    screen.blit(menuBox_img,(980,220))
    
    if collide(mousex,mousey,980,140,120,30):
        newText=font.render("New Game",True,(255,0,0))
        if clicked==True:
            mainMenu=False
    else:
        newText=font.render("New Game",True,(255,255,255))
    screen.blit(newText,(990,145))

    if collide(mousex,mousey,980,180,120,30):
        loadText=font.render("Load Game",True,(255,0,0))
        if clicked==True:
            showSaves=not showSaves
    else:
        loadText=font.render("Load Game",True,(255,255,255))
    screen.blit(loadText,(990,185))

    if showSaves==True:
        for i in range(6):
            screen.blit(menuBox_img,(1120,140+i*40))
            if collide(mousex,mousey,1120,140+i*40,120,30):
                text=font.render("Save "+str(i+1),True,(255,0,0))
                if clicked==True:
                    loadSave(i)
                    mainMenu=False
            else:
                text=font.render("Save "+str(i+1),True,(255,255,255))
            screen.blit(text,(1130,145+i*40))



    if collide(mousex,mousey,980,220,120,30):
        exitText=font.render("Exit Game",True,(255,0,0))
        if clicked==True:
            pygame.quit()
            sys.exit()
    else:
        exitText=font.render("Exit Game",True,(255,255,255))
    screen.blit(exitText,(990,225))

    
    

def drawMenuOptions():
    global desert
    screen.blit(grassDemo_img,(590,560))
    colour=(0,0,0)
    if collide(mousex,mousey,590,560,80,80):
        colour=(255,0,0)
        if clicked==True:
            desert=False
    elif desert==False:
        colour=(255,0,0)

    pygame.draw.rect(screen,colour,(590,560,80,80),2)

    colour=(0,0,0)
    screen.blit(desertDemo_img,(690,560))
    if collide(mousex,mousey,690,560,80,80):
        colour=(255,0,0)
        if clicked==True:
            desert=True
    elif desert==True:
        colour=(255,0,0)
    pygame.draw.rect(screen,colour,(690,560,80,80),2)

    ##Company name and details

    pygame.draw.rect(screen,(0,0,0),(590,655,180,30),2)
    nameText=font.render(companyName,True,(0,0,0))
    screen.blit(nameText,(600,660))


def saveFile(number):
    saveClass=SaveClass()
    with open("data/save"+str(number)+".p","wb") as file:
        pickle.dump(saveClass,file)
    


def loadSave(number):
    with open("data/save"+str(number)+".p","rb") as file:
        saveClass=pickle.load(file)
    saveClass.setVariables()
    


    
while True:
    screen.fill((107,142,35))
    if mainMenu==True:
        drawMenuBackground()
        drawMenuItems()
        drawMenuOptions()

    else:
        drawBackground()
        drawItems()
        drawVehicles()
        drawRisingText()
        if showUI==True:
            drawui()
            showWindows()
            drawMenuBar()
        drawFeed()
        payments()

        if (clicked==True or mouseDown==True) and mousey<860 and mouseOverWindow()==False:
            build()
        if date.day==1 and monthReset==False:
            setPrices()
            resetDeliveries()
            alert_sound.play()
            monthReset=True
            lastMonthList=currentMonthList.copy()
            currentMonthList=[cash]
            lastProfit=currentProfit
            lastExpenditure=currentExpenditure
            lastTax=currentTax
            currentProfit=0
            currentExpenditure=0
            currentTax=0
            
        elif date.day==2:
            monthReset=False
        if date.day==len(currentMonthList)+1:
            currentMonthList.append(cash)

        screenx+=xChange##Moving camera
        if screenx>0:
            screenx-=xChange
        elif screenx<-2400:
            screenx-=xChange
        screeny+=yChange
        if screeny>0:
            screeny-=yChange
        elif screeny<-3100:
            screeny-=yChange

    
    clicked=False
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==MOUSEMOTION:
            mousex,mousey=event.pos
        elif event.type==MOUSEBUTTONUP:
            if event.button==1:
                clicked=True
                mouseDown=False
        elif event.type==MOUSEBUTTONDOWN:
            
            if event.button==1:
                mouseDown=True
            elif event.button==4:
                for i in windowList:
                    i.checkScroll(scrollMenuSpeed)
            elif event.button==5:
                for i in windowList:
                    i.checkScroll(-scrollMenuSpeed)
                    
        elif event.type==KEYDOWN:
            if mainMenu==True:
                if event.key==K_BACKSPACE:
                    companyName=companyName[:-1]
                else:
                    if len(companyName)<12:
                        companyName=companyName+str(event.unicode)
            if event.key==K_d or event.key==K_RIGHT:
                xChange-=scrollSpeed
            elif event.key==K_a or event.key==K_LEFT:
                xChange+=scrollSpeed
            if event.key==K_w or event.key==K_UP:
                yChange+=scrollSpeed
            elif event.key==K_s or event.key==K_DOWN:
                yChange-=scrollSpeed

            elif event.key==K_1:
                saveFile(0)
            elif event.key==K_2:
                saveFile(1)
            elif event.key==K_3:
                saveFile(2)
            elif event.key==K_4:
                saveFile(3)
            elif event.key==K_5:
                saveFile(4)
            elif event.key==K_6:
                saveFile(5)

            elif event.key==K_ESCAPE:
                buildList=[]
                windowList=[]
                buildItem=""
            elif event.key==K_p:
                #cash+=1000
                pass
            elif event.key==K_u:
                #influence+=100
                pass
            elif event.key==K_o:
                #showUI=not showUI
                pass
                
        elif event.type==KEYUP:
            if event.key==K_d or event.key==K_RIGHT:
                xChange+=scrollSpeed
            elif event.key==K_a or event.key==K_LEFT:
                xChange-=scrollSpeed
            elif event.key==K_w or event.key==K_UP:
                yChange-=scrollSpeed
            elif event.key==K_s or event.key==K_DOWN:
                yChange+=scrollSpeed
            elif event.key==K_TAB:
                extraInfo=not extraInfo




            
    pygame.display.flip()
    clock.tick(60)


##Add products for factories               DONE
##Add buildable factories to improve goods DONE
##Images for unique factories              DONE
##Give towns population                    DONE
##Town names                               DONE
##Add feed for info                        DONE
##Give towns needs/ limits on deliveries, scores, extra stuff       DONE
##Make towns auto expand to free spaces    DONE
##Added nicer bays                         DONE
##Roads over towns                         DONE
##Fix town growth                          DONE
##Buses between towns                      DONE
##Capacity for bays                        DONE
##Hold down roads                          DONE
##Delete tool                              DONE
##Create variables for many settings/developer tools    DONE
##Lorry menu, shows routes, lets delete, lets go to, cost, scroll    DONE
##Nicer UI                                 DONE
##Add date                                 DONE
##Buildable indusrtries                    DONE
##Add train tax                            DONE
##Add costs for menu bar                   DONE
##Add trains                               DONE
##Added changable speed                    DONE
##Add extra dev stuff                      DONE
##Add image for train cargo                DONE
##Add airoplanes w storage at airport      DONE
##Fix mouse buttons and add scrolling      DONE
##Added several game speeds                DONE
##Added rising text for placed items       DONE
##Make window class-- create list of open windows    DONE
##Add main menu and settings   DONE   
##Add selling costs/ changing market, so what sold most of becomes cheapest   DONE
##Add loans etc      DONE
##Put fps in                              DONE
##Add some sound effects for -Getting Cash -Creating route -Ambient        DONE
##Redid all of the UI into black               DONE
##Added basic rivers                         DONE
##Make when roads or bays are deleted, routes are change/removed  DONE
##Add finances Menu with graphs                          DONE
##Change town growth and respect                        DONE
##Add big patches around grain farm and forestry        DONE
##Add pause                                     DONE
##Fix/sort how buses work                          DONE
##Fix pause when placing vehicles and train cargo   DONE
##Windows for refineries and factories         DONE
##Allow paying of towns                        DONE
##Fast plane glitch                           DONE
##Changed colours of feed                     DONE
##Added saving and loading the game!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DONE
##Lorries either side of road                  DONE
##Faster route menu scroll                      DONE
##Options while in a game                    DONE
##Make number of buses increase                DONE
##Close loaded files
##Added growing windows 
##Made windows clear
##Menu for company, politics, relationships    DONE
##Add influence, depending on how much is delivered     DONE

    

##Surrounding sea/ will fix wierd growth
##Add planes in airports
##Add capacity to refineries?
##Change refinery and factory graphics                   
##Add bridges
##Add capacity variable for vehicles
##Add some more sound effects, for menus
##Allow menus for individual vehicles
##Make airports not delete objects when placed
##Make so bays need to be built on road and lorry comes out
##When airports go or planes, delete
##Change route window so vehicles use same function & add planes
##Let player move w other button
##Add traffic lights and destroying lorries
##Add dark patch to oil wells
##Add laws and restrictions from towns
##More finance info
##Add requests for rewards
##try improve performance of game
##Planning permissions?
##Change airports? 
##Make trains angled
##Add random times when towns pay lots for product
##Add unique company colour
##Add delivered amount to finance menu
##Sort overlapping names
##Highscores
##Make windows move to top
##Advertising?
##Adds speeds of vehicles and info
##Make menu reset data, for new game
##Change menu items select box
##Add crossroads
##2 way trains?
##More settings for new game
##Add sliders and check boxes classes
##Reduce text rendering
##Add all data to one file
##Add taxes to finance menu
##More on main menu


##Add coal and buses to company info









"""
- Random events
- Boats
- Graphs
- Rivals
- Company Settings
- Bridges
- Different pathfinding
- Power Lines, connect to buildings to increase speed
- Upgrades
"""

















    
