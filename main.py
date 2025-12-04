import httpx
import json
import uuid
import os
import csv
import time

client = httpx.Client(timeout=30, trust_env=False)
device_id = str(uuid.uuid4())

headers = {
    'User-Agent': "okhttp/4.12.0",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/json",
    'device-id': device_id,
    'authorization': "Basic Y3VzdGJhc2ljOk9MV2llWlVvQlA=",
    'source': "eraspace",
    'platform': "eraspace-android",
    'x-source': "eraspace",
    'content-type': "application/json; charset=UTF8"
}

def login(identifier, password):
    url = "https://jeanne.eraspace.com/customers/v2/auth/login"
    json_data = {
        "identifier": identifier,
        "password": password,
        "type": "password",
    }

    try:
        print(f"\n[*] Login: {identifier}")
        response = client.post(url, headers=headers, json=json_data, timeout=30)
        data = response.json()

        if response.status_code != 200:
            print(f"[LOGIN FAILED] Response: {data}")

        token = data.get("data", {}).get("token")
        return token

    except Exception as e:
        print(f"Error Login: {e}")
        return None

def save_cookie_interactive(identifier, token):
    folder = "cookies"
    filename = f"{folder}/cookies.json"

    os.makedirs(folder, exist_ok=True)

    data_list = []

    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                if content:
                    data_list = json.loads(content)
        except json.JSONDecodeError:
            data_list = []

    is_found = False
    for item in data_list:
        if item.get("nomor") == identifier:
            item["cookies"] = token
            is_found = True
            print(f"[UPDATE] Token diperbarui.")
            break

    if not is_found:
        data_list.append({
            "nomor": identifier,
            "cookies": token
        })
        print(f"[NEW] Token ditambahkan.")

    with open(filename, "w") as f:
        json.dump(data_list, f, indent=4)

def load_numbers():
    path = "akun/akun.csv"
    if not os.path.exists(path):
        print("File akun/akun.csv tidak ditemukan!")
        return []

    numbers = []
    with open(path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                numbers.append(row[0].strip())

    return numbers

def saveallcookies_main():
    print("============= AUTO LOGIN & SAVE COOKIE TOOLS =============")
    print("===================== By Syailendra ======================")

    numbers = load_numbers()
    if not numbers:
        print("Tidak ada nomor ditemukan di akun/akun.csv")
        return

    print(f"\nTotal nomor ditemukan: {len(numbers)}")
    print("Memulai proses login...")

    for num in numbers:
        print(f"\n==============================")
        print(f"Memproses nomor: {num}")
        password = input(f"Masukkan password untuk {num}: ")
        token = login(num, password)

        if not token:
            print(f"[FAILED] Login gagal untuk {num}")
            continue

        save_cookie_interactive(num, token)
        print(f"[SUCCESS] Token untuk {num} disimpan.")


if __name__ == "__main__":
    saveallcookies_main()
