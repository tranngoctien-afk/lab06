import tkinter as tk

# Define the function for the "Pause" button
def pause_recording():
    status_label.config(text="Recording Paused")

# Define the function for the "Start" button
def start_recording():
    status_label.config(text="Recording Started")

# Define the function for the "End" button
def end_recording():
    status_label.config(text="Recording Ended")

def create_window():
    window = tk.Tk()
    window.title("Frame Recorder")
    window.geometry("600x300")
    window.configure(bg='lightpink')
    
    # Title label
    title_label = tk.Label(window, text="Frame Recorder", font=("Arial", 24), bg='lightpink')
    title_label.pack(pady=10)
    
    # FPS input
    fps_frame = tk.Frame(window, bg='lightpink')
    fps_label = tk.Label(fps_frame, text="create an", font=("Arial", 14), bg='lightpink')
    fps_label.pack(side=tk.LEFT)
    fps_entry = tk.Entry(fps_frame, font=("Arial", 14))
    fps_entry.pack(side=tk.LEFT, padx=5)
    fps_label_2 = tk.Label(fps_frame, text="fps video", font=("Arial", 14), bg='lightpink')
    fps_label_2.pack(side=tk.LEFT)
    fps_frame.pack(pady=10)
    
    # Buttons
    button_frame = tk.Frame(window, bg='lightpink')
    pause_button = tk.Button(button_frame, text="Pause", font=("Arial", 14), command=pause_recording)
    pause_button.pack(side=tk.LEFT, padx=10)
    start_button = tk.Button(button_frame, text="Start", font=("Arial", 14), command=start_recording)
    start_button.pack(side=tk.LEFT, padx=10)
    end_button = tk.Button(button_frame, text="End", font=("Arial", 14), command=end_recording)
    end_button.pack(side=tk.LEFT, padx=10)
    button_frame.pack(pady=10)
    
    # Status label
    global status_label
    status_label = tk.Label(window, text="Recording Paused", font=("Arial", 14), bg='lightpink')
    status_label.pack(pady=10)
    
    window.mainloop()

create_window()