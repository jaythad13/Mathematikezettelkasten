---
tags:
- math-147/13
- math-147/14
- top
---

Let $(X, \mathcal{T})$ be a topological space.

Compactness is both, a covering property, and also a size restriction. In some sense, it's the next best thing to being finite.

##### _definition:_ cover, open cover, subcover

Suppose $A \subseteq X$ and $\mathcal{O} = \{ U_{\alpha} \}_{\alpha \in \mathcal{I}}$ is a collection of subsets of $X$. $\mathcal{O}$ is a cover of $A$ if $A \subseteq \bigcup_{\alpha \in \mathcal{I}} U_{\alpha}$.

$\mathcal{O}$ is an open cover if each $U_{\alpha}$ is open.

If $\mathcal{O}' \subseteq \mathcal{O}$ is also a cover of $A$, it is called a subcover of $\mathcal{O}$.

##### _definition:_ compact

A subset $A \subseteq X$ is compact if every open cover of $A$ admits a finite subcover.

It turns out that since the [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subspace topology]] plays nicely with compactness (a compact set in a subspace topology is compact in the whole topology, et c.), without loss of generality we can assume our compact set is just the whole space.

##### _theorem:_ the Bolzano-Weierstrass theorem

If $X$ is compact, and $A \subseteq X$ is an infinite subset, $A$ has a limit point.

###### _proof:_

Suppose by way of contradiction that $A$ does not have a limit point. Then every point $x \not\in A$ has an open neighbourhood $U_{x}$ not intersecting $A$ and every point $a \in A$ has an open neighbourhood $U_{a}$ that has empty intersection with ${A \setminus a}$. The collection of these open neighbourhoods $\mathcal{O} = \{ U_{x} \mid x \in X \}$ is an open cover of $A$.

Since each open neighbourhood contains at most one point of $A$, any finite subset of $\mathcal{O}$ would not cover $X$. This is a contradiction because $X$ is compact.

Compactness is also intimately connected with something called the finite intersection property.

##### _definition:_ finite intersection property

A collection of sets has the finite intersection property if every finite subcollection has non-empty intersection.

It is interesting to ask whether checking for the finite intersection property is sufficient to determine whether the collection as a whole has non-empty intersection. This is certainly not always true — in ${[-1, 1] \setminus \{ 0 \} }$, the sets $\{ [-1 / n, 1 / n] \}_{n \in \mathbb{N}}$ have the finite intersection property, but the infinite intersection is empty. 

The spaces for which checking the finite intersection property (for closed sets) is sufficient are exactly the compact sets.

##### _theorem:_ compactness is equivalent to FIP $\implies$ non-empty intersection

$X$ is compact if and only if collections of closed sets with the finite intersection property have non-empty intersection.

###### _proof:_

First suppose $X$ is compact. We will show that any collection of closed sets with empty intersection cannot have the finite intersection property. Suppose that $\{ A_{\alpha} \}_{\alpha \in \mathcal{I}}$ has empty intersection. By [[Mathematical Analysis I --- math-131/notes/Open and closed sets#_theorem _ De Morgan's law|De Morgan's law]], for $U_{\alpha} = {X \setminus A_{\alpha}}$, we have an open cover
$$
\bigcup_{\alpha \in \mathcal{I}} U_{\alpha} = X \setminus \bigcap_{\alpha \in \mathcal{I}} A_{\alpha} = X.
$$

Since $X$ is compact, it follows that there is a finite subcover $\{ U_{\alpha_{1}}, \dots, U_{\alpha_{n}} \}$. But then if
$$
\bigcup_{i = 1}^n U_{\alpha_{i}} = X \setminus \bigcap_{i = 1}^n A_{\alpha_{i}} = X
$$
the intersection $\bigcap_{i = 1}^n A_{\alpha_{i}}$ must be empty. That is, $\{ A_{\alpha} \}_{\alpha \in \mathcal{I}}$ does not have the finite intersection property.

Now suppose that $X$ is not compact. Then there must be an open cover $\{ U_{\alpha} \}_{\alpha \in \mathcal{I}}$ that does not admit a subcover. By the same application of De Morgan's law as previously, the collection of closed sets given by $A_{\alpha} = {X \setminus U_{\alpha}}$ has empty intersection. We claim that this is despite $\{ A_{\alpha} \}_{\alpha \in \mathcal{I}}$ satisfying the finite intersection property. 

By De Morgan's law, for any finite subcollection $\{ A_{\alpha_{1}}, \dots, A_{\alpha_{n}} \}$, we can write
$$
\bigcap_{i = 1}^n A_{\alpha_{i}} = X \setminus \bigcup_{i = 1}^n U_{\alpha_{i}}.
$$
Since $\{ U_{\alpha} \}_{\alpha \in \mathcal{I}}$ does not admit any finite subcovers, the finite union of $U_{\alpha_{i}}$ is not the whole space $X$, and thus, the finite subcollection of $A_{\alpha_{i}}$ has non-empty intersection. Since the finite subcollection was arbitrary, $\{ A_{\alpha} \}_{\alpha \in \mathcal{I}}$ has the finite intersection property.

##### _proposition:_ closed subspaces of compact spaces are compact

If $X$ is compact and $A \subseteq X$ is closed, then $A$ is compact.

###### _proof sketch:_

Suppose $\mathcal{O}$ is an open cover of $A$. Then $\mathcal{O} \cup \{ X \setminus A \}$ is an open cover of $X$. It reduces to a finite subcover $\mathcal{O}'$. Since ${X \setminus A}$ has no intersection with $A$, we can remove it from $\mathcal{O}'$ to get a finite subcover of $\mathcal{O}$. That is $A$ is compact.

##### _proposition:_ compact subsets of Hausdorff spaces are closed

If $X$ is [[Topology --- math-147/notes/Separation properties#_definition _ Hausdorff spaces, $T_{2}$ spaces|Hausdorff]] and $A \subseteq X$ is compact, then $A$ is closed.

###### _proof:_

Consider any point $p \in {X \setminus A}$. We will show that it's not a limit point of $A$. Since $X$ is Hausdorff, for each $a \in A$, we have $p \neq a$ and there is an open neighbourhood of $a$, say $U_{a}$ that doesn't intersect a corresponding open neighbourhood $V_{a}$ of $p$.

$\mathcal{O} = \{ U_{a} \}_{a \in A}$ is an open cover of $A$ and admits a finite subcover $\mathcal{O}' = \{ U_{a_{1}}, \dots, U_{a_{n}} \}$. The corresponding $V_{a_{i}}$ have finite intersection $V$ that is disjoint from each $U_{a_{i}}$, and thus, their union. Since $A \subseteq \bigcup_{i = 1}^n U_{a_{i}}$ it too is disjoint from $V$. This non-intersecting open neighbourhood [[Topology --- math-147/notes/Limit points and closed sets#_proposition _ limit points not in the set|is sufficient to show]] that $p \not\in A$ is not a limit point of $A$.

##### _example:_ compact subsets need not be closed

##### _theorem:_ compact Hausdorff spaces are normal

If $X$ is compact and Hausdorff, $X$ is [[Topology --- math-147/notes/Separation properties#_definition _ normal spaces, $T_{4}$ spaces|normal]] (and in fact, $T_{4}$, [[Topology --- math-147/notes/Separation properties#_proposition _ hierarchy of separation properties|and thus]], $T_{3}$).

###### _proof sketch:_

Use a similar trick to above to show $X$ is at least [[Topology --- math-147/notes/Separation properties#_definition _ regular spaces, $T_{3}$ spaces|regular]], then extend to normality.