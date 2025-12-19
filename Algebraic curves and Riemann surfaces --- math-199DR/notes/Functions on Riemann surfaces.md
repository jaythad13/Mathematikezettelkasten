---
tags:
- math-199DR/4
- math-199DR/5
- diff-geo
- complex
- cx-geo
---

Here let $X$ be a Riemann surface with a maximal atlas $\mathcal{A}$ consisting of charts $(U_{\alpha}, \phi_{\alpha})$ indexed by $\alpha \in \mathcal{I}$.

### Holomorphic functions

The raison d'etre for the complicated definition of a [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Riemann surfaces#_definition _ (compact, connected) Riemann surface, (holomorphic) atlas|holomorphic atlas]] is that we want to define holomorphic functions on (open sets) of a Riemann surface. In particular, we push everything to the complex numbers and since all charts are holomorphically equivalent, we're okay. Here we're going to show that this really works.

Let $W$ be an open subset of $X$, and $f$ be a function $W \to \mathbb{C}$ (till [[#_examples _ dumb examples of holomorphic functions|we talk about examples of holomorphic functions]]).

##### _definition:_ holomorphic functions

$f$ is **holomorphic** on all of $W$ if $f \circ \phi_{\alpha}^{-1}$ is a [[Complex analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|holomorphic]] function $\phi_{\alpha}^{\text{img}}(W \cap U_{\alpha}) \to \mathbb{C}$ for all $\alpha \in \mathcal{I}$.

The ring of all holomorphic functions on $W$ is denoted $\mathscr{O}_{X}(W)$.

$f$ is **holomorphic at a point** $p \in X$ if $f$ is holomorphic on an open set containing $p$.

The ring of all holomorphic functions at $p$ is denoted $\mathscr{O}_{X, p}$.

---

We don't actually have to check holomorphicity on each chart — because the transition maps are holomorphic, different charts agree about what holomorphicity is, and thus we can just check holomorphicity on a cover of $W$ by charts.

##### _proposition:_ compatible charts agree on holomorphicity

Given two charts $(\phi_{1}, U_{1}), (\phi_2, U_{2})$ and a function $g : U_{1} \cap U_{2} \to \mathbb{C}$, the function $g \circ \phi_{1}^{-1} : \phi_{1}^\text{img}(U_{1} \cap U_{2}) \to \mathbb{C}$ is holomorphic if and only if $g \circ \phi_{2}^{-1}$ is.

###### _proof:_

We will only prove one direction of the implication since it is symmetric in the indices. Suppose $g \circ \phi_{1}^{-1}$ is holomorphic. Recall that for $\phi_{1}, \phi_{2}$ to be in the same (holomorphic) atlas, they must satisfy the compatibility condition that $\phi_{1} \circ \phi_{2}^{-1}$ is a holomorphic function $\phi_{2}^\text{img}(U_{1} \cap U_{2}) \to \phi_{1}^\text{img}(U_{1} \cap U_{2})$. Thus, by the chain rule
$$
(g \circ \phi ^{-1}_{1}) \circ (\phi_{1} \circ \phi_{2}^{-1}) = g \circ \phi_{2}^{-1}
$$
is holomorphic.

---

##### _corollary:_ check once to prove holomorphicity

$f$ is holomorphic on $W$ if there is an open cover by charts $W \subseteq \bigcup_{\alpha \in \mathcal{J} \subseteq \mathcal{I}} U_{\alpha}$ such that $f \circ \phi_{\alpha}^{-1}$ is holomorphic on $\phi_{\alpha}(W \cap U_{\alpha})$ for each $\alpha$.

$f$ is holomorphic at a point $p \in X$ if there is a chart $(\phi, U)$ with $f \circ \phi ^{-1}$ holomorphic at $\phi(p)$.

$f$ is holomorphic on $W$ if it is holomorphic at every point $p \in W$.

---

All the obvious examples of functions that should be holomorphic are holomorphic.

##### _examples:_ dumb examples of holomorphic functions

1) Every chart is a holomorphic function on its domain.
2) Consider $\mathbb{C}$ and its open subsets as Riemann surfaces, a holomorphic function $f : U \to \mathbb{C}$ (in the classical sense) is a holomorphic function on the Riemann surface $U$.
3) A constant function is holomorphic.

---

In our definitions of $\mathscr{O}_{X}(W)$ and $\mathscr{O}_{X, p}$ we called the sets of holomorphic functions rings. We could do this because sum and product preserve holomorphicity.

