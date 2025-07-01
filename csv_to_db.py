import pandas as pd
import sqlite3
import os


def choose_csv_file() :

    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

    if not csv_files :
        print("Aucun fichier CSV présent dans le dossier.")
    elif len(csv_files) == 1 :
        print(f"Conversion du fichier {csv_files[0]} en table de données.")
        return csv_files[0]

    print("Fichiers CSV disponibles :")
    for index, file in enumerate(csv_files) : 
        print(f"{index + 1}. {file}")

    while True : 
        try : 
            user_choice = int(input("Entrez le numéro du fichier à convertir : "))
            if 1 <= user_choice <= len(csv_files) : 
                print(f"Fichier choisi : {csv_files[user_choice - 1]}.")
                return csv_files[user_choice - 1]
            else : 
                print("Numéro invalide.")
        except ValueError : 
            print("Numéro invalide.")


def convert_csv_to_db(csv_file) :
    df = pd.read_csv(csv_file)
    db_name = csv_file.replace(".csv", "")

    conn = sqlite3.connect(f"{db_name}.db")
    df.to_sql("examples_table", conn, if_exists="replace", index=False)

    print(f"Table examples_table dans la BD {db_name}.bd maintenant configurée.")

    #test = conn.execute(f"SELECT * FROM examples_table LIMIT 5").fetchall()
    #for ligne in test : 
    #    print(ligne)



file_to_convert = choose_csv_file()
convert_csv_to_db(file_to_convert)



