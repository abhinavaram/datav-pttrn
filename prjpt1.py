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
    colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown']
    highlighted_colors = []

    fig, axes = plt.subplots(len(charts), 1, figsize=(10, 6 * len(charts)))

    for i, (x_columns, y_columns) in enumerate(charts):
        ax = axes[i] if len(charts) > 1 else axes

        first_y_color = colors[i % len(colors)]
        second_y_color = colors[(i + 1) % len(colors)]

        for j, y_column in enumerate(y_columns):
            if j == 0:
                ax.plot(df[x_columns[0]], df[y_column], color=first_y_color, marker='o')
            elif j == 1:
                ax.plot(df[x_columns[0]], df[y_column], color=second_y_color, marker='o')

        highlight_colors = list(set(colors) - set(highlighted_colors))
        highlighted_colors.append(highlight_colors[0])

        while True:
            start_value = float(input("Enter the starting x-axis value (or 0 to finish): "))
            if start_value == 0:
                break

            end_value = float(input("Enter the ending x-axis value: "))

            start_index = df[df[x_columns[0]] == start_value].index[0]
            end_index = df[df[x_columns[0]] == end_value].index[0]

            # Plot the highlighted part with the specified color
            ax.plot(df[x_columns[0]][start_index:end_index + 1], df[y_columns[0]][start_index:end_index + 1], color=highlight_colors[0], marker='o')

        ax.set_title('Line Chart')
        ax.set_xlabel('X Values')
        ax.set_ylabel('Y Values')

    plt.tight_layout()
    plt.show()


