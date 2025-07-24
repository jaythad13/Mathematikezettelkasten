---
tags:
- math-145/13
- math-145/14
- alg-top
- hom-alg
---

In order to prove that [[Simplicial homology and graph theory --- math-145/notes/Simplicial homology|simplicial homology]] really is a [[Simplicial homology and graph theory --- math-145/notes/Whitehead equivalence#Whitehead invariants|Whitehead invariant]], we will need some machinery to generally analyse the objects of cohomology that we've been looking at so far. We will need the theory of chain complexes which generalise the boundary maps of chains we've been looking at, and some facts that are true in abelian categories.

### Chain complexes

##### _definition:_ chain complex

A chain complex $V_{\bullet}$ is a collection of vector spaces $V_{n}$ and linear maps $\partial_{n} \to V_{k + 1} \to V_{k}$
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		V_{0} & \ar[l, "\partial_{0}"] V_{1} & \ar[l, "\partial_{1}"] V_{2} & \ar[l, "\partial_{2}"] \dots
	\end{tikzcd}
\end{document}
```
such that $\partial_{k - 1} \partial_{k} = 0$ for all $n$.

Note that his is a weakening of the notion of an [[Abstract algebra --- math-171/notes/Exact sequences#_definition _ exact sequence|exact sequences]] — we only require $\operatorname{img} \partial_{k} \subseteq \ker \partial_{k - 1}$ instead of equality. The degree to which it is not exact is measured by homology.

##### _definition:_ boundaries, cycles, and homology of a chain complex

Let $V_{\bullet}$ be a chain complex.

The $k$-boundaries of $V_{\bullet}$ are $\mathrm{B}_{k}(V) = \operatorname{img} \partial_{k} \subseteq V_{k}$.

The $k$-cycles of $V$ are $\mathrm{Z}_{k}(V) = \operatorname{ker} \partial_{k - 1} \subseteq V_{k}$.

The $k$th homology of $V$ is $\mathrm{H}_{k}(V) = \mathrm{Z}_{k}(V) / \mathrm{B}_{k}(V)$.

There is of course, a notion of morphisms of chain complexes.

##### _definition:_ chain map

Given chain complexes $V_{\bullet}, W_{\bullet}$, a chain map $T_{\bullet} : V_{\bullet} \to W_{\bullet}$ between them is a collection of maps $T_{k} : V_{k} \to W_{k}$ so that the squares in the following diagram commute —
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		V_{0} \ar[d, "T_{0}"] & \ar[l, "\partial_{V, 0}"] V_{1} \ar[d, "T_{1}"] & \ar[l, "\partial_{V, 1}"] V_{2} \ar[d, "T_{2}"] & \ar[l, "\partial_{V, 2}"] \dots \\
		W_{0} & \ar[l, "\partial_{W, 0}"] W_{1} & \ar[l, "\partial_{W, 1}"] W_{2} & \ar[l, "\partial_{W, 2}"] \dots
	\end{tikzcd}
\end{document}
```


We can check that the maps of chain complexes in fact give rise to maps of their homology

##### _proposition:_ maps of chain complexes give maps of homology

Given a chain map $T_{\bullet} : V_{\bullet} \to W_{\bullet}$, there is a linear map $\mathrm{H}_{k}T_{\bullet} : \mathrm{H}_{k}(V) \to \mathrm{H}_{k}(W)$ by $\gamma + \operatorname{img} \partial_{V, k} \mapsto$. The collection of all these maps is called $\mathrm{H} T_{\bullet}$.

We want to know when two chain maps induce the same map on homology, so that eventually we can show that we have isomorphisms of each homology. Chain homotopies give us a way to do this.

##### _definition:_ chain homotopy

Given chain maps $S_{\bullet}, T_{\bullet} : V_{\bullet} \to W_{\bullet}$, a chain homotopy $K_{\bullet} : S_{\bullet} \to T_{\bullet}$ is a collection of maps $K_{k} : V_{k} \to W_{k + 1}$ such that $K_{k} \partial_{k} + K_{k + 1} \partial_{k + 1} = T_{k} - S_{k}$.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		V_{0} \ar[dd, "T_{0}"] \ar[dd, shift right, "S_{0}"']  \ar[rdd, "K_{0}"'] & \ar[l, "\partial_{V, 0}"] V_{1} \ar[dd, "T_{1}"] \ar[dd, shift right, "S_{1}"'] \ar[rdd, "K_{1}"'] & \ar[l, "\partial_{V, 1}"] V_{2} \ar[dd, "T_{2}"] \ar[dd, shift right, "S_{2}"'] \ar[rdd, "K_{2}"'] & \ar[l, "\partial_{V, 2}"] \dots \\ \\
		W_{0} & \ar[l, "\partial_{W, 0}"] W_{1} & \ar[l, "\partial_{W, 1}"] W_{2} & \ar[l, "\partial_{W, 2}"] \dots
	\end{tikzcd}
\end{document}
```

##### _theorem:_ chain homotopic chain maps induce the same map on homology

Given chain homotopy $K : S \to T$ on chain maps $S, T : V \to W$, the induced maps on homology are equal — $S_{*} = T_{*}$.

### The snake lemma

The snake lemma is a fact of homological algebra that gives you a long exact sequence from a pair of exact sequences and a morphism between them.

##### _definition:_ map of short exact sequences

Given two [[Abstract algebra --- math-171/notes/Exact sequences#_example _ short exact sequence|short exact sequences]], a map between them is three maps such that the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A \ar[r, "p"] \ar[d, "\alpha"] & B \ar[r, "q"] \ar[d, "\beta"] & C \ar[r] \ar[d, "\gamma"] & 0 \\
		0 \ar[r] & A' \ar[r, "p'"] & B' \ar[r, "q'"] & C' \ar[r] & 0
	\end{tikzcd}
\end{document}
```
Note that it suffices to show that 

##### _lemma:_ the snake lemma

Given a map of short exact sequences
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A \ar[r, "p"] \ar[d, "\alpha"] & B \ar[r, "q"] \ar[d, "\beta"] & C \ar[r] \ar[d, "\gamma"] & 0 \\
		0 \ar[r] & A' \ar[r, "p'"] & B' \ar[r, "q'"] & C' \ar[r] & 0
	\end{tikzcd}
\end{document}
```
there is an exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker \alpha \ar[r, "p"] & \ker \beta \ar[r, "q"] & \ker \gamma \ar[llld, "\delta"'] \\
		\mathrm{coker} \, \alpha \ar[r, "p'"'] & \mathrm{coker} \, \beta \ar[r, "q'"'] & \mathrm{coker} \, \gamma \ar[r] & 0
	\end{tikzcd}
\end{document}
```


###### _proof:_

The diagram to chase in is
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker \alpha \ar[r, "p"] \ar[d, hook] & \ker \beta \ar[r, "q"] \ar[d, hook] & \ker \gamma \ar[d, hook] \\
		0 \ar[r] & A \ar[r, "p"] \ar[d, "\alpha"] & B \ar[r, "q"] \ar[d, "\beta"] & C \ar[d, "\gamma"] \ar[r] & 0 \\
		0 \ar[r] & A' \ar[r, "p'"] \ar[d, two heads] & B' \ar[r, "q'"] \ar[d, two heads] & C' \ar[d, two heads] \ar[r] & 0 \\
		& \mathrm{coker} \, \alpha \ar[r, "p'"] & \mathrm{coker} \, \beta \ar[r, "q'"] & \mathrm{coker} \, \gamma \ar[r] & 0
	\end{tikzcd}
\end{document}
```


By the commutativity of the diagram (since $p' \circ \alpha = \beta$) defining the map of short exact sequences, $p^\text{img}(\ker \alpha) \subseteq \ker \beta$ and similarly, we have $q^\text{img}(\ker \beta) \subseteq \ker \gamma$. Thus, $p, q$ really do restrict to maps of kernels. Similarly, since $p' \circ \alpha = \beta \circ p$, we have $p'^{\text{img}}(\operatorname{img} \alpha) \subseteq \operatorname{img} \beta$. We can do the same thing for $q'$. Thus, we have shown that $p, q, p', q'$ give maps between the desired spaces.

We're only left to define $\delta$. Consider an element $c \in \ker \gamma$. Then since $q$ is surjective, there is some $b + \operatorname{img} p \in B / \operatorname{img} p$ with $q(b) = c$. That is, we have a map $\ker \gamma \to \operatorname{coker} p$. Note that this is the restriction of the inverse of the isomorphism $B / \ker p \to C$. Consider $\beta(b)$. By commutativity of the diagram $q' \circ \beta(b) = \gamma(c) = 0$. Thus, $\beta(b) \in \ker q'$, and by exactness, $\beta(b) \in \operatorname{img} p'$. Thus, $\beta(b) = p'(a')$ for some $a' \in A'$ (since $p'$ is injective, $a'$ is unique). For any distinct $b_{1} \in b + \operatorname{img} p$, we have $b_{1} - b = p(a)$ for some unique $a \in A$. Thus, $\beta(b - b_{1}) = \beta(p(a))$ which, by commutativity of the diagram is $p'(\alpha(a))$. Thus, the $\beta(b_{1}) = p'(a' + \alpha(a))$. Thus, we have a map $b + \operatorname{img} p \mapsto a' + \operatorname{img} \alpha$ from $\operatorname{coker} p$ to $\operatorname{coker} \alpha$. This long chain of reasoning gives us $\delta$. Since it can be expressed as the composition of a bunch of complicated homomorphisms on quotients, it is a homomorphism.

Now we have to show exactness. Since $p$ is injective, it restricts to an injective map on kernels, and since $q'$ is surjective, it restricts to a surjective map on cokernels. Thus, we have exactness at $\ker \alpha$ and $\operatorname{coker} \gamma$. 

We know that $q \circ p = 0$ on kernels since it is zero on the whole spaces. However, we aren't guaranteed exactness since something in the $\ker q$ may not necessarily come from something in $p^\text{img}(\ker \alpha)$, but just something else in $\operatorname{img} p \cap \ker \beta$. We need to verify that it can only come from $\ker \alpha$. We diagram-chase. If $b \in \ker q$, then by exactness at $B$ and injectivity of $p$ we have some unique $a \in A$ such that $p(a) = b$. By exactness, $p' \circ \alpha(a) = \beta(b) = 0$. But $p'$ is injective, so $\alpha(a) = 0$ and thus, $a \in \ker \alpha$. Thus, we have exactness at $\ker \beta$.

Now we need to show exactness at $\operatorname{coker} \beta$. Once again, we do have $q' \circ p' = 0$ but we're not guaranteed exactness. We need to show that if $q'(b' + \operatorname{img} \beta) = 0$, then $p'(a' + \operatorname{img} \alpha) = b' + \operatorname{img} \alpha$ for some $a' \in A'$. For $q'(b' + \operatorname{img} \beta) = 0$ in $\operatorname{coker} \gamma$, we must have $q'(b')  = \gamma(c)$ for some $c \in C$. Since $q$ is surjective, we have some $b \in B$ such that $q(b) = c$, and this $b$ has $\beta(b) \in B'$. Thus, $b' + \operatorname{img} \beta = b' - \beta(b) + \operatorname{img} \beta$. Since $q'(b') = q' \circ \beta(b)$, we have $q'(b' - \beta(b)) = 0$. It follows that $p'(a') = b' - \beta(b)$ for some $a' \in A'$, and thus, $b' + \operatorname{img} \beta = b' - \beta(b) + \operatorname{img} \beta = p'(a' + \operatorname{img} \alpha)$. 

First we prove exactness at $\ker \gamma$. We need to show $\delta(q(b)) = 0$ for all $b \in \ker \beta$. Note that $\delta(q(b))$ is given by some map $b + \operatorname{img} p \mapsto a' + \operatorname{img} \alpha$ where $p'(a') = \beta(b) = 0$. Since $p'$ is injective, $a' + \operatorname{img} \alpha = 0$. We also need to show that if $\delta(c) = 0$ for $c \in \ker \gamma$, we have $c = q(b)$ for some $b \in \ker \gamma$. If $\delta(c) = 0$, we know that for any $b_{0} + \operatorname{img} p$ with $q(b_{0}) = c$, we have $p'(0 + \operatorname{img} \alpha) = \beta(b_{0})$. Thus, by exactness, there is some $a \in A$ such that $\beta(p(a)) = \beta(b_{0}) = p'(\alpha(a_{0}))$. Choose $b = b_{0} - p(a)$. Clearly $\beta(b) = 0$, and $q(b_{0} - p(a)) = q(b_{0}) - q \circ p(a) = c$. We have exactness at $\ker \gamma$!

Finally, we have to show exactness at $\operatorname{coker} \alpha$. The easy bit is to show that $p'(\delta(c)) = 0$ for all $c \in \ker \gamma$. Of course, $\delta(c) = a' + \operatorname{img} \alpha$ where $p'(a') = \beta(b)$ for some $b$ with $q(b) = c$, so $p'(\delta(c)) \in \operatorname{img} \beta$ and is zero in $\operatorname{coker} \beta$. The hard bit is to show that if $p'(a' + \operatorname{img} \alpha) = 0$, then $a' = \delta(c)$ for some $c \in \ker \gamma$. Since $p'(a' + \operatorname{img} \alpha) = 0$ in $\operatorname{coker} \beta$, $p'(a') = \beta(b)$ for some $b$. But $\gamma \circ q(b) = q' \circ p'(a') = 0$ by commutativity of the diagram and exactness at $B'$, so $q(b) \in \ker \gamma$. Since $\delta(q(b)) = a'$ we have the desired $c = q(b)$.

> And that's the snake!

\- Jill Clayburgh, as Kate Gunzinger in It's My Turn