---
tags:
- ladr/6B
- self-study
- lin-alg
---

The Riesz representation theorem gives the relationship between two ways to get a number from vectors — applying a linear functional and taking the inner product with another vector.

### Reviewing linear functionals

Recall the definition of a [[Dual spaces|linear functional]]:

##### _definition:_ linear functional

A linear functional on $V$ is a linear map from $V$ to $\bb{F}$. That is, a linear functional is an element of $\mathcal{L}(V, \bb{F})$.

##### _example:_ linear functionals on $\bb{F}^3$

The function $\varphi : \bb{F}^3 \to \bb{F}$ given by 
$$
\varphi(z_1, z_2, z_3) = z_1 + 2 z_2 + 3 z_3
$$
is a linear functional in ${\bb{F}^3}^\vee$. Note that we could also write this as 
$$
\varphi(v) = \langle v, u \rangle
$$
under the Euclidean inner product, with $u = (1, 2, 3) \in \bb{F}^3$.

##### _example:_ linear functional on $\mathcal{P}_2(\bb{R})$

The function $\psi : \mathcal{P}_2(\bb{R}) \to \bb{R}$ given by
$$
\psi(p) = \int_{-1}^1 p(x) \cos{\pi x} \, dx 
$$
is a linear function in ${\mathcal{P}_2(\bb{R})}^\vee$. For this example it is unclear if we could write this as
$$
\psi(p) = \langle p, u \rangle
$$
for some $u \in \mathcal{P}_2(\bb{R})$ with some inner product. Unlike the previous example, we can't just take the inner product given by the integral of the product of functions over $[-1, 1]$ and $u = \cos{\pi x}$ since $\cos{\pi x}$ is not a polynomial.

### Riesz representation theorem

The Riesz representation theorem shows us that we can always find a way to write a functional as an inner product of the input with some fixed vector $u$, even in examples like the previous one where there is no obvious choice for $u$.

##### _theorem:_ Riesz representation theorem

Suppose $V$ is finite-dimensional and $\varphi$ is a linear functional on $V$. Then there is a unique vector $u \in V$ such that
$$
\varphi(v) = \langle v, u \rangle
$$
for every $v \in V$.

###### _proof:_

First we show that there does exist some such $u$.

Since $V$ is finite-dimensional, we have an orthonormal basis $e_1, \ldots, e_m$. For any $v \in V$ we can write
$$
v = \langle v, e_1 \rangle e_1 + \cdots + \langle v, e_m \rangle e_m
$$
which gives us
$$
\varphi(v) = \langle v, e_1 \rangle \varphi (e_1) + \cdots + \langle v, e_m \rangle \varphi(e_m) = \langle v, \overline{\varphi(e_1)} e_1 + \cdots + \overline{\varphi(e_m)} e_m \rangle.
$$
That is, for any arbitrary $v \in V$, we have
$$
\varphi(v) = \langle v, u \rangle
$$
where $u = \overline{\varphi(e_1)} e_1 + \cdots + \overline{\varphi(e_m)} e_m$.

Now we show that there is only one such $u$.

If $\varphi(v) = \langle v, u_1 \rangle = \langle v, u_2 \rangle$ for all $v \in V$, then
$$
\langle v, u_1 \rangle - \langle v, u_2 \rangle = \langle v, u_1 - u_2 \rangle = 0
$$
for all $v \in V$. Thus, 
$$
\langle u_1 - u_2, u_1 - u_2 \rangle = \norm{u_1 - u_2}^2 = 0.
$$
Thus $u_1 - u_2 = 0$ and $u_1 = u_2$, giving us a unique representation.

Note that since $u$ is determined uniquely, even though the expression for involves $e_1, \ldots, e_m$, it doesn't actually depend on the choice of orthonormal basis. Thus, we have the following corollary.

##### _corollary:_

For finite-dimensional $V$, some $\varphi \in V^\vee$, and orthonormal bases of $V$ $e_1, \ldots, e_m$ and $f_1, \ldots, f_m$ we have
$$
\overline{\varphi(e_1)} e_1 + \cdots + \overline{\varphi(e_m)} e_m = \overline{\varphi(f_1)} f_1 + \cdots + \overline{\varphi(f_m)} f_m.
$$
###### _proof:_

By the Riesz representation theorem, we have a unique $u \in V$ such that $\varphi(v) = \langle v, u \rangle$ for all $v \in V$. Specifically
$$
u = \overline{\varphi(e_1)} e_1 + \cdots + \overline{\varphi(e_m)} e_m 
$$
and
$$
u = \overline{\varphi(f_1)} f_1 + \cdots + \overline{\varphi(f_m)} f_m.
$$
Thus, 
$$
\overline{\varphi(e_1)} e_1 + \cdots + \overline{\varphi(e_m)} e_m = \overline{\varphi(f_1)} f_1 + \cdots + \overline{\varphi(f_m)} f_m
$$
as desired.


##### _example:_ a representation of a linear functional on $\mathcal{P}_2(\bb{R})$

Consider the [[#_example _ linear functional on $ mathcal{P}_2( bb{R})$|previous example]] of a linear functional on $\mathcal{P}_2(\bb{R})$: 
$$
\varphi(p) = \int_{-1}^1 p(x) \cos{\pi x} \, dx
$$
for all $p \in \mathcal{P}_2(\bb{R})$.

The [[#_theorem _ Riesz representation theorem|Riesz representation theorem]] gives us a way to find a polynomial $q \in \mathcal{P}_2(\bb{R})$ such that $\varphi(p) = \langle p, q \rangle$ for all $p$, for any choice of inner product. Since it makes computations easier to choose an inner product that works nicely with the functional, and [[Gram-Schmidt procedure#_example _ an orthonormal basis of $ mathcal{P}_2( bb{R})$|we have computed an orthonormal basis for it]] already, we choose 
$$
\langle p, q \rangle = \int_{-1}^1 p(x) q(x) \, dx.
$$
and the corresponding orthonormal basis
$$
\frac{1}{\sqrt 2}, \sqrt{\frac{3}{2}}x, \sqrt{\frac{45}{8}}(x^2 - \frac{1}{3}).
$$
Then we have
$$
q = \overline{\varphi(\frac{1}{\sqrt{2}})} \frac{1}{\sqrt{2}} + \overline{\varphi(\sqrt{\frac{3}{2}}x)} \sqrt{\frac{3}{2}}x + \overline{\varphi(\sqrt{\frac{45}{8}}(x^2 - \frac{1}{3}))} \sqrt{\frac{45}{8}}(x^2 - \frac{1}{3})
$$
which we can just calculate to get
$$
q = - \frac{45}{2 \pi^2} (x^2 - \frac{1}{3}).
$$