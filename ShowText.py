import tkinter
import customtkinter as ct

ct.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = ct.CTk()
root.geometry("1280x720")

frame = ct.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

left_frame = ct.CTkFrame(frame, height=300)
left_frame.grid(row=0, column=0)

root.mainloop()