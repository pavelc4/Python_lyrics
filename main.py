import time
import sys
import pygame
import os

def tampilkan_lirik(lirik, durasi, delay_awal, kecepatan):
    for i, baris in enumerate(lirik):
        # Tambahkan delay sebelum menampilkan lirik
        time.sleep(delay_awal)  # Delay sebelum menampilkan lirik

        # Tampilkan setiap kata dalam baris
        for kata in baris.split():
            # Tampilkan kata dengan efek pengetikan
            for huruf in kata:
                print(huruf, end='', flush=True)  # Tampilkan huruf tanpa newline
                time.sleep(kecepatan)  # Delay sesuai kecepatan per huruf
            print(' ', end='', flush=True)  # Tambahkan spasi setelah kata
            time.sleep(0.2)  # Delay tambahan setelah setiap kata
        print()  # Pindah ke baris baru setelah semua kata ditampilkan
        time.sleep(durasi[i])  # Delay sesuai durasi yang ditentukan

def main():
    # Inisialisasi pygame
    pygame.mixer.init()
    
    # Path ke file audio
    audio_path = "/home/vell/Documents/prjkt/py/asset/song.mp3"  # Ganti dengan path yang benar
    print("Loading audio from:", audio_path)  # Debugging path

    # Cek apakah file ada
    if not os.path.isfile(audio_path):
        print("File tidak ditemukan:", audio_path)
        return

    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print("Error loading audio file:", e)
        return

    # Lirik dan durasi (dalam detik) untuk setiap baris
    lirik = [
        "Hold my hands, dont-dont tell your friends",
        "Cerita kemaren, ku ingat kermanen",
        "Manis mu kaya permen, I hope this never end",
        "Oh can you be my Gwen? and ill be the Spiderman",
        "Sakit dadaku, ku mulai merindu",
        "Ku bayangkan jika kamu tidur di samping ku",
        "Di malam yang semu",
        "Pejamkan mata ku",
        "Ku bayangkan tubuhmu jika di pelukanku"
    ]
    
    # Durasi untuk setiap baris lirik (sesuaikan dengan lagu)
    durasi = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]  # Ganti dengan durasi yang sesuai

    # Delay sebelum menampilkan lirik (dalam detik)
    delay_awal = 0.1  # Ganti dengan nilai yang sesuai untuk sinkronisasi

    # Kecepatan pengetikan (dalam detik)
    kecepatan = 0.04  # Ganti dengan nilai yang sesuai untuk kecepatan pengetikan

    # Tampilkan lirik
    tampilkan_lirik(lirik, durasi, delay_awal, kecepatan)

    # Tunggu sampai lagu selesai
    while pygame.mixer.music.get_busy():
        time.sleep(1)

if __name__ == "__main__":
    main()