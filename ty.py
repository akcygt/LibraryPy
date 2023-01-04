from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import filedialog
import ftplib
import os
import uuid
import shutil

# MySQL connection
mydb = mysql.connector.connect(
  host="your_server",
  user="your_user",
  password="your_password",
  database="your_dbname"
)

# Tkinter window
root = Tk()
root.title("Book Form")
root.geometry("600x600")

# Form fields
lbl_book_name = Label(root, text="Book Name:")
lbl_book_description = Label(root, text="Book Description:")
lbl_book_author = Label(root, text="Book Author:")
lbl_book_image = Label(root, text="Book Image:")

# Position form fields
lbl_book_name.grid(row=0, column=0)
lbl_book_description.grid(row=1, column=0)
lbl_book_author.grid(row=2, column=0)
lbl_book_image.grid(row=3, column=0)

# Create form fields
entry_book_name = Entry(root)
entry_book_description = Text(root, height=5, width=30)
entry_book_author = Entry(root)
entry_book_image = Entry(root)

# Position form fields
entry_book_name.grid(row=0, column=1, padx=10, pady=10)
entry_book_description.grid(row=1, column=1, padx=10, pady=10)
entry_book_author.grid(row=2, column=1, padx=10, pady=10)
entry_book_image.grid(row=3, column=1, padx=10, pady=10)

# Create file upload button
btn_upload = Button(root, text="Upload File", font=("Arial", 14))
def upload_file():
  # Open file selection window
  file = filedialog.askopenfile(title="Select a file")

  # Get file name and extension
  file_name, file_extension = os.path.splitext(file.name)

  # Generate random file name
  new_file_name = uuid.uuid4().hex + file_extension

  # Connect to FTP server
  ftp = ftplib.FTP("your_ftpip")
  ftp.login("yourftp_user", "yourftp_password")

  # Change current directory to /images
  ftp.cwd("/images")

  # Open file in binary mode
  with open(file.name, "rb") as f:
    # Upload file to FTP server
    ftp.storbinary("STOR " + new_file_name, f)

  # Close FTP connection
  ftp.quit()

  # Write file name to form field
  entry_book_image.insert(0, new_file_name)

# Call upload_file() function when file upload button is clicked
btn_upload.configure(command=upload_file)

# Position file upload button
btn_upload.grid(row=3, column=2, padx=10, pady=10)

# Create button to add book to database
btn_submit = Button(root, text="Add Book", font=("Arial", 14))

# Add book to database
def add_book():
  # Get form field values
  book_name = entry_book_name.get()
  book_description = entry_book_description.get("1.0", "end-1c")
  book_author = entry_book_author.get()
  book_image = entry_book_image.get()

  # Create cursor for MySQL operations
  mycursor = mydb.cursor()

  # Add book to database
  sql = "INSERT INTO books (name, description, author, image) VALUES (%s, %s, %s, %s)"
  val = (book_name, book_description, book_author, book_image)
  mycursor.execute(sql, val)

  # Commit changes to database
  mydb.commit()

# Call add_book() function when add book button is clicked
btn_submit.configure(command=add_book)

# Position add book button
btn_submit.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()