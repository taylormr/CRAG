import tkinter as tk
from tkinter import ttk
from import_csv import *

bg_color = '#2B2D2F'
bg_2_color = 'blue'
fg_color = 'white'


def explore_load(other_page):
    other_page.destroy()
    explore_init()


def landing_init():
    landing_page = tk.Tk()
    landing_page.title('COVID-19 Research At a Glance')
    width, height = landing_page.winfo_screenwidth(), landing_page.winfo_screenheight()
    landing_page.geometry('%dx%d+0+0' % (width, height))
    landing_page.configure(bg=bg_color)

    mainframe = tk.Frame(landing_page)
    mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
    mainframe.configure(bg=bg_color)

    # Add title
    # activebackground, activeforeground, anchor,
    #background, bitmap, borderwidth, cursor,
    #disabledforeground, font, foreground,
    #highlightbackground, highlightcolor,
    #highlightthickness, image, justify,
    #padx, pady, relief, takefocus, text,
    #textvariable, underline, wraplength
    title = tk.Label(mainframe, text="Welcome to C.R.A.G.",
                     fg=fg_color, width=20, font=("Helvetica", 40), background=bg_color)
    title.grid(row=1, column=2, columnspan=1, pady=100)

    # Add explore button
    explore_b = tk.Button(mainframe, text="Explore",
                          command=lambda: explore_load(landing_page), font=("Helvetica", 38), background=bg_2_color, foreground=fg_color)
    explore_b.grid(row=2, column=2, columnspan=1, pady=50)

    # Add surprise me button
    surprise_b = tk.Button(
        mainframe,  text="Surprise", font=("Helvetica", 28), background=bg_2_color, foreground=fg_color)
    surprise_b.grid(row=2, column=1, columnspan=1, pady=50, padx=80)

    # Add about us button
    about_b = tk.Button(mainframe, text="About",
                        font=("Helvetica", 28), background=bg_2_color, foreground=fg_color)
    about_b.grid(row=2, column=3, pady=50, padx=80)

    # Add clear button
    # clear_b = tk.Button(mainframe, text="Clear",
    #                    command=lambda: mainframe.destroy())
    #clear_b.grid(row=4, column=2)

    # Run main loop
    landing_page.mainloop()


def landing_load(other_page):
    other_page.destroy()
    landing_init()


def explore_init():
    explore_page = tk.Tk()
    explore_page.wm_state('zoomed')

    explore_page.title('COVID-19 Research At a Glance')
    width, height = explore_page.winfo_screenwidth(), explore_page.winfo_screenheight()
    explore_page.geometry('%dx%d+0+0' % (width, height))
    explore_page.configure(bg=bg_color)

    exframe = tk.Frame(explore_page)
    exframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
    exframe.configure(bg=bg_color)

    # Add home button
    home_b = tk.Button(exframe, text="Home",
                       command=lambda: landing_load(explore_page))
    home_b.grid(row=1, column=3, sticky='E')

    # Query entry
    query_str = tk.StringVar(explore_page)
    query_e = tk.Entry(exframe, textvariable=query_str,
                       width=50, font=("Helvetica", 18))
    query_e.grid(row=1, column=2, sticky="W")

    # Dropdown search type
    search_type = tk.StringVar(explore_page)
    search_options = ['title', 'authors', 'publish_time', 'journal', 'keyword']
    search_type.set(search_options[0])
    search_d = tk.OptionMenu(exframe, search_type, *search_options)
    search_d.grid(row=2, column=1)

    # Table
    table = ttk.Treeview(exframe, columns=(
        'title', 'authors', 'publish_time', 'journal', 'keyword'), show='headings')
    for header in search_options:
        table.heading(header, text=header)
    ttk.Style().configure('Treeview', rowheight=30)

    def summary_info(event):
        df = find(table.item(table.selection()[0])[
                  'values'][0])  # grab csv entry
        l = df.values.tolist()[0]
        top = tk.Toplevel()
        top.wm_state('zoomed')
        top.title("About This Article")

        topframe = tk.Frame(top)
        topframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
        topframe.columnconfigure(2, weight=1)
        topframe.rowconfigure(9, weight=1)
        source_x = l[1]
        title = l[2]
        doi = l[3]
        abstract = l[4]
        publish_time = l[5]
        authors = l[6]
        journal = l[7]
        url = l[10]

        title_m = tk.Label(topframe, text="Title: " + title)
        title_m.grid(row=1, column=1)
        authors_m = tk.Label(topframe, text="Author(s): " + authors)
        authors_m.grid(row=2, column=1)
        publish_time_m = tk.Label(topframe, text="Published: " + publish_time)
        publish_time_m.grid(row=3, column=1)
        journal_m = tk.Label(topframe, text="Journal " + journal)
        journal_m.grid(row=4, column=1)
        source_x_m = tk.Label(topframe, text="Source: " + source_x)
        source_x_m.grid(row=5, column=1)
        doi_m = tk.Label(topframe, text="DOI: " + doi)
        doi_m.grid(row=6, column=1)
        # abstract_m = tk.Label(topframe, text="Abstract: " + abstract)
        # abstract_m.grid(row=7, column=1)
        url_m = tk.Label(topframe, text="URL: " + url)
        url_m.grid(row=8, column=1)

        close = tk.Button(top, text="Close", command=top.destroy)
        close.grid()
        top.mainloop()
    table.bind("<Double-1>", summary_info)

    # Search
    def search_callback(*args):
        table.delete(*table.get_children())
        df = search(search_type.get(), query_str.get())
        for index, x in df.iterrows():
            table.insert("", "end", values=(x[2], x[6], x[5], x[7]))
        table.grid(row=2, column=2)
    table.grid(row=2, column=2, columnspan=2, sticky='W')
    search_b = tk.Button(exframe, text="Search", command=search_callback)
    search_b.grid(row=1, column=2, sticky='E')

    # Run main loop
    explore_page.mainloop()


if __name__ == "__main__":
    # s = ttk.Style()
    # s.theme_use('clam')
    load_csv()
    landing_init()
