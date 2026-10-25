import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk

from PIL import Image, ImageTk
import numpy as np

from edges import detect_contours
from segmentation import simple_segmentation
from utilis import rgb_to_grayscale
from filters import gaussian_blur, median_filter

def charger_image():
    global img_path, img_original, img_display
    file_path = filedialog.askopenfilename(
        title="Choisir une image",
        filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp")]
    )
    if file_path:
        img_path = file_path
        img_original = Image.open(file_path)
        img_display = img_original.copy()
        afficher_image(img_display, canvas_original)

def afficher_image(image, canvas):
    w, h = 750, 400  
    img_resized = image.resize((w, h))
    img_tk = ImageTk.PhotoImage(img_resized)
    canvas.image = img_tk
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

def appliquer_contours():
    global img_display
    if not img_original: 
        return

    root.config(cursor="watch")
    root.update()
    img_gray = rgb_to_grayscale(img_original)
   
    img_filtered = median_filter(img_gray, kernel_size=3)
    img_display = detect_contours(img_filtered)

    afficher_image(img_display, canvas_resultat)
    root.config(cursor="")
    messagebox.showinfo("Info", "Traitement des contours terminé.")

def appliquer_segmentation():
    global img_display
    if not img_original: 
        return

    root.config(cursor="watch")
    root.update()

    img_display = simple_segmentation(img_original)
    afficher_image(img_display, canvas_resultat)

    root.config(cursor="")
    messagebox.showinfo("Info", "Segmentation Otsu terminée.")

def sauvegarder_image():
    if not img_display:
        messagebox.showerror("Erreur", "Aucune image à sauvegarder.")
        return
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")],
        title="Sauvegarder l'image"
    )
    if save_path:
        img_display.save(save_path)
        messagebox.showinfo("Succès", "Image sauvegardée avec succès !")

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Détection de Contours et Segmentation")
root.geometry("1150x700") 
root.resizable(True, True)

img_path = ""
img_original = None
img_display = None

frame_gauche = ctk.CTkFrame(root, width=300, corner_radius=15, fg_color="#2b2b2b")
frame_gauche.pack(side="left", padx=10, pady=10, fill="y")

title_label = ctk.CTkLabel(frame_gauche, text="Actions", font=("Arial", 22, "bold"), text_color="white")
title_label.pack(pady=30)

button_color = "#5f2c82"
button_hover = "#49a09d"

btn_params = {
    "font": ("Arial", 14, "bold"),
    "fg_color": button_color,
    "hover_color": button_hover,
    "corner_radius": 20,
    "height": 50
}

btn_charger = ctk.CTkButton(frame_gauche, text="Charger Image", command=charger_image, **btn_params)
btn_charger.pack(pady=15, padx=20, fill='x')

btn_contours = ctk.CTkButton(frame_gauche, text="Détecter Contours", command=appliquer_contours, **btn_params)
btn_contours.pack(pady=15, padx=20, fill='x')

btn_segmentation = ctk.CTkButton(frame_gauche, text="Segmenter Image", command=appliquer_segmentation, **btn_params)
btn_segmentation.pack(pady=15, padx=20, fill='x')

btn_sauvegarder = ctk.CTkButton(frame_gauche, text="Sauvegarder Image", command=sauvegarder_image, **btn_params)
btn_sauvegarder.pack(pady=40, padx=20, fill='x')

frame_droite = ctk.CTkScrollableFrame(root, width=800, corner_radius=15, fg_color="#2b2b2b")
frame_droite.pack(side="right", padx=10, pady=10, fill="both", expand=True)

label_original = ctk.CTkLabel(frame_droite, text="Image Originale", font=("Arial", 18, "bold"), text_color="#ecf0f1")
label_original.pack(pady=(10, 5))

canvas_original = tk.Canvas(frame_droite, width=750, height=400, bg="#ECE9E6", highlightthickness=0)
canvas_original.pack(pady=10)

label_resultat = ctk.CTkLabel(frame_droite, text="Image Résultante", font=("Arial", 18, "bold"), text_color="#ecf0f1")
label_resultat.pack(pady=(20, 5))

canvas_resultat = tk.Canvas(frame_droite, width=750, height=400, bg="#ECE9E6", highlightthickness=0)
canvas_resultat.pack(pady=10)

root.mainloop()
