# Exercise Question 17: Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
# Given:

number_of_terms = 5
series = sum_series = 0
for i in range(5):
    series = series * 10 + 2
    sum_series += series
    print(series, end=" ")
print(sum_series)