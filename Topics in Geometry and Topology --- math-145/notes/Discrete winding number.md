---
tags:
- alg-top
- top
- math-145/1
---

A winding number tells you how much a (closed, oriented) curve in the plane winds (counter-clockwise) around a particular point. One way to define it is [[Complex Analysis --- math-135/notes/The argument principle and winding number#_definition _ winding number|by complex analysis]]. We want something topological. A first step is to define it for curves that look piecewise linear.

### Angles in the plane

We can't pick the angle of a point/vector in the plane uniquely, so we define it as the equivalence class of angles. In particular,

##### _definition:_ argument

The argument of $\mathbf{v} = (v_{1}, v_{2}) \in \mathbb{R}^2 \setminus \{ 0 \}$, is $\operatorname{arg} \mathbf{v}$, the equivalence class of all real $\theta$ such that $\lVert \mathbf{v} \rVert e^{i \theta}z = v_{1} + i v_{2}$ in the [[Abstract Algebra I --- math-171/notes/Fibres and quotients#_definition, theorem _ the quotient group is a group|quotient group]] $\mathbb{R} / 2 \pi \mathbb{Z}$.

This isn't satisfactory, because we want a real-valued angle function. We can do this by picking a representative of each equivalence class in a sensible way. In particular, we define $\overline{\operatorname{arg}}_{\phi}$ to be the function that picks the representative of $\operatorname{arg}$ that is $[\phi, \phi + 2 \pi)$.

Now we can define the ray of all vectors with angle $\phi$, the "death ray" at which $\overline{\operatorname{arg}}_{\phi}$ is discontinuous. Around it, the angle seems to jump from close to $\phi$ to close to $\phi + 2 \pi$.

##### _definition:_ ray at angle $\phi$

The ray at angle $\phi$ is
$$
R_{\phi}  =\{ \mathbf{v} \in \mathbb{R}^{2} \setminus \{ 0 \} \mid \operatorname{arg} (\mathbf{v}) = [\phi] \} \cup \{ 0 \}.
$$

We can use all of this to define the angle subtended by a line segment.

##### _definition:_ line segment, support of a line segment

For $\mathbf{a}, \mathbf{b} \in \mathbb{R}^2$, the line segment from $\mathbf{a}$ to $\mathbf{b}$ is, $\overline{\mathbf{a}, \mathbf{b}}$ the subset $\{ \mathbf{u} + t(\mathbf{b} - \mathbf{a}) \in \mathbb{R}^2 \mid t \in [0, 1] \} \subset \mathbb{R}^2$ and the information of which one comes first.

The set is the support of the line segment from $\mathbf{a}$ to $\mathbf{b}$.

##### _definition:_ angle cocycle

Let $\mathbf{a}, \mathbf{b} \in \mathbb{R}^2$ be such that the line segment from $\mathbf{a}$ to $\mathbf{b}$ does not cross the origin ($0$ is not in its support). It follows that $\operatorname{arg}(\mathbf{b}) - \operatorname{arg}(\mathbf{a}) \neq \pi + 2 \pi \mathbb{Z}$.

The angle subtended by the line segment $\overline{\mathbf{a},\mathbf{b}}$ is $\theta(\overline{\mathbf{a}, \mathbf{b}}, 0)$ the unique $\theta \in (-\pi, \pi)$ such that $\operatorname{arg}(\mathbf{b}) - \operatorname{arg}(\mathbf{a}) = \theta + 2 \pi \mathbb{Z}$.

The angle cocycle is the function that $\overline{\mathbf{a}, \mathbf{b}} \mapsto \theta(\overline{\mathbf{a}, \mathbf{b}}, 0)$.

More generally, we can define the angle subtended by a line segment at any point $x = \mathbf{x}$ not in its support as
$$
\theta(\overline{\mathbf{a}, \mathbf{b}}, x) = \theta(\overline{\mathbf{a} - \mathbf{x}, \mathbf{b} - \mathbf{x}}, 0).
$$

Note that the function $x \mapsto \theta(\overline{\mathbf{a}, \mathbf{b}}, x)$ is continuous, because choosing $x \not\in \operatorname{supp} \overline{\mathbf{a}, \mathbf{b}}$ is like cutting out rays of death from the plane. In fact, thinking of everything as complex numbers, we find that $w = (b - x) / (a - x)$ is never on the ray $R_{- \pi}$ and it turns out that $\theta(\overline{\mathbf{a}, \mathbf{b}}, x) = \overline{\operatorname{arg}}_{- \pi}(\mathbf{w})$.

### Discrete winding number

The discrete winding number is the winding number for things that are piecewise linear.

We can glue line segments together to form a polygon!

##### _definition:_ (directed) polygon

Given $\mathbf{a}_{0}, \mathbf{a}_{1}, \dots, \mathbf{a}_{n} \in \mathbb{R}^2$, the (directed) polygon $P(\mathbf{a}_{0}, \mathbf{a}_{1}, \dots, \mathbf{a}_{n})$ is the data of all of the lines $\overline{\mathbf{a}_{0}, \mathbf{a}_{1}}, \dots, \overline{\mathbf{a}_{n - 1}, \mathbf{a}_{n}}$. The polygon is closed if $\mathbf{a}_{0} = \mathbf{a}_{n}$.

The support of $P(\mathbf{a}_{0}, \mathbf{a}_{1}, \dots, \mathbf{a}_{n})$ is the union of all of the supports of its edges.

We will sometimes write
$$
P(\mathbf{a}_{0}, \mathbf{a}_{1}, \dots, \mathbf{a}_{n}) = \overline{\mathbf{a}_{0}, \mathbf{a}_{1}} + \dots + \overline{\mathbf{a}_{n - 1}, \mathbf{a}_{n}} = \sum_{i = 1}^n \overline{\mathbf{a}_{i - 1}, \mathbf{a}_{i}}
$$
to emphasise that the order of the edges doesn't matter.

##### _definition:_ winding number (of a polygon)

Let $\gamma = P(\mathbf{a}_{0}, \mathbf{a}_{1}, \dots, \mathbf{a}_{n})$ be a (directed polygon) and $x \in \mathbb{R}^2 \setminus \operatorname{supp} \gamma$. Then the winding number of $\gamma$ around $x$ is
$$
w(\gamma, x) = \frac{1}{2 \pi} \sum_{i = 1}^n \theta(\overline{\mathbf{a}_{i - 1}, \mathbf{a}_{i}}, x).
$$

This formula motivates the sum notation for polygons — $w$ is some sort of additive function that converts addition of lines into addition of angles since the winding number of a line is just its angle cocycle.

##### _theorem:_ winding number 

Let $\gamma$ be a closed directed polygon $P(\mathbf{a}_{0}, \mathbf{a}_{1}, \dots, \mathbf{a}_{n})$ and $x$ be a point outside its support. Then the discrete winding number is its support $w(\gamma, x)$.

###### _proof:_

Choose arbitrary representatives $\phi_{k} \in \mathbb{R}$ of each $\operatorname{arg}(\mathbf{a}_{k})$. Then $\theta(\overline{\mathbf{a}_{k - 1}, \mathbf{a}_{k}}, x)$ is in the equivalence class of $(\phi_{k} - \phi_{k - 1}) + 2 \pi \mathbb{Z}$. Adding up all of these equivalence classes, the telescoping sum gives us that $w(\gamma, x)$ is in the equivalence class of $\phi_{n} - \phi_{0} + 2 \pi \mathbb{Z}$. But of course, $\phi_{n} - \phi_{0}$ is also a multiple of $2 \pi$, so everything is a multiple of $2 \pi$ and dividing the sum by $2 \pi$ to get the winding number leaves an integer.

### Oriented cycles

We can generalise polygons by writing formal sums of arbitrary pairs of points.

##### _definition:_ $1$-chain, $1$-cycle

A $1$-chain is a formal sum
$$
\gamma = \overline{\mathbf{a}_{1}, \mathbf{b}_{1}} + \dots + \overline{\mathbf{a}_{n}, \mathbf{b}_{n}}
$$
for some $\mathbf{a}_{1}, \dots, \mathbf{a}_{n}, \mathbf{b}_{1}, \dots, \mathbf{b}_{n} \in \mathbb{R}^2$.

The $1$-chain is a $1$-cycle or closed $1$-chain if for every $\mathbf{v} \in \mathbb{R}^2$, the number of times $\mathbf{v}$ is the start of a line segment is the same as the number of times it's the end of a line segment.

(This is the same thing as looking at it as a [[Superdiscrete --- math-55A/notes/Basic graph theory#_definition _ graph|graph]] with edges given by the line segments and vertices as their endpoints and checking whether an [[Superdiscrete --- math-55A/notes/Basic graph theory#_definition _ Eulerian graphs, Eulerian circuit.|Eulerian circuit]] exists). Also note that each edge contributes a total of zero to the graph so the total sum should be zero.

We extend the definition of winding number in the obvious way.

##### _definition:_ angle cocycle (of a $1$-chain)

The angle cocycle of a $1$-chain $\gamma = \sum_{i = 1}^n \overline{\mathbf{a}_{i}, \mathbf{b}_{i}}$ about $x$ not in its support is
$$
\theta(\gamma, x) = \frac{1}{2 \pi} \sum_{i = 1}^n \theta(\overline{\mathbf{a}_{i},\mathbf{b}_{i}}, x).
$$

##### _definition:_ winding number (of a $1$-cycle)

The winding number of a $1$-cycle $\gamma = \sum_{i = 1}^n \overline{\mathbf{a}_{i}, \mathbf{b}_{i}}$ about $x$ not in its support is
$$
w(\gamma, x) = \frac{1}{2 \pi} \sum_{i = 1}^n \theta(\overline{\mathbf{a}_{i}, \mathbf{b}_{i}}, x).
$$

We can use exactly the same idea as previously to show that a $1$-cycle has integer winding number — each vertex will show up equally many times as $a_{k}$ and $b_{k}$ so the sum of differences $\operatorname{arg}(\mathbf{a}_{k} - \mathbf{x}) - \operatorname{arg}(\mathbf{b}_{k} - \mathbf{x})$ will cancel to $0$ (for $\mathbf{x} = x$).

##### _theorem:_ winding number (of a $1$-cycle) is an integer

Let $\gamma$ be a $1$-cycle in $\mathbb{R}^2$ and $x$ a point not in its support. Then $w(\gamma, x)$ is an integer.

### Properties of the winding number

It follows immediately for the formula for the winding number that it is additive.

##### _proposition:_ winding number is additive

If $\gamma = \gamma_{1} + \gamma_{2}$, and $x$ is not in either of their supports, then $w(\gamma, x) = w(\gamma_{1}, x) + w(\gamma_{2}, x)$.

##### _proposition:_ winding number is locally constant

For any $1$-cycle, then $x \mapsto w(\gamma, x)$ is constant on each of the connected regions of $\mathbb{R}^2 \setminus \operatorname{supp} \gamma$.

###### _proof sketch:_

This follows from the fact that this is a continuous function onto the integers. (Think discrete topology and connected components?)

Finally, we can determine the winding number in a much simpler way — just checking the crossings across one particular ray.

##### _proposition:_ the ray escape formula

Pick any ray $R$ starting at $x$ — $R$ is $R_{x, \phi} = \{ x + y \mid y \in R_{\phi} \}$. Then for 
$$
\operatorname{X}(\overline{\mathbf{a}, \mathbf{b}}, R) = \begin{cases}
1 & \overline{\mathbf{a}, \mathbf{b}} \text{ crosses } R \text{ counterclockwise} \\
-1 & \overline{\mathbf{a}, \mathbf{b}} \text{ crosses } R \text{ clockwise} \\
0 & \text{ otherwise }
\end{cases}
$$
we have
$$
w(\gamma, x) = \sum_{k = 1}^n \operatorname{X}(\overline{\mathbf{a}_{k}, \mathbf{b}_{k}}, R).
$$

###### _proof sketch(y):_

The essential bit is the formula
$$
\theta(\overline{\mathbf{a}, \mathbf{b}}, x) = \overline{\operatorname{arg}}_{\phi}(\mathbf{b}) - \overline{\operatorname{arg}}_{\phi}(\mathbf{a}) + 2 \pi \operatorname{X}(\overline{\mathbf{a}, \mathbf{b}}, R_{x, \phi})
$$
which can be proven either by casework or by definition of $\operatorname{X}$.