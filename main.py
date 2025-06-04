import tkinter as tk


def main():
    root = tk.Tk()
    root.title("PJ2020 GUI")

    label = tk.Label(root, text="Hello, PJ2020!")
    label.pack(padx=20, pady=10)

    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=(0, 20))

    root.mainloop()


if __name__ == "__main__":
    main()
