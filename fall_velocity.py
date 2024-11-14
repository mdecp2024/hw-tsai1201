# 設定重力加速度 (m/s²)
g = 9.8

# 定義計算速度的函數
def calculate_velocity(t):
    return g * t

# 計算不同時間的速度
time_values = [1, 2, 3, 4, 5]  # 計算1到5秒內的速度

# 輸出每秒的速度
for t in time_values:
    velocity = calculate_velocity(t)
    print(f"Time: {t}s, Velocity: {velocity} m/s")
