---
tags:
- rudin
- anal
- top
- self-study
---

It's fairly normal for us to think of a notion of distance on a space:

##### _example:_ notions of distance

1) The real numbers $\bb{R}$ with the distance $d$ between $x, y \in \bb{R}$ given by $d(x, y) = \vert x - y \vert.$
2) The complex plane $\bb{C}$ with distance $d$ between $w, z \in \bb{C}$ given by $d(w, z) = \vert w  - z \vert.$
3) The real plane $\bb{R}^2$ with the Pythagorean notion of distance: the distance $d$ between $x = (x_1, x_2), y = (y_1, y_2) \in \bb{R}^2$ is given by $d(x, y) = \Vert x - y \Vert = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}.$ This is the notion of distance used in [[Euclidean space|Euclidean geometry]].
4) The real plane $\bb{R}^2$ with the "taxicab" distance $d$ between $x = (x_1, x_2), y = (y_1, y_2) \in \bb{R}^2$ given by $d(x, y) = \vert x_1 - y_1 \vert + \vert x_2 - y_2 \vert$. This often thought of as the distance you cover when taking a cab in the grid of Manhattan.
 
The big ideas of calculus come from looking at functions on a space very closely. For "looking closely" at a function on a space to make sense, the notion of distance on that space is obviously very useful. While our idea for what that notion should be arises naturally from [[Euclidean space|Euclidean space]], in order to use distance on weirder spaces, first, we need to generally define it.

### What is a metric space?

##### _definition_: metric space, metric

A metric space is a set $X$ (whose elements we call points) with a function, called a metric, $d : X \times X \to \bb{R}_{\ge 0}$, such that
- $d$ is symmetric: for any points $p, q \in X$ we have $d(p, q) = d(q, p)$.
- $d$ is positive definite: $d(p, q) \ge 0$ and $d(p, q) = 0$ if and only if $p = q$.
- $d$ satisfies the triangle inequality: for all $p, q, s \in X$ we have $d(p, q) + d(q, r) = d(p, r)$.
##### _examples:_ metric spaces

