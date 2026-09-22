import os
import json
import sys
import urllib.request

def send_seatalk_message(webhook_url, content_text):
    # Menambahkan parameter "at_all": True agar bot melakukan mention ke semua orang
    payload = {
        "tag": "text",
        "text": {
            "content": content_text,
            "at_all": True
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        webhook_url, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            response_body = response.read().decode('utf-8')
            print(f"HTTP Status Code: {status}")
            print(f"SeaTalk Server Response: {response_body}")
    except Exception as e:
        print(f"An execution error occurred: {e}")

def main():
    webhook_url = os.environ.get("SEATALK_WEBHOOK_URL")
    if not webhook_url:
        print("Error: SEATALK_WEBHOOK_URL environment variable is missing.")
        return

    # Validasi input argumen dari cronjob/GitHub Actions
    if len(sys.argv) < 2:
        print("Error: Harap masukkan argumen pesan (contoh: python send_reminder.py 1, 2, 3, atau 4)")
        return

    # Mengambil argumen pertama setelah nama file script
    pilihan = sys.argv[1]

    if pilihan == "1":
        pesan = "Absen cuyy!! segera buat thread dan kirim SS yaa 👇"
        print("Memproses Reminder 1...")
        send_seatalk_message(webhook_url, pesan)
        
    elif pilihan == "2":
        pesan = "yokk mulai SPAM call attempt, segera buat thread pinjam CRM siapa yaa 👇"
        print("Memproses Reminder 2...")
        send_seatalk_message(webhook_url, pesan)
        
    elif pilihan == "3":
        pesan = (
            "FU TIME 🔥🔥\n"
            "segera simak thread ya untuk priority dan mekanisme FU today !! \n"
            "sekarang all team sudah include perform dan belum ada buffer, jadi datamu tanggung jawabmu ya. perbantuan tidak bisa se intens dulu\n\n"
            "mekanisme :\n"
            "priority 70% wajib di touch dulu\n"
            "pengulangan menggunakan filter CRM risk tier (1,2,90,62,50,22,65) copy paste angka tsb langsung di CRM"
        )
        print("Memproses Reminder 3...")
        send_seatalk_message(webhook_url, pesan)
        
    elif pilihan == "4":
        pesan = (
            "SEMANGATTT PAGIII para pejuang cuann💸💸\n\n"
            "awali pagi dengan bismillah, jangan sampai amount&account PTP/LM merah semua (raih promise sebanyak mungkin) dan pastikan tiap kata HALO kalian tidak terbuang sia2 dan wajib jadi PTP/LM!!\n\n"
            "selalu ingat 🕵️\n"
            "- script 8.8\n"
            "\"Dari spaylater penelponannya direkam, bersedia dihubungi diluar jam kerja agar denda tidak makin membesar ya?\"\n"
            "jika menolak input CBL.\n"
            "jika jawaban user mau melakukan pembayaran berarti script 8.8 gugur langsung script tagihan.\n"
            "- JANGAN BUANG DATA 5sc APAPUN YG TERJADI TERMASUK MV\n"
            "- jangan sampai salah klik tgl PROLONG, CBD dan nominal Partial. pastikan sebelum submit klik baik. SAYANGI insentivemu! \n\n"
            "fokus fokus fokus"
        )
        print("Memproses Reminder 4...")
        send_seatalk_message(webhook_url, pesan)
        
    else:
        print(f"Error: Argumen '{pilihan}' tidak dikenali. Gunakan angka '1', '2', '3', atau '4'.")

if __name__ == "__main__":
    main()
