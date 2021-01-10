Welcome to the Simulation of the Line Hitting Aggregate!

The definition of this process is presented in the master thesis:
Subject:	External DLA
Author: 	Tillmann Bosch
Professor: 	Steffen Winter
University: 	Institute of Technology, Karlsruhe (KIT)
2021

### How to run the simulation ###

You have the option to adjust parameters in parameters.txt:
iterations: 			Here you can adjust how many iterations shall the process run. Each iteration will result in a particle added to the cluster.
				So the particle size of the cluster is equal to iterations + 1 (since the cluster start with one particle in the origin)
color:				It is fixed that the background of the created image is black. After that you can decide whether the particles shall be printed in white, or in colors.
				If you wish to print in white, enter "no".
				If you wish to print in colors, enter "yes".
color_generation_size:		If you choose to print in color, you can specify here, after how many particles the color shall change. Speaking in generations, the first generation will 
				be in one color, the next one in a slight different color, so at the end the cluster appears in a rainbow like coloring giving a hint of in which way
				the generations of particles where added to the cluster. 
image_size_x:			Specify the width of the image. 
image_size_y:			Specity the height of the image. 


You need to have installed Python (3.7.* or higher). You furthermore need to able to run a .sh script. In Windows open Git Bash (or install it if necessary), 
change into the directory of this git repository (GIT_REPO) and run run.sh:

install dependency:
pip install pygame

cd GIT_REPO
./run.sh

HINT: If you have a problem running this, you maybe have to replace "py" with "python" or "python3" in run.sh.

The appearing numbers in the shell let you know about how many iterations are finished already. The print "line missed cluster" indicates that a randomly chosen line 
according to the definitions in the paper missed the cluster and a new line had to be chosen. 

When calculation is over, you can find an image in the images folder.

Have fun!