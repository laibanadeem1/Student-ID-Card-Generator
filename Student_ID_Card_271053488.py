import tkinter as tk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import inch
from tkinter import filedialog
from tkinter import messagebox
student_picture_path = ""
def image_uploader():
    global student_picture_path
    student_picture_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    if student_picture_path:
        print("Selected image: " + student_picture_path)
    return student_picture_path

def generate_card(name, rollnumber,major):
    if not student_picture_path:
        messagebox.showerror("Please select an image.")
        return

    my_path = 'my_pdf.pdf'
    c = canvas.Canvas(my_path, pagesize=(400, 300))
    c.setFont("Helvetica", 14)
    image_path = 'Back.png'
    c.drawImage(image_path, 0 * inch, 0 * inch, width=5.56 * inch, height=4.15 * inch)
    c.drawString(81, 150, str(name))
    c.drawString(81, 125, str(rollnumber))
    c.drawString(81, 100, str(major))
    c.drawImage(student_picture_path, 3 * inch, 0.5 * inch, width=1.75 * inch, height=2.25 * inch)
    c.showPage()
    c.save()

    messagebox.showinfo("Card generated!")

def user_input():
    ID_Card = tk.Tk()
    ID_Card.geometry("500x300")
    ID_Card.title("Student ID Card Generator")
    lable = tk.Label(ID_Card, text="Student ID card form", font=('Times New Roman', 18))
    lable.pack()

    input_frame = tk.Frame(ID_Card)
    input_frame.columnconfigure(0, weight=1)
    input_frame.columnconfigure(0, weight=1)
    #name
    namelabel = tk.Label(input_frame, text="Name:", font=('Times New Roman', 15))
    namelabel.grid(row=0, column=0, sticky=tk.W + tk.E)
    name = tk.Entry(input_frame)
    name.grid(row=0, column=1, sticky=tk.W + tk.E)
    #rollnumber
    rollnumberlabel = tk.Label(input_frame, text="Roll Number:", font=('Times New Roman', 15))
    rollnumberlabel.grid(row=1, column=0, sticky=tk.W + tk.E)
    rollnumber = tk.Entry(input_frame)
    rollnumber.grid(row=1, column=1, sticky=tk.W + tk.E)
    #major
    majorlabel = tk.Label(input_frame, text="Major:", font=('Times New Roman', 15))
    majorlabel.grid(row=2, column=0, sticky=tk.W + tk.E)
    major = tk.Entry(input_frame)
    major.grid(row=2, column=1, sticky=tk.W + tk.E)
    #image
    imagelabel = tk.Label(input_frame, text="Select Image:", font=('Times New Roman', 15))
    imagelabel.grid(row=3, column=0, sticky=tk.W + tk.E)
    image_button = tk.Button(input_frame, text="Upload", font=('Times New Roman', 13), command=image_uploader)
    image_button.grid(row=3, column=1, sticky=tk.W + tk.E)
    input_frame.pack(padx=20, pady=20)
    #button
    button = tk.Button(ID_Card, text="Submit", font=('Times New Roman', 15), command=lambda: generate_card(name.get(), rollnumber.get(), major.get()))
    button.pack(padx=10, pady=10)
    ID_Card.mainloop()

user_input()