---
tags:
- diff-eq
- math-82/3
- math-82/4
---

An important class of problems in differential equations is that of equilibrium. We care a lot about where the solution to a differential equation might finally stabilise and what it might stabilise at. Again, an example is the best way to demonstrate why we care about this type of problem.

##### _example:_ drug concentrations

A patient is being administered a certain drug intravenously. The drug is in a fluid at $5 \operatorname{mg}/\operatorname{cm}^3$ concentration, and the fluid enters the bloodstream at the rate $100 \operatorname{cm}^3/\operatorname{hr}$. The drug is also absorbed by the tissues and thus leaves the bloodstream. This happens at a rate proportional to the concentration of the drug (with rate constant $0.4$).

Thus, if $x(t)$ is the amount of the drug in the bloodstream at time $t$, we have a differential equation $x' = 500 - 0.4 x$. We can find the equilibrium value by just solving for $x' = 0$, and thus getting $x_{\text{eq}} = 1250 \operatorname{mg}$, but by solving the differential equation (by the [[Differential equations --- math-82/notes/First order linear differential equations#_proposition, definition _ solving linear differential equations, the integrating factor|integrating factor method]]) to get $x(t) = 1250(1 - e^{-0.4t})$, we can see how fast we approach equilibrium, and even exactly when.

This becomes our motivating example to define equilibrium.

##### _definition:_ equilibrium

We say a differential equation in $y$ is in equilibrium at $x_{0}$ if $y'(x_{0}) = 0$.

---