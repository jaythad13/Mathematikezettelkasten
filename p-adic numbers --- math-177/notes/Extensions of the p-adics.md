---
tags:
- alg-nt
- galois
- math-177/13
---

Extensions of the $p$-adics and number fields in general have special properties. For any $\mathbb{K} / \mathbb{Q}_{p}$ we can define a ring of integers $\mathscr{O}_{\mathbb{K}} \subseteq \mathbb{K}$ that behaves like $\mathbb{Z}_{p} \subseteq \mathbb{Q}_{p}$.

##### _definition:_ ring of integers

If $\mathbb{K}$ is a finite extension of $\mathbb{Q}_{p}$ with extended $p$-adic absolute value, then the **ring of integers of $\mathbb{K}$** is $\mathscr{O}_{\mathbb{K}} = \{ z \in \mathbb{K} \mid \lvert z \rvert_{p} \leq 1 \}$.

---

##### _proposition:_ the ring of integers is local

If $\mathbb{K}$ is a finite extension of $\mathbb{Q}_{p}$ with extended $p$-adic absolute value, then the ring of integers $\mathscr{O}_{\mathbb{K}}$ is a [[Commutative algebra --- math-189AA/notes/Local rings#_definition _ local rings|local ring]] with unique maximal ideal $\mathfrak{m}_{\mathbb{K}} = \{ z \in \mathbb{K} \mid \lvert z \rvert_{p} < 1 \}$.

---

Of course, then the natural thing to do is to define the residue field.

##### _definition:_ residue field

The residue field of a field extension $\mathbb{K} / \mathbb{Q}_{p}$ is $k_{\mathbb{K}} = \mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$.

----

This additional information allows us to understand field extensions both globally (as $\mathbb{K} / \mathbb{Q}_{p}$) and locally (as $k_{\mathbb{K}} / \mathbb{F}_{p}$).

##### _example:_ an unramified extension

Consider $\mathbb{K} = \mathbb{Q}_{5}(\sqrt{ 2 })$ this is a degree $2$ extension. Then we claim that $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}} = \mathbb{F}_{5}(\sqrt{ 2 })$ which is also a degree $2$ extension. Such an extension (with field extension and residue field extension of same degree), is called an unramified extension.

---