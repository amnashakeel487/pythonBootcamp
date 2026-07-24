import pandas as pd

# Read the squirrel data
data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

# Count squirrels by fur color
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

# Create summary dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data_dict)

# Save to a new CSV file
df.to_csv("squirrel_count.csv", index=False)

print("Analysis completed successfully!")