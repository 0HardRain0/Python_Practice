# 내적(dot) = 가중합(scope)

import numpy as np
from sympy.benchmarks.bench_meijerint import bpos


def sigmoid(z: float) -> float:
    return 1.0 / (1.0 + np.exp(-z))

def main():
    x = np.array([1.0, 2.0, 3.0])

    weights = {
        "w_a (강조/감쇠 섞기)": np.array([1.0, 0.0, -1.0]),
        "w_b (고르게 보기)":   np.array([0.2, 0.2, 0.2]),
        "w_c (전부 크게 보기)": np.array([2.0, 2.0, 2.0]),
        "w_d (2번째만 보기)":   np.array([0.0, 1.0, 0.0]),
    }

    print("x =", x, "shape =", x.shape);
    print("-" * 50)

    for name, w in weights.items():
        z = float(w @ x)
        print(f"{name}: w={w} -> w@x = {z:7.3f}  sigmoid({z}) = {sigmoid(z):.3f}")


    print("-" * 50)
    w = np.array([1.0, 0.0, -1.0])
    b = 2.0
    z1 = float(w @ x)
    z2 = z1 + b
    print(f"bias 효과: w@x={z1:.3f}  (w@x + b)={z2:.3f} sigmoid -> {sigmoid(z1):.3f} vs {sigmoid(z2):.3f}")

if __name__ == "__main__":
    main()