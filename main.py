import customtkinter as ctk
from tkinter import messagebox, simpledialog
from datetime import date, datetime
from tkcalendar import Calendar

# ================= SETTINGS =================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ================= APP =================

app = ctk.CTk()
app.geometry("1400x800")
app.title("Ultimate Todo App")

# ================= TASK STORAGE =================

tasks = []

# ================= MAIN FRAMES =================

sidebar = ctk.CTkFrame(
    app,
    width=250,
    corner_radius=0,
    fg_color="#111827"
)

sidebar.pack(side="left", fill="y")

content_frame = ctk.CTkFrame(
app,
fg_color="#1f2937"
)

content_frame.pack(
side="right",
fill="both",
expand=True
)

# ================= CLEAR PAGE =================

def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

# ================= DASHBOARD =================

def dashboard_page():
    clear_content()

    title = ctk.CTkLabel(
        content_frame,
        text="Dashboard",
        font=("Arial", 35, "bold")
    )

    title.pack(pady=30)

    total_tasks = len(tasks)

    completed_tasks = 0
    pending_tasks = 0

    for task in tasks:
        if task.get("status") == "Completed":
            completed_tasks += 1
        else:
            pending_tasks += 1

    productivity = 0

    if total_tasks > 0:
        productivity = int((completed_tasks / total_tasks) * 100)
    else:
        productivity = 0

    cards_frame = ctk.CTkFrame(
        content_frame,
        fg_color="transparent"
    )

    cards_frame.pack(pady=20)

    def create_card(name, value, color):
        card = ctk.CTkFrame(
            cards_frame,
            width=220,
            height=140,
            fg_color=color,
            corner_radius=20
        )

        card.pack(side="left", padx=20)

        label1 = ctk.CTkLabel(
            card,
            text=name,
            font=("Arial", 20, "bold")
        )

        label1.pack(pady=(25, 10))

        label2 = ctk.CTkLabel(
            card,
            text=str(value),
            font=("Arial", 40, "bold")
        )

        label2.pack()

    create_card(
        "📋 Total Tasks",
        total_tasks,
        "#2563eb"
    )

    create_card(
        "✅ Completed",
        completed_tasks,
        "#16a34a"
    )

    create_card(
        "⏳ Pending",
        pending_tasks,
        "#dc2626"
    )

    create_card(
        "🔥 Productivity",
        f"{productivity}%",
        "#9333ea"
    )

# ================= TASK PAGE =================

def task_page():
    clear_content()

    # expose these widgets to other functions (e.g., add_task)
    global task_entry, date_entry, time_entry, task_container

    title = ctk.CTkLabel(
        content_frame,
        text="Task Manager",
        font=("Arial", 35, "bold")
    )

    title.pack(pady=20)

    input_frame = ctk.CTkFrame(content_frame)

    input_frame.pack(
        padx=20,
        pady=20,
        fill="x"
    )

    task_entry = ctk.CTkEntry(
        input_frame,
        placeholder_text="Enter Task",
        width=300,
        height=45
    )

    task_entry.grid(row=0, column=0, padx=10, pady=20)

    date_entry = ctk.CTkEntry(
        input_frame,
        placeholder_text="Due Date",
        width=200,
        height=45
    )

    date_entry.grid(row=0, column=1, padx=10)

    time_entry = ctk.CTkEntry(
        input_frame,
        placeholder_text="Due Time",
        width=200,
        height=45
    )

    time_entry.grid(row=0, column=2, padx=10)
    add_btn = ctk.CTkButton(  
        input_frame,  
        text="Add Task",  
        width=150,  
        height=45,  
        command=add_task  
    )  

    add_btn.grid(row=0, column=3, padx=10)


    task_container = ctk.CTkScrollableFrame(
        content_frame
    )

    task_container.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

def get_icon(task):  

    task = task.lower()  

    if "study" in task:  
        return "📚"  

    elif "code" in task:  
        return "💻"  

    elif "gym" in task:  
        return "🏋"  

    elif "buy" in task:  
        return "🛒"  

    else:  
        return "✅"  

