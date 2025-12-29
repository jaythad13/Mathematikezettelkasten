---
tags:
- math-82/8
- diff-eq
---

Often simple differential equations give ways to solve more complicated ones (in the end we try to reduce everything to a separable equation). One example of this is how [[Differential equations --- math-82/notes/Undetermined coefficients|the solution]] to a [[Differential equations --- math-82/notes/Classifying ordinary differential equations|second order, homogenous, linear]] differential equation, say
$$
y'' + p_{1}(x) y' + p_{2}(x) y = 0
$$
gives us the general solution for the non-homogenous case.
$$
y'' + p_{1}(x) y' + p_{2}(x) y = f(x).
$$

This method is called variation of parameters. 

The idea behind variation of parameters is to guess that if linear combinations over $\mathbb{R}$ of solutions to the homogenous case are still solutions to the homogenous case, then we can guess that the non-homogeneous equation is solved by using "varying coefficients" from $C^r(\mathbb{R})$ rather than constants from $\mathbb{R}$. That is, assume $y = u_{1}(x) y_{1} + u_{2}(x) y_{2}$. Using an additional assumption about the linear combination, we solve this as a linear system.

##### _theorem:_ variation of parameters

If $y_{1}$ and $y_2$ are linearly independent solutions to the differential equation
$$
y'' + p_{1}(x) y' + p_{2}(x) y = 0,
$$
then the general solution to the differential equation
$$
y'' + p_{1}(x)y' + p_{2}(x) y = f(x)
$$
is
$$
y = -y_{1} \int \frac{y_{2} f(x)}{W(x)} \, dx + y_{2} \int \frac{y_{1} f(x)}{W(x)} \, dx
$$
where $W(x) = \det \begin{pmatrix} y_{1} & y_{2} \\ y_{1}' & y_{2}' \end{pmatrix}$ is the **Wronskian** of $y_{1}$ and $y_{2}$.

###### _proof sketch:_

Plug $y$ back in — it works!

---

##### _example:_ solving $\ddot{y} + 4y = 4 \sin(t)$ by variation of parameters

The homogenous equation $\ddot{y} + 4y = 0$ obviously has linearly independent solutions $\cos(2t)$ and $\sin(2t)$. Thus, their Wronskian is
$$
\begin{split}
W(x) & = \det\begin{pmatrix}
\cos(2t) & \sin(2t) \\
- 2 \sin(2t) & 2 \cos(2t)
\end{pmatrix} \\
 & = 2 (\cos^2(t) + \sin ^{2}(t)) \\
 & = 2.
\end{split}
$$

Then, by variation of parameters,
$$
\begin{split}
y & = -\cos(2t) \int \frac{{\sin(2t) 4 \sin(t)}}{2} \, dt + \sin(2t) \int \frac{\cos(2t) 4 \sin(t)}{2} \, dt \\
 & = -4 \cos(2t) \int \sin ^{2}(t) \cos(t) \, dt +  2 \sin(2t) \int (\cos ^{2}(t) - \sin ^{2}(t)) \sin(t) \, dt \\
 & = -\frac{4}{3} \cos(2t) (\sin ^{3}(t) + c_{1}) + 2 \sin(2t)\left( \cos(t) - \frac{\cos ^{3}(t)}{3} + c_{2} \right) \\
 & = -\frac{4}{3} \left( \cos(2t) \sin ^{3}(t) + \sin(2t) \cos^3(t) - \frac{3}{2} \sin(2t) \cos(t)  \right) + c_{1} \cos(2t) + c_{2} \sin(2t) \\
 & = -\frac{4}{3}(\cos ^{2}(t)\sin ^{3}(t) - \sin^5(t) + 2 \sin(t) \cos^4(t) - 3 \sin(t) \cos ^{2}(t))  + c_{1} \cos(2t) + c_{2} \sin(2t) \\
 & = -\frac{4}{3} \sin(t)(\cos^2(t) \sin ^{2}(t) - \sin^4(t) + 2 \cos^4(t) - 3 \cos^2(t)(\cos ^{2}(t) + \sin ^{2}(t))) + c_{1} \cos(2t) + c_{2} \sin(2t) \\
 & = \frac{4}{3} \sin(t) (\cos^4(t) + 2 \cos^2(t) \sin ^{2}(t) + \sin^4(t) ) + c_{1} \cos(2t) + c_{2} \sin(2t) \\
 & = \frac{4}{3} \sin(t) (\cos^2(t) + \sin^2(t))^2 + c_{1} \cos(2t) + c_{2} \sin(2t) \\
 & = \frac{4}{3} \sin(t) + c_{1} \cos(2t) + c_{2} \sin(2t).
\end{split}
$$
which clearly satisfies the differential equation. We can see this by choosing $c_{1} = c_{2} = 0$ and then calculating that
$$
\begin{split}
y'' + 4y  & = - \frac{4}{3} \sin(t) + \frac{16}{3} \sin(t) \\
 & = \frac{12}{3} \sin(t) \\
 & = 4 \sin(t).
\end{split}
$$
---