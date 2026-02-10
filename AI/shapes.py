import numpy as np

# 뉴런 출력
def main():
    x = np.array([1.0, 2.0, 3.0])
    W = np.array([[1.0, 0.0, -1.0],
                  [0.5, 2.0,  0.0],
                  [0.2, 3.0, 5.0]])
    b = np.array([0.1, -0.2, 0.2])

    print("x.shape:", x.shape)  # (3,)
    print("W.shape:", W.shape)  # (2,3)
    print("b.shape:", b.shape)  # (2,)

# @는 행렬 곱
    y = W @ x + b
    print("y:", y)
    print("y.shape:", y.shape)  # (2,)

    z = W @ x
    print("z:", z)
    print("z.shape:", z.shape)

# 원소별 곱과 행렬 곱의 차이
    x = np.array([1, 2, 3])
    w = np.array([4, 5, 6])
    print(w * x)  # [4,10,18] (원소별)
    print(w @ x)  # 32 (내적)


if __name__ == "__main__":
    main()
