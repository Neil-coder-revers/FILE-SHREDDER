import customtkinter as ctk
import threading
import tkinter as tk
from tkinter import filedialog
from core.shredder import secure_delete

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class SecureWipeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.geometry("600x450")
        self.center_window()
        
        self.title_bar = ctk.CTkFrame(self, height=40, fg_color="#1a1a1a", corner_radius=0)
        self.title_bar.grid(row=0, column=0, sticky="ew")
        self.title_bar.bind("<Button-1>", self.start_drag)
        self.title_bar.bind("<B1-Motion>", self.do_drag)
        
        ctk.CTkLabel(self.title_bar, text="SecureWipe", text_color="#666", font=("Arial", 12)).pack(side="left", padx=15)
        ctk.CTkButton(self.title_bar, text="✕", width=40, fg_color="transparent", hover_color="#c0392b", command=self.destroy).pack(side="right")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)

        
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=1, column=0, pady=(10, 5))
        
        ctk.CTkLabel(self.header_frame, text="SecureWipe", font=("Roboto Medium", 32), text_color="white").pack()

       
        self.file_frame = ctk.CTkFrame(self, fg_color="#2b2b2b")
        self.file_frame.grid(row=2, column=0, padx=40, pady=20, sticky="ew")
        
        self.path_entry = ctk.CTkEntry(self.file_frame, placeholder_text="Select a file or folder...", font=("Roboto", 13), border_width=0, fg_color="#2b2b2b")
        self.path_entry.pack(side="left", fill="x", expand=True, padx=15, pady=15)
        
        self.browse_btn = ctk.CTkButton(self.file_frame, text="File", width=60, command=self.browse_file, font=("Roboto", 12))
        self.browse_btn.pack(side="right", padx=(5, 15))
        
        self.browse_dir_btn = ctk.CTkButton(self.file_frame, text="Folder", width=60, command=self.browse_folder, font=("Roboto", 12))
        self.browse_dir_btn.pack(side="right", padx=0)

        
        self.action_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.action_frame.grid(row=3, column=0, pady=10)

        self.algo_var = ctk.CTkComboBox(self.action_frame, values=["Standard Wipe (3 Passes)", "Gutmann Method (35 Passes)", "Quick Wipe (1 Pass)"],
                                        width=250, border_color="#3B8ED0", button_color="#3B8ED0")
        self.algo_var.pack(pady=10)

        self.run_btn = ctk.CTkButton(self.action_frame, text="Erase File", command=self.start_wipe,
                                     font=("Roboto", 14, "bold"), height=45, width=250,
                                     fg_color="#d63031", hover_color="#b71c1c") 
        self.run_btn.pack(pady=15)

        
        self.log_box = ctk.CTkTextbox(self, height=120, fg_color="#1e1e1e", text_color="#ccc", font=("Consolas", 11), corner_radius=0)
        self.log_box.grid(row=5, column=0, sticky="ew", padx=0, pady=0)
        
        self.log("Ready.")

    def log(self, msg):
        self.log_box.insert("end", f"> {msg}\n")
        self.log_box.see("end")

    def browse_file(self):
        file = filedialog.askopenfilename()
        if file:
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, file)
            self.log(f"Selected: {file}")

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, folder)
            self.log(f"Selected Folder: {folder}")

    def start_wipe(self):
        target = self.path_entry.get()
        if not target:
            self.log("Error: No file selected.")
            return
        
        algo = self.algo_var.get()
        passes = 3
        if "1 Pass" in algo: passes = 1
        if "35 Passes" in algo: passes = 35
        
        self.log(f"Starting {passes}-pass wipe on: {target}")
        self.run_btn.configure(state="disabled", text="Erasing...")
        
        threading.Thread(target=self.run_process, args=(target, passes)).start()

    def run_process(self, target, passes):
        secure_delete(target, passes, self.log)
        self.run_btn.configure(state="normal", text="Erase File")

    def center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f'+{x}+{y}')

    def start_drag(self, event):
        self._x_drag = event.x
        self._y_drag = event.y

    def do_drag(self, event):
        x = self.winfo_pointerx() - self._x_drag
        y = self.winfo_pointery() - self._y_drag
        self.geometry(f'+{x}+{y}')

if __name__ == "__main__":
    app = SecureWipeApp()
    app.mainloop()
