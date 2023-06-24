import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\asus\Desktop\Book1.xlsx')
column_names = df.columns

print("Select the columns for the line charts:")
print("0: None (Finish selection)")
for i, column in enumerate(column_names):
    print(f"{i + 1}: {column}")

charts = []

while True:
    x_columns = []
    y_columns = []

    while True:
        selection = int(input("Enter the number of the X column (or 0 to finish): "))
        if selection == 0:
            break
        elif selection in range(1, len(column_names) + 1):
            x_columns.append(str(column_names[selection - 1]))
        else:
            print("Invalid selection!")

    while True:
        selection = int(input("Enter the number of the Y column (or 0 to finish): "))
        if selection == 0:
            break
        elif selection in range(1, len(column_names) + 1):
            y_columns.append(str(column_names[selection - 1]))
        else:
            print("Invalid selection!")

    if len(x_columns) > 0 and len(y_columns) > 0:
        charts.append((x_columns, y_columns))
    else:
        print("No columns selected. Exiting...")
        break

if len(charts) > 0:
    fig, axes = plt.subplots(len(charts), 1, figsize=(10, 6 * len(charts)))

    for i, (x_columns, y_columns) in enumerate(charts):
        ax = axes[i] if len(charts) > 1 else axes
        for y_column in y_columns:
            ax.plot(df[x_columns[0]], df[y_column], marker='o')
        ax.set_title('Line Chart')
        ax.set_xlabel('X Values')
        ax.set_ylabel('Y Values')

    plt.tight_layout()
    plt.show()

