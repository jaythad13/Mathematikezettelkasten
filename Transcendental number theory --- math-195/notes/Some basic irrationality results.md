---
tags:
- nt
- math-195/1
- math-195/2
---

What is transcendental number theory?

> Searching for hay in a haystack

\- Lenny Fukshansky

Even though $\mathbb{R} = \mathbb{Q} \sqcup (\mathbb{R} \setminus \mathbb{Q})$ and $\mathbb{R} = \overline{\mathbb{Q}} \sqcup (\mathbb{R} \setminus  \overline{\mathbb{Q}})$ are decompositions into countable and uncountable parts respectively, it's much easier to prove rationality or algebraicity of a number than to prove irrationality or transcendence.

##### _definition:_ floor function, fractional part, distance to the closest integer

For any $x \in \mathbb{R}$ we have $x \in [n, n + 1)$ for some $n \in \mathbb{Z}$. The **floor** of $x$ is $\lfloor x \rfloor = n$ and the **fractional part** of $x$ is $\{ x \}$. 

For $x$, the **distance to the closest integer** is $\lVert x \rVert = \min \{ \{ x \}, 1 - \{ x \} \}$.

---

These functions are useful — for example, they give a quick proof that $\mathbb{Q}$ is dense in $\mathbb{R}$ using the archimedean property of $\mathbb{R}$. It gives easily that $(\beta - \alpha) n > 1$ and then $\alpha n \leq \lfloor \alpha  n \rfloor + 1 < \beta n$. Then dividing through gives a rational between any two reals $\beta$ and $\alpha$. In the same way, given an irrational number, we can squeeze an irrational between any two rationals.

We give the classic example, but with a new "better" proof. The usual proof generalises to show that the square root of any prime is irrational, but doesn't help to prove a number is irrational without any known algebraicity conditions.

##### _theorem:_ $\sqrt{ 2 }$ is irrational

There is no rational $\alpha$ such that $\alpha^{2} = 2$.

###### _proof:_

Suppose by way of contradiction that $\alpha = p / q \in \mathbb{Q}$. We know (by elementary bounds) that $0 < \alpha - 1 < 1 / 2$. Let $\varepsilon = \alpha - 1$. Then $0 < \varepsilon^n < 1 / 2^n$. By the binomial theorem,
$$
\varepsilon^n = \sum_{k = 0}^n \binom{n}{k} \alpha^k (-1)^{n - k}.
$$
$\alpha^k$ is either an integer or an integer times $\alpha$ depending on the parity of $k$ (we know $\alpha$ is not an integer). Thus, $\varepsilon^n = a_{n} + b_{n} \alpha$. Using the expression $\alpha = p / q$ we can write this as
$$
\varepsilon^n = \frac{a_{n} q + b_{n} p}{q} = \frac{c_{n}}{q}
$$
Since $\varepsilon^n$ is positive, $c_{n}$ must be a positive integer, and at least $1$. But then $1 / q \leq \varepsilon^n < 1 / 2^n$. Looking at large enough $n$, we get a contradiction.

---

We get a silly corollary from this.

##### _corollary:_ irrational power of an irrational can be rational

There exist irrational numbers $a, b \in \mathbb{R} \setminus \mathbb{Q}$ such that $a^b$ is rational.

###### _proof:_

Either $\sqrt{ 2 }^{\sqrt{ 2 }}$ is rational or $(\sqrt{ 2 }^{\sqrt{ 2 }})^{\sqrt{ 2 }} = \sqrt{ 2 }^2 = 2$ is the $\sqrt{ 2 }$th power of an irrational number.

---

This is a little unsatisfactory because we don't know which is irrational. Kuzmin proved that $\sqrt{ 2 }^\sqrt{ 2 }$ is irrational in 1930, but this is very difficult. This is a special case of of the Gelfond–Schneider theorem.

Returning to irrationality results, the crucial idea of having an upper bound that goes to zero and a lower bound that is fixed is generalisable! For example, we can prove $e$ is irrational. We should probably decide on a definition of $e$ first.

##### _definition:_ $e$

$e$ is the unique real number such that the function $f(x) = e^x$ satisfies the differential equation $f' = f$.

---

##### _theorem:_ $e$ is irrational

###### _proof:_

Suppose by way of contradiction that $e = p / q \in \mathbb{Q}$.

For $n \geq 0$ let $I_{n} = \int_{0}^1 x^n e^x \, dx$. Since the integrand is positive and continuous on $(0, 1)$, so is the integral. Obviously, $I_{0} = e$. Integrating by parts we see that $I_{1} = (x e^x - e^x) \Big |_{0}^1 = 1.$ 

We claim that in general, $I_{n} = a_{n} + b_{n} e$ with $a_{n}, b_{n} \in \mathbb{Z}$. We show this by induction. Suppose $I_{n - 1}  = a_{n - 1} + b_{n - 1} e$. Integrating by parts
$$
\begin{align}
I_{n} & = \int x^n e^x \, dx  \\
& = (x^n \int e^x \, dx) \Big |_{0}^1  - n \int_{0}^1 x^{n - 1} e^x \, dx \\
 & = e - n(a_{n - 1} + b_{n - 1} e) \\
 & = -n a_{n - 1} + (- n b_{n - 1} + 1) e.