##### _proposition:_ sum, product, and quotient rules

If $f, g : X \to \mathbb{C}$ are holomorphic at $p \in X$, then $f \pm g$ and $fg$ are holomorphic at $p$. If $g(p) \neq 0$, then $f / g$ is holomorphic at $p$.

###### _proof sketch:_

$(f + g) \circ \phi = f \circ \phi + g \circ \phi$ and similarly for the other operations, so this follows by the sum, product, and quotient rules for [[Complex analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$}|holomorphic functions]].

---

### Meromorphic functions

We can also define singularities of functions — [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#Removable singularities|removable singularities]], [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#Poles|poles]], and [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#Essential singularities|essential singularities]] as well as [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#Meromorphic functions|meromorphic functions]] — just as we did on $\mathbb{C}$.

Let $p$ be a point in $X$ and let $f : U_{p}^* \to \mathbb{C}$ be a holomorphic function on a punctured neighbourhood of $p$. To define each type of singularity, we look at the behaviour of $f$ on a neighbourhood of $U$ when we push everything forward to the complex plane.

In increasing order of badness,

##### _definition:_ removable singularity

$f$ has a **removable singularity** at $p$ if there is a chart $(\phi, U)$ with $p \in U$ and $f \circ \phi ^{-1}$ has a  [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ removable singularity|removable singularity]] at $p$.

---

##### _definition:_ pole

$f$ has a **pole** at $p$ if there is a chart $(\phi, U)$ with $p \in U$ and $f \circ \phi ^{-1}$ has a  [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ pole|pole]] at $p$.

---

##### _definition:_ essential singularity

$f$ has an **essential singularity** at $p$ if there is a chart $(\phi, U)$ with $p \in U$ and $f \circ \phi ^{-1}$ has an  [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ essential singularity|essential singularity]] at $p$.

---

By the same proof as for holomorphic functions, we can show that all of these definitions don't depend on the choice of chart.

##### _definition:_ meromorphic

$f : X \to \mathbb{C}$ is **meromorphic at a point** $p \in X$ if it has, at worst, a pole at $p$.

$f$ is **meromorphic** on $W \subseteq X$ if it is meromorphic at each point of $W$.

The ring of all meromorphic functions on $W$ is denoted $\mathscr{M}_{X}(W)$.

---

##### _example:_ dumb examples of meromorphic functions

1) Every holomorphic function on $X$ is also a meromorphic function.
2) Every meromorphic function on a subset of $\mathbb{C}$ is a meromorphic function.

---

Since every meromorphic function on $\mathbb{C}$ has a [[Complex analysis --- math-135/notes/Laurent series|Laurent series]], for a chart $(\phi, U)$ and a meromorphic function $f : X \to \mathbb{C}$, we can analyse the Laurent series of $f \circ \phi^{-1}$ at each $\phi(p)$. While the Laurent series itself depends on the chart its most important property doesn't — it has the same order.

##### _proposition:_ order doesn't depend on chart

Given two charts $(\phi_{1}, U_{1})$ and $(\phi_{2}, U_{2})$ with $p \in U_{1} \cap U_{2}$ and $f$ meromorphic at $p$, the order (the degree of the lowest term of the Laurent series of) of $f \circ \phi_{1}^{-1}$ equals the order of $f \circ \phi_{2}^{-1}$.

###### _proof sketch:_

Since $\phi_{1} \circ \phi_{2}^{-1}$ is holomorphic and has non-vanishing first derivative at $p$ (since it's invertible), precomposing with its power series has no effect on the order.

---

##### _definition:_ order

The **order** of a meromorphic function $f$ at $p$ is $\operatorname{ord}_{p}f$, the minimum degree of the Laurent series of $f \circ \phi ^{-1}$ for some chart around $(\phi, U)$ with $p \in U$.

---

##### _proposition:_ basic properties of order

For meromorphic functions $f, g$ and $p \in X$,
1) $\operatorname{ord}_{p}(fg) = \operatorname{ord}_{p}f + \operatorname{ord}_{p}g$
2) $\operatorname{ord}_{p}(f / g) = \operatorname{ord}_{p} f - \operatorname{ord}_{p} g$
3) $\operatorname{ord}_{p}(f \pm g) \ge \min \{ \operatorname{ord}_{p}f, \operatorname{ord}_{p} g \}$.

---

