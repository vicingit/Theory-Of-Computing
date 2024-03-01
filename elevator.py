import tkinter as tk
from tkinter import messagebox
import time

# elevator machine
class ElevatorMachine:
    def __init__(self):
        self.current_floor = 'A'  # Start state
        self.floor_positions = {'A': 180, 'B': 120, 'C': 60}  # Y positions of each floor on the canvas

    # check whether floor is valid
    def select_floor(self, floor):
        if floor in self.floor_positions:
            start_floor = self.current_floor
            self.current_floor = floor
            return start_floor, floor
        else:
            messagebox.showerror("Invalid Floor", "Please select a valid floor!")

    def get_current_floor(self):
        return self.current_floor

# callbackfn
def select_floor_callback():
    selected_floor = floor_var.get()
    start_floor, end_floor = elevator.select_floor(selected_floor)
    if start_floor and end_floor:
        animate_elevator(start_floor, end_floor)
        current_floor_label.config(text="Current Floor: " + elevator.get_current_floor())

def animate_elevator(start_floor, end_floor):
    start_y = elevator.floor_positions[start_floor] - 20  # Adjusted to align with the top of the line representing the floor
    end_y = elevator.floor_positions[end_floor] - 20  # Adjusted to align with the top of the line representing the floor
    while start_y != end_y:
        if start_y < end_y:
            start_y += 1
        else:
            start_y -= 1
        canvas.move(elevator_visual, 0, start_y - canvas.coords(elevator_visual)[1])
        root.update()
        time.sleep(0.01)
    messagebox.showinfo("FLOOR CHANGE", f"Floor changed from {start_floor} to {end_floor}")

# Initialize Elevator Machine
elevator = ElevatorMachine()

# Create GUI
root = tk.Tk()
root.title("LIFT")
root.geometry("700x800")  # Set window size
root.configure(background='black')  # Set background color to black


frame = tk.Frame(root)
frame.pack(side="bottom", pady=20)

floor_var = tk.StringVar(frame)
floor_var.set("A")

floor_label = tk.Label(frame, text="Select Floor:")
floor_label.grid(row=0, column=0)

floor_option_menu = tk.OptionMenu(frame, floor_var, "A", "B", "C")  # Add more floors as needed
floor_option_menu.grid(row=0, column=1)

select_floor_button = tk.Button(frame, text="Select Floor", command=select_floor_callback, width=10, height=2, bg='yellow', relief="raised", borderwidth=3, bd=0, highlightthickness=0, highlightbackground='black', cursor="hand2")
select_floor_button.grid(row=0, column=2)

current_floor_label = tk.Label(frame, text="Current Floor: " + elevator.get_current_floor())
current_floor_label.grid(row=1, columnspan=3)

canvas = tk.Canvas(root, width=100, height=240)
canvas.pack()
# Draw floors
for floor, y_pos in elevator.floor_positions.items():
    canvas.create_line(0, y_pos, 100, y_pos, fill="white", width=2)  # Change the line style here
    canvas.create_text(20, y_pos - 20, text=floor, anchor='w', fill='white')

# Draw elevator visual
elevator_visual = canvas.create_rectangle(40, 160, 60, 180, fill="blue")

root.mainloop()
