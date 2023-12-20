---
tags:
- calc
- self-study
---

### The projection principle

There is an obvious relationship between $m$ real-valued functions, and functions to $\bb R^m$. The projection principle says that they are exactly the same (upto isomorphism).

##### _definition:_ component functions

The component functions of a function $f : A \to \bb R^m$ (for $A \subset \bb R^n$) are the $m$ functions $f_1, \ldots, f_m : A \to \bb R$ such that $f(\bvec x) = (f_1(\bvec x), \cdots f_m(\bvec x))$ for all $\bvec x \in A$.

Note that they are defined uniquely, and that $m$ functions from $A$ to $\bb R$, $g_1, \ldots, g_m$ would also uniquely define a function $g : A \to \bb R^m$ with component functions $g_1, \ldots, g_m$.

##### _notation:_ $\pi$, $\pi_i$

By $\pi$, we mean the identity function on $\bb R^n$ such that $\pi(\bvec x) = \bvec x$.

By $\pi_i$ we mean the $i$th projection function on $\bb R^n$ (for $i \in \bb N_n$), giving $\pi_i(\bvec x) = x_i$, for $\bvec x = (x_1, \ldots, x_n)$.

Note that then we have the $i$th component function of any function $f$ as $\pi_i \circ f$.

### Continuity

In single variable calculus, the expression $\lim_{x \to a} f(x) = L$ means that we can get $f(x)$ arbitrarily close to $L$ for $x$ values within some range of $a$. This generalises neatly in $\bb R^n$ (and indeed in all metric spaces) — we can define limits as below, and then define continuity to be where the limit and the value of a function are the same.

##### _definition:_ limit, $\lim_{\bvec x \to \bvec a} f(\bvec x)$

For a function $f : A \to \bb R^m$ (with $A \subset \bb R^n$), we say the function has limit $L$ at $\bvec a$, denoted
$$
\lim_{\bvec x \to \bvec a} f(\bvec x) = L
$$
if for every $\varepsilon > 0$ we have some $\delta > 0$ such that all $\bvec x$ with $0 < \norm{\bvec x - \bvec a} < \delta$ give us $\norm{f(\bvec x) - f(\bvec a)} < \varepsilon$.

##### _definition:_ continuity at point, continuous function

A function $f : A \to \bb R^m$ ($A \subset \bb R^n$) is continuous at $\bvec a$ if $f(\bvec a) = \lim_{\bvec x \to \bvec a} f(\bvec x)$.

We say $f$ is continuous if $f$ is continuous at every $\bvec a \in A$.

While these definitions work, continuity can be defined purely topologically, without using limits. This more general definition makes strong results easy.

##### _theorem:_ topological continuity is equivalent to $\varepsilon-\delta$ continuity

A function $f : A \to \bb R^m$ ($A \subset \bb R^n$) is continuous if and only if every open set $U$ in $\bb R^m$ has an open pre-image in $A$. More strongly, every open set $U \subset \bb R^m$ gives us $f^{\text{pre}}(U) = V \cap A$ for some open set $V \subset \bb R^n$.

##### _proof:_

Suppose $f$ is continuous. Then if $\bvec a \in f^{\text{pre}}(U)$ and thus, $f(\bvec a) \in U$, some open set, we have for every $\varepsilon$-[[Metric spaces#_definition _ r-neighbourhood, radius, $N_r(p)$|neighbourhood]] around $f(\bvec a)$ contained in $U$ (we have one, because [[Topological considerations#Open and closed sets|we have an open rectangle]] in $U$) a $\delta$-neighbourhood around $\bvec a$ such that every $\bvec b$ in that $\delta$-neighbourhood gives $f(\bvec b)$ in the $\varepsilon$-neighbourhood, and thus $f(\bvec b) \in U$. This means that the $\delta$-neighbourhood and thus, the open rectangle inside it, is contained in $f^{\text{pre}}(U)$, making $f^{\text{pre}}(U)$ open.

Suppose $f$ is "topologically continuous". Then if we look at any $\varepsilon$-neighbourhood around $f(\bvec a)$, $U$, we have that its pre-image is open. Thus, its pre-image contains an open rectangle containing $\bvec a$, and that open rectangle contains a $\delta$-neighbourhood around $\bvec a$, which has image inside the $\varepsilon$-neighbourhood.

One example of how this topological definition is useful (and also an example of how compactness is useful) is in showing that continuous functions preserve compactness.

##### _theorem:_ continuous functions preserve compactness

If $f : K \to \bb R^m$ is continuous ($K \subset \bb R^n$), and $K$ is compact, then $f^{\text{img}}(K)$ is compact.

##### _proof:_

Let $K' = f^{\text{img}}(K)$. Suppose $\mathcal O$ is an open cover of $K'$. Then each point $f(\bvec x) \in K'$ is contained in some $U \in \mathcal O$ that has an open pre-image in $K$, $U'$ (because of continuity). All of these $U'$ together contain every $\bvec x \in K$, and thus, form an open cover of $K$, $\mathcal O'$. Because $K$ is compact, we can reduce this to a finite sub-cover $\bar{\mathcal O'}$. Since all of the (finitely many) sets in $\bar{\mathcal O'}$ are pre-images of open sets and together contain every point in $K$, their (finitely many) images are open and contain every point in $K'$, and are thus, a finite sub-cover of $\mathcal O$,