def add_task():  

    task = task_entry.get()  
    date = date_entry.get().strip()  
    time = time_entry.get().strip()  

    if not date or not time:  
        messagebox.showerror("Error", "Please enter Due Date and Time")  
        return  

    try:  
        due_datetime = datetime.strptime(f"{date} {time}", "%d-%m-%Y %H:%M")  
    except Exception:  
        messagebox.showerror("Error", "Format must be DD-MM-YYYY and HH:MM")  
        return  

    if task == "":  
        messagebox.showerror(  
            "Error",  
            "Please Enter Task"  
        )  
        return  

    task_data = {  
        "task": task,  
        "status": "Pending"  
    }  

    tasks.append(task_data)  

    icon = get_icon(task)  

    current_time = datetime.now().strftime(  
        "%d-%m-%Y %H:%M"  
    )  

    task_card = ctk.CTkFrame(  
        task_container,  
        corner_radius=15  
    )  

    task_card.pack(  
        fill="x",  
        pady=10,  
        padx=10  
    )  

    task_title = ctk.CTkLabel(  
        task_card,  
        text=f"{icon} {task}",  
        font=("Arial", 22, "bold")  
    )  

    task_title.pack(  
        anchor="w",  
        padx=20,  
        pady=(10, 0)  
    )  

    details = ctk.CTkLabel(  
        task_card,  
        text=f"Due: {date} | {time}",  
        font=("Arial", 15)  
    )  

    details.pack(  
        anchor="w",  
        padx=20  
    )  

    created = ctk.CTkLabel(  
        task_card,  
        text=f"Created: {current_time}",  
        text_color="gray"  
    )  

    created.pack(  
        anchor="w",  
        padx=20  
    )  

    status = ctk.CTkLabel(  
        task_card,  
        text="Pending",  
        text_color="orange",  
        font=("Arial", 15, "bold")  
    )  

    status.pack(  
        anchor="w",  
        padx=20,  
        pady=(0, 10)  
    )  

    button_frame = ctk.CTkFrame(  
        task_card,  
        fg_color="transparent"  
    )  

    button_frame.pack(  
        anchor="e",  
        padx=20,  
        pady=10  
    )  

    # COMPLETE TASK  

    def complete_task():  

        status.configure(  
            text="Completed",  
            text_color="lightgreen"  
        )  

        task_data["status"] = "Completed"  

        dashboard_page()
          

    # DELETE TASK  

    def delete_task():  

        if task_data in tasks:  
            tasks.remove(task_data)  

        task_card.destroy()  

    # UPDATE TASK  
    def update_task():
        new_text = simpledialog.askstring("Update Task", "Enter new task")
        if new_text and new_text.strip() != "":
            new_icon = get_icon(new_text)
            task_title.configure(text=f"{new_icon} {new_text}")
            task_data["task"] = new_text

    # BUTTONS  

    complete_btn = ctk.CTkButton(  
        button_frame,  
        text="Complete",  
        width=100,  
        command=complete_task  
    )  

    complete_btn.pack(side="left", padx=5)  

    update_btn = ctk.CTkButton(  
        button_frame,  
        text="Update",  
        width=100,  
        fg_color="orange",  
        command=update_task  
    )  

    update_btn.pack(side="left", padx=5)  

    delete_btn = ctk.CTkButton(  
        button_frame,  
        text="Delete",  
        width=100,  
        fg_color="red",  
        command=delete_task  
    )  

    delete_btn.pack(side="left", padx=5)  

    task_entry.delete(0, "end")  
    date_entry.delete(0, "end")  
    time_entry.delete(0, "end")  



# ================= CALENDAR PAGE =================

