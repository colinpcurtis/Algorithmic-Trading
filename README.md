# Algorithmic-Trading
Uses a simple momentum strategy to execute buy/sell purchases of stocks

I picked 19 sub $20 stocks to analyze and used a momentum strategy to see how they performed. The strategy is that we buy a stock whenever the short term rolling average for open price moves above the long term rolling average for price.  This idea takes advantage of any rapid movements in price that deviates from its longer run behavior in the past.  

I originally wanted to use volatility somehow in the strategy, for example adding the condition that the short term volatility has to be less than the long term volatility.  The idea I had here was that if short term volatility is low, then the asset has a defined trend to its movement and we could predict that the investment will therefore be less risky than if short term volatility is high.  I'll keep adjusting the strategy to see if I can make a good condition on volatility.  

edit: I recently added a volatility condition to the algorithm.  It is the same algorithm as before with the addition that we want long term volaility to be above short term volatility.  The idea I had here was that we can exploit upward movement (i.e. the momentum part of our strategy) and the higher risk associated with higher volatility in a short term window to predict that the price should probably go up.  This condition is an "and", so it is relatively strong considering we need both upward movement and higher risk.  This means that once one of these conditions fails then we sell the stock, which usually happens within a couple days.

The trade off in this strategy is that it won't hold onto stocks in multi-day rallies, since eventually the long term volatility will will decrease and the stock will be sold.  However, this approachseems to work pretty well on a handful of stocks (EVRI, IFSPF, BCEL, AND KNSA).  Returns are generally higher using this strategy, but it comes at the expense of higher risk (i.e. lower Sharpe Ratio) and a more secure investment.  
