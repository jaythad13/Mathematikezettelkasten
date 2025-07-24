---
tags:
- alg
- alg-comb
- comb
- math-171/15x
---

Burnside's lemma is a clever application of [[Abstract algebra --- math-171/notes/Group actions#_theorem _ the orbit-stabiliser theorem|the orbit-stabiliser theorem]] to count things "up to symmetry". For example, how many three-colourings of the cube are there, up to symmetry of rotation (we consider two colourings of the cube to be the same if you can rotate one into the other). 

Notably, this lemma was not first proven by Burnside. Burnside only stated it and proved it in his 1897 book on finite groups thinking it was well known. As a result it became attributed to him. However Frobenius had proven it ten years prior (and Burnside had attributed it to him), and it was known to Cauchy even in 1845. Thus, we call it the Cauchy-Frobenius lemma

The Cauchy-Frobenius lemma relates the number of orbits of an action $G \circlearrowright X$  to the average number of fixed points of a $g \in G$.

##### _lemma:_ the Cauchy-Frobenius lemma

Let $G$ be a finite group acting on a non-empty finite set $X$. Then the number of orbits in $X$ is
$$
\lvert X : G \rvert = \frac{1}{\lvert G \rvert } \sum_{g \in G} \operatorname{fix}_{X}(g).
$$

###### _proof:_

The key insight is to rewrite the sum of all fixed points of $g \in G$ as a sum over all stabilisers of $x \in X$. Since each fixed point is summed as many times as it is fixed, we can just count the number of times each point $x \in X$ is fixed —
$$
\sum_{g \in G} \operatorname{fix}_{X}(g) = \sum_{x \in X} \operatorname{stab}_{G}(x).
$$
By the orbit-stabiliser theorem, each $\operatorname{stab}_{G}(x)$ has size $\lvert G \rvert / \lvert \mathcal{O}_{G}(x) \rvert$, so
$$
\sum_{x \in X} \operatorname{stab}_{G}(x) = \lvert G \rvert  \sum_{x \in X} \frac{1}{\lvert \mathcal{O}_{G}(x) \rvert }.
$$
Since each orbit $\mathcal{O}_{G}(x)$ gets summed $\lvert \mathcal{O}_{G}(x) \rvert$ times, the sum is just the number of orbits $\lvert X : G \rvert$. In one line,
$$
\frac{1}{\lvert G \rvert } \sum_{g \in G} \operatorname{fix}_{X}(g) = \frac{1}{\lvert G \rvert } \sum_{x \in X} \operatorname{stab}_{G}(x) = \frac{\lvert G \rvert }{\lvert G \rvert } \sum_{x \in X} \frac{1}{\mathcal{O}_{G}(x)} = \lvert X : G \rvert.
$$