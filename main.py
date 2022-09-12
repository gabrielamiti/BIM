#import
import ifcopenshell
import ifcopenshell.util.element 
from blenderbim.bim.ifc import IfcStore
modelDuplex = IfcStore.get_file()

#import IFC files
windows = (modelDuplex.by_type('IfcWindow'))

#check number of windows 
number_of_windows = len(windows)
print('number of windows', number_of_windows)

#0=first window in the list (ID 6426)

#for every window, ID, height, width and area is found and outputted 
print('calculate all windows')

totalWindowArea = 0
for window in windows:
    #every window with data    
    #each window overall width 
    #print(window.OverallWidth)
    #each window overall height 
    #print(window.OverallHeight)
    windowPropSet = ifcopenshell.util.element.get_psets(window)
    #area for each window
    area = window.OverallHeight*window.OverallWidth
    #print(area)
    #print(windowPropSet)
    print('Window ID: %s, Height: %s m, Width: %s m, Area: %s m2, Sill height: %s m, Level: %s' %(window.id(),window.OverallHeight,window.OverallWidth,area,windowPropSet.get('PSet_Revit_Constraints').get('Sill Height'),windowPropSet.get('PSet_Revit_Constraints').get('Level'))) 
    totalWindowArea = totalWindowArea + area
    
print('Total window area')
print('%s m2' %(totalWindowArea))  
