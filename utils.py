def calculate_average_percentage_increase(values):
    #method to calculate the average percentage increase for a series of values
    percentage_increases = [
        ((values[i] - values[i-1]) / values[i-1]) * 100 for i in range(1, len(values))
    ]
    
    if percentage_increases:
        average_increase = sum(percentage_increases) / len(percentage_increases)
    else:
        average_increase = 0.0
    
    return round(average_increase, 2)
