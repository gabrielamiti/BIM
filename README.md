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
Also the knowledge on Daylight and Indoor Climate were used to identify which component are relevant for a  analysis.

### IFC concepts 
Before starting analyzing the use case, the architectural IFC model needs to be done. When this is done, and can be loaded into Blender BIM, the script can be used. 
`IfcWindow` has been used as an IFC concept. 
From the `IfcWindow` object, the two attributes are used, `Overall.Height` and `Overall.Width`. 
The properties from the IfcWindow object are also collected in order to get the `PSet_Revit_Constraints` wherein the `sill height` is located. 
The window `ID` is used, to show which data is connected to the individual window. 

### Further analysis
For further uses, this script can be used as part of bigger analyse, such as energy use calculations, U-values along with checking if the pane area is above 10% of the floor area. 
This can be done, by getting building elements such as windows, walls, floor areas and ligthing fixtures. The source of this data would be the materials, properties and dimensions. These analysis could be relevant for Indoor climate and Daylight engineers. 
When the analysis of the chosen use case are done, other use cases, such as *Architectural* and *Installation* projects can begin. 
