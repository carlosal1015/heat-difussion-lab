#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class Wave1D:
    def __init__(self) -> None:
        self.X = np.linspace(start=-5, stop=5, num=1001)
        self.T = np.linspace(start=0, stop=3, num=7)
        varphi = lambda X: np.piecewise(
            x=X,
            condlist=[abs(X) <= 1, abs(X) >= 1],
            funclist=[lambda t: 2 - 2 * abs(t), 0],
        )
        self.u = lambda X, t: 0.5 * (varphi(X + t) + varphi(X - t))
        self.fig, self.ax = plt.subplots()
        self.yy = [self.u(t, self.X) for t in self.T]

    def make_plot(self):
        fig, axs = plt.subplots(
            nrows=self.T.size,
            ncols=1,
            clear=True,
            constrained_layout=True,
        )
        for ax, t in zip(axs, self.T):
            ax.plot(self.X, self.u(self.X, t), lw=1)

        plt.savefig("wave.png", dpi=300)
        plt.close()

    def update(self, t):
        self.ax.clear()
        self.ax.plot(self.X, self.yy[t])
        self.ax.set_xlim((self.X[0], self.X[-1]))
        self.ax.set_ylim((np.min(self.yy), np.max(self.yy)))
        self.ax.set_title(f"t = {self.T[t]:.2f}")
        self.ax.grid(True)

    def make_animation(self):
        anim = FuncAnimation(
            fig=self.fig, func=self.update, frames=self.T.size, interval=4000
        )
        anim.save(filename="wave1d.mp4", writer="ffmpeg", fps=60, dpi=300)


if __name__ == "__main__":
    Wave1D().make_plot()
    Wave1D().make_animation()
