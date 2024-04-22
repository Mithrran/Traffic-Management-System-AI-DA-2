import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data: Features (time of day, weekday/weekend) and labels (traffic density)
# In a real-world scenario, actual traffic data is used.
# Each row represents [time of day, weekday/weekend, traffic density]
X = np.array([[8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1],  # Weekdays
              [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0]])  # Weekends/holidays
y = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65,  # Weekdays
              15, 20, 25, 30, 35, 40, 45, 50, 55, 60])  # Weekends/holidays

# Separate data for weekdays and weekends/holidays
X_weekdays = X[:10]
y_weekdays = y[:10]
X_weekends = X[10:]
y_weekends = y[10:]

# Initialize and train the linear regression models for weekdays and weekends/holidays
model_weekdays = LinearRegression()
model_weekdays.fit(X_weekdays, y_weekdays)

model_weekends = LinearRegression()
model_weekends.fit(X_weekends, y_weekends)

# Get input from the user
while True:
    try:
        time = float(input("Enter the time of day (in hours, 0-24): "))
        if 0 <= time <= 24:
            break
        else:
            print("Please enter a valid time between 0 and 24.")
    except ValueError:
        print("Please enter a valid numerical value.")

is_weekday = input("Is it a weekday? (yes/no): ").lower() == 'yes'

# Predicting traffic density based on the input
if is_weekday:
    predicted_traffic_density = model_weekdays.predict([[time, 1]])  # 1 represents weekday
else:
    predicted_traffic_density = model_weekends.predict([[time, 0]])  # 0 represents weekend/holiday

print(f"Predicted traffic density at {time} hours:", predicted_traffic_density[0])

# To determine if it's feasible to go out based on traffic density
threshold = 40  # Example threshold value for traffic density
if predicted_traffic_density[0] > threshold:
    print("It's not feasible to go out due to high traffic density.")
else:
    print("It's feasible to go out.")

# AI for determining green signal duration based on traffic density
ai_model = LinearRegression()
ai_model.fit(X, y)

predicted_green_duration = ai_model.predict([[time, 1 if is_weekday else 0]])[0]

# Clip green signal duration to be within the range [10, 60] seconds
green_duration = max(min(predicted_green_duration, 60), 10)

# Red signal duration is the remaining time to complete a total cycle duration of 60 seconds
red_duration = 60 - green_duration

print("Traffic signal analysis:")
print(f"Green signal duration: {green_duration} seconds")
print(f"Red signal duration: {red_duration} seconds")
