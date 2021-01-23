Welcome to the Simulation of the Line Hitting Aggregate and External DLA!

### MASTER THESIS ### 
Subject:	External DLA
Author: 	Tillmann Tristan Bosch
Professor: 	Steffen Winter
University: 	Institute of Technology, Karlsruhe (KIT)
2021

### HOW TO RUN THE SIMULATION ###


## SET PARAMETERS ##

open parameters.txt and enter values there. 

aggregate:			Enter "lha" to simulate the line hitting aggregate
				Enter "dla" to simulate external dla

cluster_size: 			Enter an integer to specify how big the cluster shall get. At the end the cluster will contain exactly cluster_size points. 

background_color:		Enter a color in HEX representation as a string
				Examples: 
				"ffffff" (white)
				"000000" (black)

particle_color:			Enter a list of colors in HEX representation as strings. If you enter more than one color into the list, with the next parameter
				color_generation_size you can specify after how many iterations the next color shall be used to render the particles. This will 
				create a color layering on the particles and gives an insight of in which order the particles where added to the cluster. 
				Examples: 
				["ffffff"] (single color white)
				["000000"] (single color black)
				["2b1c8f", "cc0000"] (double color)
				["ffff00", "ff8000", "ff0000", "ff0080", "ff00ff", "8000ff", "0000ff", "0080ff", "00ffff", "00ff80", "00ff00", "80ff00"] (rainbow palette)

color_generation_size:		Enter an integer which specifies after how many iterations the color of particles shall change. 
				This wont have any effect if you choose "single" in the particle_color_mode. 

image_size_x:			Enter an integer to specify the pixel width of the image. 

image_size_y:			Enter an integer to specity the pixel height of the image. 


## INSTALL DEPENDENCIES AND RUN ##

You need to have Python (3.7.* or higher) installed. You furthermore need to be able to run a shell script. Open a shell like git-bash and execute the following: 

#Change to the directory of this repo:
cd repo-directory

#install dependencies
pip install -r requirements.txt

#run script
bash run.sh (or just ./run.sh)
HINT: If you have a problem running this, you maybe have to replace "py" with "python" or "python3" in run.sh.


## OUTPUT ##

The appearing numbers in the shell let you know about how many iterations are finished already. In the simulation of "lha" the print "line missed cluster" indicates 
that a randomly chosen line according to the definitions in the paper missed the cluster and a new line had to be chosen. 

When calculation is over, you can find an image, a json file about the calculated fractal dimensions and a json file containing the parameters in the exports folder.
The created filenames will have the following format:
{CURRENT SYSTEM TIME}__{FILE INFORMATION}__{LHA OR DLA}__{CLUSTER SIZE}__{COLOR GENERATION SIZE}.{PNG OR JSON}
Example:
Fri Jan 22 16_56_35 2021__image__lha__5000__200.png
Fri Jan 22 16_56_35 2021__fractalinfo__lha__5000__200.json
Fri Jan 22 16_56_35 2021__parameters__lha__5000__200.json
These three files where created at Fri Jan 22 16_56_35 2021 after a simulation of lha using 5000 cluster points with a color generation size of 200. 

During the process in each step the "current fractal dimension" is calculated by ln(n)/ln(radius of the cluster at time n) and saved in a list 
(compare with the definition in the paper). After the process we therefore have list of all calculated fractal dimensions of which the last value comes 
most close to the definition as in the definition a limit is taken (fractal_dimension = liminf_{n to infinity} ln(n)/ln(radius of the cluster at time n)).
The fractal information json file will contain the calculated fractal dimension values. You will find this format:

last_value: 			Last value of the calculated fractal dimension list.

every_1000th_value_average:	average of all fractal dimension values which have an index in the list which is zero modulo 1000

all_average:			average of all values in the list

every_1000th_value:		list of all fractal dimension values which have an index in the list which is zero modulo 1000

all_values:			the original list of all calculated fractal dimension values


## Enjoy the beautiful pictures and have fun! ## 