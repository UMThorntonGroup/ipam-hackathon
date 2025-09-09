#!/usr/bin/env python3# Step 1: Open a database (the whole .vtu time series)
dbname="solution-*.vtu database"
OpenDatabase(dbname)

# Add plots 
# Plot Phi with an isovolume operator for which 
AddPlot("Pseudocolor", "Phi")
AddOperator("Isovolume", 1)
IsovolumeAtts = IsovolumeAttributes()
IsovolumeAtts.lbound = 0.5
IsovolumeAtts.variable = "psi"
SetOperatorOptions(IsovolumeAtts, 0, 1)
DrawPlots()

# Add contour plot for anodic metal interface
AddPlot("Contour", "nAnodic", 1, 0)
ContourAtts = ContourAttributes()
SetActivePlots(1)
ContourAtts = ContourAttributes()
ContourAtts.changedColors = (0)
ContourAtts.colorType = ContourAtts.ColorByMultipleColors  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
ContourAtts.colorTableName = "Default"
ContourAtts.invertColorTable = 0
ContourAtts.legendFlag = 0
ContourAtts.lineWidth = 3
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
ContourAtts.contourNLevels = 10
ContourAtts.contourValue = (0.5)
ContourAtts.SetMultiColor(0, (0, 0, 0, 255))
SetPlotOptions(ContourAtts)

# Add contour plot for Cahodic metal interface
AddPlot("Contour", "nCathodic", 1, 0)
ContourAtts = ContourAttributes()
SetActivePlots(2)
ContourAtts = ContourAttributes()
ContourAtts.changedColors = (0)
ContourAtts.colorType = ContourAtts.ColorByMultipleColors  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
ContourAtts.colorTableName = "Default"
ContourAtts.invertColorTable = 0
ContourAtts.legendFlag = 0
ContourAtts.lineWidth = 3
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
ContourAtts.contourNLevels = 10
ContourAtts.contourValue = (0.5)
ContourAtts.SetMultiColor(0, (0, 0, 0, 255))
SetPlotOptions(ContourAtts)

# Add contour plot for electrolyte interface
AddPlot("Contour", "psi", 1, 0)
ContourAtts = ContourAttributes()
SetActivePlots(3)
ContourAtts = ContourAttributes()
ContourAtts.changedColors = (0)
ContourAtts.colorType = ContourAtts.ColorByMultipleColors  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
ContourAtts.colorTableName = "Default"
ContourAtts.invertColorTable = 0
ContourAtts.legendFlag = 0
ContourAtts.lineWidth = 3
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
ContourAtts.contourNLevels = 10
ContourAtts.contourValue = (0.5)
ContourAtts.SetMultiColor(0, (0, 0, 0, 255))
SetPlotOptions(ContourAtts)

DrawPlots()
