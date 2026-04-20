# import tkinter as tk
# from tkinter import ttk
# from thread_models import ManyToOne, OneToOne, ManyToMany
# from synchronization import SemaphoreDemo, MonitorDemo
# from scheduler import RoundRobinScheduler
# import threading


# class SimulatorUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Multithreading Simulator")
#         self.root.geometry("1000x700")

#         self.threads = []
#         self.model = None

#         self.setup_menu()
#         self.setup_ui()

#     # ===== MENU =====
#     def setup_menu(self):
#         menubar = tk.Menu(self.root)

#         theme_menu = tk.Menu(menubar, tearoff=0)
#         theme_menu.add_command(label="Light Mode", command=self.set_light_mode)
#         theme_menu.add_command(label="Dark Mode", command=self.set_dark_mode)

#         menubar.add_cascade(label="Theme", menu=theme_menu)
#         self.root.config(menu=menubar)

#     # ===== UI =====
#     def setup_ui(self):
#         # TITLE
#         self.title_label = tk.Label(
#             self.root,
#             text="Multi-threading Simulator",
#             font=("Arial", 24, "bold")
#         )
#         self.title_label.pack(pady=15)

#         # ===== CONTROL CARD =====
#         self.control_card = tk.Frame(self.root, bd=2, relief="ridge", padx=15, pady=15)
#         self.control_card.pack(padx=20, pady=10, fill="x")

#         tk.Label(self.control_card, text="Thread Model:", font=("Arial", 12)).grid(row=0, column=0, padx=5)

#         self.model_var = tk.StringVar()
#         self.model_dropdown = ttk.Combobox(
#             self.control_card,
#             textvariable=self.model_var,
#             values=["Many-to-One", "One-to-One", "Many-to-Many"],
#             width=18
#         )
#         self.model_dropdown.current(0)
#         self.model_dropdown.grid(row=0, column=1, padx=10)

#         tk.Button(self.control_card, text="Add Thread", width=12, command=self.add_thread).grid(row=0, column=2, padx=8)
#         tk.Button(self.control_card, text="Remove Thread", width=14, command=self.remove_thread).grid(row=0, column=3, padx=8)
#         tk.Button(self.control_card, text="Start", width=10, command=self.start_simulation).grid(row=0, column=4, padx=8)
#         tk.Button(self.control_card, text="Semaphore", width=12, command=self.run_semaphore).grid(row=0, column=5, padx=8)
#         tk.Button(self.control_card, text="Monitor", width=10, command=self.run_monitor).grid(row=0, column=6, padx=8)
#         tk.Button(self.control_card, text="Scheduler", width=12, command=self.run_scheduler).grid(row=0, column=7, padx=8)

#         # ===== THREAD CARD =====
#         self.thread_card = tk.LabelFrame(
#             self.root,
#             text="Thread Status",
#             font=("Arial", 12, "bold"),
#             padx=10,
#             pady=10
#         )
#         self.thread_card.pack(fill="both", expand=True, padx=20, pady=10)

#         # ===== LOG CARD =====
#         self.log_card = tk.LabelFrame(
#             self.root,
#             text="System Log",
#             font=("Arial", 12, "bold"),
#             padx=10,
#             pady=10
#         )
#         self.log_card.pack(fill="both", padx=20, pady=10)

#         self.log_text = tk.Text(self.log_card, height=10)
#         self.log_text.pack(fill="both")

#     # ===== ADD THREAD =====
#     def add_thread(self):
#         thread_id = len(self.threads) + 1

#         label = tk.Label(
#             self.thread_card,
#             text=f"Thread {thread_id} - READY",
#             bg="#FFD966",
#             width=35,
#             height=2,
#             font=("Arial", 11, "bold"),
#             relief="groove"
#         )
#         label.pack(pady=5)

#         self.threads.append(label)
#         self.log(f"Thread {thread_id} created")

#     # ===== REMOVE THREAD =====
#     def remove_thread(self):
#         if len(self.threads) == 0:
#             self.log("No threads to remove")
#             return

#         thread_label = self.threads.pop()
#         thread_label.destroy()

#         self.log(f"Thread {len(self.threads) + 1} removed")

#     # ===== START =====
#     def start_simulation(self):
#         selected_model = self.model_var.get()
#         self.log(f"Starting {selected_model}")

#         if selected_model == "Many-to-One":
#             self.model = ManyToOne(self.update_ui)

#         elif selected_model == "One-to-One":
#             self.model = OneToOne(self.update_ui)

#         elif selected_model == "Many-to-Many":
#             self.model = ManyToMany(self.update_ui)

