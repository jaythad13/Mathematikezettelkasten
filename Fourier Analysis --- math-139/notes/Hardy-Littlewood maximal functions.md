---
tags:
- math-139/35
- fourier
- anal
---

Given a reasonable function $f : \mathbb{R}^n \to \mathbb{C}$, the Hardy-Littlewood maximal function gives a "maximum moving average" of the function that is useful in determining convergence properties for [[Fourier Analysis --- math-139/notes/The Fourier transform|Fourier transforms]] and other objects in harmonic analysis.

##### _definition:_ Hardy-Littlewood maximal function, maximal operator

Given a function $f : \mathbb{R}^n \to \mathbb{C}$ that is locally $L^1$, its maximal function is $Mf : \mathbb{R} \to \mathbb{C}$ given by
$$
Mf(x) : \sup_{B \ni x} \frac{1}{\lvert B \rvert } \int_{B} \lvert f(x) \rvert  \, dx
$$
where $B$ is a ball centred at $x$, and $\lvert B \rvert$ is its volume.

The maximal operator is $M : f \mapsto M f$.

This comes from Hardy wanting a way to measure a batsman's worth. It's very kind to batsmen — a good batsman in bad form is valued highly, and so is a bad batsman in good form. In some sense, this is why it's a good "maximum".

Also note that the fact that $B$ is a ball (or equivalently, a cube) matters — there could be thin slivers in only one direction where the function has different behaviour. Thus, we can't integrate over a rectangle and get the same results. This essentially has to do with the fact that we contain a ball $B$ inside a cube $Q$ and the cube inside a larger dilated ball with $\lvert B \rvert < \lvert Q \rvert < c \lvert B \rvert$, whereas this is not true when $Q$ is a rectangle.

Finally, balls and the standard measure on $\mathbb{R}^n$ can actually be replaced with more general objects called balls that satisfy some properties with respect to a Borel measure.

> Maximal functions, singular integrals, and square functions can be thought of as a threefold unity.

\- Eli Stein.

We can also define the uncentred Hardy-Littlewood maximal function which considers integrals over uncentred balls. $\tilde{M} f$ is equivalent to $M f$ since $Mf \le \tilde{M} f \le c M f$, where $c$ is independent of . We see this by containing an uncentred ball $\tilde{B}$ in a centred ball $B$ thrice its size and noticing that we can choose $c$ to only depend n the volume of the ball.

##### _definition:_ uncentred Hardy-Littlewood maximal function, maximal operator

Given a function $f : \mathbb{R}^n \to \mathbb{C}$ that is locally $L^1$, its maximal function is $\tilde{M}f : \mathbb{R} \to \mathbb{C}$ given by
$$
\tilde{M}f(x) : \sup_{B \ni x} \frac{1}{\lvert B \rvert } \int_{B} \lvert f(x) \rvert  \, dx
$$
where $B$ is a ball containing $x$, and $\lvert B \rvert$ is its volume.

##### _theorem:_ the boundedness of the Hardy-Littlewood operator

If $f \in L^p$, then $\lVert M f \rVert_{p} \le c_{p} \lVert f \rVert_{p}$ where $c_{p}$ is a constant that only depends on $p$.

###### _proof:_

To prove this we need to show that $M$ is bounded on $L^\infty$. This is obvious because we defined it to be the supremum of a bounded set of integrals. 

We also need weak $(1, 1)$-boundedness for $f$ and $Mf$. That is, for any $\alpha > 0$, we want
$$
\lvert \{ x \in \mathbb{R}^n \mid Mf > \alpha \} \rvert \le \frac{c}{\alpha} \lVert f \rVert _{L^1}.
$$
If we had $L^1$ boundedness for $Mf$, then we would have which implies weak boundedness by the following chain of inequalities
$$
\alpha \lvert \{ x \in \mathbb{R}^n \mid Mf > \alpha \} \rvert \le \lVert Mf \rVert _{L^1} \le c \lVert f \rVert _{L^1}.
$$

We will show boundedness even without $\lVert Mf \rVert_{L^1} < \infty$ using the [[#_lemma _ Vitali covering lemma (or perhaps not)|Vitali covering lemma]]. Let $E_{\alpha} = \{ x \in \mathbb{R}^n \mid \tilde{M}f > \alpha \}$, and let $E \subseteq E_{\alpha}$ be a compact subset. Apply the Vitali covering lemma to get
$$
E \le c \sum_{j = 1}^k \lvert \tilde{B}_{j} \rvert < c \sum_{i = 1}^k \frac{1}{\alpha} \int_{B_{k}} \lvert f(x) \rvert  \, dx < \frac{1}{\alpha} \lVert f \rVert _{L^1}.
$$

Now, using the $L^1$ and $L^\infty$ bounds we can use the trick of Marcinkiewicz interpolation to get $L^p$. 

##### _lemma:_ Vitali covering lemma (or perhaps not)

For $n > 0$, there exists a constant $c > 0$ such that given any measurable $E \subseteq \mathbb{R}^n$ and a cover by balls
$$
E = \bigcup_{j = 1}^n B_{j},
$$
there exists a disjoint sub-cover $\{ \tilde{B}_{j} \}$ such that they cover $c$ part of the volume of $E$ —
$$
\sum_{j} \lvert \tilde{B}_{j} \rvert \geq c \lvert E \rvert .
$$
###### _proof sketch:_

Be greedy — pick the biggest ball you can at every stage.

For any balls not included, they must intersect a bigger ball. Thus, the union of the balls obtained by tripling the radius all the $\tilde{B}_{j}$ covers all of $E$. These "triple balls" of course have $3^n$ times the volume of the original balls which is a constant only depending on $\mathbb{R}^n$. Choose $c = 1/3^n$.

