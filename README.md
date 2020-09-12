# Algorithmic-Trading
Uses a simple momentum strategy to execute buy/sell purchases of stocks

I picked 19 sub $20 stocks to analyze and used a momentum strategy to see how they performed. The strategy is that we buy a stock whenever the short term rolling average for open price moves above the long term rolling average for price.  This idea takes advantage of any rapid movements in price that deviates from its longer run behavior in the past.  

I originally wanted to use volatility somehow in the strategy, for example adding the condition that the short term volatility has to be less than the long term volatility.  The idea I had here was that if short term volatility is low, then the asset has a defined trend to its movement and we could predict that the investment will therefore be less risky than if short term volatility is high.  I'll keep adjusting the strategy to see if I can make a good condition on volatility.  
