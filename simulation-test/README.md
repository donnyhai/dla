Welcome to the Simulation of the Line Hitting Aggregate and External DLA!

### MASTER THESIS ### 
Subject:	External DLA
Author: 	Tillmann Tristan Bosch
Professor: 	Steffen Winter
University: 	Institute of Technology, Karlsruhe (KIT)
2021

### HOW TO RUN THE SIMULATION ###


# SET PARAMETERS #

open parameters.txt and enter values there. 

aggregate:			Enter "lha" to simulate the line hitting aggregate
				Enter "dla" to simulate external dla

cluster_size: 			Enter an integer to specify how big the cluster shall get. At the end the cluster will contain exactly cluster_size points. 

background_color:		Enter a color in HEX representation as a string
				Examples: 
				"FFFFFF" (white)
				"000000" (black)

particle_color:			Enter a list of colors in HEX representation as strings. If you enter more than one color into the list, with the next parameter
				color_generation_size you can specify after how many iterations the next color shall be used to render the particles. This will 
				create a color layering on the particles and gives an insight of in which order the particles where added to the cluster. 
				Examples: 
				["FFFFFF"] (single color white)
				["000000"] (single color black)
				["", ""] (double color)
				[] (rainbow palette)

color_generation_size:		Enter an integer which specifies after how many iterations the color of particles shall change. 
				This wont have any effect if you choose "single" in the particle_color_mode. 

image_size_x:			Enter an integer to specify the width of the image. 

image_size_y:			Enter an integer to specity the height of the image. 


# INSTALL DEPENDENCIES AND RUN #

You need to have Python (3.7.* or higher) installed. You furthermore need to be able to run a .sh script. In Windows open Git Bash (or install it if necessary), 
change into the directory of this git repository (GIT_REPO) and run run.sh:

install dependency:
pip install pygame

cd GIT_REPO
./run.sh

HINT: If you have a problem running this, you maybe have to replace "py" with "python" or "python3" in run.sh.

The appearing numbers in the shell let you know about how many iterations are finished already. In the simulation of "lha" the print "line missed cluster" indicates 
that a randomly chosen line according to the definitions in the paper missed the cluster and a new line had to be chosen. 

When calculation is over, you can find an image and text file about the calculated fractal dimensions in the images folder.
The created files names will have the following format:
{CURRENT SYSTEM TIME}__{IMAGE OR FRACTAL INFORMATION}__{LHA OR DLA}__{CLUSTER SIZE}__{COLOR GENERATION SIZE}.{PNG OR TXT}
Example:
Fri Jan 22 16_56_35 2021__image__lha__5000__200.png
Fri Jan 22 16_56_35 2021__fractalinfo__lha__5000__200.txt
These two files where created at Fri Jan 22 16_56_35 2021 after a simulation of lha using 5000 cluster points with a color generation size of 200. 

The fractal information txt file will contain the calculated fractal dimension values during the process.
CONTINUE

Have fun!