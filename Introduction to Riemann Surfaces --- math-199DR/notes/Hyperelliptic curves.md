---
tags:
- math-199DR/11
- cx-geo
- alg-geo
---

Remember [[Algebraic Geometry --- math-176/notes/Elliptic curves#_proposition, definition _ reducing cubics, elliptic curves|elliptic curves]]? They look like complex solution sets of equations $y^{2} = x^3 + Ax + B$ or perhaps $y^{2} = p(x)$ for any cubic in $x$. They generalise to hyperelliptic curves — complex (projective) solution sets of $y^{2} = h(x)$ for $h$ some polynomial in $x$ of degree $2g + 1$ or $2g + 2$ and all distinct roots.

By considering $h(z)$ on two copies of [[Introduction to Riemann Surfaces --- math-199DR/notes/Riemann surfaces#_example _ the Riemann sphere and the complex projective line|the Riemann sphere]], puncturing the sphere at the zeroes, and then gluing the spheres along the zeroes, we get the desired Riemann surface — it contains projective solutions at infinity, and has two copies of $y$ for each $h(x)$ except when $h(x) = 0$, where they are glued together.

How can we do this formally? And without dealing with projective space?

##### _definition:_ hyperelliptic curve

Given a polynomial $h$ of degree $2g - 1$ or $2g - 2$ with all distinct roots.

##### _proposition:_ hyperelliptic curves are compact

The hyperelliptic curve $Z$ corresponding to $y^{2} = h(x)$ is compact.

###### _proof sketch:_

We can decompose $Z$ into two compact sets and take their union — consider the solutions with $\lvert x \rvert \le 1$ and the solutions with $\lvert z \rvert \le 1$. When $\lvert x \rvert > 1$, $\lvert z \rvert \le 1$. Thus, these two compact sets cover $Z$.

##### _proposition:_ the genus of a hyperelliptic curves

The hyperelliptic curve $Z$ corresponding to $y^{2} = h(x)$ 

###### _proof sketch:_

Consider $\pi : Z \to \mathbb{C}_{\infty}$ by $(x, y) \mapsto x$ or $(z, w) \mapsto 1 / z$ and anything else sent to $\infty$. We claim this map has degree $2$.

We want solutions to $y^{2} = h(x)$ where $h$ has degree $2g + 1$ or $2g + 2$. If $h$ has degree $2g + 1$ there's an extra ramification point at infinity. In either case, we have a bunch of [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ ramification point, branch point|ramification points]] of multiplicity $2$ (they can have multiplicity at most $2$ and anything less wouldn't be ramified). Computing the genus $g_{Z}$ from [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#Hurwitz' formula|Hurwitz' formula]], we get $g_{Z} = g$ as desired.

Recall that maps $Z \to \mathbb{C}_{\infty}$ of degree $2$ [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological invariants of a surface#_definition _ monodromy (representation) of a holomorphism|monodromy representations]] $\pi_{1}(\mathbb{C}_{\infty} \setminus B) \to S_{2}$. It is a fact of topology that for $\lvert B \rvert = 2 g + 2$ the fundamental group in question is the free group with $2g + 1$ generators. 