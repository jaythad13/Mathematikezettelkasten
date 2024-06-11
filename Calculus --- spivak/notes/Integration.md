---
tags:
- spivak
- calc
- anal
- self-study
---

Once we have a nice notion of [[Calculus --- spivak/notes/Integration over closed rectangles|integrating functions over closed rectangles]], it's easy to extend this to arbitrary bounded subsets of $\mathbb{R}^n$. Just multiply the function by an indicator function to say whether it's in the subset, and then integrate over the whole closed rectangle that it's bounded by. But is this product integrable? Most of the time.

### An aside on integrability

Recall the notion of the [[Calculus --- spivak/notes/Continuity#_definition _ oscillation, $o(f, bvec a)$, $M(f, bvec a, delta)$, $m(f, bvec a, delta)$|oscillation]] of $f$ at $\mathbf{a}$. $o(f, \mathbf{a})$ is the limit of the difference of the maximum and minimum values of $f$ on smaller neighbourhoods of $\mathbf{a}$. This allows us to bound the difference between maximum and minimum values, and thus, bound the difference between [[Calculus --- spivak/notes/Integration over closed rectangles#_definition _ lower and upper sums|lower and upper sums]].

##### _lemma:_ bounded oscillation gives bounded $U(f, P) - L(f, P)$

Let $A \subset \mathbb{R}^n$ be a closed rectangle and let $f : A \to \mathbb{R}^n$ be a bounded function such that $o(f, \mathbf{a}) < \varepsilon$ for all $\mathbf{a} \in A$. Then there is a [[Calculus --- spivak/notes/Integration over closed rectangles#_definition _ partition, subrectangles|partition]] of $A$ (say $P$) such that $U(f, P) - L(f, P) < \varepsilon v(A)$.

###### _proof:_

At each point $\mathbf{a} \in A$, there is a $\delta$-neighbourhood of $\mathbf{a}$ where $M(f, \mathbf{a}, \delta) - m(f, \mathbf{a}, \delta) < \varepsilon$ (by definition of the limit). Consider any closed rectangle subset of the $\delta$-neighbourhood that contains $\mathbf{a}$ and call it $U_{\mathbf{a}}$. Note that $M_{U_{\mathbf{a}}} - m_{U_{\mathbf{a}}} < \varepsilon$ as well. Since the interiors of all the $U_{\mathbf{a}}$ cover $A$ and $A$ is compact, a finite subset of them will cover $A$. That is, we can choose $U_{\mathbf{a}_{1}}, \dots, U_{\mathbf{a}_{k}}$ that cover $A$. 

Define a partition $P$ where all subrectangles in $\mathcal{S}(P)$ are contained in some $U_{\mathbf{a}_{i}}$ (to see that this is possible, just define a partition of each $U_{\mathbf{a}_{i}}$ being careful to make sure that the intersections are partitioned the same way for different $U_{\mathbf{a}_{i}}$). Each subrectangle $s$ will have $M_{s} - m_{s} < \varepsilon$ Then
$$
\begin{split}
U(f, P) - L(f, P) & = \sum_{s \in \mathcal{S}(P)} (M_{s} - m_{s}) v(s) \\
 & < \varepsilon \sum_{s \in \mathcal{S}(P)} v(s) \\
 & = \varepsilon v(A).
\end{split}
$$
Note that we needed the [[Calculus --- spivak/notes/Topological considerations#Compactness|compactness]] of $A$ — otherwise the local boundedness of the maximum-minimum difference wouldn't have translated to global boundedness.

This lemma gives us a very powerful result.

##### _theorem:_ almost-everywhere continuous functions are the integrable functions

Let $A$ be a closed rectangle and $f : A \to \mathbb{R}$ a bounded function. Let $B = \{ \mathbf{b} \in A \mid f \text{ is not continuous at } \mathbf{b} \}$. Then $f$ is integrable if and only if $B$ has measure $0$.

###### _proof:_

First we will show that $B$ having measure $0$ is sufficient for integrability.

Choose any $\varepsilon > 0$. Note that the subset of $B$ for which we can't bound the oscillation of $f$ by $\varepsilon$ [[Calculus --- spivak/notes/Continuity#_proposition _ sufficiently discontinuous sets are closed|is closed]], and thus, [[Calculus --- spivak/notes/Topological considerations#_corollary _ closed bounded sets are exactly the compact sets|is compact]]. Call this $B_{\varepsilon}$. To be precise, $B_{\varepsilon} = \{ \mathbf{b} \in B \mid o(f, \mathbf{b}) \ge \varepsilon \}$. Then since it is a compact measure zero set, [[Calculus --- spivak/notes/Measure#_proposition _ measure $0$ compact sets have content $0$|it has content zero]]. Thus, we have closed rectangles $U_{1}, \dots, U_{n}$ with interiors covering $B_{\varepsilon}$ and $\sum_{i = 1}^n v(U_{i}) < \varepsilon$.

We can partition $A$ (call the partition $P$) with subrectangles $s \in \mathcal{S}(P)$ such that $s$ is either a subset of some $U_{i}$ (we will say $s \in \mathcal{S}_{1}$) or has no intersection with $B_{\varepsilon}$ (we will say $s \in \mathcal{S}_{2}$). To see that this is possible, just cover $B_{\varepsilon}$ with subrectangles that are a subset of $U_{i}$ first, and then extend the partition to the rest of $A$.

Notice that we can bound the sum over the subrectangles in $\mathcal{S}_{1}$. We know that we have a total bound on the difference between the maximum and minimum of $f$ on $A$ since it is bounded. Specifically, if $\lvert f(\mathbf{a}) \rvert < M$ for all $\mathbf{a} \in A$, then $M_{s} - m_{s} < 2M$ for each subrectangle $s$. Thus, we have
$$
\sum_{s \in \mathcal{S}_{1}} v(s) (M_{s} - m_{s}) < 2M \varepsilon 
$$
By the [[#_lemma _ bounded oscillation gives bounded $U(f, P) - L(f, P)$|the previous lemma]], we can partition each of the $s \in \mathcal{S}_{2}$ (call the partition $P_{s}$) so that $U(f, P_s) - L(f, P_{s}) < \varepsilon v(s)$. This gives us a refined partition (say $P'$) on $A$ consisting of the subrectangles of each subrectangle in $\mathcal{S}_{2}$ (call the collection $\mathcal{S}'_{2}$) and the subrectangles in $\mathcal{S}_{1}$. This partition gives us
$$
\begin{split}
U(f, P') - L(f, P') & = \sum_{s' \in \mathcal{S}(P')} (M_{s} - m_{s}) v(s') \\
 & = \sum_{s \in \mathcal{S_{1}}} (M_{s} - m_{s}) v(s) + \sum_{s' \in \mathcal{S}_{2}'} (M_{s} - m_{s}) v(s') \\
 & < 2 M \varepsilon + \sum_{s \in \mathcal{S}_{2}} \varepsilon v(s) \\
 & \le 2 M \varepsilon + \varepsilon v(A) \\
 & = \varepsilon(2M + v(A))
\end{split}
$$
Since $\varepsilon$ can be any positive real, we can make this difference between upper and lower sums arbitrarily small. [[Calculus --- spivak/notes/Integration over closed rectangles#_theorem _ integrable upper and lower sums get arbitrarily close|Thus]], $f$ is integrable.

Suppose that $f$ is integrable. Note that the union of all $B_{1/k}$ gives us all the discontinuous points of $f$ ([[Calculus --- spivak/notes/Continuity#_proposition _ continuous functions do not oscillate|continuous points have no oscillation]]). We can show that each of these has measure $0$, and thus, [[Calculus --- spivak/notes/Measure|so does their countable union]].

Since $f$ is integrable, we choose a partition $P$ such that $U(f, P) - L(f, P) < \varepsilon/k$. Let $\mathcal{S}_{1/k}$ be the set of all of the subrectangles that intersect $B_{1/k}$. $\mathcal{S}_{1/k}$ must cover $B_{1/k}$ (since there are no other subrectangles in the partition that will cover it). Note that $M_{s} - m_{s} \ge 1/k$ for each of these $s$ since within their intersection with $B_{1/k}$ even an arbitrarily small neighbourhood of some $\mathbf{b} \in B_{1/k}$ will have sufficiently big $M_{s} - m_{s}$. Thus, we can bound the sum of the volumes by the difference of the upper and lower sums.
$$
\begin{split}
\frac{1}{k} \sum_{s \in \mathcal{S}_{1/k}} v(s) & \le \sum_{s \in \mathcal{S}_{1/k}} (M_{s} - m_{s})v(s) \\
 & \le \sum_{s \in \mathcal{S}(P)} (M_{s} - m_{s}) v(s) \\
 & = U(f, P) - L(f, P) \\
 & < \frac{\varepsilon}{k}.
\end{split}
$$

From this we get that $\sum_{s \in \mathcal{S}_{1/k}} v(s) < \varepsilon$ for any $\varepsilon$, and thus, that each $B_{1/k}$ has content $0$.

### Integrating over arbitrary sets

Now, we can define the integral of a bounded function over an arbitrary set $C \subset A$.

##### _definition:_ characteristic function of a set

For any $C \subset \mathbb{R}^n$, the characteristic function of $C$ is defined by
$$
\chi_{C}(\mathbf{x}) = \begin{cases}
0  & \mathbf{x} \not\in C \\
1 & \mathbf{x} \in C.
\end{cases}
$$

Now we just need to check that the discontinuities of the product $f \chi_{C}$ are on a small enough set that the function is still integrable. This reduces to just checking for $f$ and $\chi_{C}$ individually. Obviously we want to deal with $f$ continuous-almost-everywhere, and we claim that for nice enough $C$, $\chi_{C}$ is continuous-almost-everywhere since it is only discontinuous on the boundary of $C$.

##### _proposition:_ the characteristic function is integrable if $\partial C$ has measure $0$

The characteristic function $\chi_{C} : \mathbb{R}^n \to \mathbb{R}$ is integrable on $A$ if and only if the boundary of $C$ has measure $0$.

###### _proof:_

We will show that $\chi_{C}$ is discontinuous at $\mathbf{a} \in A$ if and only if it's on the boundary of $C$.

Suppose $\mathbf{a}$ is in the interior of $C$. Then there is an open $\delta$-neighbourhood of $\mathbf{a}$ contained in $C$. For any $\mathbf{x}$ in this $\delta$-neighbourhood, $\lvert f(\mathbf{x}) - f(\mathbf{a}) \rvert = 0 < \varepsilon$ for any positive $\varepsilon$. Thus, $\chi_{C}$ is continuous at $\mathbf{a}$.

Suppose $\mathbf{a}$ is in the exterior of $C$. Then there is an open $\delta$-neighbourhood of $\mathbf{a}$ contained in $\mathbb{R}^n \setminus C$. For any $\mathbf{x}$ in this $\delta$-neighbourhood, $\lvert f(\mathbf{x}) - f(\mathbf{a}) \rvert = 0 < \varepsilon$ for any positive $\varepsilon$. Thus, $\chi_{C}$ is continuous at $\mathbf{a}$.

Suppose $\mathbf{a}$ is on the boundary of $A$. Then every $\delta$-neighbourhood of $\mathbf{a}$ contains points of both, $\mathbf{a}$ and $\mathbb{R}^n \setminus C$. Thus, there is no $\delta$-neighbourhood such that $\lvert f(\mathbf{x}) - f(\mathbf{a}) \rvert < 1$ for all $\mathbf{x}$ in the $\delta$-neighbourhood. That is, $\chi_{C}$ is discontinuous at $\mathbf{a}$.

Thus, $\chi_{C}$ is integrable if and only if $\partial C$ has measure $0$.

This motivates us to categorise such "nice" sets.

##### _definition:_ Jordan-measurable

A subset is said to be Jordan-measurable if it is bounded and has boundary with measure $0$.

And then finally, we have the definition of the integral of such "nice" sets.

##### _example:_ non-Jordan measurable set

We can still have sets that are not Jordan-measurable, and thus, for which integrals are not defined. See [[Calculus --- spivak/attachments/exercises/Calculus on Manifolds/ex 3/ex 3.pdf|the exercises]].


##### _definition:_ integral

The integral of a bounded function $f : A \to \mathbb{R}$ (for $A \subset \mathbb{R}^n$) over a Jordan measurable set $C \subset A$ is the integral of its product with the characteristic function of $C$ over $A$. That is,
$$
\int_{C} f = \int_{A} f \, \chi_{C}.
$$

Now, we can also define the volume of Jordan measurable sets —

##### _definition:_ length, area, volume

The volume of a Jordan measurable set $C$ is $v(C) = \int_{C} 1$.

Obviously, length is the volume of a $1$-dimensional set and area is the volume of a $2$-dimensional set.