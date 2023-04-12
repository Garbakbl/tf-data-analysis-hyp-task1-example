from scipy.stats import norm

chat_id = 356550601

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    z_alpha = norm.ppf(1 - 0.04/2)
    z = (p1 - p2) / (p * (1 - p) * (1/x_cnt + 1/y_cnt))**0.5
    return abs(z) > z_alpha