\end{align}
$$

Again, we play the same trick to get
$$
I_{n} = \frac{a_{n} q + b_{n} p}{q} = \frac{c_{n}}{q}
$$
for some positive integer $c_{n} > 1$. But we can bound $I_{n}$ as follows —
$$
\begin{align}
I_{n} & = \int_{0}^1 x^n e^x \, dx  \\
 & = e \int_{0}^1 x^n \, dx  \\
 & = \frac{e}{n + 1}.
\end{align}
$$
Again, this gives a contradiction for large enough $n$.


---

This trick goes even further to prove irrationality of $\pi$! The trouble is that the thing we're bounding gets even more complicated.

##### _theorem:_ $\pi$ is irrational

###### _proof:_

Suppose by contradiction that $\pi$ is rational, and so $\pi / 2 = a/b \in \mathbb{Q}$.

For each $n \in \mathbb{N}$ define
$$
I_{n}(x) = \int_{-1}^1 (1 - z^{2})^n \cos(xz) \, dz.
$$
It can be proved by integration by parts (twice) that, for all $n > 2$,
$$
x^{2} I_{n}(x) = 2n(2n - 1) I_{n - 1}(x) - 4n(n - 1)I_{n - 2}(x).
$$
Now define $J_{n}(x) = x^{2n + 1} I_{n}(x)$ to get the identity
$$
J_{n}(x) 2n(2n - 1)J_{n - 1}(x) - 4n(n - 1) x^{2} J_{n - 2}(x).
$$
Finally, compute
$$
J_{0}(x) = 2 \sin x
$$
and
$$
J_{1}(x) = - 4x \cos x + 4 \sin x.
$$

By induction, we can prove that
$$
J_{n}(x) = n!  (p_{n}(x) \sin x + q_{n}(x) \cos x)
$$
where $p_{n}, q_{n}$ are polynomials in $\mathbb{Z}[x]$ of degree at most $n$. Evaluating at $\pi / 2$ we get
$$
(\pi / 2)^{2n + 1} I_{n}(\pi / 2) = J_{n}(\pi / 2) = n! p_{n}(\pi / 2).
$$
Rewriting with $\pi / 2 = a / b$ we get
$$
\frac{a^{2n + 1}}{n!} I_{n}(\pi / 2) = b^{2n + 1} p_{n}(\pi / 2).
$$

We can compute a bound on $I_{n}(\pi / 2)$.
$$
\begin{align}
I_{n}(\pi / 2) & = \int_{-1}^1 (1 - z^{2})^n \cos(\pi z) \, dz \\
 & \leq \int_{-1}^1 (1 - z^{2})^n \, dx  \\
 & \leq C
\end{align}
$$
Also, since the integrand is positive, so is the integral. This implies that $p_{n}(\pi / 2)$ must also always be positive. Since $b^{2n + 1}$ is greater than any denominator in $p_{n}(\pi / 2)$ (it has integer coefficients and degree at most $n$) then $p_{n}(\pi / 2)$ is bounded below by $1$. But the other side $I_{n}(\pi / 2) a^{2n + 1} / n! \to 0$ as $n \to \infty$ so we have a contradiction. 

---

However, we don't just want irrationality results. We also want to know how well these irrationals can be approximated by rationals. For example, we can get a baby version of Dirichlet's theorem for $\sqrt{ 2 }$. It tells us that in order to get better rational approximations to $\sqrt{ 2 }$, the rational approximations must have larger and larger denominators.

##### _theorem:_ Dirichlet's theorem for $\sqrt{ 2 }$

For any $a, b \in \mathbb{N}$ we must have $\lvert \sqrt{ 2 } - a / b \rvert \geq 3 b^{2}$.

###### _proof:_

Since $\sqrt{ 2 }$ is not rational, we must have $2b^{2} \neq a^{2}$ and so $\lvert 2b^{2} - a^{2} \rvert \geq 1$. Factoring we get
$$
\lvert \sqrt{ 2 } - a / b \rvert \geq \frac{1}{(\sqrt{ 2 } b + a) b} = \frac{1}{b^{2} (\sqrt{ 2 } + a / b)}.
$$
If $\sqrt{ 2 } + a / b \leq 3$ we are done. 

Suppose $b = 1$ (that is, $a / b$ is an integer). Then $\lvert \sqrt{ 2 } - a \rvert > \sqrt{ 2 } - 1 > 1 / 3$. Thus, if $b = 1$ we have $\lvert \sqrt{ 2 } - a / b \rvert \geq 1 / 3 b^{2} = 1 / 3$.

Suppose $b \geq 2$. If $\sqrt{ 2 } + a / b > 3$ then $a / b > 3 - \sqrt{ 2 } > 3 / 2$. Then $\lvert a / b - \sqrt{ 2 } \rvert > 3 - 2 \sqrt{ 2 } > 1 / 12$. But then $b \geq 2$ implies $1 / 12 \geq 1 / 3b^{2}$ so we have the desired inequality.

---