---
tags:
- math-135/1
- math-135/2
- anal
---

Complex analysis is the study of differentiable functions $f : \mathbb{C} \to \mathbb{C}$. Why is this any different from real analysis? Here are some examples.
- A differentiable function $f : \mathbb{C} \to \mathbb{C}$ with $f(1/n) = 0$ always is just $0$ everywhere
- If $f$ is bounded, it must be constant
- If $f$ doesn't attain $1$ and $-1$ (or any two complex numbers), it is constant.

Most of these differences are due to a deep "representation" type result that says the information inside a "two-dimensional" region in the complex plane can be represented by its one-dimensional boundary.
![[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ Cauchy integral formula|Cauchy integral formula]]

### Complex numbers and the complex plane

##### _definition:_ the complex numbers, $\mathbb{C}$

The complex numbers are one of the following isomorphic notions
- $\mathbb{R}[i]$ where $i^2 = -1$
- $\mathbb{R}[x]/(x^2 + 1)$
- The matrices on $\mathbb{R}^{2}$ of the form $\begin{bmatrix}a & b \\ -b & a\end{bmatrix}$

To see how the first two are equivalent, consider $\varphi : f \mapsto f(i)$. $\varphi$ has kernel $(x^{2} + 1)$. This is essentially just replacing $x$ with $i$ in each polynomial. The first and third are equivalent because of the isomorphism $\varphi : a + bi \mapsto \begin{bmatrix} a & b \\ -b & a\end{bmatrix}$. Also see that we can write the matrix as $\sqrt{ a^{2} + b^{2} } \begin{bmatrix} \cos \theta & \sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$ — rotating by the argument $\theta$ and then scaling by the magnitude.

Often we write a complex number $z$ as $a + bi$ for some pair real numbers $i$. We say $a$ is the real part of $z$ — $\operatorname{Re} i$ and $b$ is the imaginary part of $i$ — $\operatorname{Im} i$.

The complex plane gives us a nice way to visualise the complex numbers. If we map $z = a + bi$ to $(a, b) \in \mathbb{R}^{2}$, then the addition of complex numbers corresponds to adding vectors and multiplication corresponds to adding their angle form the positive $x$-axis and multiplying their magnitudes.

Since the complex numbers are really just trying to make $\mathbb{R}$ algebraically complete, it makes sense to think of them as $\mathbb{R}[x]/(x^{2} + 1)$. In particular, in this view, $\mathbb{R}$ cannot really distinguish between $i$ and $-i$. In fact, the complex roots of a real polynomial come in pairs $a + bi$ and $a - bi$. Thus, it's natural to define the complex conjugate.

##### _definition:_ complex conjugate, $\overline{z}$

The complex conjugate of $z = a + bi$ is $\overline{z} = a - bi$.

See below, some facts about the complex conjugate (we don't prove them).

##### _proposition:_ algebraic properties of complex conjugation

For any $z, w \in \mathbb{C}$, with $z = a + bi$
1) $\overline{z} + \overline{w} = \overline{z + w}$
2) $\overline{z} \, \overline{w} = \overline{zw}$
3) $z + \overline{z} = 2a$
4) $z - \overline{z} = 2bi$

This also allows us to define the natural notion of the magnitude of a complex number (coinciding with its length in the complex plane)

##### _definition:_ norm, magnitude, $\lvert z \rvert$

The norm or magnitude of $z = a + bi$ is $\lvert z \rvert = \sqrt{ z \overline{z} } = \sqrt{ a^{2} + b^{2} }$.

The norm bounds the real and imaginary parts of $z$ in the obvious way — it's clear that $a, b < \sqrt{a^{2} + b^{2}}$.

Note that the norm is multiplicative —
$$
\begin{split}
\lvert zw \rvert & = \sqrt{ zw \overline{zw} } \\
 &  = \sqrt{ z \overline{z}w\overline{w}  }\\
 & = \sqrt{ z \overline{z} } \sqrt{ w\overline{w} } \\
 & = \lvert z \rvert \lvert w \rvert .
\end{split}
$$

The norm gives an easy way to see that $\mathbb{C}$ is a field — for any non-zero $z$, $\overline{z} / \lvert z \rvert^{2}$ is a multiplicative inverse.

The magnitude is also clearly positive definite, and satisfies the triangle inequality.

##### _theorem:_ triangle inequality

For any $z, w \in \mathbb{C}$ we have $\lvert z + w \rvert \le \lvert z \rvert + \lvert w \rvert$.

###### _proof:_

Since both sides are non-negative, we can compare their squares instead. 
$$
\begin{split}
\lvert z + w \rvert^2 & = (z + w)\overline{(z + w)} \\
 & = \lvert z \rvert ^{2} + \lvert w \rvert ^{2} + \overline{z}w + z \overline{w} \\
 & = \lvert z \rvert ^{2} + \lvert w \rvert ^{2} + 2 \operatorname{Re} (\overline{z} w) \\
 & \le \lvert z \rvert ^{2} + \lvert w \rvert ^{2} + 2 \lvert \overline{z}w \rvert  \\
 & = \lvert z \rvert ^{2} + \lvert w \rvert ^{2} + 2 \lvert z \rvert  \lvert w \rvert \\
 & = (\lvert z \rvert + \lvert w \rvert )^{2}.
\end{split}
$$

##### _corollary:_ reverse triangle inequality

For any $z, w \in \mathbb{C}$ we have $\lvert z - w \rvert \ge \lvert \lvert z \rvert - \lvert w \rvert \rvert$.

###### _proof:_

We can write $z = z - w + w$ and $w = w - z + z$. Then, by the triangle inequality, we have $\lvert z \rvert \le \lvert z - w \rvert + \lvert w \rvert$ and $\lvert w \rvert \le \lvert w - z \rvert + \lvert z \rvert$. In other words, we have
$$
\begin{split}
\lvert z - w \rvert & \ge \lvert z \rvert - \lvert w \rvert  \\
\lvert z - w \rvert & \ge \lvert w \rvert - \lvert z \rvert 
\end{split}
$$
Naturally, with the triangle inequality, this magnitude gives us a metric on $\mathbb{C}$ that makes it a [[Complex Analysis --- math-135/notes/Analysis and (metric) topology review|metric/topological space]].

### Polar representation

Finally, every complex number can be given in polar representation. If we accept as shorthand $e^{i \theta} = \cos \theta + i \sin \theta$, then we can see that every complex number can be represented by its magnitude, $\lvert z \rvert$, and its angle from the positive $x$ axis, $\theta$, also called its argument. Notice that $z$ does not have a unique argument. 

If we accept that the shorthand $e^{i \theta}$ follows the regular multiplication rules for exponents, this also gives a justification for thinking of complex multiplication as adding angles and dilating by the magnitude. That is $e^{i \theta} e^{i \varphi} = e^{i(\theta + \varphi)}$. You can also think about this by using similar triangles (see Knopp?).