import sqlite3
import pandas as pd
import os
from datetime import datetime
import random

# Veritabanı dosyasının adı
db_path = "arac_verileri.db"

# Eğer önceden oluşturulmuşsa sil (temiz başlangıç)
if os.path.exists(db_path):
    os.remove(db_path)

# Veritabanı bağlantısı oluştur
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Tabloyu oluştur
cursor.execute("""
CREATE TABLE veriler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarih TEXT NOT NULL,
    hiz REAL,
    sicaklik REAL,
    yakit REAL,
    devir INTEGER
);
""")
conn.commit()

# Örnek iki kayıt ekle (şimdilik)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
veriler = [
    (now, 65.2, 78.5, 54.3, 2200),
    (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 82.0, 90.1, 42.7, 3000)
]

cursor.executemany("INSERT INTO veriler (tarih, hiz, sicaklik, yakit, devir) VALUES (?, ?, ?, ?, ?)", veriler)
conn.commit()

# Verileri pandas ile görüntüle
df = pd.read_sql_query("SELECT * FROM veriler", conn)
print(df)

# Bağlantıyı kapat
cursor.close()
conn.close()
