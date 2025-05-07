---
tags:
- math-139/36
- fourier
- anal
---

To get the Calderón-Zygmund decomposition, we need to first have a covering result on closed sets in $\mathbb{R}^n$. 

##### _theorem:_ Whitney decomposition

For $F \subseteq \mathbb{R}^n$ a closed, non-empty set, there is a cover of $\mathbb{R}^n \setminus F$ with cubes $\{ Q_{k} \}$ such that the interiors of the cubes are disjoint and the side lengths of the cubes are propertional to their distance from $F$.

##### _theorem:_ generalised Whitney decomposition

There exist constants $1 < c_{1} < c_{2}$ such that, given any closed, non-emtpy set, there exists collection of balls $\{ B_{k} \}$ such that the balls are pairwise disjoint, $\{ c_{1} B_{k} \}$ a cover of ${\mathbb{R}^n \setminus F}$, and $\{ c_{2} B_{k} \}$.

If one constructs disjoint cubes $Q_{k}$ each with $B_{k} \subseteq Q_{k} \subseteq c_{1} B_{k}$, then we recover the Whitney deceomposition.

##### _theorem:_ Calderon-Zygmund decomposition

Given $f \in L^1(\mathbb{R}^n)$, and some positive constant $\alpha$, then one can decompose $f = g + b$ where $\lvert g(x) \rvert < c \alpha$ almost everywhere, and $b(x) = \sum_{k} b_{k}(x)$ and there exists $\{ c_{1} B_{k} \}$ such that %%some covering property here%% Further,
$$
\int_{c_{1} B_{k}} \lvert b_{k}(x) \rvert \, dx \le c \alpha \lvert c_{1} B_{k} \rvert 
$$
%%more niceness properties here%%

###### _proof sketch:_

We give the decomposition but don't prove that it is nice

Let $E_{\alpha} = \{ x \in \mathbb{R}^n \mid \tilde{M}f(x) > \alpha \}$, and apply the generalised Whitney decomposition to the closed complement $\mathbb{R}^n \setminus E_{\alpha}$ to get $Q_{k}$ covering $E_{\alpha}$ with the desired properties.

Let
$$
g(x) = \begin{cases}
f(x) & x \notin E_{\alpha} \\
\displaystyle \frac{1}{\lvert Q_{k} \rvert } \int_{Q(k)} f(x) \, dx & x \not\in Q_{k}.
\end{cases}
$$
and let
$$
b_{k}(x) = \left( f(x) - \frac{1}{\lvert Q_{k} \rvert } \int_{Q_{k}} f(x) \, dx  \right) \cdot \chi_{Q_{k}} (x) 
$$
Then $f = g + \sum_{k} b_{k}$

##### _definition:_ singular integral operators

The singular integral operator $T$ is defined by
$$
T f(x) = \int_{\mathbb{R}^n} K(x, y) f(y) \, dy
$$
where $K$ is singular near $x = y$.

##### _theorem:_ boundedness of the singular integral operators

If there exists a constant $A$ such that $\lVert T f \rVert_{L^q} \le A \lVert f \rVert_{L^q}$ (that is, if $T$ is bounded in $L^p$) and there exists a measurable function $K$ such that for some $c > 1$, any fixed $y_{0} \in B(y, \delta)$ gives
$$
\int_{\mathbb{R}^n \setminus B(y, c \delta)} \lvert K(x, y) - K(x, y_{0}) \rvert  \, dx < A
$$
then for all $1 < p < q$, $T$ is bounded on $L^p$ — that is, $\lVert T f \rVert_{L^p} \le A \lVert f \rVert_{L^p}$.

###### _proof sketch:_

The proof follows similarly to the [[Fourier Analysis --- math-139/notes/Hardy-Littlewood maximal functions#_theorem _ the boundedness of the Hardy-Littlewood operator|proof of the boundedness of the maximal operator]]. We first show weak $(1, 1)$-boundedness for $T$. We do Calderón-Zygmund decomposition at height $c \alpha$ to show that