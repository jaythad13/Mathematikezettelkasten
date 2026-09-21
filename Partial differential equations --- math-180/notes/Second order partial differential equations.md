---
tags:
- math-180/5
- pde
---

### The Dirichlet problem in $\mathbb{R}^n$

Recall the **Laplacian**, the second order differential operator $\Delta$ that sends $f : \mathbb{R}^n \to \mathbb{R}$ to $\sum_{i = 1}^n \partial_{x_{i}^{2}} f$.

Suppose $\Omega \subseteq \mathbb{R}^n$ is an open, connected region. Given $f : \Omega \to \mathbb{R}$ and $g : \partial \Omega \to \mathbb{R}$, we want to find $u : \Omega \to \mathbb{R}$ such that $\Delta u = f$ everywhere in $\Omega$ and $u = g$ on $\partial \Omega$. It suffices to solve this separately in the cases that $f = 0$ and $g = 0$ (since $\Delta$ is a linear operator).