---
tags:
  - math-199DR/10
  - math-199DR/11
  - cx-geo
  - alg-geo
---

##### _definition:_ monodromy (representation) of a covering map

Given a cover $f : U \to X$ (of finite [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_theorem _ degree is constant|degree]] $d$), the fundamental group $\pi(X)$ acts on $U$ and specifically $f^\text{pre}(\{ q \})$, then there exists a permutation representation (read, [[Abstract algebra --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphism]])
$$
\rho : \pi_{1}(X) \to \mathfrak S_{d}
$$
called the monodromy representation of $f$.

But this only allows us to think about maps with no [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_definition _ ramification point, branch point|ramification]] — since the map is a local homeomorphism everywhere. How can we deal with ramification?

##### _definition:_ monodromy (representation) of a holomorphism

Given a [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]] $\pi : X \to Y$ the monodromy of $\pi$ is the monodromy representation of $\pi_{\mid U} : U \to V$ where $U$ and $V$ are $X$ and $Y$ without [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_definition _ ramification point, branch point|ramification points and branch points]] respectively.

Note that a monodromy representation must be transitive in its image because we can lift something something %%do later%%

This isn't just a necessary condition, it's also sufficient!

##### _theorem:_

For a Riemann surface $X$, given a permutation representation $\rho : \pi(X) \to \mathfrak S_{d}$ such that its image is transitive. Then there exists a cover $f : U \to X$ of degree $d$ such that $\rho$ is the monodromy representation of the cover.

###### _proof sketch(y):_

Choose $U = U_{0} / H$ where $H$ is the subgroup of all $h \in \pi_{1}(X)$ such that $\rho(h)$ fixes $1$. It has [[Abstract algebra --- math-171/notes/Lagrange's theorem#_definition _ index, $ lvert G H rvert$|index]] $d$. Trust Alan that the rest of the details work out

Note that we could give two monodromy representations that are essentially the same by pre and post-composing with a permutation and its inverse. These give the same cover, but are also in the "same conjugacy class". We have a correspondence between conjugacy classes of monodromy representations and connected covers of $X$ of degree $d$.

By pullback atlas covers of Riemann surfaces are Riemann surfaces too.

Given a Riemann surface $X$, and a covering Riemann surface $U$, we want to classify all the holomorphic maps $U \to X$ of given degree $d$ and with branch points only in the give set $B$. We know what unramified maps to ${X \setminus B}$ look like — they are covers. By [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_theorem _ identity theorem|identity theorem]] and the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_corollary _ ramification points are discrete|discreteness of branch points]] we can classify finite degree maps by classifying conjugacy classes of monodromy representations  $\rho : \pi_{1}(X \setminus B) \to \mathfrak S_{d}$.

When $X$ is (very) nice and simple, the fundamental group $\pi_{1}(X \setminus B)$ is reasonable.

##### _example:_ finite degree maps to the Riemann sphere

Recall that [[Riemann surfaces and algebraic curves --- math-199DR/notes/Riemann surfaces#_example _ the Riemann sphere and the complex projective line|the Riemann surfaces]] (and equivalently $\mathbb{C} \mathbb{P}^1$) is a topological sphere.

### Galois theory

Given a holomorphism $\pi : X \to Y$, let $K$ be [[Riemann surfaces and algebraic curves --- math-199DR/notes/Functions on Riemann surfaces#Nice function fields|the function field]] of global meromorphic maps on $X$ — $K = \mathcal{M}_{X}(X)$. Let $k$ be the pullback of the meromorphic functions on $Y$ — $\pi^* \mathcal{M}_{V}( V)$. Then $K / k$ is field extension of degree $\deg \pi$ and the normal closure of $K / k$, say $L / k$ has Galois group $\operatorname{Gal}(L / k) \cong \rho(\pi_{1}(X))$ for the $\rho$ the monodromy representation of $\pi$. Essentially this is because the natural $z \mapsto \omega_{d}^n z$ that preserves $z^d$ looks like rotation.

The inverse Galois problem is whether, given a group $G$, we can find a field extension $K / k$ with normal closure $L / k$ and $\operatorname{Gal}( / k) = G$. Since the function fields over pullbacks of function fields have Galois group equal to the monodromy representation of the holomorphism, we have a new question!

Given a group $G$, is there a holomorphism $\pi : X \to Y$ (of compact, connected Riemann surfaces) with (image of) monodromy representation $G$? 

The answer is yes! In fact, even if we fix $Y$ (say as $\mathbb{C}_{\infty}$) the answer is yes.

##### _examples:_ solutions to the inverse Galois problem

For any cyclic group $\mathbb{Z} / d \mathbb{Z}$, the map $\mathbb{C}_{\infty} \to \mathbb{C}_{\infty}$ by $z \mapsto z^d$ has monodromy group $\mathbb{Z} / d \mathbb{Z}$.

For any dihedral group $D_{2d}$, the map $\mathbb{C}_{\infty} \to \mathbb{C}_{\infty}$ by
$$
z \mapsto \frac{4 z^d}{(z^d + 1)^{2}}
$$
has monodromy group $D_{2d}$.

For a generic polynomial $p$ of degree $d$, the map $p : \mathbb{C}_{\infty} \to \mathbb{C}_{\infty}$ has the largest possible monodromy group — $\mathfrak{S}_{d}$.