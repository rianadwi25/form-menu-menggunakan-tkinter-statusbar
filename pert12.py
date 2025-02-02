import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh Program Menu dengan Tkinter dan Status Bar")
root.geometry("400x300")

# fungsi untuk membuka form baru
def new_file():
   new_window = tk.Toplevel(root)
   new_window.title("Form Baru")
   new_window.geometry("300x200")
   
   # Membuat label dan entry di form baru
   label_name = tk.Label(new_window, text="Nama:")
   label_name.pack(pady=10)
   
   entry_name = tk.Entry(new_window, width=30)
   entry_name.pack(pady=5)
   
   label_age = tk.Label(new_window, text="Umur:")
   label_age.pack(pady=10)
   
   entry_age = tk.Entry(new_window, width=30)
   entry_age.pack(pady=5)
   
   # Tombol untuk menyimpan data
   def save_data():
       name = entry_name.get()
       age = entry_age.get()
       messagebox.showinfo("Data Tersimpan", f"Nama: {name}, Umur: {age}")
       
   btn_save = tk.Button(new_window, text="Simpan", command=save_data)
   btn_save.pack(pady=20)
    
def open_file():
    new_window = tk.Toplevel(root)
    new_window.title("Form Penjumlahan")

    def hitung_penjumlahan():
        try:
            angka1 = float(entry_angka1.get())
            angka2 = float(entry_angka2.get())
            jumlah = angka1 + angka2
            entry_hasiljlh.delete(0, tk.END)
            entry_hasiljlh.insert(0, f"{jumlah}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
    
    #Label dan entry angaka pertama
    label_angka1 = tk.Label(new_window, text="Masukkan angka Pertama:", anchor="w")
    label_angka1.grid(row=0, column=0, padx=10, pady=5)

    entry_angka1 = tk.Entry(new_window)
    entry_angka1.grid(row=0, column=1, padx=10, pady=5)

    #Label dan entry angka kedua
    label_angka2 = tk.Label(new_window, text="Masukkan angka Kedua:", anchor="w")
    label_angka2.grid(row=1, column=0, padx=10, pady=5)

    entry_angka2 = tk.Entry(new_window)
    entry_angka2.grid(row=1, column=1, padx=10, pady=5)
    
    #tombol untuk menghitung penjumlahan
    tombol_jawab = tk.Button(new_window, text="Jawaban", command=hitung_penjumlahan)
    tombol_jawab.grid(row=2, column=0, columnspan=1, pady=5)

    #Label untuk menampilkan hasil penjumlahan
    label_hasil = tk.Label(new_window, text="Jawaban:")
    label_hasil.grid(row=5, column=0, pady=10)
        
    entry_hasiljlh = tk.Entry(new_window)
    entry_hasiljlh.grid(row=5, column=1, padx=10, pady=5)
    
def save_file():
    messagebox.showinfo("save File", "Menyimpan File")
    
def about():
    messagebox.showinfo("About", "Ini adalah contoh program menu")
    
def exit_app():
    root.quit()
    
# Membuat menu bar
menu_bar = tk.Menu(root)

#Membuat menu "File"
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Membuat menu "Help"
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Menampilkan menu bar pada jendela utama 
root.config(menu=menu_bar)

# Membuat fungsi untuk menampilkan waktu dan tanggal pada satus bar
def update_status_bar():
    now = datetime.now()
    current_time = now.strftime("%A, %d %B %Y")
    status_bar.config(text=f"Tanggal:{current_time}")
    root.after(1000, update_status_bar) # Memperbarui setiap 1 detik
    
# Membuat status bar
status_bar = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Memanggil fungsi untuk memperbarui status bar
update_status_bar()

# Menjalankan aplikasi
root.mainloop()