---
tags:
- math-199DR/7
- math-199DR/10
- alg-top
- diff-geo
---

There are two fundamental topological invariants of a surface — the Euler characteristic and the genus. The genus is explicitly the number of holes in the surface, but the Euler characteristic is easier to compute, and carries the same information. We will define both and prove this relationship.

We will also some machinery from algebraic topology.

### Genus

The genus of a surface counts the number of holes in it cutting out curves.

##### _definition:_ genus 

The genus of a (connected) surface $X$ is $g_{X}$, the maximum number of disjoint simple closed curves that can be removed from the surface while leaving it connected.

##### _example:_ the genus of some surfaces

The genus of
1) the sphere $S^1$ is $0$
2) the torus $S^1 \times S^1$ is $1$ (cut it into a cylinder or in the opposite direction into a rectangle)
3) the Möbius strip is $1$ (cut along the centre)


### Euler characteristic

The Euler number is a fundamental topological invariant. Here we will define for Riemann surfaces (and in the process, define it for $2$-manifolds in general).

##### _definition:_ triangulation

A triangulation $X_{T}$ of a surface $X$ is a collection of closed subsets $\{ \Delta \}$ of $X$, each homeomorphic to a triangle such that any two triangles are disjoint, intersect only at a single vertex, or intersect at a single edge.

##### _definition:_ Euler characteristic of a triangulation

The characteristic of a triangulation $X_{T}$ is $\chi(X_{T}) = V - E + F$, where $V$ is the number of vertices, $E$ is the number of edges, and $F$ is the number of faces in the triangulation.

##### _definition:_ Euler characteristic

The Euler characteristic of a surface $X$ is $\chi(X) = \chi(X_{T})$ for a triangulation $X_{T}$.

##### _example:_ Euler characteristics of some surfaces

The Euler characteristic of
1) the sphere is $\chi(S^2) = 2$ (build an octahedron out of eight triangles)
2) the cylinder is $\chi(S_{1} \times [0, 1]) = 0$ (build four squares out of two triangles each, and make them into a square cylinder)
3) the disc is $\chi(\mathbb{D}) = 1$ since $\mathbb{D} \cong \Delta$ and the triangle has Euler characteristic $1$.
4) the torus is $\chi(S^1 \times S^1) = 1$ (identify the ends of the cylinder losing $4$ edges)

We should probably explain why this is well-defined.

##### _proposition:_ the Euler characteristic doesn't depend on the triangulation

For any surface $X$, any two triangulations $X_{T_{1}}$ and $X_{T_{2}}$ have $\chi(X_{T_{1}}) = \chi(X_{T_{2}})$.

###### _proof sketch:_

Essentially, we use the [[Calculus --- spivak/notes/Integration over closed rectangles#_corollary _ any upper sum is greater than any lower sum|common refinement trick]] just as we did to prove [[Topics in Geometry and Topology --- math-145/notes/Continuous and differentiable winding number#_theorem _ the continuous winding number theorem|the continuous winding number theorem]].

A refinement of a triangulation is a triangulation of the triangulation. By checking manually, one can see that a refinement of any triangle still has the same Euler characteristic. Thus, the refinement of any triangulation of a surface still has the same Euler characteristic.

By overlaying two triangulations one can see that any two triangulations have a common refinement — take the union of their vertices and edges and add vertices where edges cross edges. Since $X_{T_{1}}$ and $X_{T_{2}}$ have the same Euler characteristic as their comon refinement $X_{T}$, they have the same Euler characteristic as each other.

##### _theorem:_ Euler characteristic and genus

For $X$ a compact orientable $2$-manifold without boundary (for our purposes, [[Introduction to Riemann Surfaces --- math-199DR/notes/Riemann surfaces|a Riemann surface]]), of genus $g$,
$$
\chi(X) = 2 - 2 g.
$$

###### _proof sketch:_

Notice that the sphere $S^2$ satisfies $\chi(S^1) = 2 - 2 g_{S^1}$ with $g_{S^1} = 0$.

It is a theorem that all surfaces come from adding handles to a sphere — removing two discs and adding a cylinder in its place. Adding a handle, almost by definition adds $1$ to the genus. However, removing the two discs drops the Euler characteristic by $1$ for each, and adding the cylinder doesn't change the Euler characteristic. That is, adding $1$ to the genus, drops the Euler characteristic by $2$.

By induction from our base case $g = 0$, $\chi(X) = 2$, we get that in general
$$
\chi(X) = 2 - 2 g.
$$

### Homotopy

##### _definition:_ paths, loops

In a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]] $X$, a path is a continuous map $\gamma : [0, 1] \to X$.

