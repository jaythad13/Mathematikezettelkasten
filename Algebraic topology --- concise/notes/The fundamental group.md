---
tags:
- math-147
- alg-top
---

The simplest homotopy invariant to define is then the fundamental group. This catches holes in topological spaces that loops cannot deform to a point around. In order to define the fundamental group, we first need the notion of path homotopy and several properties of path homotopy classes.

### Paths and path homotopy

Recall from [[Topology --- math-147/notes/Connectedness and path-connectedness#Path-connectedness|path-connectedness]] the definition of a path.

![[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ path|Connectedness and path-connectedness]]

We want to consider these paths up to deformation, leaving the endpoints in place.

##### _definition:_ path homotopy, equivalence

Two paths $\alpha, \beta$ in $X$ are equivalent or path homotopic, denoted $\alpha \sim \beta$ if $\alpha, \beta$ are [[Algebraic topology --- concise/notes/Homotopy#_definition _ homotopic, homotopy, homotopic relative to|homotopic relative to]] $\{ 0, 1 \}$.

The path homotopy equivalence class of a path $\alpha$ is denoted $[\alpha]$.

---

##### _example:_ any two paths in $\mathbb{R}^n$ with the same endpoint are homotopic

Use the [[Algebraic topology --- concise/notes/Homotopy#_example _ the straight line homotopy|straight line homotopy]]. It isn't hard to check that it preserves endpoints.

---

##### _definition:_ loop

A **loop** in $X$ is a path $\alpha$ in $X$ with $\alpha(0) = \alpha(1)$. The point $x_{0} = \alpha(0) = \alpha(1)$ is called the base point of $\alpha$.

Equivalently, a loop is a based continuous map $(S^1, p) \to (X, x_{0})$.

---

Loops with non-trivial homotopy class help identify holes in the surface.

The following lemmas about paths and path homotopy will prove to be very useful.

##### _lemma:_ paths can be understood locally

Let $\alpha : [0, 1] \to X$ be a path, and let $\{ U_{\alpha} \}$ be a cover of $X$. Then there exists some $n$ such that each subinterval $I_{i} = \left[ \frac{i - 1}{n}, \frac{i}{n} \right] \subseteq [0, 1]$ has $\alpha^\text{img}(I_{i}) \subseteq U_{\alpha_{i}}$ for some $\alpha_{i}$.

###### _proof:_
[[Topology --- math-147/attachments/homework/hw 9/hw 9.pdf#page=6|is in the homework]].

---

##### _lemma:_ path homotopies can be understood locally

Let $H : [0, 1] \times [0, 1] \to X$ be a continuous map, and let $\{ U_{\alpha} \}$ be a cover of $X$. Then there exists some $n$ such that each subsquare $I_{i, j} = \left[ \frac{i - 1}{n}, \frac{i}{n} \right] \times \left[ \frac{j - 1}{n}, \frac{j}{n} \right] \subseteq [0, 1]$ has $\alpha^\text{img}(I_{i, j}) \subseteq U_{\alpha_{i, j}}$ for some $\alpha_{i, j}$.

###### _proof:_
follows similarly — use [[Topology --- math-147/notes/Topological properties of metric spaces#_lemma _ the Lebesgue number lemma|the Lebesgue number lemma]].

---

### Constructing the fundamental group

We construct the fundamental group by defining what it means to take the product of paths, showing that it is associative, demonstrating a path that doesn't change the homotopy class of paths on taking products, and demonstrating an inverse path, taking products with which returns the "identity" path. This amounts to proving the [[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ group, identity, inverse|group axioms]].

Of course, we only need these notions for loops (with a choice of base point). Further, it doesn't even make sense to have a group of paths since you can only compose paths when the end point of the first is the starting point of the second. However, it will be useful to have the notion of composing paths in general, so we write propositions as generally as possible.

##### _definition:_ composition of paths

If $\alpha, \beta$ are paths in $X$ with $\alpha(1) = \beta(0)$ then their **composition** is the path
$$
\alpha \cdot \beta (s) = \begin{cases}
\alpha(2 s) & s \in [0, 1 / 2] \\
\beta(2s - 1) & s \in [1 / 2, 1].
\end{cases}
$$

Equivalently, the composition of two loops $\alpha, \beta : S^1 \to X$ is the composition of the [[Topology --- math-147/notes/Quotient and identification spaces#_definition _ wedge sum|wedge sum]] along the two basepoints, $\alpha \vee \beta : S^1 \vee S^1 \to X$, which depends on the order of $\alpha$ and $\beta$) with the natural map $S^1 \to S^1 \vee S^1$.

---

Less obvious is that this composition descends to equivalence classes as well. We denote the composition of equivalence classes $[\alpha] \cdot [\beta]$.

##### _proposition:_ composition of equivalence classes of paths

If $\alpha, \alpha', \beta, \beta'$ are paths in a space $X$ such that $\alpha \sim \alpha'$ and $\beta \sim \beta'$, and $\alpha(1) = \beta(0)$, then $\alpha \cdot \beta \sim \alpha' \cdot \beta'$. That is, $[\alpha] \cdot [\beta] = [\alpha \cdot \beta]$ is well-defined.

###### _proof:_

Let $H_{a} : [0, 1] \times [0, 1] \to X$ be a homotopy giving $\alpha \sim \alpha'$ and $H_{b} : [0, 1] \times [0, 1] \to X$ a homotopy giving $\beta \sim \beta'$.

Note that $[1, 2] \times [0, 1] \cong [0, 1] \times [0, 1]$ are homeomorphic by the translation $f : (x, y) \mapsto (x - 1, y)$. The pullback $f^{*}H_{b} = H_{b} \circ f : [1, 2] \times [0, 1] \to X$ is then a function with $f^{*} H_{b}(1, t) = \beta(0)$ and $f^{*} H_{b}(2, t) = \beta(1)$ for all $t$. That is, $H_{a}$ and $f^{*} H_{b}$ are continuous functions on closed sets that agree on their intersection $\{ 1 \} \times [0, 1]$ where
$$
H_{a}(1, t) = \alpha(1) = \beta(0) = f^{*} H_{b}(2, t).
$$

Thus, by the [[Topology --- math-147/notes/Continuous functions#_lemma _ the gluing lemma|gluing lemma]], we get one continuous function $H : [0, 2] \times [0, 1] \to X$.

Now we use the homeomorphism $g : [0, 1] \times [0, 1] \to [0, 2] \times [0, 1]$ by $(x, y) \mapsto (2x, y)$. We claim the pullback $g^{*} H = H \circ g : [0, 1] \times [0, 1] \to X$ is the desired homotopy. We can check that $g^{*}H(0, t) = H(0, t) = \alpha(0)$ and $g^{*}H(1, t) = H(2, t) = \beta(1)$ for all $t$. We need to show that $g^{*} H(s, 0) = \alpha \cdot \beta(s)$ and $g^{*}H(s, 1) = \alpha' \cdot \beta'(s)$. We just demonstrate the computation for $g^{*}H(s, 0)$ since the other follows by the exact same steps.
$$
\begin{align}
		g^{*} H(s, 0) & = H(2s, 0) \\
			      & = \begin{cases}
			H_{a}(2s, 0) & s \in [0, 1/2] \\
			H_{b}(2s - 1, 0) & s \in [1/2, 1]
		\end{cases} \\
			      & = \begin{cases}
				      \alpha(2s, 0) & s \in [0, 1/2] \\
				      \beta(2s - 1, 0) & s \in [1/2, 1].
			      \end{cases} \\
			      & = \alpha \cdot \beta(s).
\end{align}
$$

---

##### _proposition:_ composition of equivalence classes is associative

For paths, $\alpha, \beta, \gamma$ in $X$ such that all products below are defined,
$$
([\alpha] \cdot [\beta]) \cdot [\gamma] = [\alpha] \cdot ([\beta] \cdot [\gamma]).
$$

---

##### _definition:_ the constant path

The **constant path** at $x_{0}$ is the constant function $e_{x_{0}} : [0, 1] \to \{ x_{0} \} \subseteq X$.

---

##### _proposition:_ the constant path behaves like the identity

For any path $\alpha$ from $x_{0}$ to $x_{1}$ in $X$, we have $[e_{x_{0}}] \cdot [\alpha] = [\alpha] = [\alpha] \cdot [e_{x_{1}}]$.

###### _proof:_

Consider $F_{0} : [0, 1] \times [0, 1] \to X$ with
$$
F_{0}(s, t) = \begin{cases}
			e_{x_{0}}((1/2 - t/2)s) & s \in [0, 1/2 - t/2] \\
			\alpha((1/2 + t/2)s) & s \in [1/2 - t/2, 1].
\end{cases}
$$
We claim this is a homotopy witnessing $e_{x_{0}} \cdot \alpha \sim \alpha$. Similarly, we claim that
$$
F_{1}(s, t) = \begin{cases}
			\alpha((1/2 + t/2)s) & s \in [0, 1/2 + t/2] \\
			e_{x_{1}}((1/2 - t/2) s) & s \in [1/2 + t/2, 1]
\end{cases}
$$
is a homotopy witnessing $\alpha \sim \alpha \cdot e_{x_{1}}$. Notice that they are well-defined when the two intervals in the cases intersect since $e_{x_{0}} = \alpha(0)$ and $\alpha(1) = e_{x_{1}}$.

Since the arguments are very similar for both, we fully detail the argument for $F_{0}$ pointing out where it may substantially differ for $F_{1}$. Clearly $F_{0}(0, t) = e_{x_{0}} \cdot \alpha$ and $F_{0}(1, t) = \alpha$, and similarly, $F_{1}$ is a function that goes from $\alpha \cdot e_{x_{1}}$ to $\alpha$. Since $F_{0}$ is always $e_{x_{0}}$ at points $(0, t)$ and $\alpha$ at points $(1, t)$

Note that we can divide the domain into three closed sets — the triangle $T_{0} = \{ (s, t) \mid 0 \le s \le 1/2, t \le 1 - 2s \}$, the trapezoid that is the closure $Q_{0} = \overline{[0, 1] \times [0, 1] \setminus T_{0}}$, and their intersection along the line $\{ (s, t) \mid 0 \le s \le 1/2, t = 1 - 2 s \}$. For $F_{1}$, we consider the triangle $T_{1} = \{ (s, t) \mid 1/2 \le s \le 1, t \le 2s - 1 \}$ and the corresponding $Q_{1}$ and intersection instead. By the gluing lemma, it suffices to show that $F_{0}$ is continuous on each of these closed set.

On the triangle $T_{0}$, $F_{0}(s, t) = e_{x_{0}}(s) = x_{0}$. That is, $F_{0}$ is constant, and thus, continuous. Thus, along the line $T_{0} \cap Q_{0}$, $F_{0}$ is also constant, and thus continuous. Thus, we only need show that $F_{0}$ is continuous on $Q_{0}$. 

Note that the image of $[0, 1] \times [0, 1]$ under $F_{0}$ is just $\alpha^{\text{img}}([0, 1])$. Thus, it suffices to consider open sets of the image. Any open $U \subseteq \alpha^{\text{img}}([0, 1])$ has open pre-image in $[0, 1]$, and since $s \mapsto (1/2t + t/2)s$ is continuous in $s$, it has an open pre-image under $s \mapsto F_{0}(s, t)$ in $[1/2 - t/2, 1]$ as well. We must show that the union of these pre-images is open. We will write $\alpha^{\text{pre}}(U)$ as the union of basic open intervals, and show that, for each interval, the union of the corresponding intervals in each $[1/2 - t/2, 1]$ is open. Since the union of these open sets is open, we will have that $\alpha^{\text{pre}}(U)$ is open, and $F_{0}$ is continuous on $Q_{0}$, completing the proof.

In the top interval of $[0, 1] \times [0, 1]$ $(a, b)$ corresponds to $(a, b) \times \{ 1 \}$. In the horizontal interval corresponding to $t$, $(a, b)$ corresponds to $I_{t} = (1/2 - t/2 + (1/2 + t/2) a, 1/2 - t/2 + (1/2 + t/2) b)$ which we abbreviate to $I_{t} = (a_{t}, b_{t})$. Thus, their union is
$$
I = \{ (s, t) \mid 0 \le t \le 1, s \in I_{t} \}.
$$

For each $(s, t) \in I$, there is some $(s - \delta, s + \delta) \subsetneq I_{t}$, and thus there is some sufficiently small $\varepsilon > 0$ such that $(s - \delta, s + \delta) \times (t - \varepsilon, t + \varepsilon) \subseteq I$. Specifically, by considering the slopes $m_{a}$ and $m_{b}$ of lines defining $a_{t}$ and $b_{t}$ as functions of $t$, we get
$$
\varepsilon < \min \{ (a_{t} - (s - \delta)) / m_{a}, (b_{t} - (s + \delta)) / m_{b} \}.
$$
Thus, $I$ is the union of basic open sets and is open.

---

##### _definition:_ the reverse path

For a path $\alpha$ in $X$, its **reverse path** is $\alpha ^{-1}$ defined by $\alpha ^{-1}(s) = \alpha(1 - s)$.

---

##### _proposition:_ the reverse path behaves like the inverse

For a path $\alpha$ in $X$, starting at $x_{0}$, its composition with its reverse path is homotopic to the constant path — $[\alpha] \cdot [\alpha ^{-1}] = [e_{x_{0}}]$.

###### _proof:_

Consider the function
$$
F(s, t) = \begin{cases}
			\alpha_{\mid [0, t]}(s) & s \in [0, 1/2 - t/2] \\
			e_{\alpha(t)} & s \in [1/2 - t/2, 1/2 + t/2] \\
			\alpha_{\mid [1 - t, 1]} & s \in [1/2 + t/2, 1].
		\end{cases}
$$

We claim that this is a homotopy witnessing $\alpha \cdot \alpha^{-1} \sim e_{x_{0}}$. Clearly $F$ satisfies the boundary conditions to be the desired homotopy — $F(s, 1) = e_{x_{0}}$ and $F(s, 0) = \alpha \cdot \alpha^{-1}$, and $F(0, t) = F(1, t) = x_{0}$ for all $t$. Thus, we only need to prove that $F$ is continuous. There are 3 natural closed sets we can divide  $[0, 1] \times [0, 1]$ into, corresponding to the three cases defining $F$. These are the triangles
$$
T_{1} = \{ (s, t) \mid 0 \le t \le 1, s \le 1/2 - t/2 \} \quad \text{and} \quad T_{2} = \{ (s, t) \mid 0 \le t \le 1, s \ge 1/2 + t/2 \}
$$
and the closure of their complement, the triangle $T_{3}$.

We can separately check that $F$ is continuous on each of these triangles. On $T_{3}$, $F$ is constant at $e_{x_{0}}$. On $T_{1}$ the homotopy is the composition of continuous functions — $F_{\mid T_{1}}(t, s) = \alpha \circ \pi_{s}$. On $T_{2}$ this is is also true — $F_{\mid T_{2}}(t, s) = \alpha(1 - \pi_{s}(s, t))$. Thus, $F$ is continuous on $T_{1}$ and $T_{2}$ as well. Clearly $F$ is continuous on their intersections since it is constant on each — each of the intersections is in $T_{3}$ where $F$ is constant. Thus, by the gluing lemma, $F$ is continuous and the desired homotopy.

---

All of these propositions above suffice to show that the fundamental group really is a group. That is,

##### _definition:_ fundamental group

For a choice of base point $x_{0} \in X$, the **fundamental group based at $x_{0}$** is $\pi_{1}(X, x_{0})$, the group of equivalence classes of loops with base point $x_{0}$ under composition.

---

##### _definition:_ simply connected

$X$ is **simply connected** if it is [[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ path-connected|path-connected]] and $\pi_{1}(X, x_{0}) = 0$ for each $x_{0} \in X$.

---