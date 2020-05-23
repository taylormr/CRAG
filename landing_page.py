import tkinter as tk
from import_csv import *
from explore_page import *


def explore_load(other_page):
    other_page.destroy()
    explore_init()


def landing_init():
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
    explore_b = tk.Button(mainframe, text="Explore",
                          command=lambda: explore_load(landing_page))
    explore_b.grid(row=2, column=2)

    # Add surprise me button
    surprise_b = tk.Button(mainframe, text="Surprise")
    surprise_b.grid(row=3, column=2)

    # Add about us button
    about_b = tk.Button(mainframe, text="About")
    about_b.grid()

    # Add clear button
    clear_b = tk.Button(mainframe, text="Clear",
                        command=lambda: mainframe.destroy())
    clear_b.grid(row=4, column=2)

    # Run main loop
    landing_page.mainloop()


def landing_load(other_page):
    other_page.destroy()
    landing_init()


def explore_init():
    explore_page = Tk()
    explore_page.wm_state('zoomed')

    exframe = Frame(explore_page)
    exframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
    exframe.columnconfigure(5, weight=1)
    exframe.rowconfigure(5, weight=1)

    # Add title
    title = Label(exframe, text="Explore COVID-19 Research")
    title.grid(row=1, column=1)

    # Add home button
    home_b = Button(exframe, text="Home",
                    command=lambda: landing_load(explore_page))
    home_b.grid(row=2, column=2)

    # Query
    query_str = StringVar(explore_page)
    query_e = Entry(exframe, textvariable=query_str)
    query_e.grid(row=3, column=3)

    # Dropdown search type
    search_type = StringVar(explore_page)
    search_options = ['title', 'authors', 'publish_time', 'journal', 'keyword']
    search_type.set(search_options[0])
    search_d = OptionMenu(exframe, search_type, *search_options)
    search_d.grid(row=1, column=2)

    # Table
    table = ttk.Treeview(exframe, columns=(
        'title', 'authors', 'publish_time', 'journal', 'keyword'), show='headings')
    for header in search_options:
        table.heading(header, text=header)

    # Search
    def search_callback(*args):
        table.delete(*table.get_children())
        df = search(search_type.get(), query_str.get())
        for index, x in df.iterrows():
            table.insert("", "end", values=(x[2], x[6], x[5], x[7]))
        table.grid(row=1, column=3)

    search_b = Button(exframe, text="Search", command=search_callback)
    search_b.grid(row=1, column=4)

    # Run main loop
    explore_page.mainloop()


if __name__ == "__main__":
    load_csv()
    landing_init()