#         for i in range(len(self.threads)):
#             self.model.add_task(i + 1)

#     # ===== UPDATE =====
#     def update_ui(self, thread_id, state):
#         thread = self.threads[thread_id - 1]

#         colors = {
#             "RUNNING": "#77DD77",
#             "WAITING": "#FF6961",
#             "READY": "#FFD966",
#             "TERMINATED": "#C0C0C0"
#         }

#         self.root.after(0, lambda: thread.config(
#             text=f"Thread {thread_id} - {state}",
#             bg=colors.get(state, "#FFD966")
#         ))

#         self.log(f"Thread {thread_id} → {state}")

#     # ===== SEMAPHORE =====
#     def run_semaphore(self):
#         self.log("Semaphore Demo Started")
#         sem = SemaphoreDemo(self.update_ui)

#         for i in range(len(self.threads)):
#             threading.Thread(target=sem.run, args=(i + 1,)).start()

#     # ===== MONITOR =====
#     def run_monitor(self):
#         self.log("Monitor Demo Started")
#         monitor = MonitorDemo(self.update_ui)

#         for i in range(len(self.threads)):
#             threading.Thread(target=monitor.run, args=(i + 1,)).start()

#     # ===== SCHEDULER =====
#     def run_scheduler(self):
#         self.log("Scheduler Started")

#         scheduler = RoundRobinScheduler(self.update_ui, self.log)
#         threading.Thread(target=scheduler.run, args=(len(self.threads),)).start()

#     # ===== THEME =====
#     def set_dark_mode(self):
#         self.apply_theme("#1e1e1e", "white", "#2c2c2c")

#     def set_light_mode(self):
#         self.apply_theme("SystemButtonFace", "black", "white")

#     def apply_theme(self, bg, fg, frame_bg):
#         self.root.configure(bg=bg)

#         for widget in self.root.winfo_children():
#             self.update_widget(widget, bg, fg, frame_bg)

#     def update_widget(self, widget, bg, fg, frame_bg):
#         try:
#             if isinstance(widget, (tk.Frame, tk.LabelFrame)):
#                 widget.configure(bg=bg)

#             elif isinstance(widget, tk.Label):
#                 widget.configure(bg=bg, fg=fg)

#             elif isinstance(widget, tk.Button):
#                 widget.configure(bg=frame_bg, fg=fg)

#             elif isinstance(widget, tk.Text):
#                 widget.configure(bg=frame_bg, fg=fg, insertbackground=fg)
#         except:
#             pass

#         for child in widget.winfo_children():
#             self.update_widget(child, bg, fg, frame_bg)

#     # ===== LOG =====
#     def log(self, message):
#         self.log_text.insert(tk.END, message + "\n")
#         self.log_text.see(tk.END)



















# import tkinter as tk
# from tkinter import ttk
# from thread_models import ManyToOne, OneToOne, ManyToMany
# from synchronization import SemaphoreDemo, MonitorDemo
# from scheduler import RoundRobinScheduler
# import threading
# from PIL import Image, ImageTk


# class SimulatorUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Multithreading Simulator")
#         self.root.geometry("1000x700")
#         self.root.configure(bg="#121212")

#         self.threads = []
#         self.model = None

#         self.setup_menu()
#         self.setup_ui()

#     # ===== MENU =====
#     def setup_menu(self):
#         menubar = tk.Menu(self.root)

#         theme_menu = tk.Menu(menubar, tearoff=0)
#         theme_menu.add_command(label="Light Mode", command=self.set_light_mode)
#         theme_menu.add_command(label="Dark Mode", command=self.set_dark_mode)

#         menubar.add_cascade(label="Theme", menu=theme_menu)
#         self.root.config(menu=menubar)

#     # ===== UI =====
#     def setup_ui(self):

#         # ===== HEADER =====
#         header = tk.Frame(self.root, bg="#1f1f1f", height=80)
#         header.pack(fill="x")

#         title = tk.Label(
#             header,
#             text="⚡ Multithreading Simulator",
#             font=("Segoe UI", 22, "bold"),
#             fg="white",
#             bg="#1f1f1f"
#         )
#         title.pack(pady=20)

#         # ===== OPTIONAL LOGO =====
#         try:
#             img = Image.open("cpu.png")
#             img = img.resize((40, 40))
#             self.logo = ImageTk.PhotoImage(img)

#             logo_label = tk.Label(header, image=self.logo, bg="#1f1f1f")
#             logo_label.place(x=20, y=20)
#         except:
#             pass

