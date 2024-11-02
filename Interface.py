import customtkinter as ctk
import sound_manager as sm
import time
import threading
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

sound_manager = sm.SoundManager()

def play_sound():
    sound_manager.playsound('./sounds/ca-ching.mp3')

root = ctk.CTk()
root.title("Repair Rush")
root.geometry("1280x720")

menu_ouvert = None

# Profil du joueur (élargi pour correspondre à la barre de progression)
profile_frame = ctk.CTkFrame(root, width=600, height=150, corner_radius=10, fg_color="#FFA500")
profile_frame.place(x=10, y=10)

# Ajout de l'image du joueur
image_path = "Images/qatari_boss.png"  # Assurez-vous que l'image est dans le dossier 'Images'
image = Image.open(image_path)  # Charger l'image
photo_de_profil = ctk.CTkImage(light_image=image, size=(80, 80))  # Création de l'image avec Pillow

# Affichage de l'image dans le label
profile_image_label = ctk.CTkLabel(profile_frame, text="", image=photo_de_profil)
profile_image_label.place(x=10, y=10)  # Positionner l'image

# Nom et entreprise
profile_label = ctk.CTkLabel(profile_frame, text="Mr Boss", font=("Arial", 16), text_color="black")
profile_label.place(x=100, y=10)
entreprise_label = ctk.CTkLabel(profile_frame, text="Boss International", font=("Arial", 10), text_color="black")
entreprise_label.place(x=100, y=40)

info_label = ctk.CTkLabel(profile_frame, text="Jour actuel\nArgent actuel\nRevenus par période\nCoûts fixes\nSolde net",
                          font=("Arial", 10), text_color="black")
info_label.place(x=100, y=70)

progress_bar = ctk.CTkProgressBar(root, width=600, height=30, progress_color='green')
progress_bar.place(x=10, y=170)

# Barre de progression
def update_progress_bar():
    while True:
        for i in range(3001):
            progress_bar.set(i / 3000)
            time.sleep(0.01)
        play_sound()
        progress_bar.set(0)

def start_progress():
    threading.Thread(target=update_progress_bar, daemon=True).start()

# Monnaie sélectionnée par défaut (euros)
selected_currency = "€"

# Menu déroulant pour sélectionner la monnaie
currency_options = ["€", "$", "£"]
currency_var = ctk.StringVar(value=selected_currency)

# Fonction pour mettre à jour la monnaie sélectionnée
def update_currency(choice):
    global selected_currency
    selected_currency = choice
    afficher_machines()  # Mettre à jour l'affichage des machines avec la nouvelle monnaie

scrollable_frame = ctk.CTkScrollableFrame(root, width=600, height=300, fg_color="#FF7F7F")
scrollable_frame.place(x=650, y=100)

# Fonction pour afficher les machines
def afficher_machines():
    global menu_ouvert
    menu_ouvert = 'machines'
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    machine_info = [
        {"Nom": "Machine 1", "Durée": "5 sec", "Apport": "$100", "Type": "X", "Prix": 100},
        {"Nom": "Machine 2", "Durée": "10 sec", "Apport": "$200", "Type": "X", "Prix": 200},
        {"Nom": "Machine 3", "Durée": "15 sec", "Apport": "$300", "Type": "X", "Prix": 300},
        {"Nom": "Machine 4", "Durée": "20 sec", "Apport": "$400", "Type": "X", "Prix": 400},
        {"Nom": "Machine 5", "Durée": "25 sec", "Apport": "$500", "Type": "X", "Prix": 500}
    ]
    for i, machine in enumerate(machine_info):
        machine_label = ctk.CTkLabel(scrollable_frame, text=f"{machine['Nom']} - {machine['Durée']} - {machine['Apport']} - {machine['Type']}")
        machine_label.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
        buy_button = ctk.CTkButton(scrollable_frame, text=f"Acheter ({machine['Prix']} {selected_currency})", width=100)
        buy_button.grid(row=i, column=1, padx=10, pady=5)

# Fonction pour afficher les techniciens
def afficher_techniciens():
    global menu_ouvert
    menu_ouvert = 'techniciens'
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    technician_info = [
        {"Nom": "Technicien 1", "Spécialité": "Mécanique", "Durée": "5 sec", "Salaire": "$100"},
        {"Nom": "Technicien 2", "Spécialité": "Électrique", "Durée": "10 sec", "Salaire": "$200"},
        {"Nom": "Technicien 3", "Spécialité": "Informatique", "Durée": "15 sec", "Salaire": "$300"},
        {"Nom": "Technicien 4", "Spécialité": "Mécanique", "Durée": "20 sec", "Salaire": "$400"},
        {"Nom": "Technicien 5", "Spécialité": "Électrique", "Durée": "25 sec", "Salaire": "$500"}
    ]
    for i, technician in enumerate(technician_info):
        technician_label = ctk.CTkLabel(scrollable_frame, text=f"{technician['Nom']} - {technician['Spécialité']} - {technician['Durée']} - {technician['Salaire']}")
        technician_label.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
        hire_button = ctk.CTkButton(scrollable_frame, text=f"Engager ({technician['Salaire']} {selected_currency})", width=100)
        hire_button.grid(row=i, column=1, padx=10, pady=5)

