---
tags:
- diff-eq
- math-82/1
---

An important part of dealing with differential equations is learning to classify them. Having the vocabulary to describe the salient properties of an [[What are differential equations?#_definition _ ordinary differential equations|ordinary differential equation]] can be very useful to determine their behaviour, deeper properties, and whether analytic solution strategies apply.

### Order

##### _definition:_ order of a differential equation

The order of a differential equation is the order of the highest derivative of the dependent variable in the equation.

##### _example:_ the order of some differential equations

1) $y' y''' + x y^5 = 27$ is a third order differential equation (where $y$ is a function of $x$).
2) $y' y''' + x y^{(5)} = 27$ is a fifth order differential equation. Note the difference between $y^5$ ($y$ to the fifth power) and $y^{(5)}$ (the fifth derivative of $y$).
3) $\ddot{x} + \omega^2 x = 0$ is a second order differential equation (notice that $x$ can be the dependent variable too — $x$ is a function of $t$ here),

### Autonomous and non-autonomous

##### _definition:_ autonomous and non-autonomous differential equations

An autonomous differential equation is a differential equation that involves no functions of the independent variable, apart from the dependent variable and its derivatives.

A non-autonomous differential equation is a differential equation that is not autonomous.

##### _example:_ autonomous differential equation

$y'' = 2 y^2 y'$ is autonomous (note that we don't think of constants as "constant functions of the independent variable" because that would be silly).

##### _example:_ non-autonomous differential equation

$y'' = t^2 y'$ is non-autonomous.

### Linearity

##### _definition:_ linear differential equation

A differential equation is linear if it is an equality of linear combinations of the dependent variable and its derivatives (and constant functions) over the ring of functions of the independent variable.

##### _example:_ linear differential equation

$y' + \ln(x^2 \arcsin(x e^x)) y = 0$ is a linear differential equation despite how horrible and non-linear the coefficient of $y$ is.

##### _example:_ non-linear differential equation

$y'y = y''$ is a non-linear differential equation.

We can also talk about whether a linear differential equation is homogenous or not.

##### _definition:_ homogenous and non-homogenous linear differential equation

A homogenous differential linear differential equation involves linear combinations containing constant functions (not as coefficients).

A non-homogenous linear differential equation is a linear differential equation that is not homogenous.

##### _example:_ homogenous differential equations

$y' + y = 0$ and $y'' = xy$ are homogenous.

##### _example:_ non-homogenous differential equations

$y' + y = \sin x$ and $y''' - 6 = y$ are non-homogenous.