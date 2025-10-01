# -*- coding: utf-8 -*-

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]


class GraduatedColorsRenderer:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "graduatedcolor"
        self.description = "Create a graduated colored map based on a specific attribute of a layer"
        self.canRunInBackground = False
        self.category = "MapTools"

    def getParameterInfo(self):
        """Define the tool parameters."""
        param0 = arcpy.Parameter(
            displayName="Input ArcGIS Pro Project Name",
            name="aprxInputName",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        param1 = arcpy.Parameter(
            displayName="Layer to Classify",
            name="LayerToClassify",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        )
        param2 = arcpy.Parameter(
            displayName="Garage CSV File",
            name="GarageCSVFile",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        param3 = arcpy.Parameter(
            displayName="Output Project Name",
            name="OutputProjectName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        readTime = 3 # time for users to read the progress
        start = 0 # beginning position of the progressor
        map = 100 # end position
        step = 33  # progress interval to move the progressor along

        arcpy.SetProgress("step", "Validating Project File...", start, max, step)
        time.sleep(readTime) # pause the execution for 2.5 seconds

        arcpy.AddMessage("Validating Project File...")

        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText)
        
        campus = project.listMaps('Maps')[0]

        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Finding your map layer...")

        for layer in campus.listLayers():
            if layer.isFeatureLayer:
                symbology = layer.symbology
                if hasattr(symbology, 'renderer'):
                    if layer.name == parameters[1].valueAsText:
                        arcpy.SetProgressorPosition(start + step*2)
                        arcpy.SetProgressorLabel("Calculating and classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and classifying...")

                        symbology.updateRenderer('GraduatedColorsRenderer')
                        symbology.renderer.classificationField = "Shape_Area"
                        symbology.renderer.breakCount = 5
                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]

                        layer.symbology = symbology
                        arcpy.AddMessage("Finish Generating Layer...")
                    else:
                        print("NO layers found")

        arcpy.SetProgressorPosition(start + step*3)
        arcpy.SetProgressorLabel("Saving...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving...")

        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + ".aprx")
        return
