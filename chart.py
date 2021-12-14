import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

pct_fee = 0.1/100
start_balance = 1_000



df = pd.read_csv('2019-May.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

df = df.loc[::5,['Close','Timestamp']]

df.fillna(method='ffill', inplace=True)
df['sma_long'] = df['Close'].rolling(100).mean()
df['sma_longl'] = df['sma_long'].shift(1)
df['sma_short'] = df['Close'].rolling(20).mean()
df['sma_shortl'] = df['sma_short'].shift(1)


df.dropna(inplace=True)
# df.reset_index(inplace=True, drop=True)


buy_m = (df['sma_longl'] > df['sma_shortl']) & (df['sma_long'] <= df['sma_short'])
sell_m = (df['sma_shortl'] > df['sma_longl']) & (df['sma_short'] <= df['sma_long'])


sell_df = df.loc[sell_m,['Timestamp','Close']]
buy_df = df.loc[buy_m,['Timestamp','Close']]

if sell_df.index[0] < buy_df.index[0]:
    sell_df.drop(sell_df.index[0], inplace=True)

if buy_df.index[-1] > sell_df.index[-1]:
    sell_df = sell_df.append(df.iloc[-1,:2],ignore_index=True)

sell_df.reset_index(inplace=True, drop=True)
buy_df.reset_index(inplace=True, drop=True)



trades_df = pd.DataFrame()

trades_df['Timestamp_start'] = buy_df['Timestamp']
trades_df['Timestamp_stop'] = sell_df['Timestamp']
trades_df['Duration'] = trades_df['Timestamp_stop'] - trades_df['Timestamp_start']
trades_df['ROI'] = ((sell_df['Close']/buy_df['Close'])*(1-pct_fee)**2)-1
trades_df['%ROI'] = trades_df['ROI']*100

balance = pd.Series([start_balance]).append(trades_df['ROI']+1, ignore_index=True)
balance = balance.cumprod()[1:].reset_index(drop=True)
trades_df['end_balance'] = balance.values


wins = trades_df[trades_df['%ROI']>0].shape[0]
losses = trades_df.shape[0] - wins
end_balance = trades_df['end_balance'].iloc[-1]

print("Trades Executed", trades_df.shape[0])
print(f"Wins:", wins, "\nLosses:", losses)
print("Start Balance", start_balance, "\nEnd Balance", end_balance)
print("Total Profit", end_balance-start_balance)
print("%ROI Info:")
print("Minimum", trades_df['%ROI'].min())
print("Maximum", trades_df['%ROI'].max())
print("Mean", trades_df['%ROI'].mean())
print("Median", trades_df['%ROI'].median())

df.plot(x='Timestamp',y=['Close','sma_short','sma_long'])
trades_df.plot(x='Timestamp_stop', y='end_balance')
trades_df.plot(x='Timestamp_stop', y=['%ROI'], kind='bar')
plt.show()
