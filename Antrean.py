class SistemAntrean:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(f"[+] Antrean Masuk: {data}")

    def dequeue(self):
        if not self.is_empty(tampilkan_pesan=False):
            data = self.queue.pop(0)
            print(f"[-] Antrean Dilayani: {data}")
            return data
        print("[!] Gagal: Antrean Kosong!")
        return None

    def peek(self):
        if not self.is_empty(tampilkan_pesan=False):
            print(f"[?] Data paling depan saat ini: {self.queue[0]}")
            return self.queue[0]
        return None

    def is_empty(self, tampilkan_pesan=True):
        kosong = len(self.queue) == 0
        if tampilkan_pesan:
            print(f"[*] Apakah antrean kosong? {kosong}")
        return kosong



print("=== SIMULASI LANGKAH ANTREAN  ===")
antrean = SistemAntrean()
antrean.enqueue("0001 - Gilang")       
antrean.enqueue("0002 - Ronald")       
antrean.peek()                        
antrean.dequeue()                     
antrean.is_empty()                   
antrean.dequeue()                     
antrean.is_empty()                   

print("\n")


print("=== PENGUJIAN FITUR ANTREAN  ===")
test_antrean = SistemAntrean()
test_antrean.enqueue("0001 - Gilang")
test_antrean.enqueue("0002 - Ronald")
test_antrean.dequeue()
test_antrean.peek()
test_antrean.is_empty()