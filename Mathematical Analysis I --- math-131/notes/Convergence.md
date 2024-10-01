---
tags:
- math-131/10
---

Here we deal with the intuitive notion of convergence by making it rigorous for metric spaces, As usual, $X$ is a metric space with metric $d$.

##### _definition:_ sequence

A sequence is a function $\{ x_{n} \}_{n} : \mathbb{N} \to X$ with $n \mapsto x_{n}$.

##### _definition:_ convergence

Suppose $\{ x_{n} \}_{n}$ is a sequence in $X$. We say that $\{ x_{n} \}_{n}$ converges to $x \in X$, or $x_{n} \to x$ or $\lim_{ n \to \infty } x_{n} = x$ if, for each $\varepsilon > 0$ there exists some $N \in \mathbb{N}$ such that $d(x_{n}, x) < \varepsilon$ for all $n \ge N$.

Equivalently, $\{ x_{n} \}_{n}$ converges to $x$ if every neighbourhood $N_{r}(x)$ contains all but finitely many $x_{n}$.

##### _example:_ using the Archimedean property

The sequence $\{ 1/n \}_{n}$ converges in $\mathbb{R}$ to $0$ by the [[Mathematical Analysis I --- math-131/attachments/homework/hw 1/hw 1.pdf#page=4|Archimedean property]].

##### _proposition:_ convergent sequences are bounded

If a sequence converges, it must be bounded.

###### _proof sketch:_

For all the infinitely many $x_{n}$ with $n \ge N$ we can bound the sequence to within distance $\varepsilon$ of what it converges to, and for the rest of the finitely many $x_{n}$, they are bounded by the maximum of their distances from $x$.

However, the converse isn't true.

##### _example:_ non-convergent bounded sequence

$\{ (-1)^n \}_{n}$ is a bounded sequence that doesn't converge.

##### _proposition:_ limit points induce convergent sequences

If $x$ is a [[Analysis --- rudin/notes/Metric spaces#_definition _ limit point|limit point]] of $E \subset X$, then there is a sequence $\{ x_{n} \}_{n}$ in $E$ converging to $x$.

###### _proof sketch:_

Choose $x_{n}$ to be some point of $E$ such that $x_{n} \in N_{1 / n}(x)$.

##### _proposition:_ the continuity of operations on the complex numbers

If $a_{n} \to A$ and $b_{n} \to B$, then $a_{n} + b_{n} \to A + B$ and $a_{n} b_{n} \to AB$. If $b_{n} \neq 0$ for all $n$ and $B \neq 0$, then $a_{n} / b_{n} \to A / B$.

###### _proof sketch:_

For $\varepsilon > 0$, choose $N_{a}, N_{b}$ such that $\lvert A - a_{n} \rvert < \frac{\varepsilon}{2}$ and $\lvert B - b_{n} \rvert < \frac{\varepsilon}{2}$ for all $n$. Thus, by the triangle inequality $\lvert A + B - (a_{n} + b_{n}) \rvert < \varepsilon$. Thus $a_{n} + b_{n} \to A + B$.

Notice that $AB - a_{n} b_{n} = - (A - a_{n})(B - b_{n}) - A(B - b_{n}) - B(A - a_{n})$. Thus by choosing sufficiently large $n$, we get
$$
\lvert AB - a_{n} b_{n} \rvert < \lvert A - a_{n} \rvert \lvert B - b_{n} \rvert + \lvert A \rvert  \lvert B - b_{n} \rvert + \lvert B \rvert  \lvert A - a_{n} \rvert < \varepsilon
$$
for any $\varepsilon$ we choose. Thus $a_{n} b_{n} \to AB$.

First we show $\frac{1}{b_{n}} \to \frac{1}{B}$ under our hypotheses. Let $b_{n}$ be bounded with $m < \lvert b_{n} \rvert < M$ which we know is true since it converges. Further, since all $b_{n} \neq 0$, we know $m > 0$. Thus,
$$
\left\lvert  \frac{1}{B} - \frac{1}{b_{n}}  \right\rvert = \frac{\lvert b_{n} - B \rvert }{b_{n} B} < \frac{\lvert b_{n} - B \rvert  m}{B}
$$
which we can make as small as we want by choosing $n$ sufficiently large. Then, it follows by the proof of convergence of products that $a_{n} / b_{n} \to A / B$.

##### _proposition:_ component-wise convergence — the projection principle

Let $y_{n} = (y_{n_{1}}, \dots, y_{n_{k}}) \in \mathbb{R}^k$. $y_{n} \to y = (y_{1}, \dots, y_{k})$ if and only if $y_{n_{i}} \to y_{i}$ for each $i \in \{ 1, \dots, k \}$.

###### _proof:_

Suppose $y_{n} \to y$. If $n > N$ gives $\lVert y - y_{n} \rVert < \varepsilon$, then since $\lVert y - y_{n} \rVert^{2} < \varepsilon^{2}$, each $(y_{i} - y_{n_{i}})^{2} < \varepsilon^{2}$, and thus, $\lvert y_{i} - y_{n_{i}} \rvert < \varepsilon$ for all $n > N$.

Suppose $y_{n_{i}} \to y_{i}$ for all $i \in \{ 1, \dots, k \}$. Then choose $N$ such that $n > N$ gives us $\lvert y_{n_{i}} - y_{i} \rvert < \frac{\varepsilon}{\sqrt{ k }}$. Thus the sum of their squares $\lVert y - y_{n} \rVert^{2}$ is less than $\varepsilon^{2}$. Thus, $\lVert y - y_{n} \rVert < \varepsilon$.

##### _example:_ projection principle breaks in infinite dimensions

Consider $y_{n} = (0, \dots, 0, 1, 0, \dots) \in \mathbb{R}^\infty$. Though each $y_{n_{i}}$ converges to $0$, $\lVert y_{n} \rVert = 1$ always, and thus, $y_{n_{i}}$ does not converge.