def calendar_page():
    clear_content()

    title = ctk.CTkLabel(
        content_frame,
        text="Task Calendar",
        font=("Arial", 35, "bold")
    )

    title.pack(pady=20)

    calendar_frame = ctk.CTkFrame(
        content_frame,
        corner_radius=20
    )

    calendar_frame.pack(
        padx=20,
        pady=20,
        fill="both",
        expand=True
    )

    cal = Calendar(
        calendar_frame,
        selectmode="day",
        date_pattern="dd-mm-yyyy"
    )

    cal.pack(
        pady=20,
        padx=20,
        fill="both",
        expand=True
    )

    selected_date_label = ctk.CTkLabel(
        calendar_frame,
        text="Selected Date:",
        font=("Arial", 22, "bold")
    )

    selected_date_label.pack(pady=20)

    def get_date():
        selected_date = cal.get_date()
        selected_date_label.configure(
            text=f"Selected Date: {selected_date}"
        )

    select_btn = ctk.CTkButton(
        calendar_frame,
        text="Get Selected Date",
        width=200,
        height=45,
        command=get_date
    )

    select_btn.pack(pady=20)

def check_alaram():
    now = datetime.now()
    for task in tasks:
        if task.get("status") == "Pending":
            try:
                due_date = datetime.strptime(task.get("due_date",""), "%d-%m-%Y %H:%M")
            except:
                continue
            if now >= due_date:
                messagebox.showinfo("Task Due", f"{task['task']} is due now!")

# ================= ANALYTICS PAGE =================

def analytics_page():
    clear_content()

    title = ctk.CTkLabel(
        content_frame,
        text="Analytics",
        font=("Arial", 35, "bold")
    )

    title.pack(pady=30)

    total_tasks = len(tasks)

    completed = 0

    for task in tasks:
        if task.get("status") == "Completed":
            completed += 1

    pending = total_tasks - completed

    analytics_text = f"""

Total Tasks : {total_tasks}

Completed Tasks : {completed}

Pending Tasks : {pending}
"""

    label = ctk.CTkLabel(
        content_frame,
        text=analytics_text,
        font=("Arial", 25)
    )

    label.pack(pady=50)

# ================= SETTINGS PAGE =================

def settings_page():
    clear_content()

    title = ctk.CTkLabel(
        content_frame,
        text="Settings",
        font=("Arial", 35, "bold")
    )

    title.pack(pady=30)

    def dark_mode():
        ctk.set_appearance_mode("dark")

    def light_mode():
        ctk.set_appearance_mode("light")

    dark_btn = ctk.CTkButton(
        content_frame,
        text="Dark Mode",
        width=220,
        height=55,
        command=dark_mode
    )

    dark_btn.pack(pady=20)

    light_btn = ctk.CTkButton(
        content_frame,
        text="Light Mode",
        width=220,
        height=55,
        command=light_mode
    )

    light_btn.pack(pady=20)

# ================= SIDEBAR =================

logo = ctk.CTkLabel(
sidebar,
text="⚡ Ultimate Todo",
font=("Arial", 28, "bold")
)

logo.pack(pady=40)

dashboard_btn = ctk.CTkButton(
sidebar,
text="🏠 Dashboard",
height=50,
command=dashboard_page
)

dashboard_btn.pack(
pady=10,
padx=20,
fill="x"
)

tasks_btn = ctk.CTkButton(
sidebar,
text="📝 Tasks",
height=50,
command=task_page
)

tasks_btn.pack(
pady=10,
padx=20,
fill="x"
)

calendar_btn = ctk.CTkButton(
sidebar,
text="📅 Calendar",
height=50,
command=calendar_page
)

calendar_btn.pack(
pady=10,
padx=20,
fill="x"
)

analytics_btn = ctk.CTkButton(
sidebar,
text="📊 Analytics",
height=50,
command=analytics_page
)

analytics_btn.pack(
pady=10,
padx=20,
fill="x"
)

settings_btn = ctk.CTkButton(
sidebar,
text="⚙ Settings",
height=50,
command=settings_page
)

settings_btn.pack(
pady=10,
padx=20,
fill="x"
)

# ================= DEFAULT PAGE =================

dashboard_page()

# ================= RUN APP =================

app.mainloop()
