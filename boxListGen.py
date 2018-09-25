list_object = open("boxListTxt", 'w')
boxListAr = []
contList = 1
y = True
n = False
def GenList():
    if contList == 1:
        boxLen = int(input("The Box's Length is: "))
        boxWid = int(input("The box's Width is: "))
        boxHei = int(input("The box's Height is: "))
        double = bool(input("Is the box Double Walled?"))
        flat = bool(input("Is the box flat?"))
        retail = float(input("The box price is: "))
        box = {"Name":str(boxLen)+'x'+str(boxWid)+'x'+str(boxHei),"Length":boxLen,"Width":boxWid,"Height":boxHei,"Double":double,"Flat":flat,"Cost":retail}
        boxListAr.append(box)
        # cont = input("Continue?")
# GenList()
while True:
    if contList == False:
        break
    GenList()
    contList = bool(input("Continue?"))

list_object.write(str(boxListAr))
list_object.close