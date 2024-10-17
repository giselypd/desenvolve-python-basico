import datetime

tempo = datetime.datetime.now()
data = f"{tempo.day:02d}/{tempo.month:02d}/{tempo.year:02d}"
hora = f"{tempo.hour:02d}:{tempo.minute:02d}:{tempo.second:02d}"

print(f"Data: {data}")
print(f"Hora: {hora}")