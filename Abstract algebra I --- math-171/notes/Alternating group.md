---
tags:
- alg
- math-171/14
---

Remember how subgroups of index $2$ [[Lagrange's theorem#_proposition _ index $2$ subgroups are normal|are normal]]? Let's look at an example.

##### _example:_ the sign of a permutation

Consider $\sigma \in S_{n}$, Then we can write $\sigma$ as the [[Group combinatorics and symmetric groups#_proposition _ every permutation is the composition of transpositions|product of transpositions]]. This product is not unique — there is more than one way to do this. However, the number of transpositions is either always even or always odd. This motivates us to define

##### _definition:_ even, odd for transpositions

For $\sigma \in S_{n}$, we call $\sigma$ odd or even (respectively) if it can be written as a product of an odd or even number of transpositions (respectively).

Thus, we can consider the mapping
$$
\begin{split}
\operatorname{sgn} & : S_{n} \to \{ -1, 1 \} \\
& :\sigma \mapsto \begin{cases}
1 & \text{if } \sigma \text{ is even} \\
-1 & \text{if } \sigma \text{ is odd}.
\end{cases}
\end{split}
$$
We claim this is a homomorphism (with the operation of multiplication on the target space). Note then that the set of even permutations is the kernel of $\operatorname{sgn}$, and is thus a normal subgroup. We define

##### _definition:_ alternating group of order $n$

The alternating group of order $n$, is $A_{n}$, the group of all even permutations in $S_{n}$.

Then the short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A_n \ar[r, hook] & S_n \ar[r, "\mathrm{sgn}"] & \{ 1, -1 \} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
tells us that $S_{n} /A_{n} \cong \{ -1, 1 \}$, $S_{n} / A_{n}$ has order $2$, and thus, $\lvert S_{n} : A_{n} \rvert = 2$ (this is all by [[Group isomorphism theorems|the first isomorphism theorem]]).
