# Simulation Boolesches Modell 

# Pakte zum Zeichnen von Kreisen
library("plotrix")

# Euklidische Norm
ENorm = function(x){sqrt(sum(x^2))}

# Koerner: Kreise mit zufaelligen Radien

# Intensitaet Poisson-Prozess
int = 20

# Simmuliere Punkte in [-1,2]^2. Beobachtungsfenster: [0,1]^2

# Anzahl der Punkte
n = rpois(1, 9*int)

# Positionen der Punkte
P = matrix(0, ncol=n, nrow=2)
P[1,] = runif(n, -1, 2)
P[2,] = runif(n, -1, 2)

# Simmuliere Radien
# (Hier koennen unterschiedliche Verteilungen gewaehlt werden)
r = runif(n, 0.05, 0.15)
# r = abs(rnorm(n, 0, 0.1))

# Plotten der Keime und Koerner
plot(10,10,xlim=c(0,1),ylim=c(0,1),asp=1,xlab="",ylab="")

# Plotte das Innere der Kreise
for(i in 1:n){
  draw.circle(x=P[1,i], y=P[2,i], radius=r[i], nv=200, col="lightblue", border="lightblue")
}

# Plotte den Rand der Kreise
for(i in 1:n){
draw.circle(x=P[1,i], y=P[2,i], radius=r[i], nv=200)
}

# Plotte Punkte
points(x=P[1,], y=P[2,], pch=16)




