---
tags:
- math-174/9
- rep-th
- fourier
---

Let $G$ be a finite group. [[Fourier analysis --- math-139/notes/Finite Fourier analysis|We've already seen]] how to do Fourier analysis when $G$ is abelian. We can do much of the same for general $G$.

##### _definition:_ discrete Fourier transform

Suppose $\rho, V$ is a representation of $G$. Suppose $f \in \mathbb{F}[G]$. Then the **(discrete) Fourier transform of $f$ with respect to $\rho$** is the ring homomorphism $f \mapsto \hat{f}(\rho) = \rho(f)$ where $\rho$ is the structure map $\mathbb{C}[G] \to \operatorname{End}_{\mathsf{Ab}} V$.

---

From now on, fix a unitary representation $\rho, V$ and write $\hat{f}$ for $\hat{f}(\rho)$.

##### _theorem:_ Fourier inversion

Suppose $f \in \mathbb{F}[G]$. Then
$$
f = \sum_{g \in G} \left( \frac{g}{\#G} \sum_{\rho \in \widehat{G}} d_{\rho} \operatorname{tr} (\rho(g^{-1}) \hat{f}(\rho)) \right)
$$

---