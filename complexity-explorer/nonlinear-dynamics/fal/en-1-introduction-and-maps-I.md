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

**Orbit / Trajectory** of a dynamical system**: **  
A sequence of values of the **state variables** of the system.

> ex.  
> The progression that iterates \($$x_{0}, x_{1}, x_{2}, ...$$\) in the logistic map
>
> > **state variables are also the names of functions in equations like the cos in**
> >
> > $$x_{n+1} = cos(x_{n})$$

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

What happens to the attractors in the dynamics of the logistic map as the parameter r changes:

**Periodic Orbit / Limit Cycle type of Attractor:                                                    
**When r&gt;= 3, we sometimes see two or more predominante states, which are the periods.

**Biforcations:                                                  
**There are changes in the amount of periods as we change the parameter **r**. The change happens in the topology of the attractor, it is a qualitative change. The fixed point does not move, it vanishes.

When we slowly raise the r value and the period doubles, we have a period doubling bifurcation sequence.

**Chaotic Attractor / Strange Attractors:                                                  
**Periods that seem to have a pattern but don't. Different inicial conditions show different state variable values on the periods.

## Maps II

### [2.1 Return Maps](https://www.complexityexplorer.org/courses/94-nonlinear-dynamics-mathematical-and-computational-approaches/segments/7986)

The _**first **_**return map**, **correlation plot**, or **cobweb diagram** is used to represent **scalar data** \(a single number, nor a vector\). Instead of ploting the _time domain plot_ $$(n, x_{n})$$ we plot $$(x_{n}, x_{n+1})$$ because it brings out the correlations between successive points. It is called the first return map because we use n+1 and not, for example, n+2 for the y axis.

This allows us to make grafical analysis of the function $$x_{n+1}=rx_{n}(1-x_{n}) $$

