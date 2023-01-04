from tkinter import *
import mysql.connector

# MySQL bağlantısı
mydb = mysql.connector.connect(
  host="your_server",
  user="your_user",
  password="your_password",
  database="your_database"
)

# Tkinter penceresi
root = Tk()
root.title("Üyelik Yönetimi")
root.geometry("600x600")

# Üye ekleme alanlarını oluşturun
lbl_username = Label(root, text="Kullanıcı Adı:")
lbl_password = Label(root, text="Parola:")
lbl_name = Label(root, text="Adı Soyadı:")
lbl_email = Label(root, text="E-posta:")

lbl_username.grid(row=0, column=0)
lbl_password.grid(row=1, column=0)
lbl_name.grid(row=2, column=0)
lbl_email.grid(row=3, column=0)

entry_username = Entry(root)
entry_password = Entry(root, show="*")
entry_name = Entry(root)
entry_email = Entry(root)

entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
entry_name.grid(row=2, column=1, padx=10, pady=10)
entry_email.grid(row=3, column=1, padx=10, pady=10)

# Üyelik bilgilerini veritabanına ekleme düğmesini oluşturun
btn_submit = Button(root, text="Üyeyi Ekle", font=("Arial", 12), bg="lightgreen")
btn_submit.grid(row=4, column=1, padx=10, pady=10)

# Üyelik bilgileri
def add_member():
  username = entry_username.get()
  password = entry_password.get()
  name = entry_name.get()
  email = entry_email.get()


  mycursor = mydb.cursor()

  
  sql = "INSERT INTO members (username, password, name, email) VALUES (%s, %s, %s, %s)"
  val = (username, password, name, email)
  mycursor.execute(sql, val)

    
  mydb.commit()

 
  lbl_status = Label(root, text="Üye başarıyla eklendi!", font=("Arial", 12), fg="green")
  lbl_status.grid(row=5, column=1)

# Üyelik bilgilerini ekleme düğmesine tıklandığında add_member() fonksiyonunu çağırın
btn_submit.configure(command=add_member)

# Üyelik güncelleme alanlarını oluşturun
lbl_update_id = Label(root, text="Güncellenecek Üyenin ID'si:", font=("Arial", 12))
lbl_update_username = Label(root, text="Yeni Kullanıcı Adı:", font=("Arial", 12))
lbl_update_password = Label(root, text="Yeni Parola:", font=("Arial", 12))
lbl_update_name = Label(root, text="Yeni Adı Soyadı:", font=("Arial", 12))
lbl_update_email = Label(root, text="Yeni E-posta:", font=("Arial", 12))

lbl_update_id.grid(row=6, column=0)
lbl_update_username.grid(row=7, column=0)
lbl_update_password.grid(row=8, column=0)
lbl_update_name.grid(row=9, column=0)
lbl_update_email.grid(row=10, column=0)

entry_update_id = Entry(root)
entry_update_username = Entry(root)
entry_update_password = Entry(root, show="*")
entry_update_name = Entry(root)
entry_update_email = Entry(root)

entry_update_id.grid(row=6, column=1, padx=10, pady=10)
entry_update_username.grid(row=7, column=1, padx=10, pady=10)
entry_update_password.grid(row=8, column=1, padx=10, pady=10)
entry_update_name.grid(row=9, column=1, padx=10, pady=10)
entry_update_email.grid(row=10, column=1, padx=10, pady=10)

# Üyelik bilgilerini güncelleme düğmesini oluşturun
btn_update = Button(root, text="Üyeyi Güncelle", font=("Arial", 12), bg="lightblue")
btn_update.grid(row=11, column=1, padx=10, pady=10)

# Üyelik bilgilerini güncelleme işlemini gerçekleştirin
def update_member():
  update_id = entry_update_id.get()
  update_username = entry_update_username.get()
  update_password = entry_update_password.get()
  update_name = entry_update_name.get()
  update_email = entry_update_email.get()

  # MySQL işlemleri için bir imleç oluşturun
  mycursor = mydb.cursor()
 # Üyelik bilgilerini güncelleyin
  sql = "UPDATE members SET username=%s, password=%s, name=%s, email=%s WHERE id=%s"
  val = (update_username, update_password, update_name, update_email, update_id)
  mycursor.execute(sql, val)

 
  mydb.commit()

  # Başarılı bir şekilde güncellendiyse kullanıcıyı bilgilendirin
  lbl_status = Label(root, text="Üye başarıyla güncellendi!", font=("Arial", 12), fg="blue")
  lbl_status.grid(row=12, column=1)

# Üyelik bilgilerini güncelleme düğmesine tıklandığında update_member() fonksiyonunu çağırın
btn_update.configure(command=update_member)

# Üyelik silme alanlarını oluşturun
lbl_delete_id = Label(root, text="Silinecek Üyenin ID'si:", font=("Arial", 12))
lbl_delete_id.grid(row=13, column=0)

entry_delete_id = Entry(root)
entry_delete_id.grid(row=13, column=1, padx=10, pady=10)

# Üyelik bilgilerini silme düğmesini oluşturun
btn_delete = Button(root, text="Üyeyi Sil", font=("Arial", 12), bg="red", fg="white")
btn_delete.grid(row=14, column=1, padx=10, pady=10)

# Üyelik bilgilerini silme işlemini gerçekleştirin
def delete_member():
  delete_id = entry_delete_id.get()

  # MySQL işlemleri için bir imleç oluşturun
  mycursor = mydb.cursor()

  # Üyelik bilgilerini silin
  sql = "DELETE FROM members WHERE id=%s"
  val = (delete_id,)
  mycursor.execute(sql, val)

  # Veritabanında değişiklikleri kaydedin
  mydb.commit()

  # Başarılı bir şekilde silindiyse kullanıcıyı bilgilendirin
  lbl_status = Label(root, text="Üye başarıyla silindi!", font=("Arial", 12), fg="red")
  lbl_status.grid(row=15, column=1)

# Üyelik bilgilerini silme düğmesine tıklandığında delete_member() fonksiyonunu çağırın
btn_delete.configure(command=delete_member)


# MySQL işlemleri için bir imleç oluşturun
mycursor = mydb.cursor()



root.mainloop()