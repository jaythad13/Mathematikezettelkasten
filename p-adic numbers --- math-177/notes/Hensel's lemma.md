---
tags:
- alg-nt
- math-177/8
- math-177/9
- math-177/18
---

Hensel's lemma allows us to solve diophantine equations over $\mathbb{Q}_{p}$ by solving them over [[p-adic numbers --- math-177/notes/The p-adic numbers#Residue fields and the ring structure of $ mathbb{Z}_{p}$|its residue field]] $\mathbb{F}_{p}$. In some sense, you can think of it as an intermediate value theorem or Newton's method. If $f(z_{0})$ is zero modulo $p$, then it is sort of small. Hensel's lemma says that as long as this isn't a local minimum or local maximum, we can find an actual zero.

##### _example:_ Hensel's lemma in action

We can show that $\sqrt{ -1 } \in \mathbb{Z}_{5}$. This follows since $f = x^{2} + 1 \in \mathbb{Z}_{p}[x]$ has $f(2) \neq 0 \pmod 5$ and $f' = 2x$ has $f'(2) \neq 0 \pmod 5$. We constructed this in a manner similar to the proof of Hensel's lemma on [[p-adic numbers --- math-177/attachments/homework/hw 3/hw 3.pdf#page=3|the homework]]. In fact there are two square roots since we also have $f(3) \neq 0 \pmod{5}$ and $f'(3) \neq 0 \pmod 5$. This is the additive inverse of the one we constructed previously.

---

To prove Hensel's lemma however, we need another lemma about formal derivatives. Essentially this says that if $p \mid y$, then $f(x + y) = f(x) \pmod p$.

##### _lemma:_ [[Analysis --- math-131/notes/Mean value theorems#Taylor's theorem|Taylor's theorem]] for formal derivatives

For any $f \in \mathbb{Z}_{p}[x]$ we have
$$
f(x + y) = f(x) + f'(x) y + g(x, y) y^{2}
$$
for some polynomial $g \in \mathbb{Z}_{p}[x, y]$.

###### _proof:_

Suppose $f(x) = a_{0} + a_{1} x + \dots + a_{n} x^n$. Then 
$$
f(x + y) = \sum_{i = 0}^n a_{i} \sum_{k = 0}^i \binom{i}{k} x^{i - k} y^k
$$
by [[Superdiscrete --- math-55A/notes/The binomial theorem#_theorem _ the binomial theorem|the binomial theorem]]. We can rewrite this as
$$
\begin{align}
f(x + y) & = \sum_{i = 0}^n a_{i} (x^i + i y x^{i - 1} + y^{2} g_{i}(x)) \\
 & = \sum_{i = 0}^n a_{i} x^i + y \sum_{i = 0}^n i a_{i} x^{i - 1} + y^{2} \sum_{i = 0}^n a_{i} g_{i}(x, y) \\
 & = f(x) + f'(x) y + g(x, y) y^{2}
\end{align}
$$
choosing $g(x, y) = \sum_{i = 0}^n a_{i} g_{i}(x, y)$.

---

##### _lemma:_ Hensel's lemma

Suppose $f \in \mathbb{Z}_{p}[x]$ and there is some $z_{1} \in \mathbb{F}_{p}$ with $f(z_{1}) = 0 \pmod p$ and $f'(z_{1}) \neq 0 \pmod p$. Then there exists a unique $z \in \mathbb{Z}_{p}$ with $z = z_{0} \pmod p$ and $f(z) = 0$.

###### _proof:_

We recursively construct a sequence of [[p-adic numbers --- math-177/notes/The p-adic numbers#_definition _ $p$-adic integers, $ mathbb{Z}_{p}$|compatible residues]] $z_{n}$ such that $f(z_{n}) = 0 \pmod {p^n}$. It follows then that $f(z) = 0$ for $z$ given by the residue sequence $z_{n}$.

$z_{1}$ is the first element of our sequence. Suppose we have term $z_{n}$. We want to construct $z_{n + 1} = z_{n} + q p^n$ such that $f(z_{n + 1}) = 0$. (We can choose $q$). By our previous lemma
$$
\begin{align}
f(z_{n + 1}) & = f(z_{n}) + f'(z_{n}) q p^n + g(x, y) q^{2} p^{2n} \\
 & = 0 + p^n(f'(z_{n}) q + g(x, y) q^{2} p^n)
\end{align}
$$
Since $z_{n} = z_{0} \pmod p$ we have $f'(z_{n}) = f'(z_{0}) \neq 0 \pmod{p}$. Thus, $f'(z_{n})$ is a unit in $\mathbb{F}_{p}$. Thus, we can choose $q$ so that $f'(z_{n}) q = - g(x, y) q^{2} p^n \pmod p$. That is, we can choose $q$ such that $f'(z_{n}) q + g(x, y) q^{2} p^n$ is divisible by $p$. Thus,  $f(z_{n + 1}) = 0 + p^{n + 1} q'$ which is $0$ modulo $p^{n + 1}$. By induction we are done (with construction).

We are only left to show uniqueness.

---

##### _corollary:_ lifting roots

Suppose $f \in \mathbb{Z}[x]$ and there is some $z_{1} \in \mathbb{Z} / (p)$ such that $f(z_{1}) = 0 \pmod{p}$ and $f'(z_{1}) \neq 0 \pmod{p}$. Then for each $n \in \mathbb{N}$, there is some $z_{n} \in \mathbb{Z} / (p^n)$ such that $f(z_{n}) = 0 \pmod{p^n}$.

---

In fact, Hensel's lemma works for any finite extension $\mathbb{K} / \mathbb{Q}_{p}$. Just replace $p$ with the [[p-adic numbers --- math-177/notes/Rings of integers and ramification#_proposition, definition _ the maximal ideal is principal, uniformiser|uniformiser]] $\pi$. The proof goes through! That is to say,

##### _theorem:_ Hensel's lemma for extensions of $\mathbb{Q}_{p}$

Suppose $\mathbb{K}$ is a finite extension of $\mathbb{Q}_{p}$, $f \in \mathscr{O}_{\mathbb{K}}[x]$ and $z_{1} \in \mathscr{O}_{\mathbb{K}}$ has $f(a) \equiv 0$ and $f'(z_{1}) \not \equiv 0$ in $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$. Then there exists a unique $z \in \mathscr{O}_{\mathbb{K}}$ such that $f(z) = 0$ and $z \equiv z_{1}$ in $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$.

---