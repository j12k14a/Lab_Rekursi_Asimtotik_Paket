
from time import perf_counter
from lab_rekursi import (
    fib_naif,
    fib_memo,
    binary_search_rek,
    pangkat_cepat,
)


def ukur(fungsi, *args, ulang=3):
    """Mengukur rata-rata waktu eksekusi dalam milidetik."""
    total = 0.0

    for _ in range(ulang):
        mulai = perf_counter()
        fungsi(*args)
        selesai = perf_counter()
        total += (selesai - mulai) * 1000

    return total / ulang


# ==================================================
# D1. FIBONACCI
# ==================================================
print("D1. Fibonacci (ms)")
print(f"{'n':>6} | {'fib_naif':>12} | {'fib_memo':>12}")
print("-" * 38)

for n in (20, 22, 24, 26, 28, 30):
    waktu_naif = ukur(fib_naif, n, ulang=3)
    waktu_memo = ukur(fib_memo, n, ulang=10)

    print(f"{n:6} | {waktu_naif:12.4f} | {waktu_memo:12.4f}")


# ==================================================
# D2. PENCARIAN LINEAR VS BINARY SEARCH REKURSIF
# ==================================================
def pencarian_linear(arr, target):
    """Mencari target menggunakan pencarian linear."""
    for i, nilai in enumerate(arr):
        if nilai == target:
            return i

    return -1


print("\nD2. Pencarian (ms), target tidak ada")
print(f"{'n':>9} | {'linear':>12} | {'binary_rek':>12}")
print("-" * 40)

for n in (1_000, 10_000, 100_000, 1_000_000):
    data = list(range(n))
    target = -1

    # Data dibuat di luar pengukuran waktu.
    waktu_linear = ukur(
        pencarian_linear, data, target, ulang=3
    )

    # Binary search sangat cepat, sehingga diulang lebih banyak
    # agar pengukuran lebih stabil.
    waktu_binary = ukur(
        binary_search_rek, data, target, ulang=100
    )

    print(f"{n:9} | {waktu_linear:12.4f} | {waktu_binary:12.4f}")


# ==================================================
# D3. PANGKAT NAIF VS PANGKAT CEPAT
# ==================================================
def pangkat_naif(x, n):
    """
    Menghitung x^n menggunakan perkalian berulang.
    Implementasi iteratif digunakan khusus untuk eksperimen
    agar tidak terkena batas kedalaman rekursi Python.
    """
    hasil = 1

    for _ in range(n):
        hasil *= x

    return hasil


print("\nD3. Pangkat 3^n (ms)")
print(f"{'n':>6} | {'pangkat_naif':>14} | {'pangkat_cepat':>14}")
print("-" * 42)

for n in (500, 1_000, 2_000, 4_000, 8_000):
    waktu_naif = ukur(
        pangkat_naif, 3, n, ulang=1
    )

    waktu_cepat = ukur(
        pangkat_cepat, 3, n, ulang=3
    )

    print(f"{n:6} | {waktu_naif:14.4f} | {waktu_cepat:14.4f}")


print("\nEksperimen D1, D2, dan D3 selesai.")
