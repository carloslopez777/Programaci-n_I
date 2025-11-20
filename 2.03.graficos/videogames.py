import pandas as pd
import numpy as np
import matplotlib.pyplot as pit

sales_data = {
    "GameID": ["G1","G2","G3","G4","G5","G6"],
    "Title": ["GTA 5", "Zelda", "Super Mario", "Red Dead Redemption", "Minecraft", "Mario Kart"],
    "Genre": ["RPG", "RPG", "Platform", "RPG", "Open World", "Platform"],
    "Publisher": ["Rockstar", "Nintendo", "Nintendo", "Rockstar", "Mojang", "Nintendo"],
    "Units_Sold_Millions": [15.5, 20.1, 8.0, 12.3, 18.2, 19.6]
}

sales_df = pd.DataFrame(sales_data)

reviews_data = {
    "GameID": ["G1","G2","G3","G4","G5","G7"],
    "Critic_Score": [10, 10, 7.4, 9.5, 10, 9.7],
    "User_Score": [9.4, 9.8, 8.2, 9.8, np.nan, 9.6]
}

reviews_df = pd.DataFrame(reviews_data)

print("--- Datos de Ventas (crudos) ---")
print(sales_df)
print("--- Datos de Reseñas (crudos) ---")
print(reviews_df)

mean_user_score = reviews_df["User_Score"].mean()
reviews_df["User_Score"] = reviews_df["User_Score"].fillna(mean_user_score)

print(f"\n --- Reseñas (Limpias, NaN rellenado con {mean_user_score})---")
print(reviews_df)

df = pd.merge(sales_df, reviews_df, on="GameID", how="inner")

print("\n --- Tabla fusionada de ventas + reseñas --- ")
print(df)

df["Revenue_Estimate_Billions"] = (df["Units_Sold_Millions"]*50)/1000

df["Score_Gap"] = df["Critic_Score"] - df["User_Score"]

df["Critic_Score_100"] = df["Critic_Score"] * 10

print("\n --- Tabla transformada (Con nuevas columnas)")
print(df)

genre_sales = df.groupby("Genre")["Units_Sold_Millions"].sum().sort_values(ascending=False)
print(genre_sales)

pit.bar(genre_sales.keys(),genre_sales)
pit.title("Ventas Totales por Género")
pit.ylabel("Unidades Vendidas (En Millones)")
pit.xlabel("Género")
pit.grid(axis="y", linestyle="dotted", alpha=0.7)
pit.tight_layout()
pit.show()