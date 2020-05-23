from tkinter import *
from tkinter import ttk
from import_csv import *
from landing_page import *


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
    explore_init()
