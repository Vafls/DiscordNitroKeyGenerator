import random
import string
import tkinter as tk

def generate_nitro_key(length=19):
    characters = string.ascii_letters + string.digits
    key = ''.join(random.choice(characters) for i in range(length))
    return key

def generate_keys():
    num_keys = int(entry.get())
    keys_generated = [generate_nitro_key() for _ in range(num_keys)]
    result_text.delete(1.0, tk.END)
    for key in keys_generated:
        result_text.insert(tk.END, key + '\n')

root = tk.Tk()
root.title("Nitro Key Generator (by Vafls)")
root.geometry("800x600")  
root.resizable(False, False)  

label = tk.Label(root, text="Enter number of keys to generate:")
label.pack()

entry = tk.Entry(root)
entry.pack()

generate_button = tk.Button(root, text="Generate Keys", command=generate_keys)
generate_button.pack()

result_text = tk.Text(root, height=10, width=30)
result_text.pack()

root.mainloop()
