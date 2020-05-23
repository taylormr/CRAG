import tkinter as tk
from import_csv import *

landing_page = tk.Tk()
landing_page.wm_state('zoomed')

mainframe = tk.Frame(landing_page)
mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
mainframe.columnconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)

# Add title
title = tk.Label(mainframe, text="Welcome to CRAG")
title.grid(row=1, column=1)

# Add explore button
explore_b = tk.Button(text="Explore")
explore_b.grid(row=2, column=2)

# Add surprise me button
surprise_b = tk.Button(mainframe, text="Surprise")
surprise_b.grid(row=3, column=2)

# Add about us button
about_b = tk.Button(text="About")
about_b.grid()

# Run main loop
landing_page.mainloop()
