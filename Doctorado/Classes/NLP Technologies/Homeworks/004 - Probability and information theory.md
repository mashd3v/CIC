# Probability and information theory

- **What is the purpose of probability theory?**
  Allos us to make uncertain statements and to reason in the presence of uncertanty.
- **What is the purpose of information theory?**
  Enables us to quantify the amount of uncertanty in a probability distribution.
- **Why the concept of probability is necessary?**
  Because many branches of computer science deal mostly with entities that are entirely deterministic and certain. Machine learning must always deal with uncertain quantities and sometimes stochastic (nondeterministci) quantities.
- **What are the two approaches to probability?**
  Frequentist probability and Bayesian probability.
- **What is a random variable?**
  Is a variable that can take on different values randomly.
- **What is a probability distribution?**
  Is a description of how likely a random variable or set of random variables is to take on each of its possible states.
- **What is joint, marginal, and conditional probability?**
  A probability distribution over discrete variables may be described using a probability mass function (PMF). We tipically denote PMF with a capital $P$. Often we associate each random variable with a different PMF and the reader must infer which PMF to be used on the identity of the random variable, rather than on the name of the function; $P(x)$ is usually not the same as $P(y)$.

  - PMF can act on many variables at the same time, Such a probability distribution over many variables is known as a **joint probability distribution**.
  - Sometimes we know the probability distribution over a set of variables and we want to know the probability distribution over just a subset og them. The probability distribution over a subset is known as the **marginal probability distribution**.
    $$P(X=x)=∑_{y}P(X=x,Y=y)$$
  - In many cases, we are interested in the probability of some event, given that some other event has happened. This is called a **conditional probability**. We denote the conditional probability that y$ = y$ given x$ = x$ as $P($y$= y|$x$ = x)$. This conditional probability can be computed with the formula:
  $$P(y=y|x=x)=\frac{P(y=y, x=x)}{P(x=x)}$$

- **What is independence and conditional independence of random variables?**
  **Independence of random variables.** Two random variables $X$ and $Y$ are considered independent if the occurrence (or non-occurrence) of an event associated with one variable does not affect the probability of occurrence of events associated with the other variable. Formally, $X$ and $Y$ are independent if and only if: $P(X=x∩Y=y)=P(X=x)⋅P(Y=y)$
  **Conditional independence** refers to the independence of two random variables given some information about a third variable. Specifically, $X$ and $Y$ are conditionally independent at $Z$ if, for all values of $z$ in the range of $Z$, X and Y are independent given $Z=z$. This is expressed as:$P(X=x∩Y=y∣Z=z)=P(X=x∣Z=z)⋅P(Y=y∣Z=z)$
- **What are the formulas for expectation, variance, standard deviation, covariance?**
  - **Expectation (or Expected Value)** The expectation, denoted as E(X) or μ, represents the mean value of a random variable. $E(X)=∑_{i}xi⋅P(X=x_{i})$. In the continuous case: $E(X)=∫_{-∞}^{∞}x⋅f(x)dx$.
  - **Variance.** Variance measures the dispersion of a random variable around its expectation. $Var(X)=E((X-E(X))^2)$
  - **Standard Deviation.** The standard deviation is simply the positive square root of the variance and is denoted as $σ$. $σ=Var(X)$
  - **Covariance.** Covariance measures the joint variance of two random variables.
    $Cov(X,Y)=E((X-E(X))(Y-E(Y))))$
  - **Correlation Coefficient** The correlation coefficient($ρ$) normalises the covariance by dividing by the product of the standard deviations of X and Y.$ρ=\frac{Cov(X,Y)}{σX⋅σY}$
    The correlation coefficient is in the range $[-1,1]$, where 1 indicates a perfect positive correlation, $-1$ indicates a perfect negative correlation, and $0$ indicates no linear correlation.
- **What is the covariance matrix of a vector x?**

- **What are common probability distributions?**

  - **Normal (Gaussian) Distribution.** Models many natural phenomena and is widely used due to the central limit theorem. It has a bell shape and is characterised by its mean(μ) and standard deviation(σ).
  - **Bernoulli distribution.** Models experiments with two possible outcomes (success or failure). It is a special case of the binomial distribution with n=1.
  - **Binomial distribution.** Models the number of successes in n independent trials, where each trial has two possible outcomes with the same probability of success(p).
  - **Poisson Distribution.** Models the number of events occurring in a fixed time interval or space, when events are rare and occur independently.
  - **Exponential Distribution.** Models the time between successive events in a Poisson process. It is a continuous distribution and is commonly used to model waiting times.
  - **Uniform Distribution.** All possible values have the same probability of occurring. The discrete uniform distribution assigns the same probability to each possible value, while the continuous uniform distribution assigns the same probability to all values in an interval.
  - **Chi-Square distribution.** Used in statistical inference and models the sum of squares of independent standard normal normal random variables.

- **What are the properties of logistic sigmoid and softplus functions?**

- **What does it mean that a function saturates?**

- **What is the Bayes’ rule?**

- **What is self-information of a random variable value?**

- **What is the entropy of a random variable?**

- **What is the Kulback-Leibler divergence?**

- **What is cross-entropy?**
