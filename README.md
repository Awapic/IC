# IC 
IC is part of AwaP-IC - a QGIS tool that calculates the Area-weighted average Perimeter (AwaP) and Interface Catchment (IC), two measures developed by Pafka & Dovey (2017), that combined, capture the capacities of urban morphologies to enable and attract pedestrian movement. While AwaP and IC should be considered together in the analysis of walkable access, in this 1.0 version of the AwaP-IC software the two measures are provided by distinct plugins. 

IC calculates the total length of public/private interfaces reachable from a starting point and within a given walking distance. IC is relevant for walking as most urban attractions, such as dwellings, shops and workplaces, are accessed through the public/private interface, where buildings meet the street. High IC values indicate high capacity for accommodating urban attractions. Together, these two measures account for both street width and block size, measuring both walkable access and what one gets access to.

[AwaP](https://github.com/Awapic/AwaP) is a measure of urban permeability, that calculates the average perimeter of urban blocks within a study area, weighing the perimeter of each block by its area. This way the impact of a large block will be proportional with the share of the study area it occupies, and its effect as a major-barrier to movement is not lost in the average. The lower the AwaP, the easier is to walk through the urban fabric. An AwaP of 400m corresponds to a square block of 100x100m, often taken as the maximum block-length that still allows good permeability.

## Base requirements
The base requirement for the calculation of these measures is a layer of urban blocks drawn as polygons, or closed polylines. Lines within the blocks, such as lot subdivisions, will be ignored. However other errors in the urban blocks layer may not be recognised by the software, and may lead to errors, or long processing times. As both AwaP and IC are calculated in metres, a projected coordinate system should be used in the QGIS project. Instead of the very common WGS84 - EPSG:4326 which uses degrees as a unit for distance, the projected WGS84/Pseudo-Mercator - EPSG:3857 which measures distances in metres may be used.

# IC tool

Interface catchment (IC) is a measure of the total length of public-private interfaces within a given walking distance (Pafka and Dovey 2017). The difference between IC and other catchment metrics is that it also accounts for the street width. IC looks at which edges of urban blocks may be accessed from a given starting point within a maximum walking distance. The assumption here is that a person is able to walk through any open space that is not occupied by urban blocks.

The IC tool requires the following parameters to be set (Figure 1):
- *Blocks layer* - A layer containing the urban blocks for which the IC will be calculated. This layer can have polygon geometries, or linear geometries where outlines of urban blocks are represented as closed polylines.
- *Dead-end removal* - A parameter that specifies if the dead-end streets should be removed from blocks prior to calculating IC, and the maximum width of the dead-end streets to be removed. Per default this option is disabled, as IC is meant to measure all attractions within walking distance, including attractions located in dead-ends. For an explanation of the dead-end removal process see Section “dead-end removal” above.
- *Starting point* - A starting point from which the IC calculation will commence is required. This starting point can be set in one of three ways:
   - *By selecting the starting point layer* - Take into consideration the fact that there must be only one starting point defined at a time. If the starting point layer has multiple point objects, a single point which is to be set as a starting point of IC calculation needs to be selected with a selection tool in QGIS.
   - *By selecting a point on the map* - When the ‘SELECT’ button is clicked, the IC tool interface will temporarily disappear from the screen and wait for the user to click on the map. The map coordinates of the point where the user has clicked will be set as the starting point.
   - *By defining the point coordinates* - Whenever the starting point is set via one of the previously mentioned options, its coordinates will be shown in the starting point coordinates X and Y fields. However, these coordinates can be also edited directly.

  Regardless of which option has been used for selecting the starting point, when the plugin is run, the current coordinates present in these fields will be used to define the starting point for IC calculation.
- *Maximum walking distance* - The distance a pedestrian can walk in the IC calculation. The default value is 400 metres, frequently used in urban planning as average walking distance.

![IC GUI](./figures/IC-gui.png)

Figure 1: IC plugin interface

#### Reference:
Pafka E & Dovey K. (2017) [Permeability and Interface Catchment: Measuring and Mapping Walkable Access](https://www.researchgate.net/publication/306087166_Permeability_and_interface_catchment_measuring_and_mapping_walkable_access). Journal of Urbanism 10(2): 150-162.

#### Acknowledgement:
The development of this software has been supported by a seed grant provided by the [Transport, Health and Urban Design (THUD)](https://thud.msd.unimelb.edu.au/home) Research Hub of the Melbourne School of Design.