A loop is a path $\gamma$ with $\gamma(0) = \gamma(1)$.

##### _definition:_ homotopic

Two paths $\gamma_{1}, \gamma_{2}$ are homotopic if there's a continuous map $[0, 1] \times [0, 1] \to X$ with $H(0, t) = \gamma_{1}(t)$ and $H(1, t) = \gamma_{2}(t)$, such that $H(s, 0)$ and $H(s, 1)$ are constant. 

This forms an equivalence relation with [[Topics in Geometry and Topology --- math-145/notes/Continuous and differentiable winding number|winding number]] able to tell non-homotopic loops apart.

##### _definition:_ the fundamental group (based ay $x \in X$)

The set of loops based at $x \in X$ (with $\gamma(0) = \gamma(1) = x$) forms $\pi_{1}(X, x)$, the (first) fundamental group of $X$ (based at $x$) with $\gamma_{1} \gamma_{2} : [0, 2] \to X$  equal to $\gamma_2$ on $[0, 1]$ and $\gamma_{1}$ on $[1, 2]$. 

If $X$ is [[Complex Analysis --- math-135/notes/Analysis and (metric) topology review#_definition _ path-connected|path-connected]] (which is [[Complex Analysis --- math-135/notes/Analysis and (metric) topology review#_proposition _ path-connectedness and connectedness are equivalent on open sets|equivalent to connected for manifolds]]).

### Covering spaces

##### _definition:_ covering map, covering space

$f : X \to Y$ is a covering map and $X$ is a covering space for $Y$ if for every $p \in Y$, there exists some $W \subseteq Y$ containing $p$ with every $f^\text{pre}(W)$ is a disjoint union of open sets in $X$, say $U_{\alpha}$ where each $U_{\alpha}$ is homeomorphic to $W$ under the restriction $f_{|U}$.

##### _example:_ $\mathbb{C} \setminus \{ 0 \}$ covers itself non-trivially

$z \mapsto z^n$ is a covering map ${ \mathbb{C} \setminus \{ 0 \} } \to {\mathbb{C} \setminus \{ 0 \}}$.

##### _theorem:_ paths lift

For any covering map $f : X \to Y$ and loop $\gamma : [0, 1] \to Y$ based at $q = f(p)$, we can lift $\gamma$ to a unique path $\tilde{\gamma} : [0, 1] \to X$ such that the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		I \ar[r, "\tilde{\gamma}"] \ar[rd, "\gamma"] & X \ar[d, "f"] \\
		& Y
	\end{tikzcd}
\end{document}
```



Notice that this induces a group action of $\pi_{1}(Y, q)$ on a covering space $f : X \to Y$.

##### _theorem:_ the universal cover

For any real manifold $X$ (satisfying some technical condition that all [[Introduction to Riemann Surfaces --- math-199DR/notes/Riemann surfaces#_definition _ (compact, connected) Riemann surface, (holomorphic) atlas, chart|Riemann surfaces]] satisfy), there exists a unique (up to cover isomorphism) cover $f_{0} : U_{0} \to X$ such that the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		U_{0} \ar[r, "g"] \ar[rd, "f_{0}"] & U \ar[d, "f"] \\
		& X
	\end{tikzcd}
\end{document}
```

Quotienting $U_{0}$ by $\pi_{1}(X, p)$ gives $X$ and quotienting by any subgroup gives a connected cover.

##### _example:_ the universal cover of the punctured plane

The universal cover of ${\mathbb{C} \setminus \{ 0 \}}$ is the cover $f : \mathbb{C} \to {\mathbb{C} \setminus \{ 0 \}}$ by $f(z) = e^z$.

### Monodromy

##### _definition:_ monodromy (representation) of a covering map

Given a cover $f : U \to X$ (of finite [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_theorem _ degree is constant|degree]] $d$), the fundamental group $\pi(X)$ acts on $U$ and specifically $f^\text{pre}(\{ q \})$, then there exists a permutation representation (read, [[Abstract Algebra I --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphism]])
$$
\rho : \pi_{1}(X) \to \mathfrak S_{d}
$$
called the monodromy representation of $f$.

But this only allows us to think about maps with no [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ ramification point, branch point|ramification]] — since the map is a local homeomorphism everywhere. How can we deal with ramification?

