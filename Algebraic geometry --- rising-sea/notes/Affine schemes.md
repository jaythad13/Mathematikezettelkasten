---
tags:
- alg-geo
- comm-alg
---

Let $A$ be a ring.

Affine schemes are the basic "gluing blocks" of schemes in general, analogous to the role $\mathbb{R}^n$ or the open ball in $\mathbb{R}^n$ plays for manifolds. Just as $\mathbb{R}^n$ is a [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|ringed space]], so is each affine scheme. However, in contrast, [[Algebraic geometry --- rising-sea/notes/Examples of affine schemes|there are lots of very different affine schemes]] (one for each ring). Each affine scheme is then determined by the combination of its set (of points) its space ([[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topology]]), and its [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|structure sheaf.]]

### The set (of points)

Affine schemes are all $\operatorname{Spec} A$ for some ring $A$.

##### _definition:_ the points of the set of an affine scheme

Let $A$ be a ring. Then the **set of points of $\operatorname{Spec} A$** is the set of [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|prime ideals]] of $A$.

---

To avoid confusion between between $\mathfrak{p} \in \operatorname{Spec} A$ as a point and $\mathfrak{p} \subseteq A$ as an ideal, we may sometimes use the notation $[\mathfrak{p}]$ to indicate that we are talking about the point.

The best example of an affine scheme is the affine line over $\mathbb{C}$ — $\mathbb{A}^1_{\mathbb{C}} = \operatorname{Spec} \mathbb{C}[x]$.

![[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#_proposition _ the points of the complex affine line]]

In general, we can define $\mathbb{A}^1_{A} = \operatorname{Spec} A[x_{1}, \dots, x_{n}]$ over any ring $A$ (typically $A$ is a field). When $A$ is a non-algebraically closed field, this can behave very differently. For example

### The functions (or more alliteratively, the sections)

Though we can't define the structure sheaf yet, we can see what the [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|global functions]] of it are. Essentially, $\mathscr{O}_{\operatorname{Spec} A}(\operatorname{Spec} A) = A$.

##### _definition:_ (global) functions on an affine scheme, value, vanishing at a point

The **(global) functions on $\operatorname{Spec} A$** are the elements $a \in A$.

The **value** of a global function $a \in A$ at a point $\mathfrak{p} \in \operatorname{Spec} A$ is $a \pmod {\mathfrak{p}}$ — the image of $a$ under $A \to A / \mathfrak{p}$.

$a$ **vanishes** at $\mathfrak{p}$ if it has value $0$ at $\mathfrak{p}$.

---

Note that $a$ vanishes at $\mathfrak{p}$ if and only if $a \in \mathfrak{p}$.

In some ways and sometimes, functions behave like we might expect them to.

![[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#_proposition _ values of functions on $ mathbb{A} 1_{ mathbb{C}}$ are values of polynomials in $ mathbb{C}$|Examples of affine schemes]]

However, they don't always. In particular, functions can take values in different rings,

![[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#_example _ values of a function on $ operatorname{Spec} mathbb{Z}$ in different fields]]

and are not always determined by their values at points.

![[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#_example _ functions are not determined by their values|Examples of affine schemes]]

While this behaviour may seem somewhat pathological, we can characterise it completely, so it becomes a feature, not a bug. We claim that the functions that vanish at every point are exactly those that power to $0$. This is just saying that functions contained in every prime ideal are exactly the [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_definition _ nilpotents|nilpotents]].

![[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_proposition _ the nilradical is an ideal and the intersection of primes|Nilpotents and the nilradical]]

Thus, any two functions that take the same value at every point differ by a nilpotent. Passing to the quotient $A / \mathfrak{N}$ means that functions are determined by their value on $\operatorname{Spec} A / \mathfrak{N}$. This leads to the following definition.

##### _definition:_ reduced (ring)

(A ring) $A$ is **reduced** if it has no non-zero nilpotents. Equivalently its nilardical is $\mathfrak{N} = (0)$.

---

### The space (the Zariski topology)

### The structure sheaf