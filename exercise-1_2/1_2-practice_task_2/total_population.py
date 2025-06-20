total_population = ((2008, 6789088686), (2009, 6872767093), (2010, 6956823603), (2011, 7041194301), (2012, 7125828059), (2013, 7210581976), (2014, 7295290765), (2015, 7379797139), (2016, 7464022049), (2017, 7547858925), (2018, 7631091040), (2019, 7713468100), (2020, 7794798739));

popol_b = (6789088686, 6872767093, 6956823603, 7041194301, 7125828059, 7210581976, 7295290765, 7379797139, 7464022049, 7547858925, 7631091040, 7713468100, 7794798739);

# By default, max() on a tuple of tuples compares the first element of each inner tuple.
# In this case, it's the year.
max_by_default = max(total_population)
print(f"The max tuple by default is: {max_by_default}")

# To find the max based on the population (the second element), we use a key.
max_by_population = max(total_population, key=lambda item: item[1])
print(f"The max tuple by population is: {max_by_population}")

# Note that in this specific dataset, the year and population both increase together,
# so the result is the same. But the method of getting there is different.








