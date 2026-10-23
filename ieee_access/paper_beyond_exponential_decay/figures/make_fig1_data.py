"""Generate the data table for Fig. 1 (decay regimes) of Beyond Exponential Decay.

Pure-Python (no numpy) so it runs on any interpreter. Writes fig1_data.dat with
columns: n, uniform, log_k, sqrt_k, sat_k.

Illustrative parameters (stated in the figure caption):
  uniform model     P = (1 - e)^n,                 e = 0.01
  two-rate model    P = (1 - e_key)^k * prod_{i=1}^{n-k} (1 - e_non(i))
                    e_key = 0.05, e_non(i) = 0.02 * i^(-1.5)  (summable)
  k(n):  log:  ceil(3 ln n)      sqrt: ceil(sqrt n)      sat: min(ceil(sqrt n), 20)
"""
import math
import os

E_UNIFORM = 0.01
E_KEY = 0.05
E_NON_C = 0.02
E_NON_P = 1.5
K_MAX = 20
N_MAX = 100_000


def main() -> None:
    # cumulative log of the non-key factor: L[m] = sum_{i=1}^{m} ln(1 - e_non(i))
    log_nonkey = [0.0] * (N_MAX + 1)
    acc = 0.0
    for i in range(1, N_MAX + 1):
        acc += math.log(1.0 - E_NON_C * i ** (-E_NON_P))
        log_nonkey[i] = acc

    def two_rate(n: int, k: int) -> float:
        k = min(k, n)
        return math.exp(k * math.log(1.0 - E_KEY) + log_nonkey[n - k])

    # log-spaced grid of n from 10 to N_MAX (integers, deduplicated)
    grid = sorted({int(round(10 ** (1 + 4 * t / 200))) for t in range(201)})
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fig1_data.dat")
    with open(out_path, "w", encoding="ascii") as f:
        f.write("n uniform log_k sqrt_k sat_k\n")
        for n in grid:
            uniform = (1.0 - E_UNIFORM) ** n
            k_log = math.ceil(3 * math.log(n))
            k_sqrt = math.ceil(math.sqrt(n))
            k_sat = min(k_sqrt, K_MAX)
            f.write(
                f"{n} {uniform:.6e} {two_rate(n, k_log):.6e} "
                f"{two_rate(n, k_sqrt):.6e} {two_rate(n, k_sat):.6e}\n"
            )
    print(f"wrote {out_path} ({len(grid)} rows)")
    # sanity values at a few n
    for n in (100, 1000, 10000, 100000):
        print(n, f"{(1-E_UNIFORM)**n:.3g}", f"{two_rate(n, math.ceil(3*math.log(n))):.3f}",
              f"{two_rate(n, math.ceil(math.sqrt(n))):.3f}", f"{two_rate(n, min(math.ceil(math.sqrt(n)), K_MAX)):.3f}")


if __name__ == "__main__":
    main()
