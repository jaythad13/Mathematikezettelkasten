---
tags:
  - anal
  - complex
  - math-135/7
  - math-135/8
---

Singularities are points where functions are undefined. We show that they can be categorised into (in increasing order of badness) removable singularities, poles, and essential singularities. Meromorphic functions are almost holomorphic, but they have poles at some points.

### Zeroes

Zeroes of a function are what you think they are.

##### _definition:_ zero of a function.

We say $z_{0}$ is a zero of $f$ if $f(z_{0}) = 0$.

Near a zero of the function, we have

##### _proposition:_ characterising holomorphic functions near zeroes

Suppose $\Omega$ is a region, and $f : \Omega \to \mathbb{C}$ is holomorphic and not identically zero. Then, for each zero $z_{0}$, there exists a neighbourhood $N_{r}(z_{0}) \subset \Omega$, in which $f(z) = (z - z_{0})^n g(z)$ for some holomorphic and non-vanishing $g : N_{r}(z_{0}) \to \mathbb{C}$.

###### _proof:_

By the contrapositive of the [[Complex analysis --- math-135/notes/Cauchy integral formula#_theorem _ identity theorem|identity theorem]], we know that there is a punctured neighbourhood $N^*_{r}(z_{0})$ where $f$ does not vanish (otherwise $z_{0}$ would be a limit point of the zeroes of $f$).

Consider the power series expansion of $f$ about $z_{0}$ in $N_{r}^*(z_{0})$ —
$$
f(z) = \sum_{n = 0}^\infty a_{n} (z - z_{0})^n.
$$
For the first $n$ such that $a_{n} \neq 0$, we can factor out $(z - z_{0})^n$ to get
$$
f(z) = (z - z_{0})^n \sum_{k = n}^\infty a_{n} (z - z_{0})^{k - n}.
$$
Then $g(z) = \sum_{k = n}^\infty a_{n}(z - z_{0})^{k - n}$ doesn't vanish in the punctured neighbourhood $N_{r}^*(z_{0})$ since that would make $f$ vanish.

### Poles

##### _definition:_ pole

Consider $f$, with $z_{0}$ a singularity of $f$. If there exists a neighbourhood $N_{r}(z_{0})$ in which the function
$$
g(z) = \begin{cases}
\frac{1}{f(z)} & z \neq z_{0} \\
0 & z = z_{0}
\end{cases}
$$
is holomorphic, then $z_{0}$ is a pole of $f$.

##### _proposition:_ meromorphic functions have polynomial denominators

If $f$ has a pole at $z_{0}$, then there exists a punctured neighbourhood $N^*_{r}(z_{0})$ in which $f(z) = (z - z_{0})^{-n} h(z)$ for some holomorphic, non-vanishing $h(z)$. $h$ is unique.

###### _proof:_

$1/f$ is holomorphic in $N^*_{r}(z_{0})$ and can be extended to $g$ which has a zero at $z_{0}$. Write
$$
g(z) = (z - z_{0})^n \eta(z)
$$
for some holomorphic non-vanishing $\eta(z)$. Then just choose $h = 1 / \eta$ to get the result.

##### _proposition, definition:_ principals and residues

If $f$ has a pole of order $n$ at $z_{0}$, then
$$
f(z) = \frac{a_{-n}}{(z - z_{0})^n} + \dots + \frac{a_{-1}}{z - z_{0}} + G(z)
$$

The first $n - 1$ negative coefficients are called the principal part, and $a_{-1}$ is called the residue.
###### _proof sketch:_

Apply power series to the previous result.

##### _theorem:_ calculating residues

If $f$ has a pole of order $n$ at $z_{0}$, then
$$
\operatorname{res}_{z_{0}}f = \lim_{ z \to z_{0} } \frac{1}{(n - 1)!} \frac{d^{n - 1} \left( (z - z_{0})^n f \right )}{dz^{n - 1}} (z).
$$

###### _proof sketch:_

The multiplication gets rid of the principal part, the derivatives get rid of everything else but add a factorial.

We're finally ready to talk about meromorphic functions!

### Meromorphic functions

##### _definition:_ meromorphic functions

For any open $\Omega \subset \mathbb{C}$ and $f : \Omega \to \mathbb{C}$, if there exists $\{ z_{i} \} \subset \Omega$ such that
1) $f$ is holomorphic on $\Omega \setminus \{ z_{i} \}$
2) $\{ z_{i} \}$ has no limit point
3) $f$ has poles at the $z_{i}$, 
we say $f$ is meromorphic.

