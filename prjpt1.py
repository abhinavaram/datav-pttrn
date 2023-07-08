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
    highlight_columns = []

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
            highlight_choice = input(f"Do you want to highlight {column_names[selection - 1]}? (y/n): ")
            if highlight_choice.lower() == 'y':
                highlight_columns.append(str(column_names[selection - 1]))
        else:
            print("Invalid selection!")

    if len(x_columns) > 0 and len(y_columns) > 0:
        charts.append((x_columns, y_columns, highlight_columns))
    else:
        print("No columns selected. Exiting...")
        break

if len(charts) > 0:
    colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown']
    highlight_colors = ['yellow', 'cyan', 'magenta', 'lime', 'pink']

    fig, axes = plt.subplots(len(charts), 1, figsize=(10, 6 * len(charts)))

    for i, (x_columns, y_columns, highlight_columns) in enumerate(charts):
        ax = axes[i] if len(charts) > 1 else axes

        for j, y_column in enumerate(y_columns):
            color_index = j % len(colors)
            ax.plot(df[x_columns[0]], df[y_column], color=colors[color_index], marker='o')

        for j, highlight_column in enumerate(highlight_columns):
            if j >= len(highlight_colors):
                print(f"Not enough highlight colors defined. Skipping highlighting for {highlight_column}.")
                continue

            while True:
                start_value = float(input(f"Enter the starting x-axis value for {highlight_column} (or 0 to finish): "))
                if start_value == 0:
                    break

                end_value = float(input(f"Enter the ending x-axis value for {highlight_column}: "))

                start_index = df[df[x_columns[0]] == start_value].index[0]
                end_index = df[df[x_columns[0]] == end_value].index[0]

                # Plot the highlighted part with the specified color
                ax.plot(df[x_columns[0]][start_index:end_index + 1], df[highlight_column][start_index:end_index + 1], color=highlight_colors[j], marker='o')

        ax.set_title('Line Chart')
        ax.set_xlabel('X Values')
        ax.set_ylabel('Y Values')

    plt.tight_layout()
    plt.show()



