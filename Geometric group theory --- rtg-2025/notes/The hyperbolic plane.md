---
tags:
- ggt
- cx-geo
- rtg-2025/1
- rtg-2025/2
---

Recall the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Riemann surfaces#_example _ the Riemann sphere and the complex projective line|Riemann sphere as complex projective space]] 
$$
\mathbb{C} \mathbb{P}^1 = (\mathbb{C}^{2} \setminus \{ 0 \}) / \mathbb{C}^\times
$$
where we quotient by the action of $\mathbb{C}^\times$ by scalar multiplication. Note that it is the [[Topology --- math-147/attachments/exam/exam.pdf#page=1|one point compactification]] of $\mathbb{C}$, and also homeomorphic to the $2$-sphere $S^{2}$ (by stereographic projection).

Hyperbolic geometry occurs on a subset of $\mathbb{C} \mathbb{P}^1$.

##### _definition:_ upper half-plane, hyperbolic plane

The upper half-plane or hyperbolic plane is the subset of complex projective space
$$
\mathbb{H}^{2} = \{ (z : w) \in \mathbb{C} \mathbb{P}^1 \mid w = 1 \text{ and } \operatorname{Im} z > 0 \}.
$$

In the $S^{2}$ model of the complex projective line, this is the "strict upper hemisphere". It doesn't include its (topological) boundary, $\partial \mathbb{H}^{2} = \mathbb{R} \mathbb{P}^1$ which is the equator.

### Möbius transformations

We will build geometry on $\mathbb{H}^{2}$ from the perspective of Felix Klein — by defining what group we want to [[Geometric group theory --- rtg-2025/notes/Isometric actions|act isometrically]] on it. It's a fact of complex analysis that any automorphisms of $\mathbb{H}^{2}$ extend to $\mathbb{C} \mathbb{P}^1$, and so it's natural to study the automorphisms of the Riemann sphere and just see which of them restrict to the hyperbolic plane.

##### _definition:_ Möbius transformation

The group action $\mathrm{GL}_{2}(\mathbb{C}) \circlearrowright \mathbb{C}\mathbb{P}^1$ by
$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix} (z : w) = \left( {az + bw} : {cz + dw} \right)
$$
is called the action by Möbius transformations. Note that the action of a matrix $A$ on a point $(z : w)$ is exactly the same as the action by matrix multiplication — we have $A \cdot (z : w) = (x : y)$ where $(x, y) = A(z, w)$.

Each function $(z : w) \mapsto A \cdot (z : w)$ is called a Möbius transformation and the group of all Möbius transformations is called $\operatorname{Möb} \mathbb{C}\mathbb{P}^1$.

Recall that $\operatorname{Möb} \mathbb{C} \mathbb{P}^1$ [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_examples _ interesting isomorphisms|is exactly the automorphism group]] of the Riemann sphere as a Riemann surface/complex manifold/algebraic curve.

