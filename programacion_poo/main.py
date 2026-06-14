# ==========================================
# Programa principal
# Gestión de Mascotas usando POO
# ==========================================

from mascota import Mascota

# Crear objetos 
mascota1 = Mascota(
    "Max",
    "Perro",
    3
)

mascota2 = Mascota(
    "Mimosa",
    "Gata",
    2
)

# Mostrar información y ejecutar acciones
mascota1.mostrar_informacion()
mascota1.hacer_sonido()

print()  

mascota2.mostrar_informacion()
mascota2.hacer_sonido()
