from statsmodels.stats.proportion import proportions_ztest

chat_id = 356550601

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.04
    _, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='two-sided')
    return p_value < alpha
