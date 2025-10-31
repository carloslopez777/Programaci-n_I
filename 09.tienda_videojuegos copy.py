print("Bienvenidos a Game World")

info_tienda = ("Más que un juego, una experiencia", 2025)

inventario = {
    "Minecraft": {"precio": 350, "stock": 20},
    "GTA5": {"precio": 700, "stock": 12},
    "FC25": {"precio": 1200, "stock": 25},
}

print(inventario["GTA5"]["precio"])

print("Vendiste una copia de tu primer juego: ")

inventario["Minecraft"]['stock'] = 19
print(inventario["Minecraft"])

print("Lista actualizada")