These properties follow easily from the corresponding properties for meromorphic functions on $\mathbb{C}$.

### Theorems from complex analysis

As might be expected, many theorems about holomorphic and meromorphic functions on subsets of $\mathbb{C}$ carry over exactly to $f : X \to \mathbb{C}$ by checking them for $f \circ \phi ^{-1}$ where $(\phi, U)$ is some appropriate chart on $X$.

##### _proposition:_ discreteness of zeroes and poles

If $f : W \to \mathbb{C}$ is not identically zero on the connected open subset $W \subseteq X$, then the zeroes (and poles) of $f$ form a discrete subset of $W$ (every point is [[Topology --- math-147/notes/Limit points and closed sets#_definition _ isolated point|isolated]]).

###### _proof sketch:_

[[Complex analysis --- math-135/notes/Cauchy integral formula#_theorem _ identity theorem|This is true]] when $X =  \mathbb{C}$. Suppose $S$, the set of zeroes of $f$ has a limit point $p$ in $W$. Consider the chart $(\phi, U)$ with $p \in U$. This also contains a set of zeroes having a limit point at $p$ and pushing to $\mathbb{C}$ by $\phi$ keeps this — the set of zeroes of $f \circ \phi ^{-1}$ has a limit point at $\phi(p)$. Now $f \circ \phi ^{-1}$ is identically zero on $\phi^\text{img}(U)$, and thus is identically zero on $U$.

Since $W$ is connected, we can move this around to every point in $W$.

---

##### _corollary:_ compact Riemann surfaces have finitely many poles and zeroes

##### _theorem:_ identity theorem

Suppose $f, g : W \to \mathbb{C}$ are meromorphic on a connected open set $W \subseteq X$. If $f = g$ on a subset $S \subseteq W$ which has a [[Topology --- math-147/notes/Limit points and closed sets#_definition _ limit point|limit point]] in $W$, $f = g$ identically on all of $W$.

---

##### _theorem:_ open mapping theorem

If $W \subseteq X$ is a connected open set and $f : W \to \mathbb{C}$ is holomorphic on $W$, then $f^\text{img}(U)$ is open for every open $U \subseteq W$.

###### _proof sketch:_

For each open $U \subseteq W$, by restricting charts to their intersection with $U$, we can choose an open cover of charts $U = \bigcup_{\alpha \in \mathcal{J} \subseteq \mathcal{I}} U_{\alpha}$. Each of these has $f \circ \phi ^{-1}_{\alpha}$ holomorphic, and thus, by the [[Complex analysis --- math-135/notes/The argument principle and winding number#_theorem _ open mapping theorem|open mapping theorem]] of complex analysis, is an open map. But then $\phi_{\alpha}$, being a homeomorphism is an open map too. Thus, $f = (f \circ \phi_{\alpha} ^{-1}) \circ \phi_{\alpha}$ is an open map.

---

##### _corollary:_ maximum modulus theorem

If $f$ is holomorphic and non-constant, (on a connected open set $W \subseteq X$), then $\lvert f \rvert$ does not achieve a maximum.

---

The maximum modulus theorem can be applied on compact Riemann surfaces to classify global holomorphic functions (in a way that fails over $\mathbb{C}$). This is a similar result to [[Complex analysis --- math-135/notes/Cauchy integral formula#_theorem _ Liouville's theorem|Liouville's theorem]], the hypothesis of which essentially forces $\mathbb{C}$ to behave as if it were compact.

##### _theorem:_ global holomorphic functions are constant

If $X$ is compact, and $f : X \to \mathbb{C}$ is holomorphic on all of $X$, then $f$ is constant.

###### _proof:_

Since $f$ is holomorphic, it is [[Analysis --- math-131/notes/Continuity#_definition _ continuity|continuous]], and thus, so is $\lvert f \rvert$. Since $X$ is compact, $\lvert f \rvert$ [[Analysis --- math-131/notes/Continuity#_corollary _ the image of a compact set has a maximum and minimum|achieves a maximum]], and thus, must be constant.

---

### Riemann surfaces as ringed spaces

Notice that each for each open $W \subseteq X$, the $\mathscr{O}_{X}(W)$ is a [[Abstract algebra --- math-171/notes/Rings#_definition _ commutative ring|commutative ring]] (in fact, it is a $\mathbb{C}$-algebra — its ring structure is compatible with its [[Linear algebra done right --- ladr/notes/Vector spaces|vector space]] structure over $\mathbb{C}$). It's not necessarily an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]] since $W$ may not be connected and then we can have [[Abstract algebra --- math-171/notes/Rings#_definition _ zero divisor|zero divisors]].

Moreover, if we have open sets $V \subseteq W \subseteq X$, we have a map $\mathscr{O}_{X}(W) \to \mathscr{O}_{X}(V)$ that sends a function on $W$ to its restriction to $V$ (in fact this is an injection by [[Complex analysis --- math-135/notes/Cauchy integral formula#_corollary _ unique analytic continuation|analytic continuation]]). To be exact, this is a [[Algebraic geometry --- rising-sea/notes/Functors|contravariant functor]] from the poset category on the topology of $X$ (with inclusions being the morphisms) to the category of [[Abstract algebra --- math-171/notes/Rings#_definition _ commutative ring|commutative rings]].

That is, $\mathscr{O}_{X}$ forms a [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|sheaf]] of rings that turns the Riemann surface $X$ into a [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, isomorphism of ringed spaces, functions, global functions|ringed space]] with structure sheaf $\mathscr{O}_{X}$. It's easy to see that $\mathscr{O}_{X, p}$ really is the stalk of $\mathscr{O}_{X}$ at $p$, and further, that it is a [[Commutative algebra --- math-189AA/notes/Local rings#_definition _ local rings|local ring]] with unique maximal ideal $\mathfrak{m}_{X, p} = \{ f \mid f(p) = 0 \}$. Thus, $X$ is a [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ local ringed spaces, residue fields|local ringed space]].

We will show that this data suffices to morphisms of Riemann surfaces too, but we will not do much more with it.

### Nice function fields

In cases when the $X$ is nice, we can classify all the global meromorphic functions on it!

##### _example:_ meromorphic functions on the Riemann sphere and projective line

It's a theorem from complex analysis that the only meromorphic functions $f$ satisfying $f(1 / z)$ meromorphic on the Riemann sphere $\mathbb{C}_{\infty}$ are rational —

![[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_theorem _ classifying meromorphic functions on the extended complex plane]]

The big thing we're doing here is transferring everything to $\mathbb{C}$ by saying $f$ is meromorphic at $\infty$ if $f(1 / z)$ has, at worst, a [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ pole|pole]] at $0$.

A non-example of a meromorphic function is $\sin(z)$ extended to $\mathbb{C}_{\infty}$ — $\sin(1/z)$ has an [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ essential singularity|essential singularity]] at $0$.

A nice fact is that for any $f$ meromorphic on $\mathbb{C}_{\infty}$ the order of a function everywhere on $\mathbb{C}$ is canceled out by the order at $0$. That is,
$$
\sum_{p \in \mathbb{C}_{\infty}} \operatorname{ord}_{p}f = 0
$$
since every zero is a pole at infinity and every pole is a zero at infinity.

In homogeneous coordinates on $\mathbb{C}\mathbb{P}^1$ we can write zeroes and poles at $\infty$ as zeroes or poles of rational functions with homogeneous numerator and denominator of the same degree. That is, a meromorphic function $f$ has
$$
f(w : z) = \frac{\prod_{i = 1}^n (b_{i} z - a_{i} w)}{\prod_{i = 1}^m (c_{i} z - d_{i} w)}
$$
and thus, $f$'s behaviour at infinity is just $f$'s behaviour at $w = 0$.

---

##### _example:_ meromorphic functions on the torus

Recall that the complex torus $\mathbb{C} / \Lambda$ [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Riemann surfaces#_example _ Algebraic Geometry --- math-176/notes/Elliptic curves _proposition, definition _ reducing cubics, elliptic curves elliptic curves|is a Riemann surface]]. Note that defining meromorphic functions $f$ on $\mathbb{C} / \Lambda$ is the same as defining $\Lambda$-periodic ($f(z + \omega) = f(z)$ for all $\omega \in \Lambda$) meromorphic function on $\mathbb{C}$. We build these out of the Jacobi $\Theta$ function
$$
\Theta_{\tau}(z) = \sum_{n = - \infty}^\infty e^{\pi i(n^{2} \tau + 2 n z)}.
$$

Since the zeroes of $\Theta$ lie at $1 /2 + \tau / 2 + \Lambda$, by shifting the Jacobi theta function around and taking rational functions of it, we get meromorphic functions with prescribed zeroes and poles.

---