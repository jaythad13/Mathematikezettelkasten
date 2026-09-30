---
tags:
- alg-nt
- math-172/6
- math-172/8
- math-172/9
---

Galois theory is about finding roots to polynomials. The simplest case is that of quadratic number fields.

##### _definition:_ (real, imaginary) quadratic number fields

A **quadratic number field** is $\mathbb{Q}[\sqrt{ d }]$ for some square free $d \in \mathbb{Q}$.

Equivalently, it is a [[Transcendental number theory --- math-195/notes/Number fields#_definition _ number field|number field]] of degree $2$.

If $d > 0$, then $\mathbb{Q}[\sqrt{ d }]$ is a **real quadratic number field**. Else, $\mathbb{Q}[\sqrt{ d }]$ is an **imaginary quadratic field**.

---

Note, $\mathbb{Q}[\sqrt{ d }]$ is in fact a field. It's a domain ($x^{2} - d$ is irreducible and thus, prime), finite-dimensional over $\mathbb{Q}$. Since multiplication by any number is $\mathbb{Q}$-linear and injective, multiplication by any number has an inverse.

![[Algebraic geometry --- rising-sea/notes/Integral dependence and integral homomorphisms#_example _ quadratic integer rings|Integral dependence and integral homomorphisms]]

We will often think about ideals of $\mathscr{O}_{\mathbb{K}}$ as special $\mathbb{Z}$-submodules, which we call **sublattices**. 

##### _proposition:_ characterising ideals among sublattices

Suppose $\mathscr{O}_{\mathbb{K}} = \mathbb{Z}[\eta] \subseteq \mathbb{K}$, for some imaginary quadratic number field $\mathbb{K} / \mathbb{Q}$. Then a sublattice $M \subseteq \mathscr{O}_{\mathbb{K}}$ is an ideal if and only if $\eta M \subseteq M$.

---

### Imaginary quadratic number fields

When $d < 0$, we have some extra tools.

##### _definition:_ norm

Suppose $\mathbb{Q}(\sqrt{ d })$ is an imaginary quadratic number field. Suppose $\alpha = a + b \sqrt{ d }$.

The **norm** is $N : \mathscr{O}_{\mathbb{Q}(\sqrt{ d })} \to \mathbb{Z}$ by $\alpha \mapsto a^{2} - b^{2} d$. It is multiplicative and positive definite.

---

This is a useful definition!

##### _proposition:_ characterising units in an imaginary quadratic number field

Suppose $\mathbb{K}$ is an imaginary quadratic number field. Then $\alpha \in \mathscr{O}_{\mathbb{K}}$ is a unit if and only if $N(\alpha) = 1$.

###### _proof:_

Suppose $N(\alpha) = \alpha  \overline{\alpha} = 1$. Then, by definition $\alpha$ is a unit.

Suppose $\alpha$ is a unit. Then $N(\alpha \alpha ^{-1}) = N(\alpha) N(\alpha ^{-1}) = 1$. Thus, $N(\alpha)$ is a unit. Since $N$ is positive definite, $N(\alpha) = 1$.

---

This also controls the splitting of prime integers into non-primes in higher number fields.

##### _example:_ $3$ is a prime in the Gaussian integers, $5$ splits, and $2$ is ramified

If $3 = \alpha \beta$ is a non-trivial factorisation in $\mathbb{Z}[i]$, then we would have $N(3) = N(\alpha) N(\beta)$, and thus, $9 = N(\alpha) N(\beta)$. By unique factorisation, we must have $N(\alpha) = 3$, but there are no integer solutions to $a^{2} + b^{2} = 3$.

Conversely, $(2 + i)(2 - i) = 5$.

What's even weirder is that $2 = (1 + i)(1 - i)$ and these two factors are in fact associates.

---

However, imaginary quadratic fields can have bad behaviour in their ring of integers. $\mathbb{Z}[i]$ is not bad, but the rest of the negative $d$ with $d \equiv 3 \pmod 4$ lose unique factorisation in their ring of integers $\mathbb{Z}[\sqrt{ d }]$.

##### _proposition:_ rings of integers that are not UFDs

If $d < -1$ and $d \equiv 3 \pmod 4$, then $\mathbb{Z}[\sqrt{ d }]$ is *not* a [[Abstract algebra --- math-171/notes/Unique factorisation#_definition _ factorisation, factorisation domains, unique factorisation domains|UFD]].

###### _proof:_

Let $e = (1 - d) / 2$. Then $2 e = 1 - d = (1 - \sqrt{ d })(1 + \sqrt{ d })$. First, we show $2$ is irreducible, and then that it doesn't divide either of the irreducibles on the other side. 

$2$ has norm $4$. Thus, if $2 = \alpha \beta$ is non-trivial factorisation, we must have $N(\alpha) = 2$ and thus $a^{2} -d b ^{2} = 2$ for some $a, b \in \mathbb{Z}$.  

But $2 \nmid (1 \pm \sqrt{ d })$ since $\mathbb{Z}[\sqrt{ d }]$ does not contain $(1 \pm \sqrt{ d }) / 2$.

---

This example doesn't work for $d \equiv 1 \pmod 4$ because the ring of integers does contain $(1 \pm \sqrt{ d })/2$. The hard result we are working towards is the following.

##### _theorem:_ Gauss and Heegner–Stark's theorems

Let $\mathbb{K} = \mathbb{Q}(\sqrt{ d })$ be an imaginary quadratic field. Then $\mathscr{O}_{\mathbb{K}}$ is a UFD if and only if
$$
d \in \{ -1, -2, -3, -7, -11, -19, -43, -67, -163 \}.
$$

---

##### _theorem:_ imaginary quadratic number rings are Dedekind domains

###### _proof:_

If $\mathfrak{a} \subseteq \mathscr{O}_{\mathbb{K}}$ is maximal, it is prime and its own unique prime factorisation.

Else, $\mathfrak{a} \subseteq \mathfrak{b}$ [[Galois theory --- math-172/notes/The ideal class group#_corollary _ subideals are multiples of their superideals|and thus]] $\mathfrak{a} = \mathfrak{b} \mathfrak{c}$. Factorisation must terminate since $\mathscr{O}_{\mathbb{K}}$ is [[Algebraic geometry --- rising-sea/notes/Noetherian rings and modules#_definition _ Noetherian rings|Noetherian]] by [[Algebraic geometry --- rising-sea/notes/Noetherian rings and modules#_theorem _ the Hilbert basis theorem|Hilbert's basis theorem]]. In particular, we get a factorisation $\mathfrak{a} = \mathfrak{p}_{1} \cdots \mathfrak{p}_{n}$ into *maximal* ideals.

Uniqueness follows by the standard induction proof. If $\mathfrak{p}_{1} \cdots \mathfrak{p}_{n} = \mathfrak{q}_{1} \cdots \mathfrak{q}_{m}$, then $\mathfrak{p}_{1} \mid \mathfrak{q}_{i}$ for some $i$. Say $i = 1$. That is, $\mathfrak{q}_{1} \subseteq \mathfrak{p}_{1}$. Since $\mathfrak{q}_{1}$ is maximal, $\mathfrak{q}_{1} = \mathfrak{p}_{1}$. The rest follows by induction on $n$.

---

Note that this theorem requires $\mathfrak{a} \subseteq \mathfrak{b}$ to imply $\mathfrak{b}$ divides $\mathfrak{a}$. This is not universal, but [[Galois theory --- math-172/notes/The ideal class group#_corollary _ subideals are multiples of their superideals|is true for imaginary quadratic number rings]]. This is a special case of a more general result — to be a [[Galois theory --- math-172/notes/Dedekind domains#_definition _ Dedekind domain|Dedekind domain]], [[Galois theory --- math-172/notes/Dedekind domains#_proposition _ equivalent conditions to be a Dedekind domain|it suffices]] for $\mathfrak{a} \subseteq \mathfrak{b}$ to imply $\mathfrak{b}$ divides $\mathfrak{a}$.

##### _corollary:_ imaginary quadratic number rings are UFDs if and only if they are PIDs

$\mathscr{O}_{\mathbb{K}}$ is a UFD if and only if they are PIDs.

###### _proof:_

PID implies UFD [[Abstract algebra --- math-171/notes/Unique factorisation#_corollary _ every PID is a UFD|is standard]].

Suppose $\mathscr{O}_{\mathbb{K}}$ is a UFD. By unique factorisation of proper ideals, it suffices to show that every prime is principal. Suppose $a \in \mathfrak{p} \subseteq \mathscr{O}_{\mathbb{K}}$ is a non-zero element of a prime ideal. Let $a = p_{1} \cdots p_{n}$ be its unique prime factorisation. Since $\mathfrak{p}$, one of the $p_{i}$, say $p_{1}$, is in $\mathfrak{p}$. Then $(p_{1}) \subseteq \mathfrak{p}$. Since $p_{1}$ is prime, and all non-zero primes in $\mathscr{O}_{\mathbb{K}}$ are maximal, we must have $(p_{1}) = \mathfrak{p}$.

---

### Splitting, ramifying, or remaining inert

Let $\mathbb{K} = \mathbb{Q}(\sqrt{ d }) / \mathbb{Q}$ be an imaginary quadratic number field and let $\mathscr{O}_{\mathbb{K}}$ be its number ring. Then one interesting question we can ask is what primes lie above a given prime.

##### _definition:_ splitting, ramifying, remaining inert

---

##### _proposition:_ characterising primes that remain inert

Suppose $p \in \mathbb{Z}$  is prime. Suppose $d \equiv 2, 3 \pmod 4$. $p$ remains inert on [[Commutative algebra --- math-189AA/notes/Contraction and extension#Extension|extension]] to $\mathscr{O}_{\mathbb{K}}$ if and only if $x^{2} - d$ is irreducible in $\mathbb{F}_{p}[x]$.

Suppose $d \equiv 1 \pmod 4$. $p$ remains inert if and only if $x^{2} - x + h$ is irreducible in $\mathbb{F}_{p}[x]$.

###### _proof:_

Suppose $d \equiv 2, 3 \pmod 4$. Consider the commutative diagram obtained by modding out by $(p)$ and then $(x^{2} - d)$ or $(x^{2} - d)$ and then $(p)$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathbb{Z}[x] \ar[r] \ar[d] & \mathbb{F}_{p}[x] \ar[d] \\
		\mathcal{O}_{\mathbb{K}} \ar[r] & A
	\end{tikzcd}
\end{document}
```

Suppose $(p)$ is a prime on extension to $\mathscr{O}_{\mathbb{K}}$. Since $\mathscr{O}_{\mathbb{K}}$ is a [[Galois theory --- math-172/notes/Dedekind domains#_proposition _ equivalent conditions to be a Dedekind domain|Dedekind domain]], $(p)$ is maximal, and thus, $A$ is a field. Then $(x^{2} - d)$ is maximal and $x^{2} - d$ must be irreducible.

Conversely, suppose $x^{2} - d$ is irreducible. Then $(x^{2} - d)$ is maximal, $A$ is a field, and so $(p) \subseteq \mathscr{O}_{\mathbb{K}}$ is maximal and prime.

Identical considerations give the proof for $d \equiv 1$.

---