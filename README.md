# Haust-Network-AutoTx

## Panduan Penggunaan
### 1. **Persiapan Awal**  
   Jalankan perintah berikut untuk mempersiapkan sistem Anda:  
   ```bash
   apt update && upgrade
   screen -S haus
   git clone https://github.com/jeripangestu/Haust-Network-AutoTx
   cd Haust-Network-AutoTx
   pip3 install web3
   pip3 install python-dotenv 
### 2. Konfigurasi Private Key
- Buka file `.env` di direktori proyek.
- Masukkan *Private Key* EVM Anda pada bagian setelah =

### 3. Tambahkan Address Wallet
- Buka file konfigurasi atau masukkan alamat wallet yang akan ditransfer.
- Gunakan format **1 baris untuk 1 address**.

### 4. Jalankan Script
- Jalankan file Python dengan perintah berikut di terminal atau command prompt:
  ```bash
  python haus-auto-tx.py
