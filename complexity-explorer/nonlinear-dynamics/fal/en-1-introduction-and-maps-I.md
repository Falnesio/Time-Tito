# Anotações para Nonlinear Dynamics: Mathematical and Computational Approaches

[Sumário](README.md)

## 1 Introduction and Maps I

### [1.1 Introduction to nonlinear dynamics](https://www.complexityexplorer.org/courses/94-nonlinear-dynamics-mathematical-and-computational-approaches/segments/7970)

**Deterministic systems** are sensitive to inicial conditions, they are not random, cause and effect are linked, the present state affects future states.  
**Dynamic systems** evolve with time.  
**Nonlinear systems** have importante variables with nonlinear relationships.  
**Chaotic systems** are _nonlinear_ and _dynamic_.  
Complex behavior arises from simple deterministic nonlinear systems.

> Systems:  
> &gt; Dynamic \[ Nonlinear \[ \[ Complex \], \[ Chaotic \] \] \]

Our basic study of behavior in nature is based on the pressumption of linear behavior, while the vast majority of natural behaviors that evolve in time are nonlinear. A large ammount of natural systems are chaotic and may not be studied utilizing only pen and paper, we need the help of computers with experimental mathmatics.

Loreenz in the 1963 paper Deterministic Nonperiodic Flow, was the first person to study the patterns of chaos and the sensitivity of the evolution of those systems within the context of those patterns.  
Li and Yorke in the paper Period Three Implies Chaos, were the first to use the word chaos to describe this behavior.

### 

### [1.2 Maps and difference equations](https://www.complexityexplorer.org/courses/94-nonlinear-dynamics-mathematical-and-computational-approaches/segments/7971)

First we will be **studying maps** \(systems that operate in_ discrete time_\), and then **flows** \(_continuous_ time functions\). **Discrete time** can be understood as time being counted in _integers_ \(each time being a tick and each tick associated to a map or state\), and **continuous** time can be understood as time being counted using _real numbers_.

Discrete time is measured with **difference equations:** $$x_{n+1}=f(x_{n})$$  
[Joshua's Logistic tools](http://tuvalu.santafe.edu/~joshua/?section=3), [Same tools on course site](https://www.complexityexplorer.org/courses/94-nonlinear-dynamics-mathematical-and-computational-approaches/segments/7985)

> examples:  
> **cossine map:** $$x_{n+1}=cos(x_{n})$$  
> applying x = 48º and iterating 3 times we would reach a value close to .9998477 and not change. When this happens its called a** "Fixed Point" **or **asymptote **on the map.
>
> **logistic map:** $$x_{n+1}=R_{x_i}(1-x_{n})$$  
> simple population model that maps the unit interval to itself  
> x = state, 0 &lt; x &lt;1  
> n = time, $$\mathbb{N}$$  
> R = paramater, $$\mathbb{N}| R < 4$$, for R &gt; 4, the map blows up.
>
> for $$x_{0}=0.2$$ and R = 2:
>
> | $$x_{1}$$ | $$R*x_{0}(1-x_{0})$$ |
> | :--- | :--- |
> |  | 2\(0.2\)\(1 - 0.2\) |
> |  | 0.32 |
> | $$x_{2}$$ | 2\(0.32\)\(1 - 0.32\) |
> |  | 0.44 |
> | $$x_{3}$$ | 0.49 |
> | $$x_{4}$$ | 0.50 |
> | $$x_{5}$$ | 0.50                **-&gt;**  **Fixed Point** |
>
> The parameter changes fixed point, inicial conditions don't.

[Homework](/complexity-explorer/nonlinear-dynamics/fal/en-homework-1-2.md), [Worksheet](/complexity-explorer/nonlinear-dynamics/fal/en-worksheet-1-7.md)

Continuous time is measured in **differential equations:**

#### 

#### [1.3 Transients and attractor](https://www.complexityexplorer.org/courses/94-nonlinear-dynamics-mathematical-and-computational-approaches/segments/7975)

**Orbit / Tragectory** of a dynamical system**: **  
A sequence of values of the **state variables** of the system.

> ex.  
> The progression that iterates \($$x_{0}, x_{1}, x_{2}, ...$$\) in the logistic map

$$x_{0}$$ is called the initial position of the state variable\(s\).  
It can reach an asymptote called a fixed point after passing through other states which are called the **transientes**.

The fixed point is a point which does not move with the dynamics of the system: $$f(x^*) = x^*$$.

**Attractor / Attracting Fixed Point: **  
A fixed point to which the logistic map orbit converges when system is perturbed and iterations tend towards infinity.  
Different initial condition still lead here.

1. **Basin of Attraction:** A good analogy is thinking of the oceans as rain water basin attractors and land as the transiente states and the rivers are attractors.
2. The more distante the initial conditions is to the fixed point, the bigger will be the transiente states.

**Unstable Fixed Point:**  
A point which may remain stable if unperturbed. Initial conditions at the point make this point remain fixed.

#### [1.4 Parameters and bifurcations](https://www.complexityexplorer.org/courses/94-nonlinear-dynamics-mathematical-and-computational-approaches/segments/7978)

What happens to the attractors in the dynamics of the logistic map as the parameter r changes.

**Periodic Orbit / Limit Cycle type of Attractor:    
**When r&gt;= 3, we sometimes see two or more predominante states, which are the periods.

**Biforcations:  
**The changes in the amount of periods as we change the parameter **r**. Thereis a change in the topology of the attractor it is a qualitative change. The fix point does not move, it vanishes.

**Chaotic Attractor / Strange Attractors:  
**Periods that seam to have a pattern but don't. Different inicial conditions show different state variable values on the periods.











