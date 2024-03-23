# Gaussian Distribution Function

This Python script demonstrates the Gaussian distribution function, also known as the normal distribution. The Gaussian distribution is a continuous probability distribution that is symmetric about its mean, with a characteristic bell-shaped curve. It is widely used in various fields due to its mathematical tractability and applicability to natural phenomena.

## Table of Contents

- [Introduction](#introduction)
- [Gaussian Distribution](#gaussian-distribution)
  - [Standard Normal Cumulative Distribution Function (phi)](#standard-normal-cumulative-distribution-function-phi)
  - [Standard Normal Probability Density Function (pdf)](#standard-normal-probability-density-function-pdf)
- [Script Usage](#script-usage)
- [Dependencies](#dependencies)

## Introduction

The Gaussian distribution is defined by two parameters: the mean ($\mu$) and the standard deviation ($\sigma$). These parameters determine the center and spread of the distribution, respectively. The probability density function (PDF) of the Gaussian distribution describes the likelihood of observing a value $x$ given the distribution's parameters.

## Gaussian Distribution

### Standard Normal Cumulative Distribution Function (phi)

The standard normal cumulative distribution function $\phi(x)$ represents the probability that a standard normal random variable is less than or equal to $x$. It is defined as:

$$
\phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{t^2}{2}} dt
$$

Where:
- $x$ is the value at which to evaluate the cumulative distribution function.
- $e$ is the base of the natural logarithm.

### Standard Normal Probability Density Function (pdf)

The standard normal probability density function $f(x)$ describes the probability density of observing a value $x$ from a standard normal distribution. It is defined as:

$$
f(x|\mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

Where:
- $x$ is the value at which to evaluate the probability density function.
- $\mu$ is the mean of the distribution.
- $\sigma$ is the standard deviation of the distribution.

## Script Usage

To run the script, execute it from the command line and provide the number of points to use for drawing the probability density function:

```
python script_name.py <number_of_points>
```

- `number_of_points`: Number of points to use for drawing the probability density function.

The script will display the standard normal probability density function using the specified number of points.

## Dependencies

This script requires the following dependencies:
- `math`: Standard Python math library for mathematical operations.
- `stddraw`: External library for simple drawing operations.
- `sys`: Standard Python library for system-specific parameters and functions.