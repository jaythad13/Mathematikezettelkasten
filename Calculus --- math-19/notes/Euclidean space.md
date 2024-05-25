---
tag:
- math-19
- calc
- lin-alg
lecture: math-19-1
---

The geometry that we are used to is Euclidean space, so much so that we don't really think of any other geometry existing. The good news is that for this course we don't need to think about any other geometry existing either. The bad news is that we aren't really used to Euclidean space in general so much as one particular Euclidean space - $\bb{R}^3$. 

To get used to thinking about Euclidean space in general, lets look at some examples
##### _examples:_ Euclidean spaces

1) The real numbers $\bb{R}$ (with the distance $d$ between $x, y \in \bb{R}$ given by $d(x, y) = \vert x - y \vert$ ) give us the geometry of the real number line. It is a Euclidean space.
2) The complex plane $\bb{C}$ (the complex numbers (with distance $d$ between $x, y \in \bb{C}$ given by $d(x, y) = \vert x - y \vert$) gives us a plane with the same notion of distance and geometry that we're used to. It too is a Euclidean plane.
3) The real plane $\bb{R}^2$ is the prototypical example of a Euclidean geometry - it is the example that Euclid himself studied. It encodes the usual notion of distance that we think about - distance along a flat plane that we get by using Pythagoras' theorem.
4) Real space $\bb{R}^3$ models (only sort of) the space that we live in. At normal speeds, and when we're not thinking too hard about physics, our world feels like a flat and reasonable place where distance doesn't change depending on who's looking at it. This apparent niceness is what motivates thinking about $\bb{R}^3$ at all. Again, we get distance by using Pythagoras' theorem. This time we have to apply it twice.

Note that in all of these examples we specified a notion of distance. Also, in all of these examples, there is the more subtle point that we have the notion of adding and points in Euclidean space. The notion of a geometric space, or a space at all is not encapsulated by the set of things it contains - it requires additional structure. To do the combination of geometry and analysis that we want to do, that additional structure is a [[Metric spaces|metric]] given by the [[Norms|norm]] on a [[Vector spaces|vector space]]. This motivates our definition of Euclidean space.

##### _definition:_ Euclidean spaces

Euclidean spaces are the [[Prototypical vector spaces|real and complex vector spaces]] $\bb{R}^n$ and $\bb{C}^n$ with [[Inner product spaces|inner product]] given by 
$$
\langle (u_1 \ldots u_n), (v_1, \ldots v_n) \rangle = u_1 \overline{v_1} + \ldots + u_1 \overline{v_n},
$$and the induced norm and metric.