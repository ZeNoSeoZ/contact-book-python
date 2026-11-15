import json

print("===== Kontakt kitabçası =====")

try:
    with open("kontaktlar.json", "r", encoding="utf-8") as file:
        contacts = json.load(file)

except FileNotFoundError:
    contacts = {}

except json.JSONDecodeError:
    contacts = {}

def save_contacts(contacts):
    with open("kontaktlar.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii = False, indent = 4)

def add_contact(contacts):
    name = input("Ad əlavə edin: ")
    number = input("Nömrə əlavə edin: ").strip()
    if name == "" or number == "":
        print("Ad və nömrə boş ola bilməz!")
    elif number in contacts:
        print("Bu nömrə kontaktda var:", contacts[number])
      
    else:
        contacts[number] = name
        save_contacts(contacts)
        print(name, "əlavə edildi!")

def update_name(contacts):
    number = input("Dəyişmək istədiyiniz adın nömrəsini daxil edin: ").strip()
    if number in contacts:
        name = input("Ad daxil edin: ")
        if name != "":
            old_name = contacts[number]
            contacts[number] = name
            save_contacts(contacts)
            print("Dəyişdirildi:", old_name)
            print("Yeni ad:", name)
        else:
            print("Ad boş ola bilməz!")
    else:
        print("Bu nömrə kontaktlarda mövcud deyil.")

def delete_contact(contacts):
    number = input("Silmək istədiyiniz nömrə: ").strip()
    if number in contacts:
        name = contacts[number]
        print("Silindi:", name)
        del contacts[number]
        save_contacts(contacts)

    else:
        print("Tapılmadı")

def search_contact(contacts):
    number = input("Nömrə axtarın: ").strip()
    if number in contacts:
        name = contacts[number]
        print("Tapıldı:", name)
    else:
        print("Tapılmadı")
    
def show_all(contacts):
    if not contacts:
        print("Kontakt yoxdur")
    else:
        for number, name in contacts.items():
            print("Ad:",name,"-","Nömrə:",number)


while True:

    print("\n1. Əlavə et")
    print("2. Adı yenilə")
    print("3. Sil")
    print("4. Axtar")
    print("5. Kontaktlar")
    print("6. Çıxış")

    choice = input("Seçiminizi daxil edin (1-6): ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        update_name(contacts)

    elif choice == "3":
        delete_contact(contacts)

    elif choice == "4":
       search_contact(contacts)

    elif choice == "5":
        show_all(contacts)

    elif choice == "6":
        print("Proqramdan çıxılır...")
        break

    else:
        print("Yanlış seçim!\n")