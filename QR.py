import qrcode

print("=== GENERADOR DE CÓDIGOS QR ===\n")

# 1. Pedir enlace
enlace = input("Ingresá el enlace para generar el QR: ")

# 2. Nombre del archivo
nombre_archivo = input("Nombre del archivo (sin .png): ")
if nombre_archivo.strip() == "":
    nombre_archivo = "codigo_qr"

# 3. Menú de diseños
print("\nSeleccioná el diseño:")
print("1  - Clásico (negro sobre blanco)")
print("2  - Azul moderno")
print("3  - Verde")
print("4  - Rojo")
print("5  - Morado")
print("6  - Naranja")
print("7  - Gris")
print("8  - Celeste")
print("9  - Amarillo")
print("10 - Invertido (blanco sobre negro)")
print("11 - Negro sobre amarillo")
print("12 - Blanco sobre azul oscuro")

opcion = input("\nOpción (1-12): ")

# 4. Diseños con colores HEX
diseños = {
    "1": ("#000000", "#FFFFFF"),
    "2": ("#1DA1F2", "#FFFFFF"),
    "3": ("#2ECC71", "#FFFFFF"),
    "4": ("#E74C3C", "#FFFFFF"),
    "5": ("#9B59B6", "#FFFFFF"),
    "6": ("#E67E22", "#FFFFFF"),
    "7": ("#7F8C8D", "#FFFFFF"),
    "8": ("#00BCD4", "#FFFFFF"),
    "9": ("#F1C40F", "#000000"),
    "10": ("#FFFFFF", "#000000"),
    "11": ("#000000", "#F1C40F"),
    "12": ("#FFFFFF", "#0A1AFF")
}

# Si elige mal, usa diseño clásico
color_qr, color_fondo = diseños.get(opcion, ("#000000", "#FFFFFF"))

# 5. Crear QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(enlace)
qr.make(fit=True)

imagen = qr.make_image(
    fill_color=color_qr,
    back_color=color_fondo
)

# 6. Guardar y mostrar
archivo_final = f"{nombre_archivo}.png"
imagen.save(archivo_final)
imagen.show()

print(f"\n✔ Código QR generado correctamente: {archivo_final}")
