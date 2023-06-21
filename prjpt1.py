import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\asus\Desktop\Book1.xlsx')

column_names = df.columns

print("Select the columns for the line chart:")
print("0: None (Finish selection)")

# Store selected column names and their respective index range
selected_columns = []

for i, column in enumerate(column_names):
    print(f"{i + 1}: {column}")

    while True:
        selection = int(input("Enter the number of the Y column (or 0 to finish): "))
        if selection == 0:
            break
        elif selection in range(1, len(column_names) + 1):
            column_name = str(column_names[selection - 1])
            start_index = int(input(f"Enter the start index for {column_name}: "))
            end_index = int(input(f"Enter the end index for {column_name}: "))
            selected_columns.append((column_name, start_index, end_index))
            break
        else:
            print("Invalid selection!")

# Plotting the line chart with index highlighting
for y_column, start_index, end_index in selected_columns:
    x_values = df[selected_columns[0][0]]  # Use the first selected column as X values
    y_values = df[y_column]
    plt.plot(x_values, y_values, marker='o')

    # Highlight the specified index range
    plt.fill_between(x_values, y_values, where=(x_values >= start_index) & (x_values <= end_index), alpha=0.3)

plt.title('Line Chart')
plt.xlabel('X Values')
plt.ylabel('Y Values')

plt.show()


