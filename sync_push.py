import pyodbc
import pandas as pd
import subprocess

def extraer_datos_sql():
    server = 'jehovamekaddesh'
    database = 'From_Notebook'
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    try:
        print("Conectando a SQL Server...")
        conn = pyodbc.connect(conn_str)
        query = "SELECT * FROM dbo.orders_limpio"
        print("Extrayendo datos...")
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"[ERROR] Conexion SQL: {e}")
        return None

def actualizar_y_subir():
    df = extraer_datos_sql()
    if df is not None:
        df.to_csv('app.csv', index=False)
        print("Archivo app.csv actualizado.")
        try:
            print("Subiendo a GitHub...")
            subprocess.run(["git", "add", "app.csv"], check=True)
            subprocess.run(["git", "commit", "-m", "Actualizacion automatica desde SQL"], check=True)
            subprocess.run(["git", "push"], check=True)
            print("¡PROCESO EXITOSO!")
        except Exception as e:
            print(f"[ERROR] Git: {e}")
    else:
        print("[CANCELADO] Fallo la extraccion.")

if __name__ == "__main__":
    actualizar_y_subir()
