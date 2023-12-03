"""
Ian Chan A00910012
Edro Gonzales A01257468
"""
import tkinter as tk


def on_cell_click(each_row, each_column):
    if (each_row, each_column) == (0, 0) or (each_row, each_column) == (6, 4):
        output_text.set(f"You are at the Hospital! Pikachu feels better now.")
    else:
        output_text.set(f"Clicked on cell ({each_row}, {each_column})")


# Create the main application window
root = tk.Tk()
root.title("Text-based Game")

# Create and configure widgets
label = tk.Label(root, text="Welcome to Pikachu's Adventure!", font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=11, pady=10)

output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text)
output_label.grid(row=1, column=0, columnspan=11, pady=10)

# Create a grid of labeled cells to represent cells
for row in range(2, 13):
    for column in range(11):
        # Add a label inside each cell
        if (row - 2, column) == (0, 0) or (row - 2, column) == (6, 4):
            label_text = "Hospital"
        else:
            label_text = f"({row - 2}, {column})"

        cell_label = tk.Label(root, text=label_text, width=10, height=2,
                              relief="solid", padx=2, pady=2, fg="black")

        # Color the Hospital cells blue
        if (row - 2, column) == (0, 0) or (row - 2, column) == (6, 4):
            cell_label.configure(bg="sky blue")
        # Make entire row 5 dark grey
        elif row == 7 or column == 5:
            cell_label.configure(bg="dark grey")
        else:
            cell_label.configure(bg="light green")

        cell_label.grid(row=row, column=column)

        # Configure the label as a button
        cell_label.bind("<Button-1>", lambda event, r=row - 2, c=column: on_cell_click(r, c))

# Start the main event loop
root.mainloop()
