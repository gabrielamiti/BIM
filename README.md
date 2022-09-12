# Assignment 1 
## Markdown file 
#### Group 6 
##### Gabriela Miti Tsuge Costa (s220075)
##### Kirstine Mia Odgaard (s193464)

### Use case
The chosen use case is *Indoor and energy* and *Daylight*. For these use cases the script tries to identify the window height, width area and sill height for each window, and a calculation of the total window area. The script is written in Python, to be run in Blender console, where an IFC model is loaded, using [Blender BIM](https://blenderbim.org/)

### How the script addresses the problem 
Firstly, the IFC open shell file is imported, along with Blender BIM to the script. IfcOpenShell.util.element is also imported, to get the sill height of the windows. 

The windows are found by identifying the windows type, called IfcWindow. 
The number of windows is found by finding a length of the window list. The number of windows is hereby counted. In the example IFC file are there 24 windows, starting from 0 to 23. 
 
Next, the window ID, height, width, area, and sill height is found for each window. 
Instead of finding this data 24 times, a loop is used. For each window of the found windows, the window height, width is found, and from that the area is calculated. `ifcopenshell.util.element.get_psets(window)` is used to get more properties of the window. A part of that data is the sill height. Then the user of the program is informed about this data. The text is outputted by using string concatenation, to mix text and variables.  
Inside the loop each area is summed and added to the variable that holds the total window area.

### Non BIM expertise 
By using the mathematical formula, `A=h*w` , the area is found. 
An excel sheet with all information from the IFC file is used, to check if the data from the script is correct. 

### IFC concepts 
`IfcWindow` has been used as an IFC concept. 
From the `IfcWindow` object, the two attributes are used, `Overall.Height` and `Overall.Width`. 
The properties from the IfcWindow object are also collected in order to get the `PSet_Revit_Constraints` wherein the `sill height` is located. 
The window `ID` is used, to show which data is connected to the individual window. 
