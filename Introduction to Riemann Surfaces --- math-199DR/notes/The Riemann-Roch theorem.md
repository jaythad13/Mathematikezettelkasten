---
tags:
- math-199DR/20
- math-199DR/21
- cx-geo
- alg-geo
---

### Adèles and Laurent tail divisors

Given [[Introduction to Riemann Surfaces --- math-199DR/notes/Algebraic curves#Meromorphic functions form a function field|the function field nature]] of $\mathcal{M}_{X}(X)$, the Riemann-Roch theorem is really a statement of class field theory. The idea is that $\mathcal{O}_{X}(X)$ is a ring looking something like $\mathbb{C}[[z]]$ that can be turned into a field looking something like $\mathbb{C}((z))$ at each point (not quite because we don't want to allow [[Complex Analysis --- math-135/notes/Laurent series#_theorem _ classifying singularities|essential singularities]] with infinitely many negative degree terms). We don't want to consider the information of all these $\mathbb{C}((z))$ at once because we'd never be able to glue them all together. It's nonsensical to have poles at every point, so we really just want to look at an object whose elements have have finitely many poles but has holomorphic power series everywhere else. This is the ring of adèles.

##### _definition:_ ring of adèles of an algebraic curve

The ring of adéles of $X$ is
$$
\mathbb{A}_{X} = \left\{  \prod_{p \in X} \mathcal{M}_{X, p} \mid f_{p} \in \mathcal{O}_{X, p} \text{ for all but finitely many}  \right\}.
$$

It's a [[Abstract Algebra I --- math-171/notes/Rings#_definition _ rings|ring]] under component-wise addition and multiplication.

Note that this is the same as picking a non-trivial Laurent series at finitely many points of $X$, which is what the book defines a "Laurent tail divisor" to be (actually the adéles we define are slightly larger because linear conditions on the poles aren't enough to guarantee gluing things together, but we're going to ignore that information anyway).  Note that this definition carries a nice embedding of $\mathcal{M}_{X}(X)$ by $\alpha : f \mapsto (\dots, f, f, f, \dots, )$.

Looking at these adèles helps us because they carry geometric representations of the spaces we want. Specifically we can define parallelotopes and quotients by them which filter by divisors we want to investigate, and allow us to compare them by.

##### _definition:_ parallelotopes, coparallelotopes

Given a divisor $D \in \operatorname{Div} X$ the corresponding parallelotope $\Lambda(D)$ is the additive [[Abstract Algebra I --- math-171/notes/Subgroups#_definition _ subgroup, $ le$|subgroup]] of all adèles such that $\operatorname{ord} f_{p} \geq - D(p)$.

The corresponding coparallelotope $\Lambda^\perp(D)$ is $\mathbb{A}_{X} / \Lambda(D)$ and the additive subgroup of all adèles such that the top term of each $f_{p} < -D(p)$.

Notice then that [[Introduction to Riemann Surfaces --- math-199DR/notes/The Riemann-Roch spaces of a divisor#_definition _ the Riemann-Roch function space of a divisor|the Riemann-Roch space]] $\mathcal{L}(D)$ is just the intersection $\Lambda(D) \cap \operatorname{img} \alpha$. We can also get a characterisation in terms of $\Lambda^\perp(D)$.

##### _definition:_ truncation maps, truncation of a meromorphic function

For divisors $D_{1} \le D_{2}$ the truncation map is the linear map $t_{D_{1}}^{D_{2}} : \Lambda^\perp(D_{1}) \to \Lambda^\perp(D_{2})$ with
$$
t_{D_{1}}^{D_{2}}\left( \sum_{n = m}^M a_{n} z^n  \right) = \sum_{n = m}^{-D_{2}(p)} a_{n} z^n
$$
at each point $p$.

The truncation of a meromorphic function $f$ is $\alpha_{D}(f)$ where $\alpha_{D} = t^D_{\operatorname{div} f}$ wherever $\operatorname{div} f \leq D$.

This map has the nicest possible property in that diagrams commute, and thus, that the they commute with the truncation of meromorphic functions. That is,

##### _proposition:_ truncations commute

For divisors $D_{1} \le D_{2} \le D_{3}$, the diagram
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\Lambda^\perp (D_{1}) \ar[r, "t_{D_{1}}^{D_{2}}"] \ar[rr, bend right , "t_{D_{1}}^{D_{3}}"']& \Lambda^\perp(D_{2}) \ar[r, "t_{D_2}^{D_{3}}"] & \Lambda^\perp(D_{3})
	\end{tikzcd}
\end{document}
```
commutes, and thus, so does
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{M}_{X}(X) \ar[r, "\alpha_{D_{2}}"] \ar[rr, bend right , "\alpha_{D_{3}}"']& \Lambda^\perp(D_{2}) \ar[r, "t_{D_2}^{D_{3}}"] & \Lambda^\perp(D_{3})
	\end{tikzcd}
\end{document}
```

Now we see the nice characterisation of the functions bounded by $D$ that we wanted — we get $\mathcal{L}(D) = \operatorname{ker} \alpha_{D}$. The truncations will let us compare $\mathcal{L}(D)$ for different divisors.

Later, in the proof of [[Introduction to Riemann Surfaces --- math-199DR/notes/Serre duality|Serre duality]] it will be important to also know that these coparallelotopes behave nicely under linear equivalence.

##### _definition:_ multiplication maps

Given any $D \in \operatorname{Div} X$ and $f \in \mathcal{M}_{X}(X)$ the corresponding multiplication map $\Lambda^\perp(D) \to \Lambda^\perp(D - \operatorname{div} f)$ is given by 
$$
\mu_{f}^D(g_{p}) = f g_{p}.
$$

##### _proposition:_ multiplication maps are isomorphisms

$\mu_{f}^D$ is an isomorphism with $(\mu_{f}^D)^{-1} = \mu_{1 / f}^{D - \operatorname{div f}}$.


### Mittag-Leffler problems and the idèle class group as an obstruction space

So far what we've done is defined an exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathcal{L}(D) \ar[r, hook] & \mathcal{M}_{X}(X) \ar[r, "\alpha_{D}"] & \Lambda^\perp(D)
	\end{tikzcd}
\end{document}
```
We want to turn this into a short exact sequence by collapsing the first two terms into a quotient and considering the cokernel on the other side. 

##### _definition:_ the first "cohomology" of $D$

The first "cohomology" of $D$ is $\mathrm{H}^1(D) = \operatorname{coker} \alpha_{D}$.

Why is this at all a natural thing to do?

The analytic answer is that this is an obstruction space —
$$
\operatorname{coker} \alpha_{D} = \Lambda^\perp(D) / \operatorname{img} \alpha_{D}
$$
measures the dimension of which choices of Laurent series at points can't be glued together to a meromorphic function with precisely those tails.

Note that this is harder than [[Introduction to Riemann Surfaces --- math-199DR/notes/Algebraic curves#_proposition _ Laurent series approximation|Laurent series approximation]] — Laurent series approximation allowed us to get the desired behaviour at finitely many points, but with no guarantee that there wouldn't be poles at the rest.

The number theoretic answer is that using the relationship $\mathbb{A}_{X} = \Lambda(D) \oplus \Lambda^\perp(D)$ we can describe $\mathrm{H}^1(D)$ as
$$
\mathrm{H}^1(D) = \frac{\mathbb{A}_{X} / \Lambda(D)}{\Lambda^\perp(D) \cap \mathcal{M}_{X}(X)} \cong \frac{\mathbb{A}_{X}}{\Lambda(D) + \mathcal{M}_{X}(X)}.
$$
which is actually the (ray?) class group of the function field $\mathcal{M}_{X}(X)$. This is a central object of study in class field theory (one of the central fields of study in algebraic number theory).

Finally the geometric answer is that (as the notation suggests) $\mathrm{H}^1(D)$ is really the cohomology of the invertible sheaf associated to the line bundles associated to $D$, and since $\mathcal{L}(D)$ is really related to the line bundle, it's natural to consider $\mathrm{H}^1(D)$.

All of this just means that we have a map of short exact sequences (a commutative diagram) for any pair of divisors on $X$ with $D_{1} \le D_{2}$.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathcal{M}_{X}(X) / \mathcal{L}(D_{1}) \ar[r, "\alpha_{D_{1}}"] \ar[d, two heads] & \Lambda^\perp(D_{2}) \ar[r, two heads] \ar[d, "t"]  & \mathrm{H}^1(D_{1})  \ar[r] \ar[d] & 0 \\
		0 \ar[r] & \mathcal{M}_{X}(X) / \mathcal{L}(D_{2}) \ar[r, "\alpha_{D_{2}}"] & \Lambda^\perp(D_{2}) \ar[r, two heads] & \mathrm{H}^1(D_{2}) \ar[r] & 0
	\end{tikzcd}
\end{document}
```

Here the map on the left follows from $\mathcal{L}(D_{1}) \subseteq \mathcal{L}(D_{2})$, $t$ is the suitable truncation, and the map on the right is also a truncation.

By the snake lemma, we have a short exact sequence of kernels of the vertical maps (since the vertical maps are all surjections, the cokernels are all $0$).

The kernel of the left vertical map is $\mathcal{L}(D_{2}) / \mathcal{L}(D_{1})$ and we will call the kernel of the right vertical map $\mathrm{H}^1(D_{2} / D_{2})$ (for what I think are reasons motivated by cohomology). The short exact sequence is then

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathcal{L}(D_2) / \mathcal{L}(D_{1}) \ar[r] & \ker t \ar[r] & \mathrm{H}^1(D_{1} / D_{2}) \ar[r] & 0
	\end{tikzcd}
\end{document}
```

$\ker t$ is clearly $\deg D_{2} - \deg D_{1}$ dimensional — just look at the basis of $1 / z_{p}^n$ that get sent to zero under truncation at each point to get $\sum_{p \in X} D_{2}(p) - D_{1}(p)$ basis vectors.

It follows that $\mathrm{H}^1(D_{1} / D_{2})$ is finite-dimensional since $\ker t$ surjects onto it. Infact, we have the following fact.

##### _lemma:_ almost Riemann-Roch

For $D_{1}, D_{2} \in \operatorname{Div} X$ and $D_{1} \leq D_{2}$
$$
\dim H_{1}(D_{1} / D_{2}) + \dim \mathcal{L}(D_{2}) / \mathcal{L}(D_{1}) = \deg D_{2} - \deg D_{1}
$$

###### _proof:_
is an application of the rank-nullity theorem.

Since the Riemann-Roch spaces are finite dimensional, we get (from the rank nullity theorem applied to)

### The (weak) Riemann-Roch theorem and philosophy

With the assumption that $\dim \mathrm{H}^1(D)$ is finite dimensional, we have essentially proved Riemann-Roch. It allows us to write
$$
\dim \mathrm{H}^1(D_{1} / D_{2}) = \dim \mathrm{H}^1(D_{1}) - \dim \mathrm{H}^1(D_{2})
$$
for $D_{1} \le D_{2}$.

Plugging this into the formula we just obtained gives us a formula to compare any two comparable divisors [[Introduction to Riemann Surfaces --- math-199DR/notes/The Riemann-Roch spaces of a divisor#_definition _ ordering on divisors|in the divisor poset]] —
$$
\dim \mathcal{L}(D_{1}) - \deg D_{1} - \dim \mathrm{H}_{1}(D_{1}) = \dim L(D_{2}) - \deg D_{2} - \dim \mathrm{H}^1(D_{2}).
$$
Since any two divisors have a common supremum, this in fact extends to all divisors — the expression
$$
\dim \mathcal{L}(D) - \deg D - \dim \mathrm{H}^1(D)
$$
is the same for any divisor $D \in \operatorname{Div} X$.

For the zero divisor $\dim \mathcal{L}(0) = 1$ and $\deg 0 = 0$, so comparing any divisor to the zero divisor, we get the (weak) Riemann-Roch theorem —

##### _theorem:_ the (weak) Riemann-Roch theorem

For any $D \in \operatorname{Div} X$ 
$$
\dim \mathcal{L}(D) - \mathrm{H}^1(D) = 1 + \deg D + \mathrm{H}^1(0).
$$

This theorem is "weak" in the sense that it doesn't give the full picture of Riemann-Roch. It only trades the computation of $\mathcal{L}(D)$ for the computation of $\mathrm{H}^1(D)$. Really, what we want the Riemann-Roch theorem to say is that the only obstructions to the construction of the algebraic/analytic space/line bundle/invertible sheaf $\mathcal{L}(D)$ are topological.

This is just a consequence of the way we defined $\mathrm{H}^1$ — one could take a more geometric (and high-powered) approach and define $\mathrm{H}^1(D)$ to be the cohomology of the invertible sheaf associated to the line bundle $\mathcal{L}(D)$ associated to the divisor $D$. Then it would be obvious that the $\mathrm{H}^1(D)$ is a topological invariant, but you'd have the opposite problem of translating everything back down to earth. (There is technically a proof of Brill and Noether in Fulton's book that might not use Serre duality, but I think they do the same thing as Lang and sort of define in the Serre duality)

The solution to both problems is Serre duality. We've seen already in the adèlic approach how $\mathrm{H}^1(D)$ might be related to differential forms. For us, Serre duality will give an explicit isomorphism, allowing us to give the complete form of Riemann-Roch.

### Finite dimensionality of the obstruction space

### Riemann-Roch with Serre duality