##### _definition:_ monodromy (representation) of a holomorphism

Given a [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]] $\pi : X \to Y$ the monodromy of $\pi$ is the monodromy representation of $\pi_{\mid U} : U \to V$ where $U$ and $V$ are $X$ and $Y$ without [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ ramification point, branch point|ramification points and branch points]] respectively.

Note that a monodromy representation must be transitive in its image because we can lift something something %%do later%%

This isn't just a necessary condition, it's also sufficient!

##### _theorem:_

For a Riemann surface $X$, given a permutation representation $\rho : \pi(X) \to \mathfrak S_{d}$ such that its image is transitive. Then there exists a cover $f : U \to X$ of degree $d$ such that $\rho$ is the monodromy representation of the cover.

###### _proof sketch(y):_

Choose $U = U_{0} / H$ where $H$ is the subgroup of all $h \in \pi_{1}(X)$ such that $\rho(h)$ fixes $1$. It has [[Abstract Algebra I --- math-171/notes/Lagrange's theorem#_definition _ index, $ lvert G H rvert$|index]] $d$. Trust Alan that the rest of the details work out

Note that we could give two monodromy representations that are essentially the same by pre and post-composing with a permutation and its inverse. These give the same cover, but are also in the "same conjugacy class". We have a correspondence between conjugacy classes of monodromy representations and connected covers of $X$ of degree $d$.

By pullback atlas covers of Riemann surfaces are Riemann surfaces too.

Given a Riemann surface $X$, and a covering Riemann surface $U$, we want to classify all the holomorphic maps $U \to X$ of given degree $d$ and with branch points only in the give set $B$. We know what unramified maps to ${X \setminus B}$ look like — they are covers. By [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_theorem _ identity theorem|identity theorem]] and the [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_corollary _ ramification points are discrete|discreteness of branch points]] we can classify finite degree maps by classifying conjugacy classes of monodromy representations  $\rho : \pi_{1}(X \setminus B) \to \mathfrak S_{d}$.

When $X$ is (very) nice and simple, the fundamental group $\pi_{1}(X \setminus B)$ is reasonable.

##### _example:_ finite degree maps to the Riemann sphere

Recall that [[Introduction to Riemann Surfaces --- math-199DR/notes/Riemann surfaces#_example _ the Riemann sphere and the complex projective line|the Riemann surfaces]] (and equivalently $\mathbb{C} \mathbb{P}^1$) is a topological sphere.

### Galois theory

Given a holomorphism $\pi : X \to Y$, let $K$ be [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#Nice function fields|the function field]] of global meromorphic maps on $X$ — $K = \mathcal{M}_{X}(X)$. Let $k$ be the pullback of the meromorphic functions on $Y$ — $k = \pi^* \mathcal{M}_{V}( V)$.

Then $K / k$ is field extension of degree $\deg \pi$ and the normal closure of $K / k$, say $L / k$ has Galois group $\operatorname{Gal}(L / k) \cong \rho(\pi_{1}(X))$ for the $\rho$ the monodromy representation of $\pi$.

Essentially this is because the natural $z \mapsto \omega_{d}^n z$ that preserves $z^d$ looks like rotation.