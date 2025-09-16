---
tags:
- comm-alg
- math-189AA/7
---

If $A$ is the best $A$-module, and free modules are second best, then the third best are their direct summands — projective modules.

##### _definition:_ direct summand

For an $A$-module $P$ we say an $A$-module $M$ is a direct summand of $P$ if $P \cong M \oplus N$. 

Note that we don't require $M, N$ to be submodules of $P$ and the direct sum to be internal.

---

##### _definition:_ projective module

An $A$-module $M$ is projective if it is a direct summand of a [[Commutative algebra --- math-189AA/notes/Modules#_example _ free modules|free module]]. That is, there is some $A$-module $N$ so that $M \oplus N \cong \bigoplus_{i \in \mathscr{I}} A$.

---

##### _example:_ projective modules

Since $\mathbb{Z} / (6) \cong \mathbb{Z} / (2) \oplus \mathbb{Z} / (3)$, the two modules $\mathbb{Z} / (2)$ and $\mathbb{Z} / (3)$ are projective $\mathbb{Z} / (6)$-modules.