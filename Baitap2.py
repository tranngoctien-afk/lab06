import tkinter as tk

# Define the functions for the buttons
def quick_scan():
    status_label.config(text="Quick Scan Started")

def web_protection():
    status_label.config(text="Web Protection Enabled")

def quarantine():
    status_label.config(text="Quarantine Activated")

def full_scan():
    status_label.config(text="Full Scan Started")

def simple_update():
    status_label.config(text="Simple Update Started")

def scan_now():
    status_label.config(text="Scan Now Started")

def create_window():
    window = tk.Tk()
    window.title("AtarBals Modern Antivirus")
    window.geometry("800x500")
    window.configure(bg='white')
    
    # Main frame
    main_frame = tk.Frame(window, bg='white')
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Sidebar
    sidebar = tk.Frame(main_frame, bg='blue', width=200)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)
    
    # Sidebar labels and button
    sidebar_labels = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
    for label_text in sidebar_labels:
        label = tk.Label(sidebar, text=label_text, font=("Arial", 14), bg='blue', fg='white', anchor='w', padx=20)
        label.pack(fill=tk.X, pady=5)
    
    scan_now_button = tk.Button(sidebar, text="Scan Now", font=("Arial", 14), bg='green', fg='white', command=scan_now)
    scan_now_button.pack(pady=20, padx=20, fill=tk.X)
    
    # Main content area
    content_area = tk.Frame(main_frame, bg='white')
    content_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    # Title and subtitle
    title_label = tk.Label(content_area, text="Scan", font=("Arial", 24), bg='white')
    title_label.pack(pady=10)
    subtitle_label = tk.Label(content_area, text="Premium will be free forever. You just need to click button.", font=("Arial", 14), bg='white')
    subtitle_label.pack(pady=5)
    
    # Function buttons
    button_texts = [("Quick Scan", quick_scan), ("Web Protection", web_protection), 
                    ("Quarantine", quarantine), ("Full Scan", full_scan), 
                    ("Simple Update", simple_update)]
    
    for text, command in button_texts:
        button = tk.Button(content_area, text=text, font=("Arial", 14), bg='magenta', fg='black', command=command)
        button.pack(pady=5)
    
    # Status label
    global status_label
    status_label = tk.Label(content_area, text="Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}", font=("Arial", 14), bg='white', fg='red')
    status_label.pack(pady=20)
    
    window.mainloop()

create_window()