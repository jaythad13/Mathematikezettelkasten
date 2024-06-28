---
tags:
- math-82/3
- diff-eq
---

Even when we don't have a nice differential equation that we can solve analytically (because it isn't of one of the nice types or because something we have to integrate can't be integrated analytically), we can understand what its properties are with slope fields. These just involve drawing short segments of slope equal to the derivative of the dependent variable at every point where it is defined.

##### _example:_ the slope field of $y' = xy$

We can sample just a few points and determine the behaviour of the graph.

| $x/y$ | $-2$ | $-1$ | $0$ | $1$  | $2$  |
| ----- | ---- | ---- | --- | ---- | ---- |
| $-2$  | $4$  | $2$  | $0$ | $-2$ | $-4$ |
| $-1$  | $2$  | $1$  | $0$ | $-1$ | $-2$ |
| $0$   | $0$  | $0$  | $0$ | $0$  | $0$  |
| $1$   | $-2$ | $-1$ | $0$ | $1$  | $2$  |
| $2$   | $-4$ | $-2$ | $0$ | $2$  | $4$  |
This table of $y'$ at various points $(x, y)$ determines the slope field below.

![[S0_slopeFieldExample.jpeg]]
The orange lines show the slope at various points $(x, y)$ and the green curves show different possible solutions of the differential equation. Since the differential equation is solvable, we can see that the green curves correspond to different $y$-intercepts $y_{0}$ for the curve $y_{0} e^{x^2}$.