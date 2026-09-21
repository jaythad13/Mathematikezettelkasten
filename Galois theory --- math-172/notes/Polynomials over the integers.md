---
tags:
- alg
- math-172/5
---

We already know $\mathbb{Q}[x]$ [[Abstract algebra --- math-171/notes/Unique factorisation#_examples _ Euclidean domains|is a Euclidean domain]], and thus, a PID. We will see that $\mathbb{Z}[x]$ is in fact a [[Abstract algebra --- math-171/notes/Unique factorisation#_definition _ unique factorisation domains|UFD]]. In fact, we will see that $\mathbb{Z}[x]$ and $\mathbb{Q}[x]$ are very closely related. This is a special case of a more general fact about [[Abstract algebra --- math-171/notes/Unique factorisation#_proposition _ UFDs are preserved by localisation|localising UFDs]]. We will also see that the map $\mathbb{Z}[x] \to \mathbb{F}_{p}[x]$ is very useful. In some sense, this is studying $\mathbb{A}^1$ by studying the [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_example _ affine space as an affine space-bundle|fibres of the map]] $\mathbb{A}^1 \to \operatorname{Spec} \mathbb{Z}$.

### Primitive polynomials and Gauss' lemma (the general fibre)

Our goal is to compare $\mathbb{Z}[x]$ to $\mathbb{Q}[x]$. Once we have got rid of the extra irreducibles in $\mathbb{Z}$, these look the same.

##### _definition:_ primitive polynomials

$f(x) = \sum_{i = 0}^n a_{i} x^i \in \mathbb{Z}[x]$ is a **primitive** if $\gcd(a_{0}, \dots, a_{n}) = 1$ and $a_{n}$ is a positive integer.

---

##### _lemma:_ prime integers in $\mathbb{Z}[x]$

Suppose $p \in \mathbb{Z}$. Then $(p) \subseteq \mathbb{Z}[x]$ is prime if and only if $(p) \subseteq \mathbb{Z}$ is prime.

###### _proof:_

Suppose $p \in \mathbb{Z}$ and $(p) \subseteq \mathbb{Z}[x]$ is prime. But in a domain all primes are irreducible, thus $p$ is irreducible in $\mathbb{Z}[x]$ and also in $\mathbb{Z}$, and all [[Abstract algebra --- math-171/notes/Unique factorisation#_proposition _ UFD if and only if irreducible elements are exactly the primes|irreducibles are prime]] since $\mathbb{Z}$ [[Superdiscrete --- math-55A/notes/Prime numbers#_theorem _ unique factorisation|is a UFD]].

The converse is obvious since $\mathbb{F}_{p}[x]$ is a domain.

---

##### _lemma:_ Gauss' lemma

The product of primitive polynomials is primitive

###### _proof:_

Suppose $f = \sum a_{i} x^i, g = \sum b_{i} x^i \in \mathbb{Z}[x]$ are primitive. Suppose $fg = \sum c_{i} x^i$. If $p \mid \gcd(c_{0}, \dots, c_{m + n})$ then $p \mid fg$, and so $p \mid f$ or $p \mid g$. But since $\gcd(a_{0}, \dots, a_{m}) = \gcd(b_{0}, \dots, b_{n}) = 1$, there is no such $p$.

---

##### _lemma, definition:_ factoring into a primitive polynomial and content, content

Every non-constant polynomial $f \in \mathbb{Q}[x]$ can be written uniquely as a product $f(x) = c f_{0}(x)$ where $f_{0} \in \mathbb{Z}[x]$ is primitive and $c \in \mathbb{Q}[x]$. $c$ is an integer if and only if $f \in \mathbb{Z}[x]$. If $f \in \mathbb{Z}[x]$, then the $\gcd$ of its coefficients is $\pm c$.

$c$ is called the **content** of the polynomial.

###### _proof:_

Suppose $f \in \mathbb{Z}[x]$. Let $\pm c$ be the $\gcd$ of its coefficients with sign chosen so that $f_{0} = f / c$ has positive leading coefficient. Then $f_{0}$ is primitive. Else, clear denominators to obtain $f = g / d$ for some $g \in \mathbb{Z}[x]$ and $d \in \mathbb{Z}$. Let $g_{0}$ be the unique primitive such that $g = c g_{0}$. Then $f_{0} = g_{0}$ is primitive and $f = (c / d) f_{0}$.

Suppose $c f_{0} = c' f_{0}'$ where both $f_{0}, f_{0}'$ are primitive. Choose a prime integer $p$ divides $c$. Then $p \mid c' f_{0}'$ as well. Since $f_{0}'$ is primitive, $p$ doesn't divide the polynomial, it divides $c'$. Applying the same analysis to $c / p$ and $c' / p$ yields that every prime factor of $c$ divides $c'$ with the same multiplicity and vice-versa. Thus, $c = c'$. Since $\mathbb{Q}[x]$ is a domain, $f_{0} = f_{0}'$.

---

##### _proposition:_ division in $\mathbb{Z}[x]$ implies division in $\mathbb{Q}[x]$

Suppose $f_{0}, g \in \mathbb{Z}[x]$ with $f_{0}$ primitive. If $f_{0} \mid g$ in $\mathbb{Q}[x]$, then $f_{0} \mid g$ in $\mathbb{Z}[x]$. 

Further, if $f, g \in \mathbb{Z}[x]$ have a common non-constant factor in $\mathbb{Q}[x]$, they have a common non-constant factor in $\mathbb{Z}[x]$.

###### _proof:_

Suppose $f_{0}(x) q(x) = g(x)$ for some $q \in \mathbb{Q}[x]$. Write $g = c g_{0}$ where $g_{0}$ is primitive. Then $f_{0}(x) q(x) = c g_{0}(x)$. Since $f_{0}$ is primitive, the denominator of the coefficients of $f_{0} q$ is the same as that of $q$. But the denominator of the coefficients of $f_{0} q$ is the same as that of $c g_{0}$ which is just $1$.

Suppose $q \mid f, g$ in $\mathbb{Q}[x]$. Then let $q = c q_{0}$ and $q_{0}$ divides both $f$ and $g$ in $\mathbb{Q}[x]$. But then $q_{0}$ is primitive and in $\mathbb{Z}[x]$ so $q_{0} \mid f, g$ in $\mathbb{Z}[x]$ as well.

---

##### _proposition:_ classifying irreducibles in $\mathbb{Z}[x]$

$f \in \mathbb{Z}[x]$ is irreducible if and only if it is a prime integer or ($\pm 1$) a primitive polynomial that is irreducible in $\mathbb{Q}[x]$.

Specifically, $f \in \mathbb{Z}[x]$ is irreducible if and only if it is prime.

###### _proof:_

If $f$ is a constant, we already know

Suppose $f$ is non-constant. If $f$ is irreducible it cannot admit a prime integer as a proper factor, $f$ must be $\pm f_{0}$ for a primitive polynomial. Further, any non-trivial factorisation $f = gh$ in $\mathbb{Q}[x]$ must give rise to $f = g_{0} h_{0}$ for the corresponding primitive polynomials, which is a factorisation in $\mathbb{Z}[x]$.

Suppose $f_{0}$ is a primitive polynomial and irreducible in $\mathbb{Q}[x]$. Then it is clearly irreducible in $\mathbb{Z}[x]$.

We already know all primes are irreducible. Suppose $f \in \mathbb{Z}[x]$ is irreducible. Then it is irreducible in $\mathbb{Q}[x]$, and [[Abstract algebra --- math-171/notes/Unique factorisation#_proposition _ UFD if and only if irreducible elements are exactly the primes|thus]], prime in $\mathbb{Q}[x]$. Suppose $f \mid gh$ for some $g, h \in \mathbb{Z}[x]$. Then $f \mid gh$ in $\mathbb{Q}[x]$ and by primeness, $f$ divides one of them in $\mathbb{Q}[x]$. Thus, $f$ divides the same one in $\mathbb{Z}[x]$ as well. That is, $f$ is prime in $\mathbb{Z}[x]$.

---

##### _corollary:_ $\mathbb{Z}[x]$ is a UFD

###### _proof:_

$\mathbb{Z}$ is clearly [[Algebraic geometry --- rising-sea/notes/Noetherian rings and modules#_definition _ Noetherian rings|Noetherian]] (by, say, the [[Algebraic geometry --- rising-sea/notes/Noetherian rings and modules#_theorem _ the Hilbert basis theorem|Hilbert basis theorem]]). Thus, it is a [[Abstract algebra --- math-171/notes/Unique factorisation#_definition _ factorisation, factorisation domains, unique factorisation domains|factorisation domain]]. [[Abstract algebra --- math-171/notes/Unique factorisation#_proposition _ UFD if and only if irreducible elements are exactly the primes|Since all irreducibles are prime]], it is a unique factorisation domain.

---

### Factoring by reducing modulo $p$ (the special fibres)

Let $\psi_{p}$ be the homomorphism $\mathbb{Z}[x] \to \mathbb{F}_{p}[x]$. Then as long as $p$ isn't bad, irreducibles in $\mathbb{F}_{p}[x]$ can only come from irreducibles in $\mathbb{Z}[x]$.

##### _proposition:_ irreducibles in $\mathbb{F}_{p}[x]$ come from irreducibles in $\mathbb{Z}[x]$

Suppose $f \in \mathbb{Z}[x]$ and $p$ does not divide its leading coefficient. If $\psi_{p}(f) \in \mathbb{F}_{p}[x]$ is irreducible, then $f$ is irreducible in $\mathbb{Q}[x]$.

###### _proof sketch:_

Non-trivial factorisations in $\mathbb{Q}[x]$ get transferred to non-trivial factorisations in $\mathbb{F}_{p}[x]$ by $\psi_{p}$.

---