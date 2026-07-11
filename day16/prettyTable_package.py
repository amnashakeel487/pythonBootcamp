from prettytable import PrettyTable

# Create a table
table = PrettyTable()

# Add column names
table.field_names = ["Name", "Age", "Grade"]

# Add rows
table.add_row(["Amna", 20, "A"])
table.add_row(["maida", 21, "B+"])
table.add_row(["Sara", 19, "A-"])

# Print the table
print(table)