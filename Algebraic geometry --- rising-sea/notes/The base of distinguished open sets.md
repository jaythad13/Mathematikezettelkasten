---
tags:
- alg-geo
- comm-alg
- rising-sea/3/5
---

Let $A$ be a ring. Assume we are working in the topological space (and affine scheme) $\operatorname{Spec} A$.

The [[Algebraic geometry --- rising-sea/notes/Affine schemes#The space (the Zariski topology)|topology of an affine scheme]] can be kind of horrible. It is defined in terms of closed sets, so provides almost no intuition for opens. Further, understanding all closed sets of $\operatorname{Spec} A$ is understanding all ideals of $A$ at the very least, and really requires understanding the 

We can understand the Zariski topology via a particularly nice base instead! These only require understanding the containment of particular elements in primes. This can also be thought of as follows. The only closed sets we need to care about are $V(f)$ since we can get the rest of the $V(\mathfrak{i})$ as intersections of $V(f_{i})$ for $\mathfrak{i} = (\{ f_{i} \}_{i \in \mathscr{I}})$.

##### _definition:_ distinguished open set, doesn't vanish set

For $f \in A$, the **distinguished open set** (or **doesn't vanish set**) of $f$ is
$$
D(f) = \{ \mathfrak{p} \in \operatorname{Spec} A \mid f \not\in \mathfrak{p} \iff f(\mathfrak{p}) \neq 0 \} = \operatorname{Spec} A \setminus V(f).
$$

That is, the distinguished open set corresponding to $f$ is the locus where $f$ doesn't vanish.

---

These form a base of the Zariski topology. Usually proving that a set of open sets is a base requires proving some tedious equivalent condition. Here however, we can prove this directly. Essentially we show that the complement of the locus where an ideal vanishes is covered by the loci where each of the functions in the ideal doesn't vanish.

##### _proposition:_ the distinguished open sets form the distinguished open base

The set of all distinguished open sets $\{ D(f) \mid f \in A \}$ forms a [[Topology --- math-147/notes/Bases#_definition _ basis|base]] for the Zariski topology on $\operatorname{Spec} A$.

###### _proof:_

Each $D(f) = \operatorname{Spec} A \setminus V(f)$ is open. We show that each open set $U = \operatorname{Spec} A \setminus V(\mathfrak{i})$ is the union of all $D(f)$ with $f \in \mathfrak{i}$. 

Suppose $\mathfrak{p} \in U$. Then $\mathfrak{i} \not \subseteq \mathfrak{p}$. There must be some $f \in \mathfrak{i}$ with $f \not\in \mathfrak{p}$. That is, $\mathfrak{p} \in D(f)$. Thus, $U \subseteq \bigcup_{f \in \mathfrak{i}} D(f)$. Conversely, suppose $\mathfrak{p} \in \bigcup_{f \in \mathfrak{i}} D(f)$. Thus, $\mathfrak{p} \in D(f)$ for some $f \in \mathfrak{i}$. That is, $f \not\in \mathfrak{p}$ for some $f \in \mathfrak{i}$ implying $\mathfrak{i} \not \subseteq \mathfrak{p}$. Thus, $\mathfrak{p}$

---

### Facts about the distinguished open base

This distinguished base has some particularly nice properties blending algebra and topology.

For example, open covers by distinguished opens give us at each $\mathfrak{p} \in \operatorname{Spec} A$ some $f$ not vanishing at it. From this, we hope to generate the function $1$ which alone is non-zero at each prime. Conversely, if we can generate every function, the union of their non-vanishing loci is the whole space.

##### _proposition:_ distinguished covers generate the whole ring

$\bigcup_{i \in \mathscr{I}} D(f_{i}) = \operatorname{Spec} A$ if and only if $(\{ f_{i} \}_{i \in \mathscr{I}}) = A$.

###### _proof:_

Let $\mathfrak{i} = (\{ f_{i} \}_{i \in \mathscr{I}})$.

Suppose $\bigcup_{i \in \mathscr{I}} D(f_{i}) = \operatorname{Spec} A$. Equivalently, (by De Morgan's law) $\bigcap_{i \in \mathscr{I}} V(f_{i})$ is empty. Recall that $\bigcap_{i \in \mathscr{I}} V(f_{i}) = V(\mathfrak{i})$. But then $V(\mathfrak{i}) = \text{Ø} = V(1)$, [[Algebraic geometry --- rising-sea/notes/Affine schemes#_proposition _ vanishing sets uniquely identify only radical ideals|so]] $\sqrt{ \mathfrak{i} } = \sqrt{ (1) } = A$. That is, [[Algebraic geometry --- rising-sea/notes/Radicals of ideals#_proposition _ the radical is the intersection of all primes containing the ideal|the intersection of all primes containing]] $\mathfrak{i}$ is the whole ring, and thus, the empty intersection. Since no prime contains $\mathfrak{i}$, no maximal ideal contains $\mathfrak{i}$, so $\mathfrak{i}$ contains a unit and is the whole ring itself.

Suppose $\mathfrak{i} = A$. Consider some $\mathfrak{p} \in \operatorname{Spec} A$. If we had $\mathfrak{p} \not\in \bigcup_{i \in \mathscr{I}} D(f_{i})$, then all $f_{i} \in \mathfrak{p}$. This would force $\mathfrak{i} = A \subseteq \mathfrak{p}$ which cannot be since primes are proper ideals. Thus, every point $\mathfrak{p}$ is covered by the $D(f_{i})$.

---

This means, for one, that all open covers of an affine scheme restrict to finite subcovers. This is a notion that we will later define as [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes|quasicompactness]] (since it is topological compactness, but isn't quite the right notion that we want in algebraic geometry).

##### _corollary:_ every affine scheme is quasicompact

$\operatorname{Spec} A$ is [[Topology --- math-147/notes/Compactness#_definition _ compact|topologically compact]].

###### _proof:_

[[Topology --- math-147/notes/Compactness#_proposition _ checking compactness on a basis|It suffices]] to show every cover by distinguished opens restricts to a finite subcover. Suppose $\operatorname{Spec} A = \bigcup_{i \in \mathscr{I}} D(f_{i})$. Then $(\{ f_{i} \}_{i \in \mathscr{I}}) = A$. In fact, then there is some finite some $\sum_{i = 1}^n a_{i_{k}} f_{i_{k}} = 1$ and $(f_{i_{1}}, \dots, f_{i_{n}}) = A$. Thus, $\bigcup_{k = 1}^n D(f_{i_{k}}) = \operatorname{Spec} A$ — $\{ D(f_{i_{k}}) \}$ is a finite subcover.

---

There are also some more mundane properties.

##### _proposition:_ intersections of distinguished opens are distinguished

$D(f) \cap D(g) = D(fg)$.

###### _proof:_

By De Morgan's laws
$$
D(f) \cap D(g) = \operatorname{Spec} A \setminus (V(f) \cup V(g)) = \operatorname{Spec} A \setminus V((f) (g)) = \operatorname{Spec} A \setminus V(fg) = D(fg).
$$
Here the second equality $V(f) \cup V(g) = V((f) (g))$ is shown in the proof that the Zariski topology is a topology.

---

Notice that we can't say $D(f) \cup D(g) = D(f + g)$ (just choose $f = - g$). In general, this is because $D(f) \cup D(g) = \operatorname{Spec} A + V((f) + (g))$ and $(f) + (g)$ may not be principal.

Finally, it will be important to understand when distinguished opens are contained in each other. If $D(f) \subseteq D(g)$ then $f$ vanishes everywhere on $V(g)$ and we already have a classification of such functions.

##### _proposition:_ containment of distinguished opens

$D(f) \subseteq D(g)$ if and only if $f \in \sqrt{ (g) }$.

###### _proof:_

Since $D(f) = \operatorname{Spec} A \setminus V(f)$, $D(f) \subseteq D(g)$ is equivalent to $V(g) \subseteq V(f)$. This is equivalent to $f$ vanishing at all points of $V(g)$. [[Algebraic geometry --- rising-sea/notes/Affine schemes#_proposition _ functions vanishing on a vanishing set|This is equivalent to]] $f \in \sqrt{ (g) }$.

---

##### _corollary:_ the empty distinguished open

$D(f)$ is empty if and only if $f \in \mathfrak{N}$.

###### _proof:_

Apply the previous result to $D(f) \subseteq D((0)) = \text{Ø}$.

Directly, $D(f)$ is empty if and only if $f$ vanishes at all points $\mathfrak{p} \in \operatorname{Spec} A$ if and only if $f \in \mathfrak{p}$ for all primes of $A$, [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_proposition _ the nilradical is an ideal and the intersection of primes|if and only if]] $f \in \mathfrak{N}$.

---