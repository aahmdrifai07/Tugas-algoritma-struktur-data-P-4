total_hari = int(input("Masukkan jumlah total hari proyek: "))

tahun = total_hari // 365
sisa_hari = total_hari % 365
bulan = sisa_hari // 30

hari = sisa_hari % 30
print(f"\nProyek dikerjakan selama:")
print(f"{tahun} Tahun")
print(f"{bulan} Bulan")
print(f"{hari} Hari")
