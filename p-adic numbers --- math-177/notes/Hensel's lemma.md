---
tags:
- alg-nt
- math-177/8
---

Hensel's lemma allows us to solve diophantine equations over $\mathbb{Q}_{p}$ by solving them over [[p-adic numbers --- math-177/notes/The p-adic numbers#Residue fields and the ring structure of $ mathbb{Z}_{p}$|their residue field]] $\mathbb{F}_{p}$.

##### _lemma:_ Hensel's lemma

Suppose $f \in \mathbb{Z}_{p}[x]$ and there is some $z \in \mathbb{Z}_{p}$ with $f(z) = 0 \pmod p$ and $f'(z) \neq 0 \pmod p$. Then there exists a unique $z_{0}$ with $z_{0} = z \pmod p$ and $f(z_{0}) = 0$.