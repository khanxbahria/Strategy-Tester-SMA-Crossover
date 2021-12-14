# Strategy Tester
A python script that tests a common trading strategy utilizing Simple Moving Averages (SMA)  and evaluates the efficiency simulating possible behaviours on a given dataset of a stock/currency.

## SMA Crossover Strategy
A common trading strategy utilizing SMAs is to trade based on the position of a shorter-term SMA in relation to a longer-term SMA. For example, traders are bullish when the 20 SMA crosses above the 100 SMA and remains above the 100 SMA, and only turn bearish if the 20 SMA falls below the 100 SMA.  
[Simple Moving Average](https://tradingsim.com/blog/simple-moving-average/)  
The bot enters the trade (using all the available balance) when 20 SMA line crosses the 100 SMA line from below and exits when they cross again.

## Demo
```shell
$ python3 chart.py 
Trades Executed 62
Wins: 23 
Losses: 39
Start Balance 1000 
End Balance 1329.4938854299999
Total Profit 329.49388542999986
%ROI Info:
Minimum -2.9139345358678126
Maximum 10.527194143813379
Mean 0.4946017857853304
Median -0.5077724434231157
```
[](Figure_1.png)  
[](Figure_2.png)  
[](Figure_3.png)  