btn_machine = ctk.CTkButton(root, text="Machines", width=140, height=50, command=afficher_machines)
btn_machine.place(x=650, y=20)

btn_technicien = ctk.CTkButton(root, text="Techniciens", width=140, height=50, command=afficher_techniciens)
btn_technicien.place(x=800, y=20)

# --- PARAMÈTRES ---
def open_partie():
    options_frame.lift()
    partie_button.configure(fg_color="gray")
    son_button.configure(fg_color="#FFA500")
    profil_button.configure(fg_color="#FFA500")
    save_button.place(x=100, y=100)
    load_button.place(x=100, y=160)
    reset_button.place(x=100, y=220)
    music_label.place_forget()
    music_slider.place_forget()
    effects_label.place_forget()
    effects_slider.place_forget()
    name_label.place_forget()
    name_entry.place_forget()
    currency_label.place_forget()
    currency_dropdown.place_forget()

def open_son():
    options_frame.lift()
    partie_button.configure(fg_color="#FFA500")
    son_button.configure(fg_color="gray")
    profil_button.configure(fg_color="#FFA500")
    music_label.place(x=350, y=100)
    music_slider.place(x=350, y=140)
    effects_label.place(x=350, y=180)
    effects_slider.place(x=350, y=220)
    save_button.place_forget()
    load_button.place_forget()
    reset_button.place_forget()
    name_label.place_forget()
    name_entry.place_forget()
    currency_label.place_forget()
    currency_dropdown.place_forget()

def open_profil():
    options_frame.lift()
    partie_button.configure(fg_color="#FFA500")
    son_button.configure(fg_color="#FFA500")
    profil_button.configure(fg_color="gray")
    name_label.place(x=600, y=100)
    name_entry.place(x=600, y=140)
    currency_label.place(x=600, y=180)
    currency_dropdown.place(x=600, y=220)
    save_button.place_forget()
    load_button.place_forget()
    reset_button.place_forget()
    music_label.place_forget()
    music_slider.place_forget()
    effects_label.place_forget()
    effects_slider.place_forget()

# Fonction pour masquer l'interface principale du jeu
def hide_game_interface():
    profile_frame.place_forget()
    progress_bar.place_forget()
    scrollable_frame.place_forget()
    btn_machine.place_forget()
    btn_technicien.place_forget()
    options_button.place_forget()
    options_frame.place(x=0, y=0)

# Fonction pour afficher l'interface principale du jeu
def show_game_interface():
    profile_frame.place(x=10, y=10)
    progress_bar.place(x=10, y=170)
    btn_machine.place(x=650, y=20)
    btn_technicien.place(x=800, y=20)
    options_button.place(x=950, y=20)
    options_frame.place_forget()
    if menu_ouvert == 'machines':
        scrollable_frame.place(x=650, y=100)
        afficher_machines()
    elif menu_ouvert == 'techniciens':
        scrollable_frame.place(x=650, y=100)
        afficher_techniciens()

# Bouton pour ouvrir le menu des paramètres
options_button = ctk.CTkButton(root, text="⚙️", width=50, height=50, command=hide_game_interface)
options_button.place(x=950, y=20)

# Cadre des options (couvre toute la fenêtre)
options_frame = ctk.CTkFrame(root, width=1280, height=720, fg_color="#E8C36A")
options_frame.place_forget()

# Boutons pour les différentes sections des options (Partie, Son, Profil)
partie_button = ctk.CTkButton(options_frame, text="Partie", width=200, command=open_partie)
son_button = ctk.CTkButton(options_frame, text="Son", width=200, command=open_son)
profil_button = ctk.CTkButton(options_frame, text="Profil", width=200, command=open_profil)

# Position des boutons
partie_button.place(x=100, y=20)
son_button.place(x=350, y=20)
profil_button.place(x=600, y=20)

# Section Partie
save_button = ctk.CTkButton(options_frame, text="Sauvegarder")
load_button = ctk.CTkButton(options_frame, text="Charger une partie")
reset_button = ctk.CTkButton(options_frame, text="Réinitialiser la partie")

# Section Son
music_label = ctk.CTkLabel(options_frame, text="Musique")
music_slider = ctk.CTkSlider(options_frame)
effects_label = ctk.CTkLabel(options_frame, text="Effets Sonores")
effects_slider = ctk.CTkSlider(options_frame)

# Section Profil
name_label = ctk.CTkLabel(options_frame, text="Nom:")
name_entry = ctk.CTkEntry(options_frame)
currency_label = ctk.CTkLabel(options_frame, text="Monnaie:")
currency_dropdown = ctk.CTkComboBox(options_frame, values=currency_options, command=update_currency, variable=currency_var)

# Bouton retour
back_button = ctk.CTkButton(options_frame, text="←", width=50, command=show_game_interface)
back_button.place(x=1200, y=20)

# Lancer la barre de progression
start_progress()
afficher_machines()  # Afficher les machines au démarrage
root.mainloop()