import pandas as pd
import numpy as np
import math
from scipy.stats import norm


chat_id = 1105842906

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
               
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
    p = (x_success + y_success) / (x_cnt + y_cnt)
    
    se = math.sqrt(p * (1 - p) * (1 / x_cnt + 1 / y_cnt))
    
    z_stat = (p1 - p2) / se
    
    p_value = 2 * norm.cdf(-abs(z_stat))
    
    return p_value < 0.05
