from tkinter import *
from tkinter import ttk
from import_csv import *

load_csv()
explore_page = Tk()
explore_page.wm_state('zoomed')

# Add title
title = Label(text="Explore COVID-19 Research")
title.grid()

# Query
query_str = StringVar(explore_page)
query_e = Entry(explore_page, textvariable=query_str)
query_e.grid()


# Search
table = ttk.Treeview(explore_page, columns=(
    'title', 'authors'), show='headings')


def search_callback(*args):
    global table
    table.delete(*table.get_children())
    df = search(search_type.get(), query_str.get())
    for index, x in df.iterrows():
        table.insert("", "end", values=(x[2], x[6]))
    table.grid()


search_b = Button(explore_page, text="Search", command=search_callback)
search_b.grid()

# Dropdown search type
search_type = StringVar(explore_page)
search_options = ['title', 'authors', 'keyword']
search_type.set(search_options[0])
search_d = OptionMenu(explore_page, search_type, *search_options)
search_d.grid()


# def apply_dropdown(*args):
#    print(query_str.get())
# query_str.trace('w', apply_dropdown)


# Run main loop
explore_page.mainloop()
