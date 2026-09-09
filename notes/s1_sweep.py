#!/usr/bin/env python3
"""Protocol S1, open-loop: generic Psi-space (circle), not a helicoid manifold."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path("/home/kinaar/Projects/arena/fig/s1-sweep.png")

N = 256
L = 2.0 * np.pi
DX = L / N
X = np.linspace(0.0, L, N, endpoint=False)
V = 1.0
T = 2.0
DT = 0.002
STEPS = int(round(T / DT))
K = np.fft.fftfreq(N, d=DX) * 2.0 * np.pi
UNIF = np.ones(N) / L
EPS = 1e-12


def kl(p, q):
    p = np.clip(p, 1e-18, None)
    q = np.clip(q, 1e-18, None)
    return float(np.sum(p * np.log(p / q) * DX))


def l1(u):
    return float(np.sum(np.abs(u) * DX))


def qo(p):
    ph = np.fft.fft(p)
    return np.fft.ifft(-1j * K * V * ph).real


def qc(p):
    return UNIF - p


def evolve(p, sigma):
    p = p.copy()
    for _ in range(STEPS):
        p = p + DT * (qo(p) + sigma * qc(p))
        p = np.clip(p, 0.0, None)
        p /= p.sum() * DX
    return p


def main():
    p0 = np.exp(-((X - np.pi) ** 2) / (2 * 0.35**2))
    p0 /= p0.sum() * DX
    sigmas = np.linspace(0.0, 2.5, 26)
    p_life = evolve(p0, 0.0)

    r_vals = []
    a_vals = []
    d_vals = []
    for sigma in sigmas:
        p = evolve(p0, sigma)
        r = l1(sigma * qc(p)) / (l1(qo(p)) + EPS)
        r_vals.append(r)
        a_vals.append(kl(p, UNIF))
        d_vals.append(kl(p, p_life))

    r_vals = np.array(r_vals)
    a_vals = np.array(a_vals)
    d_vals = np.array(d_vals)
    above = np.where(r_vals >= 1.0)[0]
    sigma_star = float(sigmas[above[0]]) if len(above) else None

    fig, ax = plt.subplots(figsize=(7.2, 4.4), dpi=160)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(sigmas, r_vals, color="#6b5428", lw=2.0, label=r"$r(\sigma,T)$")
    ax.plot(sigmas, a_vals, color="#2c261c", lw=2.0, ls="--", label=r"$A[p]=\mathrm{KL}(p\|\pi_{\mathrm{O}})$")
    ax.axhline(1.0, color="#8a7a55", lw=0.8, ls=":")
    if sigma_star is not None:
        ax.axvline(sigma_star, color="#c45c4a", lw=1.4)
        ax.scatter([sigma_star], [1.0], color="#c45c4a", zorder=5)
        ax.annotate(
            rf"$\sigma_*={sigma_star:.2f}$",
            xy=(sigma_star, 1.0),
            xytext=(sigma_star + 0.18, 1.35),
            color="#c45c4a",
            fontsize=11,
        )
    ax.set_xlabel(r"$\sigma$  (open-loop gate; $C$ unused)")
    ax.set_ylabel("report at horizon $T$")
    ax.set_xlim(sigmas[0], sigmas[-1])
    ax.set_ylim(bottom=0)
    ax.legend(frameon=False, loc="upper right")
    ax.set_title(r"Protocol S1 on a circle (generic $\Psi$-space)")
    fig.tight_layout()
    fig.savefig(OUT, dpi=160)
    plt.close(fig)
    print("wrote", OUT)
    print("sigma_star", sigma_star)
    print("r[0], r[-1]", r_vals[0], r_vals[-1])
    print("A[0], A[-1]", a_vals[0], a_vals[-1])
    print("D[-1]", d_vals[-1])


if __name__ == "__main__":
    main()
