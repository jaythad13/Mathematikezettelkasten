---
tags:
  - anal
  - math-135/7
---

Singularities are points where functions are undefined. We show that they can be categorised into (in increasing order of badness) removable singularities, poles, and essential singularities.

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

### Zeroes

Zeroes of a function are what you think they are.

##### _definition:_ zero of a function.

We say $z_{0}$ is a zero of $f$ if $f(z_{0}) = 0$.

Near a zero of the function, we have

##### _proposition:_ characterising holomorphic functions near zeroes

Suppose $\Omega$ is a region, and $f : \Omega \to \mathbb{C}$ is holomorphic and not identically zero. Then, for each zero $z_{0}$, there exists a neighbourhood $N_{r}(z_{0}) \subset \Omega$, in which $f(z) = (z - z_{0})^n g(z)$ for some holomorphic and non-vanishing $g : N_{r}(z_{0}) \to \mathbb{C}$.

###### _proof:_

By the contrapositive of the [[Complex Analysis --- math-135/notes/Cauchy integral formula|identity theorem]], we know that there is a punctured neighbourhood $N^*_{r}(z_{0})$ where $f$ does not vanish (otherwise $z_{0}$ would be a limit point of the zeroes of $f$).

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

If $f$ has a pole at $z_{0}$, the n there exists a punctured neighbourhood $N^*_{r}(z_{0})$ in which $f(z) = (z - z_{0})^{-n} h(z)$ for some holomorphic, non-vanishing $h(z)$. $h$ is unique.

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

Write out the [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#_proposition, definition _ principals and residues|principles and residues]] of $f$ —
$$
f(z) = \frac{a_{-n}}{(z - z_{0})^n} + \dots + \frac{a_{-1}}{z - z_{0}} + G(z).
$$
Integrate $f$ on the keyhole contour that avoids $z_{0}$. Then the integral reduces to the integral around a circle centred at $z_{0}$. The integrals of the principle part and $G(z)$ go to zero since they are all holomorphic on $\Omega \setminus \{ z_{0} \}$. All that remains is the integral of $\frac{a_{-1}}{z -z_{0}}$ over a circle centred at $z_{0}$. We calculated that this is $2 \pi ia_{-1}$ in the [[Complex Analysis --- math-135/attachments/homework/hw 2/hw 2.pdf#page=6|second homework]].

##### _corollary:_ the residue formula for many poles

For some open $\Omega \subset \mathbb{C}$ and meromorphic $f : \Omega \to \mathbb{C}$ with $n$ poles $\{ z_{i} \} \subset \Omega$. For any curve $\gamma$ enclosing $R \supset \{ z_{i} \}$ with $\overline{R} \subset \Omega$, we have
$$
\int_{\gamma} f(z) \, dz = 2 \pi i \sum_{i = 1}^n \operatorname{res}_{z_{i}}f.
$$

###### _proof sketch:_

Consider the keyhole deformation with keyholes around each pole $z_{i}$.