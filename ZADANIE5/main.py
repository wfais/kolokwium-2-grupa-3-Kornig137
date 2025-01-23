import tkinter as tk

# Napisz funkcję create_app(), która:
# Tworzy główne okno Tkinter,
# Dodaje etykietę (label) z jakimś wstępnym tekstem (np. "Wpisz coś:"),
# Dodaje pole tekstowe (Entry), w którym użytkownik może coś wpisać,
# Dodaje przycisk (Button), po którego kliknięciu tekst z pola Entry zostanie wyświetlony w drugiej etykiecie (np. "Wpisałeś: <tekst>").


def create_app():
    """
    Tworzy i zwraca główne okno Tkinter z prostym interfejsem.
    1) Etykieta: "Wpisz coś:"
    2) Pole Entry
    3) Przycisk "Pokaż", który wyświetli wpisany tekst w innej etykiecie
    """

    form = tk.Tk()

    # title - "Prosta aplikacja Tkinter"
    form.title("Prosta aplikacja Tkinter")

    # label_instruct = umocuj przez pack
    label_instrukt = tk.Label(form, text="Wpisz coś: ")
    label_instrukt.pack(padx=5, pady=5)

    # entry_text = 
    entry_text = tk.StringVar()
    entry = tk.Entry(form, textvariable=entry_text)
    entry.pack(padx=5, pady=5)

    # label_result = tk.Label(...
    label_result = tk.Label(form, text="Tu pojawi się Twój tekst")
    label_result.pack(padx=5, pady=5)

    # zdefiniuj funkcję show_text() pobierającą wpisany tekst i wyświetlającą w label_result
    def show_text():
        label_result.config(text=f"Wpisałeś: {entry_text.get()}")

    button_show = tk.Button(form, text="Załaduj", command=show_text)
    button_show.pack(padx=5, pady=5)

    return form

if __name__ == '__main__':
    app = create_app()
    app.mainloop()