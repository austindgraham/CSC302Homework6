library(ggplot2)
library(tidyr)
library(dplyr)

load("C:/Users/T460s/Downloads/house_prices.rda")
house <- house_prices

ggplot(data=house, aes(x=date, y=house_price_index)) +
  geom_smooth() + facet_wrap(~state, ncol = 10) +
  scale_x_date(name="Year", date_breaks = '20 years', date_labels = '%y', limits = as.Date(c('1964-01-01', '2026-01-01'), breaks = as.Date(c('1980-01-01', '2020-01-01'))))


house_reshaped = gather(prices, measure, value, -date, -state, -house_price_perc)

ggplot(data=house_reshaped, aes(x=date, y=value, group = measure)) +
  geom_smooth() + facet_wrap(~state, ncol = 10) +
  scale_x_date(name="Year", date_breaks = '20 years', date_labels = '%y', limits = as.Date(c('1964-01-01', '2026-01-01'), breaks = as.Date(c('1980-01-01', '2020-01-01'))))

# In this graph, the numbers are so dis-proportionally different from one another that it gives the impression that the unemployment rate is negligible in comparison to the home price index.                            
  
