import tkinter as tk
from tkinter import scrolledtext, Text

def copy_to_clipboard(header, text, button):
    full_text = header + "\n" + text
    root.clipboard_clear()
    root.clipboard_append(full_text)
    root.update()  # Keeps the clipboard contents even after the program exits
    button.config(text="Copied!", bg="light green")

def process_and_display_text():
    input_text = input_text_area.get("1.0", tk.END)
    lines = input_text.split("\n")

    # Clear existing frames
    for widget in output_canvas_frame.winfo_children():
        widget.destroy()

    for i in range(0, len(lines), 60):
        segment = lines[i:i+60]
        header = "Translate into Arabic with the same structure:\n"
        segment_text = "\n".join(segment)

        # Create a new frame for each segment
        frame = tk.Frame(output_canvas_frame, borderwidth=2, relief="groove")
        frame.pack(padx=10, pady=5, fill=tk.X)

        label = tk.Label(frame, text=header, fg="blue")
        label.pack(side=tk.TOP, fill=tk.X)

        text_area = Text(frame, height=5, width=40)
        text_area.insert(tk.INSERT, segment_text)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_area.configure(state='disabled')  # Make the text area read-only

        # Define the copy button
        copy_button = tk.Button(frame, text="Copy", bg="light gray")
        copy_button.config(command=lambda h=header, t=segment_text, b=copy_button: copy_to_clipboard(h, t, b))
        copy_button.pack(side=tk.RIGHT, padx=10)

# Set up the main window
root = tk.Tk()
root.title("Text Processor")

# Create a text input area
input_text_area = scrolledtext.ScrolledText(root, height=10)
input_text_area.pack(pady=10)

# Create a button to process text
process_button = tk.Button(root, text="Process Text", command=process_and_display_text)
process_button.pack(pady=10)

# Create a scrollable frame to hold output segments
output_scrollbar = tk.Scrollbar(root)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_canvas = tk.Canvas(root, yscrollcommand=output_scrollbar.set)
output_scrollbar.config(command=output_canvas.yview)
output_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

output_canvas_frame = tk.Frame(output_canvas)
output_canvas.create_window((0, 0), window=output_canvas_frame, anchor="nw")

def on_frame_configure(event):
    output_canvas.configure(scrollregion=output_canvas.bbox("all"))

output_canvas_frame.bind("<Configure>", on_frame_configure)

# Run the application
root.mainloop()
