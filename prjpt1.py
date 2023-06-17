import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(r'C:\Users\asus\Desktop\Book1.xlsx')


column_names = df.columns


print("Select the columns for the line chart:")
print("0: None (Finish selection)")
for i, column in enumerate(column_names):
    print(f"{i + 1}: {column}")

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


for y_column in y_columns:
    plt.plot(df[str(x_columns[0])], df[str(y_column)], marker='o')


plt.title('Line Chart')
plt.xlabel('X Values')
plt.ylabel('Y Values')


plt.show()