1) All of the examples of "notions of distance" above are examples of metric spaces with the metric given by the "distance function".
2) The unit disc in $\bb{R}^2$ with the same metric as $\bb{R}^2$.
3) The interval $[0, 1]$ in $\bb{R}$ with the same metric as $\bb{R}$.
4) Given any metric space $X$ with metric $d$, any subset $E \subset X$ with the same metric $d$ is a metric space.
5) The unit circle $S^1$ with the distance between any two points given by the minimum arc length between them is a metric space.
6) The discrete space is, for any set $X$ the metric space obtained by applying the metric $$ d(p, q) = \begin{cases} 1 & \text{if } p \neq q \\  0 & \text{if } p = q.\end{cases}$$
7) The set vertices, $S$ of any [[Basic graph theory#_definition _ connected|simple connected graph]] $G$ can be a metric space with the metric as the graph theoretic distance between two vertices. We get the discrete space on $S$ if $G$ is the complete graph on $S$.
8) Any [[Norms|normed vector space]] is a metric space with the metric $d$ given by $d(u, v) = \Vert u - v \Vert$.

### Special subsets of metric spaces

##### _notation_: $X$

For this section, $X$ denotes a metric space with metric $d$, and any points or subsets we mention are considered to be elements or subsets of $X$.

A natural idea that comes from thinking about closeness and metric spaces is that of a neighbourhood: all the points that are in some sense close to a point. Specifically,

##### _definition:_ r-neighbourhood, radius, $N_r(p)$

The $r$-neighbourhood of some point $p$ is the set of all points within distance $r$ of $p$. That is, the $r$-neighbourhood of $p$, denoted $N_r(p)$ is given by
$$
N_r(p) = \{ q \in X : d(p, q) < r\}.
$$
We say that the $r$-neighbourhood $N_r(p)$ has radius $r$. When we don't need to make explicit the difference between metric topology and topology, we just abbreviate $r$-neighbourhood to neighbourhood

Recall the idea of open and closed intervals of $\bb{R}$:

##### _definition:_ open interval, $[a, b]$

By the closed interval $[a, b]$  we mean the set
$$
\{ x \in \bb{R} : a < x < b \}
$$
##### _definition:_ closed interval, $[a, b]$

By the closed interval $[a, b]$  we mean the set
$$
\{ x \in \bb{R} : a \le x \le b \}
$$

These motivate thinking about closed and open sets, and various other notions from $\bb{R}$ in $X$.

It's easy to think about what open sets in $X$ should be: we think of open intervals in $\bb{R}$ as sets in which we can always move a little closer to leaving the set, and still not leave the set. In $X$ we create the same intuition using neighbourhoods and open sets.

##### _definition:_ interior point

A point $p$ is an interior point of a subset $E$ if if there is a neighbourhood of $p$ contained in $E$: that is, if we have some $N_r(p) \subseteq E$.

##### _definition:_ open set

A subset $E$ is said to be an open set in $X$ if every point of $E$ is an interior point of $E$.

Thinking about closed sets in $X$ requires some more effort. We have to think about closed and open balls in $\bb{R}^n$ to motivate the definition. 

##### _definition:_ open ball

By the open ball of radius $r$, centered at $p \in \bb{R}^n$ we mean the set
$$
\{ x \in \bb{R}^n : d(p, x) = \Vert x - p \Vert < r \}
$$

##### _definition:_ closed ball

By the closed ball of radius $r$, centered at $p \in \bb{R}^n$ we mean the set
$$
\{ x \in \bb{R}^n : d(p, x) = \Vert x - p \Vert \le r \}
$$

These definitions make its somewhat more clear that a closed set is one that includes all the points that get infinitely close to it: any point that always has points of the closed ball in some neighbourhood of it will have to be in the closed ball, but a point on the sphere at the boundary of the open ball contains points of the ball at every distance, and yet is not a part of it.

##### _definition:_ limit point

A point $p$ is said to be a limit point of a subset $E$, in $X$, if every neighbourhood of $p$ contains a distinct point of $E$. That is, $p$ is a limit point if for every $r > 0$ we have some $q \in N_r(p)$ with $q \neq p$.

##### _definition:_ closed set

A subset $E$ is a closed set in $X$ if it contains all of its limit points in $X$.

Note that when we talk about limit points, open sets, and closed sets, we always mention their properties in the context of $X$. This is because these depend on the choice of metric and the set on which the metric is applied.

We also give a name to points that are not limit points

##### _definition:_ isolated point

An isolated point of a subset $E$ is a point in $E$ that is not a limit point of $E$.

##### _definition:_ perfect set

A subset $E$ is perfect in $X$ if it is closed and has no isolated points.

Some more obvious concepts that carry over from $\bb{R}$ and $\bb{R}^n$ to $X$ naturally are complements, boundedness, and denseness.

Complements are natural to think about when considering any set. For metric spaces, we think of the metric space as the 'universe', and we talk about the complement of its subsets.

##### _definition:_ complement, $E^c$

The complement of a subset $E$, denoted $E^c$ is the set of all points in $X$ that are not in $E$: $X \setminus E$.

Boundedness also has some natural intuition attached to it. In $\bb{R}$ we think of bounded sets as existing within some interval, in $\bb{R}^2$, within some disc, and in $\bb{R}^3$, within some ball. The obvious definition that arises for bounded subsets of metric spaces then is to try to include the subset at some ball centred at a point in the subset.

##### _definition:_ bounded

A subset $E$ is bounded in $X$ if for some point $p$ we have $d(p, q) < M$ for all points $q \in E$ where $M$ is some fixed real number.

The prototypical example of a dense set is $\bb{Q}$ in $\bb{R}$. Typically we think of there being a [[Real numbers|rational between any two real numbers]], but we can reframe this: given a real number, and any small neighbourhood around it, we can find a rational number in that neighbourhood. That is, every real number is a limit point of the rational numbers.

##### _definition:_ dense

A subset $E$ is dense in $X$ if every point $p$ is a limit point of $E$ or is in $E$.

These definitions lead to some fairly obvious theorems, and later, some non-obvious theorems.

##### _proposition:_ Every neighbourhood is open

For any point $p$ and radius $r > 0$, the neighbourhood $N_r(p)$ is an open set

###### _proof:_

For any point $q$ in the neighbourhood $N_r(p)$, we can construct a neighbourhood of $q$ within $N_r(p)$ by choosing its radius so that it doesn't extend outside of the space. 

Specifically, consider $\rho = r - d(p, q)$, and the neighbourhood of $q$, $N_{\rho}(q)$. It is trivial to show that $N_{\rho}(q) \subset N_r(p)$.

Any point $s$ in $N_{\rho}(q)$ must have $d(s, t) < \rho$. Then by the triangle inequality, we have 
$$
d(p, s) < d(p, q) + d(q, s) < d(p, q) + r - d(p, q) = r
$$
That is, $d(p, s) < r$, giving us $s \in N_r(p)$ for any arbitrary $s \in N_{\rho}(q)$. This in turn gives us $N_{\rho}(q) \subset N_r(p)$ for any arbirtary $q \in N_r(p)$, and thus for every point in $N_r(p)$. Thus, every point in $N_r(p)$ is an interior point: $N_r(p)$ is open. 

##### _proposition:_ Every limit point is approached by infinitely many points

If $p$ is a limit point of a subset $E$, then every neighbourhood of $p$ contains infinitely many points of $E$.

###### _proof:_

We can prove this theorem by its contrapositive: if some neighbourhood of $p$ contains finitely many points of $E$, then $p$ is not a limit point of $E$.

Suppose $N_r(p)$ contains finitely many distinct points of $E$ for some radius $r$: 
$$
N_r(p) \cap E \setminus \{ p \} = \{q_1, \ldots q_m\}
$$
Let
$$
I = N_r(p) \cap E \setminus \{ p \} 
$$

Obviously, if $I$ is empty, then by definition $p$ is not a limit point. Thus, we only have to consider non-empty $I$.

Since $I$ is non-empty and finite, so is the set of distances of points in $I$ from $p$. This gives us a well-defined, and positive 
$$
\rho = \min_{i \in \bb{N}_m} d(p, q_i)
$$

We can then look at $N_\rho(p)$, which is just small enough that no points of $E$ are in it. This is true because any point in $I$ has distance from $p$ greater than or equal to $\rho$. $N_\rho(p)$ contains no other points of $E$ because it is a subset of $N_r(p)$ ($r < d(p, q_i) < \rho$).

Thus, we have a neighbourhood of $p$ containing no distinct points of $E$, giving us the contrapositive, and thus, the theorem.

##### _corollary:_ A finite set has no limit points

##### _examples:_ closed, open, perfect, and bounded sets

The following are subsets of the [[Euclidean space|Euclidean space]] $\bb{R}^2$. Note that since they have effectively the same metric, we can also think of these sets as subsets of the [[Complex plane|complex plane]] $\bb{C}$. They are variously closed, open, perfect, and bounded as below.

Set | Closed? | Open? | Perfect? | Bounded?
--|---|--|--|--
The unit open disk: $\set{ x \in \bb{R}^2 : \Vert x \Vert < 1}$ | No, the points of the unit circle are limit points that are not in the set. | Yes, since it's a neighbourhood of $(0, 0)$. | No, we already showed it's not closed. | Yes, by a distance $1$ from $(0, 0)$.
The unit closed disk: $\set{ x \in \bb{R}^2 : \Vert x \Vert < 1}$ | Yes because we can draw a neighbourhood with no points in the disk around any point not in the disk. | No, since any neighbourhood of the points on the unit circle will not be contained in the disk. | Yes. It's closed, for all the points in the open disk subset, their neighbourhoods are all contained in the set (and are obviously non-empty in the desired way), and for all the points on the unit circle, every neighbourhood must contain some distinct point in the disk (at least some distinct point on the unit circle). | Yes, by a distance $1.1$ from $(0, 0)$.
A non-empty finite set | Yes. Since there are no limit points, they are all vacuously in the set. | No (note that this is especially specific to $\bb{R}^2$). If there is a finite set, for any point there is a closest distinct point to it, and a neighbourhood smaller than the distance to that point will not be contained in the set. | No: since there are no limit points, the non-zero number of points in the set cannot be limit points.  | Yes. Pick any point and the maximum distance of a distinct point from it.
The set of all integers $\bb{Z}$ | Yes. The integers also have no limit points: for any limit point candidate, just pick a neighbourhood of radius less than the distance to the nearest integer. | No, for any point in the integers, a neighbourhood of radius less than $1$ is not contained in the integers. | No: again, $\bb{Z}$ is nonempty and has no limit points. | No, by the Archimidean property. 
The harmonic numbers: $\set{(1/n, 0) \in \bb{R}^2 : n \in \bb{N}}$ | No: by the Archimedean property, the harmonic numbers have limit point $0$ which isn't a harmonic number. | No: the neighbourhood $(1/2, 3/2)$ around $1$ is not contained in the harmonic numbers (and so are many similar neighbourhoods excluded). | No, we already showed that the harmonic numbers aren't closed. | Yes, by a distance of $1$ from $(0, 0)$.
$\bb{R}^2$ itself | Yes. Every limit point of $\bb{R}^2$ in $\bb{R}^2$ is by definition, in $\bb{R}^2$. | Yes. Any neighbourhood in $\bb{R}^2$ of a point of $\bb{R}^2$ is again, by definition, contained in $\bb{R}^2$. | Yes, any neighbourhood of any point in $\bb{R}^2$ contains distinct points of $\bb{R}^2$. We can use the Archimedean property to show this.| No, we can go infinitely far, from every point, in every direction.
The segment $(a, b)$, or more specifically, $\set{(x, 0) : x \in (a, b)}$ | No, $a$ and $b$ are excluded limit points. | No, in $\bb{R}^2$, any neighbourhood of a point in $(a, b)$ extends outside of the segment in the second dimension. | No, we already showed it is not closed. | Yes, by a distance $\vert a - b \vert$ from $a$ or $b$.

Note that if we consider $(a, b)$ in $\bb{R}$ instead of $\bb{R}^2$, neighbourhoods don't stretch out into any second dimension and for every point, there is a neighourhood contained inside the segment, making it an open set.