![](http://mathworld.wolfram.com/images/gifs/logistic.gif)

The function defines the upside-down parabola. The increase in **r** raises the curve steepness. The line $$x_{n+1}=x_{n}$$ defines all of the possible fixed point locations by definition, and where it crosses with the parabola define the limits of fixed point location for the given function.

#### Reading the **Logistic Map**

When entering an initial value to the function, we start at the x axis on said value and project it up towards the parabola to obtain the second iteration. This next value may be projected on the inclined line and then once more onto the parabola to continue the mapping of the tragectory in this fashion.

### [2.2 Constructing the bifurcation diagram](https://www.complexityexplorer.org/courses/94-nonlinear-dynamics-mathematical-and-computational-approaches/segments/7989)

The bifurcation plot $$(r, x_{n})$$ is useful to measure changes in periods in relation to r values. In this plot, the transiente is removed. We only are able to see periodic or fixed point behavior for each incremental r value. ![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Logistic_Map_Bifurcation_Diagram%2C_Matplotlib.svg/800px-Logistic_Map_Bifurcation_Diagram%2C_Matplotlib.svg.png)![](https://upload.wikimedia.org/wikipedia/commons/f/fb/Diagram_bifurkacji_anim_small.gif)

### [2.3 Exploring the bifurcation diagram](https://www.complexityexplorer.org/courses/94-nonlinear-dynamics-mathematical-and-computational-approaches/segments/7992)

Exploring the bifurcation plots above, we notice that there exists a fixed point from r value 0, all the way up to 3 where we find a bifurcation, later becomes a four cycle and continues doubling \(in a **period doubling cascade **sequence\) until it eventually becomes a chaotic regime for greater values, where the filled banded graphing appears. We can also find **veils \(unstable periodic orbits, UPOs\)**, places within the chaotic regime that is a bit darker, where the chaotic attractor is dense.

There exists r values in between chaotic regimes that show stability. \([Period 3 Implies Chaos](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.329.5038&rep=rep1&type=pdf), checkout later\).

The bifurcation map is a fractal object. Each piece seems to represent the same characteristics as the whole \(they are** self-similar**\). Formally, they present a non-integer Hausdorff dimension. This is true for many chaotic systems.

### [ 2.4 Feigenbaum and universality](https://www.complexityexplorer.org/courses/94-nonlinear-dynamics-mathematical-and-computational-approaches/segments/7995)

This part of the course talks about the universality of chaos. In the bifurcation map, the bifurcations aren't evenly space, they get smaller as r increases. The height and width of the forks descrease at a constant ratio. The ratio for $$Δ_{1}/Δ_{2}≈Δ_{2}/Δ_{3}  $$.

$$\lim_{n\to\infty}   Δ_{n}/Δ_{n+1} ≈ 4.66$$ is the **Feigenbaum number**.

![](/complexity-explorer/nonlinear-dynamics/fal/Screenshot_2.4_0-33.png)

Mitchell Feigenbaum is responsible for the proof of that ratio, thus the number earning his name. The further we increase n, the closer we get to the number. There is a similar result but with a different ratio for the heights.

This ratio holds true for **any** and** only 1-D maps with a quadratic maximum**. This means this is true for the sine map or any other map that looks like a parabola near its maximum. "_This means that orbiting moons, pendulums, and the human heart all act the same in the throwd of chaos"_. There is speculation that this may hold true for higher dimensions, the proofs don't extend to them.

_Steve Strogatz says, the Feigenbaum number is a new physical constant, as fundamental to 1-D maps, as π is to circles_.

#### The Smale's Horseshoe map

The Smale's Horseshoe is a 2-D map. It does not operate on the unit interval like the logistic map, but on the unit squared. It starts out at a square and streches maintaining area. It then curves onto itself, cutting out the bend. This makes point that were far away come close together and points that were close spread appart. This action is repeated. The stretching and folding that creates this is a paradigm in chaos, the cause of sensitive dependence on initial conditions.  
![](https://publicism.info/science/chaos/chaos.files/image008.jpg)A 3-D version of this is the kneading of bread dough. It is the most eficient means of mixing.

A map is discrete, not like a flow which is continuous. You can think of a flow being the act of shaping and reshaping dough with your hands, and a map being a picture taken for every time that is a ball.

### [2.5 Field trip: The standard map (with Jim Meiss)](https://www.complexityexplorer.org/courses/94-nonlinear-dynamics-mathematical-and-computational-approaches/segments/7998)

Conversation with Prof. Jim Meiss of the Department of Applied Mathmatics at the University of Colorado.
He is interested in the **standard map**. Imagine we have rocking pendulum that traces an arc **x**. If it is hit at random times by a hammer, the affects differ depending to how close it is to the hammer, being null when the ball is straight down.
The angular momentum of this pendulum is **y**. We can describe this dynamic system with a map. **k** is the hit.

$$ x' = x + y - ksin(x)$$
$$ y' = y - ksin(x) $$ 

We can see from y' that is the kick is 0, the angular momentum is constant. If the kick is non-zero we have complicated dynamics which sometimes is dynamic, regular or chaotic.
We have some intermixture of some orbits being chaotic and some orbits being regular, all for the same fixed fixed parameter value. There is not only one fixed attractor (strange or otherwise).
Different initial values for different k values have different behaviors. These behaviors are in resonance with the chaotic behavior near them.
For larger values of k, the system has more regions where initial values result in chaotic behavior, with small regions of inicial values that don't.
We do not know if there is a vlue for k in which everything is chaotic.
[Here](https://epubs.siam.org/doi/book/10.1137/1.9781611974645) is the link to his book "Mathematical Modeling and Computation Differential Dynamical Systems, Revised Edition".

A **Phase Space** or **State Space** is a very powerful representation of tragectories in a dynamical system, where the axis are the state variables. 
A **Separatrix** is a curve or surface in a phase space that separates two different regions.
Integrable means that a system is not chaotic, that the equations cannot be solved in closed form.
**Dissipation** is a more general word for *friction*. In systems that are **conservative** or **Hamiltonian**, energy is conserved, they are non-dissipitive systems.
Dissipation is a necessary condition for the existence of attractors, this isn't true for chaos.






