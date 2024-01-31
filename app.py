import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class DataPlotterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Plotter Dashboard")

        self.load_data()
        self.create_widgets()

    def load_data(self):
        self.data = pd.read_csv("data.csv")

    """def create_widgets(self):
        # Combobox for selecting plot type
        plot_types = ['Line Plot', 'Scatter Plot', 'Histogram']
        self.plot_type_var = tk.StringVar()
        self.plot_type_var.set(plot_types[0])
        plot_type_combobox = ttk.Combobox(self.root, textvariable=self.plot_type_var, values=plot_types)
        plot_type_combobox.grid(row=0, column=0, padx=10, pady=10)

        # Button to generate plot
        generate_plot_button = tk.Button(self.root, text="Generate Plot", command=self.generate_plot)
        generate_plot_button.grid(row=0, column=1, padx=10, pady=10)

        # Matplotlib figure for displaying plots
        self.figure = Figure(figsize=(6, 5), dpi=150)
        self.subplot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, padx=4, pady=4)
    def generate_plot(self):
        plot_type = self.plot_type_var.get()"""
    def intitiate():
        self.figure = Figure(figsize=(6, 5), dpi=150)
        self.subplot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, padx=4, pady=4)
    def line_plot():
        self.subplot.clear()
        self.subplot.plot(self.data['max_price'], self.data['modal_price'])
        self.subplot.set_title('Line Plot')
        self.subplot.set_xlabel('Max Price')
        self.subplot.set_ylabel('Modal Price')
        self.canvas.draw()

    def Scatter_Plot():
        self.subplot.clear()
        self.subplot.scatter(self.data['max_price'], self.data['modal_price'])
        self.subplot.set_title('Scatter Plot')
        self.subplot.set_xlabel('Max Price')
        self.subplot.set_ylabel('Modal Price')
        self.canvas.draw()

    def Histogram():
        self.subplot.clear()
        self.subplot.hist(self.data['max_price'], bins=5, color='blue', edgecolor='black')
        self.subplot.set_title('Histogram')
        self.subplot.set_xlabel('Max Price')
        self.subplot.set_ylabel('Price')
        self.canvas.draw()

root = tk.Tk()
app = DataPlotterApp(root)
root.mainloop()