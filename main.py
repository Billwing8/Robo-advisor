import pandas_datareader.data as web
import pandas as pd
import pandas as pd
import numpy as np
import time

# 读取历史股票价格数据
stocks = pd.read_csv('stocks.csv',index_col=0)

# 计算历史股票价格的收益率
returns = stocks.pct_change()

# 根据收益率计算每只股票的风险和收益
risks = returns.std()
rewards = returns.mean()

# 用户输入投资金额和风险偏好
investment = float(input("请输入您的投资金额（元）："))
risk_preference = float(input("请输入您的风险偏好（0-1之间）："))

# 计算每只股票的风险权重
risk_weights = (risks / risks.sum()) * (1 - risk_preference)

# 计算每只股票的收益权重
reward_weights = (rewards / rewards.sum()) * risk_preference

# 计算每只股票的总权重
weights = risk_weights + reward_weights

# 计算每只股票应该购买的数量
quantities = (weights * investment) / stocks.iloc[-1]

# 输出建议的投资组合
print("您可以考虑以下投资组合：")
for stock, quantity in quantities.items():
    print(f"{stock}: {quantity:.2f}股")
time.sleep(50)