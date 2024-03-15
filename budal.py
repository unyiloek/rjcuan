import subprocess

# Path ke file RJ
rj = '/rjcuan/rj'

# Konfigurasi RJ
rjconfig = '/rjcuan/config.json'

# Jalankan RJ
try:
    subprocess.run([rj, '--config', rjconfig])
except FileNotFoundError:
    print('File RJ tidak ditemukan. Periksa path file RJ.')
