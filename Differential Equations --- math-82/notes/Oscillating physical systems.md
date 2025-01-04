---
tags:
- diff-eq
- math-82/6
- math-82/7
---

Second-order differential equations come up in the context of oscillating systems — there are very many of these.

##### _example:_ mass-spring systems

Suppose a mass is suspended vertically, and we choose coordinates so that $y = 0$ when the mass-spring system is in equilibrium. Then, assuming Hooke's law, an initial displacement at time $t = 0$, and a damping force proportional to the speed at which the mass moves, we have the differential equation
$$
m \ddot{y} = - k y - c \dot{y}.
$$

##### _example:_ RLC circuits

Imagine a circuit with a resistor, inductor, and capacitor connected in series to a voltage source.

```tikz
\usepackage{circuitikz}
\usepackage{amsfonts}
\begin{document}
	\begin{circuitikz}[american, voltage shift = 0.5]
	\draw (0,0)
to[vsource, v_=$\mathcal{E}(t)$] (6, 0)
to (6,2)
to[C=$C$] (4,2)
to[L=$L$] (2,2)
to[R=$R$] (0,2)-- (0,0);
	\end{circuitikz}
\end{document}
```

Using Kirchoff's voltage law, we know that the current passing through each of the components (and therefore, the charge on them at each point in time) is the same. Therefore, we can add the resultant voltage according to the formula for each component to get the differential equation
$$
\mathcal{E}(t) = \dot{q} R + \ddot{q} L + \frac{q}{C}.
$$

Note that both examples are basically the same thing — a linear combination over $\mathbb{R}$ (it's important that it isn't a linear combination over $\mathcal{C}^d(\mathbb{R})$) of the dependent variable and its first and second derivatives is equal to a function of the independent variable. They are [[Differential Equations --- math-82/notes/Classifying ordinary differential equations#Order|second order]], [[Differential Equations --- math-82/notes/Classifying ordinary differential equations#Linearity|linear]] differential equations with constant coefficients. The first case is just also [[Differential Equations --- math-82/notes/Classifying ordinary differential equations#_definition _ homogenous and non-homogenous linear differential equation|homogenous]]. It turns out that [[Differential Equations --- math-82/notes/Second order linear homogenous constant-coefficient differential equations|we can solve the homogenous case]] pretty easily!

### Damping

[[Differential Equations --- math-82/notes/Second order linear homogenous constant-coefficient differential equations#_proposition _ the solutions of $ay'' + by' + c = 0$|We've shown]] the following result — 

Let $az^2 + bz + c$ be the characteristic polynomial of $ay'' + by' + c = 0$. Then the characteristic polynomial has either

- two distinct real roots $\lambda_{1}, \lambda_{2}$, in which case any solution of the differential equation must satisfy $y(x) = c_{1} e^{ \lambda_{1} x } + c_{2} e^{ \lambda_{2} x }$ for constants $c_{1}, c_{2} \in \mathbb{R}$,
- two distinct (non-real) complex roots $\lambda_{1}, \lambda_{2}$. in which case any solution of the differential equation must satisfy $y(x) = e^{ \sigma x }(c_{1} \cos(\omega x) + c_{2} \sin(\omega x))$ for constants $c_{1}, c_{2} \in \mathbb{R}$, where $\lambda_{1} = \sigma + \omega i$,
or
- one real root $\lambda$, in which case any solution of the differential equation must satisfy $y(x) = c_{1}e^{ \lambda x } + c_{2} x e^{ \lambda x }$ for constants $c_{1}, c_{2} \in \mathbb{R}$.

Note how in both of our physical examples, the $y'$ term corresponds to a damping term. For example, if we have $c = 0$ for a mass on a spring, then $my'' + ky = 0$. Thus, $\pm i \sqrt{ k/m }$ are the roots of the characteristic polynomial, and the solutions of the differential equation are linear combinations of $\sin \omega t$ and $\cos \omega t$ for $\omega = \sqrt{ k/m }$. That is, $c = 0$, corresponds to undamped waves.

In fact, in general, when the characteristic polynomial has complex roots, the behaviour of the solution is underdamped — it oscillates around the initial value. When there's only one real root $\lambda$, the solution is critically damped — it goes straight to the initial value (it can't become less because of the exponentials). When there are two real roots, the solution is overdamped and thus, goes to zero slowly.