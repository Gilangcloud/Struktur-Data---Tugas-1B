class FiturUndo:
    def __init__(self):
        self.stack = []

    def push(self, aktivitas):
        self.stack.append(aktivitas)
        print(f"[+] Aktivitas disimpan: {aktivitas}")

    def pop(self):
        if not self.is_empty(tampilkan_pesan=False):
            aktivitas = self.stack.pop()
            print(f"[-] Dibatalkan (Undo): {aktivitas}")
            return aktivitas
        print("[!] Gagal: Tidak ada aktivitas!")
        return None

    def peek(self):
        if not self.is_empty(tampilkan_pesan=False):
            print(f"[?] Aktivitas terakhir saat ini: {self.stack[-1]}")
            return self.stack[-1]
        return None

    def is_empty(self, tampilkan_pesan=True):
        kosong = len(self.stack) == 0
        if tampilkan_pesan:
            print(f"[*] Apakah riwayat aktivitas kosong? {kosong}")
        return kosong



print("=== SIMULASI LANGKAH UNDO ===")
undo = FiturUndo()
undo.push("Validasi KRS Gilang")                     
undo.push("Update status pembayaran UKT Radish")               
undo.peek()                                       
undo.pop()                                       
undo.is_empty()                                   
undo.pop()                                        
undo.is_empty()                                   

print("\n")


print("=== PENGUJIAN FITUR UNDO ( ===")
test_undo = FiturUndo()
test_undo.push("Validasi KRS Gilang")
test_undo.push("Update status pembayaran UKT Radish")
test_undo.pop()
test_undo.peek()
test_undo.is_empty()