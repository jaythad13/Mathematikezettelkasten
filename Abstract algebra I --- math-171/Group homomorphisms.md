---
tags:
- alg
- math-171
lecture:
- math-171-5
- math-171-6
---

Remember linear maps? Homomorphisms are to things what linear maps are to vector spaces.

### Group homomorphisms

A homomorphism is a structure preserving operation. This is vague and intentionally so. We can be more specific if we know what structure we're trying to preserve.

##### _definition:_ group homomorphisms

Let $G$ and $H$ be [[Motivating groups#_definition _ group|groups]]. A group homomorphism $\varphi : G \to H$ is a function such that for all $x, y \in G$ we have
$$
\varphi(xy) = \varphi(x) \varphi(y).
$$

Note that the operation on the left hand side is on elements of $G$ and inside the input, and the operation on the right hand side is on elements of $H$ and on the output.

A natural definition we have is that of the kernel of $\varphi$ — it's just like the [[Null space|kernel/null space of a linear maps]].

##### _definition:_ kernel, $\ker \varphi$

The kernel of a group homomorphism $\varphi : G \to H$ is
$$
\ker \varphi = \{ x \in G | \varphi(x) = 1_{H} \}
$$

##### _definition:_ image, $\operatorname{Im} \varphi$

The image of a group homomorphism $\varphi : G \to H$ is
$$
\operatorname{im} \varphi = \{ \varphi(x) \in H | x \in G\}
$$

##### _examples:_ group homomorphisms

1) $\varphi : \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ by $m \mapsto m \pmod n$ is a group homomorphism (the standard definition of addition in both groups). The proof just follows from [[Modular arithmetic#_proposition _ congruence is preserved by addition and multiplication|some basic modular arithmetic]].
2) $\psi : D_{2n} \to \mathbb{Z}/2\mathbb{Z}$ by $s^j r^k \mapsto j \pmod 2$ is a group homomorphism since you can swap $s^j r^k s^l r^m = s^{j + l} r^k r^m$ when $l$ is odd, and otherwise it doesn't matter.

### Facts about homomorphisms

The following are easy to prove! Basically homomorphisms preserve anything that a group can care about. Let $G, H$ be groups with identities $1_{G}, 1_{H}$ and let $\varphi$ be a homomorphism $G \to H$.

##### _proposition:_ the identity is mapped to the identity

$$
\varphi(1_{G}) = 1_{H}
$$

##### _proof:_

$$
\begin{split}
\varphi(1_{G}) & = \varphi(1_{G} 1_{G})\\
& = \varphi(1_{G}) \varphi(1_{G})
\end{split}
$$and then right multiply by the inverse of $\varphi(1_{G})$ on both sides
$$
\varphi(1_{G})^{-1} \varphi(1_{G}) = \varphi(1_{G})^{-1} \varphi(1_{G}) \varphi(1_{G})
$$
and thus,
$$
\varphi(1_{G}) = 1_{H}.
$$

##### _proposition:_ homomorphisms send inverses to inverses

$$
\varphi(x^{-1}) = \varphi(x)^{-1}
$$

##### _proof:_

We know that
$$
\varphi(x x^{-1}) = \varphi(x)\varphi(x^{-1})
$$
and
$$
\begin{split}
\varphi(x x^{-1}) & = \varphi(1_{G}) \\
& = 1_{H}.
\end{split}
$$
Thus,
$$
\varphi(x) \varphi(x^{-1}) = 1_{H}
$$
and $\varphi(x^{-1})$ is the unique inverse of $\varphi(x)$.

##### _proposition:_ homomorphisms preserve arbitrary multiplication

$$
\varphi(x^n) = \varphi(x)^n
$$
for any integer $n$.

##### _proof sketch:_

Do it by induction — the base case is obviously true, so is the case for $n = 2$. Look at $\varphi(x^n)$ as $\varphi(x^{n - 1}x)$ and then solve by the previous case and $n = 2$.