#         # ===== CONTROL PANEL =====
#         self.control_card = tk.Frame(self.root, bg="#1e1e1e")
#         self.control_card.pack(padx=20, pady=15, fill="x")

#         tk.Label(self.control_card, text="Thread Model:",
#                  font=("Segoe UI", 11), fg="white", bg="#1e1e1e").grid(row=0, column=0, padx=10)

#         self.model_var = tk.StringVar()
#         self.model_dropdown = ttk.Combobox(
#             self.control_card,
#             textvariable=self.model_var,
#             values=["Many-to-One", "One-to-One", "Many-to-Many"],
#             width=18
#         )
#         self.model_dropdown.current(0)
#         self.model_dropdown.grid(row=0, column=1, padx=10)

#         def styled_btn(text, cmd, color):
#             return tk.Button(
#                 self.control_card,
#                 text=text,
#                 command=cmd,
#                 bg=color,
#                 fg="white",
#                 font=("Segoe UI", 10, "bold"),
#                 relief="flat",
#                 padx=10,
#                 pady=5
#             )

#         styled_btn("Add Thread", self.add_thread, "#4CAF50").grid(row=0, column=2, padx=8)
#         styled_btn("Remove Thread", self.remove_thread, "#E53935").grid(row=0, column=3, padx=8)
#         styled_btn("Start", self.start_simulation, "#2196F3").grid(row=0, column=4, padx=8)
#         styled_btn("Semaphore", self.run_semaphore, "#9C27B0").grid(row=0, column=5, padx=8)
#         styled_btn("Monitor", self.run_monitor, "#FF9800").grid(row=0, column=6, padx=8)
#         styled_btn("Scheduler", self.run_scheduler, "#00BCD4").grid(row=0, column=7, padx=8)

#         # ===== THREAD PANEL =====
#         self.thread_card = tk.LabelFrame(
#             self.root,
#             text=" Threads ",
#             font=("Segoe UI", 12, "bold"),
#             fg="white",
#             bg="#121212"
#         )
#         self.thread_card.pack(fill="both", expand=True, padx=20, pady=10)

#         # ===== LOG PANEL =====
#         self.log_card = tk.LabelFrame(
#             self.root,
#             text=" Logs ",
#             font=("Segoe UI", 12, "bold"),
#             fg="white",
#             bg="#121212"
#         )
#         self.log_card.pack(fill="both", padx=20, pady=10)

#         self.log_text = tk.Text(
#             self.log_card,
#             height=10,
#             bg="#1e1e1e",
#             fg="#00FFAA",
#             insertbackground="white",
#             font=("Consolas", 10)
#         )
#         self.log_text.pack(fill="both")

#     # ===== ADD THREAD =====
#     def add_thread(self):
#         thread_id = len(self.threads) + 1

#         frame = tk.Frame(self.thread_card, bg="#1e1e1e")
#         frame.pack(pady=6, fill="x")

#         label = tk.Label(
#             frame,
#             text=f"Thread {thread_id} - READY",
#             bg="#FFD966",
#             fg="black",
#             font=("Segoe UI", 11, "bold"),
#             padx=10,
#             pady=8
#         )
#         label.pack(fill="x")

#         self.threads.append(label)
#         self.log(f"Thread {thread_id} created")

#     # ===== REMOVE THREAD =====
#     def remove_thread(self):
#         if len(self.threads) == 0:
#             self.log("No threads to remove")
#             return

#         thread_label = self.threads.pop()
#         thread_label.master.destroy()

#         self.log(f"Thread {len(self.threads) + 1} removed")

#     # ===== START =====
#     def start_simulation(self):
#         selected_model = self.model_var.get()
#         self.log(f"Starting {selected_model}")

#         if selected_model == "Many-to-One":
#             self.model = ManyToOne(self.update_ui)

#         elif selected_model == "One-to-One":
#             self.model = OneToOne(self.update_ui)

#         elif selected_model == "Many-to-Many":
#             self.model = ManyToMany(self.update_ui)

#         for i in range(len(self.threads)):
#             self.model.add_task(i + 1)

#     # ===== UPDATE UI =====
#     def update_ui(self, thread_id, state):
#         thread = self.threads[thread_id - 1]

#         colors = {
#             "RUNNING": "#4CAF50",
#             "WAITING": "#E53935",
#             "READY": "#FFD966",
#             "TERMINATED": "#757575"
#         }

#         self.root.after(0, lambda: thread.config(
#             text=f"Thread {thread_id} - {state}",
#             bg=colors.get(state, "#FFD966")
#         ))

