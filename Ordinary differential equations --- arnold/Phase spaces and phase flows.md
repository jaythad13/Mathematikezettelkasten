---
tags:
- self-study
- diff-eq
---

Instead of first defining phase spaces and phase flows mathematically, there is a good example of how they are very useful that doesn't require any knowledge of differential equations.

##### _problem:_ the space between roads

Two non-intersecting roads lead connect city A to city B. If two cars connected by a rope of length $2l$ can travel along the different roads from $A$ to $B$ without the rope ever snapping, can do circular wagons of radius $l$ (whose centres travel along the roads) travel in opposite directions without ever colliding?

##### _solution:_

Consider the phase space that assigns to each vehicle the fraction of its distance from city A (relative to the total length of the road). This is just $M = [0, 1] \times [0, 1]$.

Specifically, if car $c_1$ moves along road $1$, car $c_2$ moves along road $2$, then we can represent the way that $c_1$ and $c_2$ move (specifically to avoid breaking the rope) by a continuous curve in $M$ from $(0, 0)$ to $(1, 1)$ (since they travel smoothly, start in city A, and end in city B). Note that at any point on their path, the distance between the cars (or any two particles on the road) will be less than $2l$.

Similarly, for the wagons, we can describe the way they move by a smooth curve from $(1, 0)$ to $(0, 1)$ (or the other way round, without loss of generality). But this curve must intersect the curve for $c_1$ and $c_2$. Thus, at some point the distance between the centres of the wagons must be less than $2l$, and at that point, they collide.