##### _theorem:_ the residue formula

For some open $\Omega \subset \mathbb{C}$ and meromorphic $f : \Omega \to \mathbb{C}$ with a single pole $z_{0} \in \Omega$, any disc $D$ containing $z_{0}$ with $\overline{D} \subset \Omega$ gives
$$
\int_{\partial D} f(z) \, dz = 2 \pi i \operatorname{res}_{z_{0}}f
$$

###### _proof sketch:_

Write out the [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_proposition, definition _ principals and residues|principles and residues]] of $f$ —
$$
f(z) = \frac{a_{-n}}{(z - z_{0})^n} + \dots + \frac{a_{-1}}{z - z_{0}} + G(z).
$$
Integrate $f$ on the keyhole contour that avoids $z_{0}$. Then the integral reduces to the integral around a circle centred at $z_{0}$. The integrals of the principle part and $G(z)$ go to zero since they are all holomorphic on $\Omega \setminus \{ z_{0} \}$. All that remains is the integral of $\frac{a_{-1}}{z -z_{0}}$ over a circle centred at $z_{0}$. We calculated that this is $2 \pi ia_{-1}$ in the [[Complex analysis --- math-135/attachments/homework/hw 2/hw 2.pdf#page=6|second homework]].

##### _corollary:_ the residue formula for many poles

For some open $\Omega \subset \mathbb{C}$ and meromorphic $f : \Omega \to \mathbb{C}$ with $n$ poles $\{ z_{i} \} \subset \Omega$. For any curve $\gamma$ enclosing $R \supset \{ z_{i} \}$ with $\overline{R} \subset \Omega$, we have
$$
\int_{\gamma} f(z) \, dz = 2 \pi i \sum_{i = 1}^n \operatorname{res}_{z_{i}}f.
$$

###### _proof sketch:_

Consider the keyhole deformation with keyholes around each pole $z_{i}$.

### Removable singularities

Removable singularities are fake singularities — the "singularity" in a function like $z / z$ perhaps.

##### _definition:_ removable singularity

If $f : \Omega \to \mathbb{C}$ has a singularity $z_{0}$, but can be extended to a a holomorphic function $g$ with $g = f$ everywhere that is not $z_{0}$, $z_{0}$ is a removable singularity of $f$.

##### _theorem:_ Riemann's theorem on removable singularities

Consider $f : \Omega \to \mathbb{C}$ for some open $\Omega \subset \mathbb{C}$, where $f$ is holomorphic with a singularity $z_{0} \in \Omega$. If $f$ is bounded on a punctured neighbourhood $N_{r}^*(z_{0})$, $z_{0}$ is a removable singularity.

###### _proof sketch:_

For a disk $D$ centred at $z_{0}$ with $\overline{D} \subset \Omega$, consider the keyhole contour to define the extension of $f$ at $z_{0}$. The inner contour goes to zero since $f$ is bounded and we are left to define
$$
f(z_{0}) = \int_{\partial D} \frac{f(z)}{z - z_{0}} \, dz 
$$

##### _corollary:_ $f$ is unbounded near poles

If $f$ is a meromorphic function with an isolated singularity at $z_{0}$, $f$ has a pole at $z_{0}$ if and only if $\lvert f(z) \rvert \to \infty$.

###### _proof:_

If $f$ has a pole at $z_{0}$, there is some holomorphic $g$ with $g(z) = 1/f(z)$ for $z \neq z_{0}$ and $g(z) = 0$. Thus, $g(z) \to 0$ near $z_{0}$, and $\lvert f(z) \rvert = \lvert 1/g(z) \rvert \to \infty$.

If $\lvert f(z) \rvert \to \infty$ as $z \to z_{0}$ then $1 / f$ is holomorphic for all $z \neq z_{0}$ and is bounded near $z_{0}$. Thus, $1/f$ has a removable singularity at $z_{0}$. Then there is $g$, the extension of $1/f$ which is holomorphic around $z_{0}$ and $f = 1 / g$ except at $z_{0}$. Since $1 / \lvert f(z) \rvert \to 0$ as $z \to z_{0}$, $g(z_{0})$ must be $0$.

### Essential singularities

##### _definition:_ essential singularity

An essential singularity is an isolated singularity of a function that is not a pole nor a removable singularity.

##### _theorem:_ Casorati-Weierstrass

If $f$ is holomorphic in $D_{r}^*(z_{0})$ with $z_{0}$ an essential singularity of $f$, then $f^\text{img}(D_{r}^*(z_{0}))$ is dense in $\mathbb{C}$.

###### _proof:_

Suppose the image of $D_{r}^*(z_{0})$ is not dense. Then there must be a point $w$ such that $D_{\delta}(w)$ contains none of the image of $D_{r}^*(z_{0})$. 

Consider $g(z) = \frac{1}{f(z) - w}$ on $D_{r}^*(z_{0})$. Note that $\lvert g(z) \rvert < 1 / \delta$, and thus, $g$ is bounded and holomorphic around $z_{0}$. Then $g$ just has a removable singularity at $z_{0}$. If we extend $g$ by $g(z_{0}) = 0$, then $f(z) - w$ has a pole at $z_{0}$. Otherwise, if $g(z_{0}) \neq 0$, $f(z) - w$ is holomorphic. In either case, $f$ cannot now have an essential singularity.

### Singularities at $\infty$

It turns out to be important to be useful to think of these functions on the [[Complex analysis --- math-135/notes/The extended complex plane|extended complex plane]] as well.

##### _definition:_ singularity at $\infty$

Given $f  : \mathbb{C} \setminus D_{r}(0) \to \mathbb{C}$ is holomorphic, if $F(z) = f\left( \frac{1}{z} \right)$ has a removable singularity/pole/essential singularity at $0$, we say $f$ has a removable singularity/pole/essential singularity at infinity.

##### _definition:_ meromorphic on the extended complex plane

We say some meromorphic $f : \mathbb{C} \to \mathbb{C}$ is meromorphic on the extended complex plane, if $f$, at worst, has a pole at $\infty$. That is, $f$ may be holomorphic, have a removable singularity or have a pole, but may not have an essential singularity there.

##### _theorem:_ classifying meromorphic functions on the extended complex plane

$f$ is meromorphic on the extended complex plane if and only if $f$ is a rational function.

###### _proof:_

Since $f$ is meromorphic on the extended complex plane, $F(z) = f\left( \frac{1}{z} \right)$ is holomorphic on $D_{r}(0)$, or has a pole/removable singularity at $0$. In any case $F$ is certainly holomorphic on some $D^*_{r}(0)$. But then $f$ is holomorphic for all $z$ with $\frac{1}{z} \in D_{r}^*(z_{0})$. That is, $f$ is holomorphic on $\mathbb{C} \setminus D_{r}(0)$.

Write $h$ as $f$ less the principal parts $f_{k}$ of each of the poles $z_{k}$. Thus, near $z_{k}$, where $f(z) = f_{k}(z) + g_{k}(z)$ for some holomorphic $g_{k}$ we only have removable singularities. Thus, $h$ can be extended to an entire function. Similarly, remove the pole at infinity. That means we $F(z) = f\left( \frac{1}{z} \right)$ only has removable singularity at $0$. Thus, $h$ must be bounded everywhere.

Thus, by [[Complex analysis --- math-135/notes/Cauchy integral formula#_theorem _ Liouville's theorem|Liouville's theorem]], we have that (the extension of $h$, and thus,) $h$ is a constant. But then $f$ is just the sum of principal parts, the pole at infinity and a constant. That is, a rational function.