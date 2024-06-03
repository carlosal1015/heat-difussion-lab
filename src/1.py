#!/usr/bin/env python

"""
Consider the 1D heat equation defining how a temperature is distributed e.g.
over a one-dimensional rod.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def f(x, t, α=1, ylim=5):
    from scipy.special import erf

    return 0.5 * (
        erf((ylim - x) / (np.sqrt(α * t))) - erf((-ylim - x) / (np.sqrt(α * t)))
    )


def animate(t):
    print("Frame", t + 1)
    plt.clf()
    X = np.linspace(start=-50, stop=50, num=200)
    Y = f(X, t + 1e-10)
    plt.plot(X, Y, color="red")
    plt.ylim(0, 1)
    plt.title(f"Temperature at time = ${t:.2f}$ unit time")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$u\left(x, t\right)$")
    plt.grid(True)


anim = FuncAnimation(fig=plt.figure(), func=animate, frames=50, interval=1)


if __name__ == "__main__":
    anim.save(filename="Heat1D.gif", writer="ffmpeg", fps=60, dpi=300)
