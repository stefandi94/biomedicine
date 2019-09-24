from utils import get_new_shape, plot
from functools import partial
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def GUI(n_components, new_sample, skip_link, mean, std, mean_shape, pca_matrix):
    window = tk.Tk()
    window.title('Shape Deformation')
    window.geometry('920x900')

    d = {}
    for i in range(n_components):
        d[i] = tk.DoubleVar()

        label = tk.Label(window, text='b{}'.format(i + 1))
        label.grid(column=0, row=2 + i)

        slider = tk.Scale(window, from_=1, to=3, orient=tk.HORIZONTAL, variable=d[i])
        slider.grid(column=1, row=2 + i)

    fig = plot(new_sample, skip_link)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(column=2, row=20)
    canvas._tkcanvas.grid(column=2, row=21)

    applyButton = tk.Button(window, text='Apply',command = partial(action, window, canvas, d, mean, std, mean_shape, pca_matrix, skip_link))
    applyButton.grid(column=1, row=20)  # row as placeholder

    window.mainloop()





def action(window, canvas, d, mean, std, mean_shape, pca_matrix, skip_link):
    coef = []
    for key in d:
        coef.append(d[key].get())

    new_shape = get_new_shape(mean, coef*std, mean_shape, pca_matrix)
    fig = plot(new_shape, skip_link)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(column=2, row=20)
    canvas._tkcanvas.grid(column=2, row=21)
