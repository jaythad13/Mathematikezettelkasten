---
tags:
- rising-sea/2/7
- alg-top
- alg-geo
---

Suppose $\pi : X \to Y$ is a continuous map of topological spaces and $\mathscr{E}$ is a sheaf on $Y$. Then using the [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ la espace étalé of a sheaf|espace étalé]] interpretation of $\mathscr{E}$ as a continuous map $\xi : E \to X$ we can define pulled back sections of $\mathscr{E}$ on $X$ as continuous maps $\sigma : U \to E$ such that $\xi \circ \sigma = \pi_{\mid U}$. We will see that this is functorial and [[Algebraic geometry --- rising-sea/notes/Adjoint functors#_definition _ adjoint functors, left adjoint, right adjoint, adjoint pair|left adjoint]] to the [[Algebraic geometry --- rising-sea/notes/Pushforward sheaves#_definition _ pushforward/direct image presheaves and sheaves|pushforward]]. This definition will be harder than that of the pushforward, but we will use it to understand sheaves on schemes. 

We will denote this by $\pi ^{-1}$ and call it the inverse image sheaf, not $\pi^*$ and the pullback sheaf. We reserve the pullback name for the adjoint to the pushforward as a functor $\mathsf{Mod}_{\mathscr{O}_{X}} \to \mathsf{Mod}_{\mathscr{O}_{Y}}$ rather than just sheaves in a general category.