rainYears = int(input("Enter the amount of years: "))
rain = 0
for year in range(rainYears):
    for month in range(1, 13):
        rain += int(input("Enter the rain amount for the month:"))


print("Total Rain:",rain, "inches")
print("Number of Months:", rainYears * 12)
print("Average Monthly Rainfall:", rain / (rainYears * 12), "inches")