#         self.log(f"Thread {thread_id} → {state}")

#     # ===== SEMAPHORE =====
#     def run_semaphore(self):
#         self.log("Semaphore Demo Started")
#         sem = SemaphoreDemo(self.update_ui)

#         for i in range(len(self.threads)):
#             threading.Thread(target=sem.run, args=(i + 1,)).start()

#     # ===== MONITOR =====
#     def run_monitor(self):
#         self.log("Monitor Demo Started")
#         monitor = MonitorDemo(self.update_ui)

#         for i in range(len(self.threads)):
#             threading.Thread(target=monitor.run, args=(i + 1,)).start()

#     # ===== SCHEDULER =====
#     def run_scheduler(self):
#         self.log("Scheduler Started")

#         scheduler = RoundRobinScheduler(self.update_ui, self.log)
#         threading.Thread(target=scheduler.run, args=(len(self.threads),)).start()

#     # ===== THEME =====
#     def set_dark_mode(self):
#         self.root.configure(bg="#121212")

#     def set_light_mode(self):
#         self.root.configure(bg="white")

#     # ===== LOG =====
#     def log(self, message):
#         self.log_text.insert(tk.END, message + "\n")
#         self.log_text.see(tk.END)


# # ===== RUN =====
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SimulatorUI(root)
#     root.mainloop()












import tkinter as tk
from tkinter import ttk
from thread_models import ManyToOne, OneToOne, ManyToMany
from synchronization import SemaphoreDemo, MonitorDemo
from scheduler import RoundRobinScheduler
import threading


class SimulatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Multithreading Simulator")
        self.root.geometry("1200x750")
        self.root.configure(bg="#0f172a")

        self.threads = []
        self.model = None

        self.setup_menu()
        self.setup_ui()

    # ===== MENU =====
    def setup_menu(self):
        menubar = tk.Menu(self.root)

        theme_menu = tk.Menu(menubar, tearoff=0)
        theme_menu.add_command(label="Light Mode", command=self.set_light_mode)
        theme_menu.add_command(label="Dark Mode", command=self.set_dark_mode)

        menubar.add_cascade(label="Theme", menu=theme_menu)
        self.root.config(menu=menubar)

    # ===== UI =====
    def setup_ui(self):

        # ===== SIDEBAR =====
        sidebar = tk.Frame(self.root, bg="#020617", width=220)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar,
                 text="⚡ Simulator",
                 font=("Segoe UI", 20, "bold"),
                 fg="#38bdf8",
                 bg="#020617").pack(pady=25)

        def side_btn(text, cmd):
            btn = tk.Button(sidebar,
                            text=text,
                            command=cmd,
                            bg="#020617",
                            fg="white",
                            font=("Segoe UI", 12, "bold"),
                            relief="flat",
                            padx=10,
                            pady=10)
            btn.bind("<Enter>", lambda e: btn.config(bg="#1e293b"))
            btn.bind("<Leave>", lambda e: btn.config(bg="#020617"))
            return btn

        side_btn("Start Simulation", self.start_simulation).pack(fill="x", padx=10, pady=6)
        side_btn("Semaphore", self.run_semaphore).pack(fill="x", padx=10, pady=6)
        side_btn("Monitor", self.run_monitor).pack(fill="x", padx=10, pady=6)
        side_btn("Scheduler", self.run_scheduler).pack(fill="x", padx=10, pady=6)

        # ===== MAIN AREA =====
        main = tk.Frame(self.root, bg="#0f172a")
        main.pack(side="right", expand=True, fill="both")

        # ===== HEADER =====
        header = tk.Frame(main, bg="#0f172a")
        header.pack(fill="x", pady=15)

        title = tk.Label(header,
                         text="Multithreading Simulator Dashboard",
                         font=("Segoe UI", 28, "bold"),
                         fg="white",
                         bg="#0f172a")
        title.pack()

        # ===== CONTROL PANEL =====
        control = tk.Frame(main, bg="#1e293b")
        control.pack(padx=20, pady=10, fill="x")

        tk.Label(control,
                 text="Thread Model:",
                 font=("Segoe UI", 13, "bold"),
                 fg="white",
                 bg="#1e293b").grid(row=0, column=0, padx=10, pady=10)

        self.model_var = tk.StringVar()

        self.model_dropdown = ttk.Combobox(
            control,
            textvariable=self.model_var,
            values=["Many-to-One", "One-to-One", "Many-to-Many"],
            width=20
        )
        self.model_dropdown.current(0)
        self.model_dropdown.grid(row=0, column=1, padx=10)

        def modern_btn(text, cmd, color):
            btn = tk.Button(control,
                            text=text,
                            command=cmd,
                            bg=color,
                            fg="white",
                            font=("Segoe UI", 11, "bold"),
                            relief="flat",
                            padx=10,
                            pady=6)
            btn.bind("<Enter>", lambda e: btn.config(bg="#334155"))
            btn.bind("<Leave>", lambda e: btn.config(bg=color))
            return btn

        modern_btn("Add Thread", self.add_thread, "#22c55e").grid(row=0, column=2, padx=6)
        modern_btn("Remove Thread", self.remove_thread, "#ef4444").grid(row=0, column=3, padx=6)
        # modern_btn("Start", self.start_simulation, "#3b82f6").grid(row=0, column=4, padx=6)
        # modern_btn("Semaphore", self.run_semaphore, "#a855f7").grid(row=0, column=5, padx=6)
        # modern_btn("Monitor", self.run_monitor, "#f59e0b").grid(row=0, column=6, padx=6)
        # modern_btn("Scheduler", self.run_scheduler, "#06b6d4").grid(row=0, column=7, padx=6)

        # ===== THREAD PANEL =====
        self.thread_card = tk.LabelFrame(
            main,
            text=" Threads ",
            font=("Segoe UI", 14, "bold"),
            fg="white",
            bg="#0f172a",
            padx=10,
            pady=10
        )
        self.thread_card.pack(fill="both", expand=True, padx=20, pady=10)

        # ===== LOG PANEL =====
        self.log_card = tk.LabelFrame(
            main,
            text=" Logs ",
            font=("Segoe UI", 14, "bold"),
            fg="white",
            bg="#0f172a",
            padx=10,
            pady=10
        )
        self.log_card.pack(fill="both", padx=20, pady=10)

        self.log_text = tk.Text(
            self.log_card,
            height=10,
            bg="#020617",
            fg="#00ff9c",
            insertbackground="white",
            font=("Consolas", 11),
            bd=0
        )
        self.log_text.pack(fill="both")

    # ===== BACKEND (UNCHANGED) =====
    def add_thread(self):
        thread_id = len(self.threads) + 1

        label = tk.Label(
            self.thread_card,
            text=f"Thread {thread_id} - READY",
            bg="#facc15",
            fg="black",
            width=40,
            height=2,
            font=("Segoe UI", 12, "bold"),
            relief="flat"
        )
        label.pack(pady=6)

        self.threads.append(label)
        self.log(f"Thread {thread_id} created")

    def remove_thread(self):
        if len(self.threads) == 0:
            self.log("No threads to remove")
            return

        thread_label = self.threads.pop()
        thread_label.destroy()

        self.log(f"Thread {len(self.threads) + 1} removed")

    def start_simulation(self):
        selected_model = self.model_var.get()
        self.log(f"Starting {selected_model}")

        if selected_model == "Many-to-One":
            self.model = ManyToOne(self.update_ui)
        elif selected_model == "One-to-One":
            self.model = OneToOne(self.update_ui)
        elif selected_model == "Many-to-Many":
            self.model = ManyToMany(self.update_ui)

        for i in range(len(self.threads)):
            self.model.add_task(i + 1)

    def update_ui(self, thread_id, state):
        thread = self.threads[thread_id - 1]

        colors = {
            "RUNNING": "#22c55e",
            "WAITING": "#ef4444",
            "READY": "#facc15",
            "TERMINATED": "#64748b"
        }

        self.root.after(0, lambda: thread.config(
            text=f"Thread {thread_id} - {state}",
            bg=colors.get(state, "#facc15")
        ))

        self.log(f"Thread {thread_id} → {state}")

    def run_semaphore(self):
        self.log("Semaphore Demo Started")
        sem = SemaphoreDemo(self.update_ui)

        for i in range(len(self.threads)):
            threading.Thread(target=sem.run, args=(i + 1,)).start()

    def run_monitor(self):
        self.log("Monitor Demo Started")
        monitor = MonitorDemo(self.update_ui)

        for i in range(len(self.threads)):
            threading.Thread(target=monitor.run, args=(i + 1,)).start()

    def run_scheduler(self):
        self.log("Scheduler Started")

        scheduler = RoundRobinScheduler(self.update_ui, self.log)
        threading.Thread(target=scheduler.run, args=(len(self.threads),)).start()

    def set_dark_mode(self):
        self.root.configure(bg="#0f172a")

    def set_light_mode(self):
        self.root.configure(bg="white")

    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SimulatorUI(root)
    root.mainloop()
















