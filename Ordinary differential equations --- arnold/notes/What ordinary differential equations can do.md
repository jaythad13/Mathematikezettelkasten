---
tags:
- self-study
- diff-eq
---

Ordinary differential equations are a mathematical tool to study particular types of processes. Specifically, ordinary differential equations allow to study some sort of _evolution_ of a system as long as that evolution is deterministic, finite-dimensional, and differentiable, using mathematical objects like phase spaces and phase flows.

### Some unrigorous definitions

Because we're studying exactly those processes, we need to have at least an intuitive idea of what it means for a process to be deterministic, finite-dimensional, and differentiable. These definitions have to be sort of hand-wavy because really, we _hard-code_ in determinism, finite-dimensionality, et c. into the well-defined mathematical objects we study, whereas here, we are defining these things as properties of less well-defined things like processes.

##### _definition:_ deterministic processes

A process is deterministic if its entire future course and its entire past are uniquely determined by its state at any "present" point in time.

##### _definition:_ phase space

The set of all possible states of a process is called its phase space.

##### _example:_ deterministic processes and their phase spaces

Classical mechanical models are a good example of deterministic processes. In any classical mechanical system (with no external force acting on it), we can predict the future motion of all its particles just using conservation of momentum and conservation of energy, and we can "wind the clock back" and do the same thing for the past, as long as we have the position and velocity (or more typically, momentum) of each particle. Thus, its phase space is just the set of all possible positions and momentums for each particle — perhaps $(\bb{R}^n \times \bb{R}^n)^m$ for $m$ particles in $n$-dimensional space.

##### _non-examples:_ deterministic processes

Both of the other common physics fields — heat propagation and quantum mechanics are non-deterministic. Specifically, heat propagation is semi-deterministic since its future can be predicted from the present state, but its past cannot, and quantum mechanics is outright non-deterministic.

##### _definition:_ finite-dimensional processes

A process is finite-dimensional if its phase space is finite dimensional — if its phase space requires finitely many parameters.

##### _example:_ finite-dimensional processes

Classical mechanical models are also finite-dimensional. As we already said, we can encode a system of $m$ particles in our typical space as $(\bb{R}^3 \times \bb{R}^3)^n$ which is $6n$-dimensional.

##### _non-examples:_ finite-dimensional processes

Other physical processes can be infinite-dimensional — fluid motion, wave propagation.

##### _definition:_ differentiable processes

A process is differentiable if its phase space has the structure of a differentiable manifold (whatever that means), ans its change of state with time is described by differentiable functions.

Roughly, this means that the that things can change smoothly, and they do change smoothly.

##### _example:_ differentiable processes

Again, classical mechanics, for obvious reasons.

##### _non-example:_ differentiable processes

Shock theory is, again for obvious reasons, not governed by differentiable processes

### Some things that ordinary differential equations do govern

We've given lots of examples of things that don't meet the criteria to be modelled effectively by ordinary differential equations. There are still some processes that are well-governed.

##### _examples:_ deterministic, finite-dimensional, differentiable processes

1) Classical mechanics, as we've already shown
2) Radioactive decay — a one parameter process (the amount of material)
3) Bacterial reproduction — also a one parameter process