Note also that $\mathbb{C}^* \le \mathrm{GL}_{2}(\mathbb{C})$ is part of the [[Abstract algebra --- math-171/notes/Group actions#_definition _ kernel, effective action|kernel]] of the group actions, so the action descends to an action of the projective general linear group $\mathrm{PGL}_{2}(\mathbb{C})$ (which incidentally is the same as $\mathrm{PSL}_{2}(\mathbb{C})$).

This action of $\mathrm{PGL}_{2}(\mathbb{C})$ on $\mathbb{C} \mathbb{P}^1$ has the interesting property that it is (sharply) $3$-transitive.

##### _proposition:_ Möbius transformations are three-transitive

For each pair of triples of points in $\mathbb{C} \mathbb{P}^1$, $(z_{1}, z_{2}, z_{3}), (w_{1}, w_{2}, w_{3})$, there is a unique Möbius transformation $f \in \operatorname{Möb} \mathbb{C} \mathbb{P}^1$ such that $f(z_{j}) = w_{j}$ for each $j$.

###### _proof:_

It suffices to prove this in the case that $(w_{1}, w_{2}, w_{3}) = (0, \infty, 1)$. We will construct the desired Möbius transformation one point at a time, fixing each previous image.

Clearly $f_{1}(z) =  z - z_{1}$ has $f_{1}(z_{1}) = 0$. Then $f_{2}(z) = z / (z - f(z_{2}))$ fixes $0$, but has a pole at $f_{1}(z_{2}) = z_{2} - z_{1}$. Finally, $f_{3}(z) = z / f_{2}(f_{1}(z_{3}))$ fixes $0$ and $\infty$ but maps $f_{2}(f_{1}(z_{3})) = (z_{3} - z_{1}) / (z_{3} - z_{2}) \mapsto 1$. Thus, $f = f_{3} \circ f_{2} \circ f_{1}$, given by
$$
f(z) = \frac{z - z_{1}}{z - z_{2}} / \frac{z_{3} - z_{1}}{z_{3} - z_{2}}
$$
is the desired Möbius transformation.

Since the map $z \mapsto 1 / z$ swaps $0$ and $\infty$ and the map $z \mapsto az / (z - a)$ swaps $a$ and $\infty$, we can deal with the case of one of the $z_{j} = \infty$ by pre composing with one of these so that $z_{j} \neq \infty$ and $z_{j} \neq z_{k}$ for $j \neq k$.

So under which Möbius transformations is the hyperbolic plane $\mathbb{H}^{2}$ is invariant?

##### _theorem:_ Möbius transformations acting on hyperbolic plane are $\mathrm{PSL}_{2}(\mathbb{R})$

The group of Möbius transformations under which $\mathbb{H}^{2}$ is invariant is isomorphic to $\mathrm{PSL}_{2}(\mathbb R)$. We write this as $\operatorname{Möb} \mathbb{H}^{2} \cong \mathrm{PSL}_{2}(\mathbb{R})$.

###### _proof sketch:_

Note that if $f$ is a Möbius transformation fixing $\mathbb{H}^{2}$, then by continuity $f$ must also fix its topological boundary. That is $f^\text{img}(\mathbb{R} \mathbb{P}^1) = \mathbb{R} \mathbb{P}^1$. Thus, any $A \in \mathrm{GL}_{2}(\mathbb{C})$ representing $f$ sends $\mathbb{R}^{2}$ to $\lambda \mathbb{R}^{2}$ for some $\lambda \in \mathbb{C}^\times$ under its action by matrix multiplication. Since any $(1 / \lambda) A$ also represents $f$, we can choose $\lambda = 1$ without loss of generality. Then $f$ must be given by a real matrix.

However, invariance of $\mathbb{R} \mathbb{P}^1$ is not sufficient ($\mathbb{R} \mathbb{P}^1$ is invariant under flipping the Riemann sphere as well). Thus, among these real matrices, we also need to restrict to those with
$$
0 < \operatorname{Im} (f(z)) = \operatorname{Im} \left( \frac{az + b}{cz + d} \right) = \frac{y}{\lvert cz + d \rvert ^{2}} \det \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$
(for $z = x + i y$). Here the second equality is a calculation that forces the matrix to have positive determinant. Again, by scaling, without loss of generality, we can assume that the determinant is $1$ (since $A / \sqrt{ \det A }$ has the same action as $A$). Finally, again by scaling we identify $A$ and $-A$.

### The hyperbolic geometry of circles

We can describe the geometry of this group action by its action on lines and circles. In particular, it preserves a very special class of circles.

##### _definition:_ circles in the complex projective line, geodesic circles

A circle on $\mathbb{C} \mathbb{P}^1$ is the set of points corresponding to a circle on the sphere under the natural homeomorphism $\mathbb{C} \mathbb{P}^1 \cong S^{2}$. The set of all such circles is denoted $\mathcal{S}$.

The set of all circles meeting $\mathbb{R} \mathbb{P}^1 \xhookrightarrow[]{} S^2$ orthogonally is distinguished and denoted $\mathcal{S}_{\mathbb{R}}$. We will call them geodesic circles, and eventually justify this name.

The circles that intersect $\infty \in \mathbb{R} \mathbb{P}^1$ look like vertical lines in $\mathbb{C}$ and so are often called lines.

A useful lemma is that the circles can be parameterised in a particular useful form.

##### _lemma:_ parameterising lines and circles in the complex plane

If $S \subseteq \mathbb{C} \mathbb{P}^1$ is a circle or a line in $\mathcal{S}$
$$
S = \{ z \in \mathbb{C} \mid \alpha \lvert z \rvert^{2} + \beta z + \bar{\beta} \overline{z} + \gamma = 0 \}
$$
for some fixed $\alpha, \gamma \in \mathbb{R}$ and $\beta \in \mathbb{C}$. 

If $S$ is a line $\alpha = 0$, and if $S$ is a circle, then $\alpha = 1$. Finally $S$ intersects the real (projective) line $\mathbb{R} \mathbb{P}^1 \subseteq \mathbb{C} \mathbb{P}^1$ orthogonally if and only if $\beta \in \mathbb{R}$.

###### _proof:_

Suppose $S$ is the circle $\{ z \in \mathbb{C} \mid \lvert z - a \rvert = r \}$ for some fixed centre $a \in \mathbb{C}$ and positive real radius $r$. (Since both sides are positive) the equation defining $S$ is equivalent to $\lvert z - a \rvert^{2} - r^{2} = 0$. The expression on the left can be rewritten as
$$
\begin{align}
\lvert z - a \rvert^{2} - r^{2} & = (z - a) \overline{(z - a)} - r^{2} \\
 & = \lvert z \rvert ^{2} - a \overline{z} - \overline{a} z - (\lvert a \rvert ^{2} + r^{2})
\end{align}
$$
Choosing $\alpha = 1$, $\beta = - \overline{a}$, and $\gamma = -(\lvert \alpha \rvert^{2} + r^{2})$ we get $S$ in the desired form. $S$ intersects the real line orthogonally exactly when $S$ has centre $a \in \mathbb{R}$ and thus, exactly when $\beta \in \mathbb{R}$.

Suppose $S$ is the line $\{ z = x + i y \in \mathbb{C} \mid y - mx + c = 0 \}$ where $m, c \in \mathbb{R}$ are fixed. The left expression in the defining equation can be rewritten
$$
(z - \overline{z}) / 2 i - (m / 2) (z + \overline{z})+ c = (-m / 2 - i / 2) z + (-m / 2 + i / 2) \overline{z} + c
$$
Choosing $\beta = (-m / 2 + i / 2)$ and $\gamma = c$, we get the desired form of the defining equation for $S$. $S$ intersects the real line orthogonally if it is given by the equation $mx + c = 0$ or equivalently $(m / 2)(z + \overline{z}) + c = 0$ which we can see from the equation above occurs exactly when $\beta \in \mathbb{R}$.

These constructions can be inverted to recover the original formulae, showing that all loci of points satisfying such an equation give lines or circles.

##### _proposition:_ Möbius transformations fix circles and lines

If $f \in \operatorname{Möb} \mathbb{H}^{2} \cong \mathrm{PSL}_{2}(\mathbb{R})$, then for each circle $S \in \mathcal{S}$ we have $f^\text{img}(S) \in \mathcal{S}$ and further, for each circle $S \in \mathcal{S}_{\mathbb{R}}$ we have $f^\text{img}(S) \in \mathcal{S}_{\mathbb{R}}$.

That is, the action $\mathrm{PSL}_{2}(\mathbb{R}) \circlearrowright \mathbb{H}^{2}$ restricts to actions by images of sets on $\mathcal{S}$ and $\mathcal{S}_{\mathbb{R}}$.

###### _proof:_

Suppose $S = \{ z \in \mathbb{C} \mid \alpha \lvert z \rvert^{2} + \beta z + \overline{\beta} \overline{z} + \gamma = 0 \}$ and $f$ is a Möbius transformation of $\mathbb{H}^{2}$ given by
$$
f(z) = \frac{az + b}{cz + d}
$$
and let $A$ denote the corresponding matrix for notational convenience. Inverting $w = f(z)$ we get the formula
$$
z = f^{-1}(w) = \frac{dw - b}{-c w + a}.
$$
Applying the defining equation of $S$ to $z$ in terms of $w$ forces an equivalent constraint on $w$. In particular,
$$
\begin{align}
& \alpha \left\lvert  \frac{dw - b}{-cw + a}  \right\rvert^{2} + \beta \frac{dw - b}{-cw + a} + \overline{\beta} \overline{\left( \frac{dw - b}{- cw + a} \right)} + \gamma \\ & = \frac{\alpha \lvert dw - b \rvert ^{2} + \beta(dw - b) {(-c \overline{w} + a) } + \overline{\beta} {(d\overline{w} - b)} (-cw + a) + \gamma \lvert -cw + a \rvert^{2}}{\lvert cw + a \rvert ^{2}} \\
 & = ( (\alpha d^{2} - (\beta + \bar{\beta}) cd + \gamma c^{2} ) \lvert w \rvert ^{2} + (- \alpha b d + \beta ad  + \bar{\beta} bc - \gamma  c a) w + (- \alpha bd + \beta bc + \bar{\beta} ad - \gamma c a) \overline{w}  \\
 & + \alpha b^{2} - (\beta + \bar{\beta}) ba + \gamma a^{2} ) / \lvert cw + a \rvert ^{2}.
\end{align}
$$
Since the coefficients are only determined by $a, b, c, d, \alpha, \beta, \gamma$, the same conditions are imposed on any $w = f(z)$. Thus, $f^\text{img}(S)$ is a circle. Further, the coefficients of $w$ and $\overline{w}$ are real exactly when $\beta$ is real (since $ad = bc$ is not allowed) giving that $f^\text{img}(S)$ intersects $\mathbb{R} \mathbb{P}^1$ orthogonally exactly when $S$ does.

In fact, this action is transitive on the circles and lines orthogonal to $\mathbb{R} \mathbb{P}^1$.

##### _proposition:_ the action of Möbius transformations is transitive on geodesic circles

The action $\mathrm{PSL}_{2}(\mathbb{R}) \circlearrowright \mathcal{S}_{\mathbb{R}}$ is transitive.

###### _proof:_
follows from the two lemmas below.

##### _lemma:_ hyperbolic lines are the Möbius strip

An element of $\mathcal{S}_{\mathbb{R}}$ is uniquely determined by the pair of points in $\mathbb{R} \mathbb{P}^1$ it intersects.

This gives a bijection $\mathcal{S}_{\mathbb{R}} \to \text{Möbius band}$. 

###### _proof sketch:_

A circle proper (in $\mathbb{C}$) intersects $x_{1}, x_{2} \in \mathbb{R}$, has centre $a = (x_{1} + x_{2}) / 2$ and radius $r = \lvert x_{1} - a \rvert$. A line intersects $x \in \mathbb{R}$ and $\infty$.

Clearly there is a bijection between $\mathcal{S}_{\mathbb{R}}$ and the set of unordered, distinct pairs of points on the boundary of $\mathbb{H}^{2}$ which is homeomorphic to $S^1$. By a standard [[Topology --- math-147/notes/Quotient and identification spaces#Identification spaces|identification space]] argument we get that this is the Möbius strip.

Another way to see this is by writing down the latter as $\operatorname{Sym}^{2} {\mathbb{R} \mathbb{P}^1} \setminus \Delta$ where $\Delta$ is the diagonal $\{ (x, x) \in \mathbb{R} \mathbb{P}^1 \times \mathbb{R} \mathbb{P}^1 \}$. The Klein bottle $\mathbb{R} \mathbb{P}^1 \times \mathbb{R} \mathbb{P}^1$ breaks down into two Möbius strips after cutting it along the diagonal. Identifying these strips is exactly $\mathbb{R} \mathbb{P}^1 \times \mathbb{R} \mathbb{P}^1 \to \operatorname{Sym}^{2} \mathbb{R} \mathbb{P}^1$.

##### _lemma:_ Möbius transformations on $\mathbb{H}^{2}$ are three-transitive on $\mathbb{R} \mathbb{P}^2$

For each pair of triples of points in $\mathbb{R} \mathbb{P}^1$, $(x_{1}, x_{2}, x_{3}), (y_{1}, y_{2}, y_{3})$, there is a unique Möbius transformation $f \in \operatorname{Möb} \mathbb{H}^{2}$ such that the extension of $f$ to $\overline{\mathbb{H}^{2}}$ by continuity has $f(x_{j}) = y_{j}$ for each $j$.

###### _proof:_

It suffices again to prove the case $(y_{1}, y_{2}, y_{3}) = (0, \infty, 1)$ (we also assume none of the $x_{j} = \infty$ but this can be dealt with separately as previously). The formula for the desired Möbius transformation
$$
f(z) = \frac{z - x_{1}}{z - x_{2}} / \frac{x_{3} - x_{1}}{x_{3} - x_{2}}
$$
was proved previously. However, we only showed that this is a Möbius transformation on $\mathbb{C} \mathbb{P} ^1$. It is still left to show that this is in $\mathrm{PSL}_{2}(\mathbb{R})$ and fixes $\mathbb{H}^{2}$. It follows simply from the fact that all the $x_{j}$ are real and the whole corresponding matrix can be rescaled without changing the transformation.

### The hyperbolic metric

The geometry described above induces a metric on the hyperbolic plane — it is the metric that turns the action of Möbius transformations into an action by isometries. We give this metric by identifying an almost unique positive, [[Topology --- math-147/notes/Continuous functions#_definition _ continuity|continuous]], $\operatorname{Möb} \mathbb{H}^{2}$-invariant $\rho : \mathbb{H}^{2} \to \mathbb{R}$ to integrate against to get the length of a path. Then we define the distance  between two points as the infimum of the lengths of paths between them. Finally, we show that geodesic circles really are geodesics.

##### _proposition:_ existence of an almost unique Möbius-invariant length function

Let $\rho : \mathbb{H}^{2} \to \mathbb{R}$ be positive and continuous. $\rho$'s integrals are Möbius-invariant —
$$
\int_{\sigma} \rho = \int_{f \circ \sigma} \rho 
$$
for each [[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ path|path]] $\sigma : [0, 1] \to \mathbb{H}^{2}$ and each $f \in \operatorname{Möb} \mathbb{H}^{2}$ if and only if $\rho(z) = c / \operatorname{Im} z$ for some positive real $c$.

###### _proof:_

First suppose $\rho$ has Möbius invariant integrals. Then for any path $\sigma$ and any $f$ we have
$$
\int_{f \circ \sigma} \rho = \int_{\sigma} \rho \circ f \lvert f' \rvert  
$$
by change of coordinates. Thus, 
$$
\int_{\sigma} \rho - \rho \circ f \lvert f' \rvert = 0.
$$
Since $\rho$ is continuous, if $\rho - \rho \circ f \lvert f' \rvert$ were ever non-zero (say positive), there would be a neighbourhood $U$ with the function positive everywhere in $U$. A small path $\sigma$ contained in $U$ would then have
$$
\int_{\sigma} \rho - \rho \circ f \lvert f' \rvert > 0
$$
and break our hypothesis. Thus, we must have $\rho = \rho \circ f \lvert f' \rvert$ everywhere, for each $f$. For $f(z) = z + b$, this forces $\rho(z) = \rho(z + b)$. Considering each $f_{w}(z) = z - \operatorname{Re} w$ at $w$ gives $\rho(w) = \rho(i \operatorname{Im} w)$ for each $w$. Finally, considering $f(z) = y z$ with $y > 0$ forces $\rho(z) = \rho(y z) y$. For $z = i$ say, this gives $\rho(y i) = \rho(i) / y$. Thus,
$$
\rho(w) = \rho(i \operatorname{Im} w) = \frac{\rho(i)}{\operatorname{Im}w}.
$$
Since the property of having Möbius-invariant integrals is stable under scaling $\rho$, we can freely scale to get $\rho(w) = c / \operatorname{Im} w$ for any positive $c = \rho(i)$. Typically we choose $c = 1$.

For any $z = x + i y$ and Möbius transformation $f$ represented by matrix $A$ with the usual entries we have
$$
\begin{align}
\rho(z) - \rho \circ f(z) \lvert f'(z) \rvert & = \frac{1}{\operatorname{Im} z} - \frac{1}{\operatorname{Im} f(z)} \lvert f'(z) \rvert  \\
 & = \frac{1}{y} - \frac{\lvert cz + d \rvert ^{2}}{y \det A} \frac{\det A}{\lvert cz + d \rvert ^{2}}  \\
 & = \frac{1}{y} - \frac{1}{y} \\
 & = 0.
\end{align}
$$

##### _definition:_ hyperbolic length, hyperbolic metric

The hyperbolic length of a path $\sigma : [0, 1] \to \mathbb{H}^{2}$ is
$$
\operatorname{length} \sigma = \int_{\sigma} \rho = \int_{0}^1 \rho(\sigma(s)) \lvert \sigma'(s) \rvert  \, ds
$$
where $\rho(z) = 1 / \operatorname{Im} z$.

The hyperbolic metric is the [[Analysis --- math-131/notes/Metric spaces#_definition_ metric space, metric|metric]] $d_{\mathbb{H}^{2}}$ given by the infimum of lengths of paths between two points —
$$
d_{\mathbb{H}^{2}}(z, w) = \inf \{ \operatorname{length} \sigma \mid \sigma(0) = z, \sigma(1) = w \}
$$

The fact that this is actually a metric follows easily from the definition of the length function as an integral of a positive continuous function.

##### _corollary:_ Möbius transformations [[Geometric group theory --- rtg-2025/notes/Isometric actions#_definition _ isometric action|act isometrically]] on the hyperbolic plane

Each $f \in \operatorname{Möb} \mathbb{H}^{2}$ preserves the distance between each pair of points $z, w \in \mathbb{H}^{2}$ —
$$
d_{\mathbb{H}^{2}}(f(z), f(w)) = d_{\mathbb{H}^{2}}(z, w).
$$

###### _proof sketch:_

Since the length function is invariant under Möbius transformation, so is the infimum of lengths between pairs of points. Thus, hyperbolic distance is invariant under Möbius transformations.

##### _theorem:_ geodesic circles are really geodesics

Suppose $S \in \mathcal{S}_{\mathbb{R}}$. Then for each pair $z, w \in S$, a regular path $\sigma : [0, 1] \to S$ from $z$ to $w$ has the minimal length $d_{\mathbb{H}^{2}}(z, w)$. 

###### _proof:_

First we show that the imaginary axis line $i\mathbb{R}$ is a geodesic. Then we show that every other circle is a geodesic by mapping it to $i \mathbb{R}$. Given $ia, ib \in i \mathbb{R}$ let $\alpha : [0, 1] \to i \mathbb{R}$ be the path by $\alpha(s) =  i (b - a) s + ia$. This is a regular path $[0, 1] \to i \mathbb{R}$ since it has non-zero derivative everywhere. We compute its length as
$$
\begin{align}
\operatorname{length} \alpha & = \int_{\alpha} \rho \\
 & = \int_{0}^1 \rho(\alpha(s)) \lvert \alpha'(s) \rvert  \, ds \\
 & = \int_{0}^1 \frac{1}{\operatorname{Im} \alpha(s)} (b - a)  \, ds \\
 & = \int_{0}^1 \frac{1}{(b - a) s + a} (b - a) \, ds \\
 & = \ln((b - a) s + a) \Big |_{0}^1 \\
 & = \ln b - \ln a \\
 & = \ln(b / a).
\end{align}
$$

Suppose we have some other path $\beta$ from $ia$ to $ib$ with $\beta(s) = x(s) + i y(s)$. Then we can bound its length from below by the length of $\alpha$ because it must move vertically. Specifically, assuming without loss of generality that $y' > 0$, we write
$$
\begin{align}
\operatorname{length} \beta & = \int_{\beta} \rho \\
 & = \int_{0}^1 \frac{1}{\operatorname{Im} \beta(s)} \lvert \beta'(s) \rvert  \, ds \\
 & = \int_{0}^1 \frac{\sqrt{ x'(s)^{2} + y'(s)^{2} }}{y(s)} \, ds \\
 & \geq \int_{0}^1 \frac{y'(s)}{y(s)} \, ds \\
 & = \ln (y(s)) \Big |_{0}^1 \\
 & = \ln b - \ln a \\
 & = \ln(b / a).
\end{align}
$$

Let $f$ be the unique Möbius transformation sending $S$ to $i \mathbb{R}$. Further, we can choose $f(z) = i$ and $\operatorname{Im} f(w) > \operatorname{Im} f(z)$. Then $\operatorname{length} \sigma = \operatorname{length} f \circ \sigma$. Since $i \mathbb{R}$ is a geodesic, $f \circ \sigma$ minimises length, and so does $\sigma$ — we have $\operatorname{length} f \circ \sigma = d_{\mathbb{H}^{2}}(z, w)$, and thus, $\operatorname{length} \sigma = d_{\mathbb H^{2}}(z, w)$.