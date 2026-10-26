from lab_rekursi import (
    faktorial,
    jumlah_digit,
    balik_string,
    is_palindrom,
    pangkat_cepat,
    fib_naif,
    fib_memo,
    binary_search_rek,
    permutasi,
    hanoi,
    ratakan,
)

total = 0
lulus = 0


def cek(nama, pengujian):
    global total, lulus
    total += 1

    try:
        pengujian()
        lulus += 1
        print(f"LULUS  {nama}")
    except Exception as error:
        print(f"GAGAL  {nama}: {error}")


def tes_faktorial():
    assert faktorial(0) == 1
    assert faktorial(5) == 120
    try:
        faktorial(-1)
    except ValueError:
        return
    raise AssertionError("Input negatif seharusnya ValueError")


def tes_jumlah_digit():
    assert jumlah_digit(0) == 0
    assert jumlah_digit(4096) == 19
    assert jumlah_digit(7) == 7
    try:
        jumlah_digit(-1)
    except ValueError:
        return
    raise AssertionError("Input negatif seharusnya ValueError")


def tes_balik_string():
    assert balik_string("data") == "atad"
    assert balik_string("") == ""
    assert balik_string("a") == "a"


def tes_palindrom():
    assert is_palindrom("Katak") is True
    assert is_palindrom("malam") is True
    assert is_palindrom("Python") is False
    assert is_palindrom("") is True


def tes_pangkat_cepat():
    assert pangkat_cepat(2, 10) == 1024
    assert pangkat_cepat(3, 4) == 81
    assert pangkat_cepat(5, 0) == 1
    try:
        pangkat_cepat(2, -1)
    except ValueError:
        return
    raise AssertionError("Eksponen negatif seharusnya ValueError")


def tes_fib_naif():
    assert fib_naif(0) == 0
    assert fib_naif(1) == 1
    assert fib_naif(10) == 55


def tes_fib_memo():
    assert fib_memo(0) == 0
    assert fib_memo(10) == 55
    assert fib_memo(100) == 354224848179261915075
    assert fib_memo(300) > 0


def tes_binary_search():
    data = [2, 5, 8, 12, 16]
    assert binary_search_rek(data, 12) == 3
    assert binary_search_rek(data, 2) == 0
    assert binary_search_rek(data, 7) == -1
    assert binary_search_rek([], 3) == -1


def tes_permutasi():
    hasil = permutasi("abc")
    assert len(hasil) == 6
    assert set(hasil) == {
        "abc", "acb", "bac", "bca", "cab", "cba"
    }
    assert permutasi("") == [""]
    assert permutasi("a") == ["a"]


def tes_hanoi():
    assert hanoi(0) == []
    assert hanoi(2) == [
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
    ]
    assert len(hanoi(3, "A", "C", "B")) == 7


def tes_ratakan():
    assert ratakan([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert ratakan([]) == []
    assert ratakan([[], [1, []], 2]) == [1, 2]
    assert ratakan(7) == [7]


print("UJI OTOMATIS MANDIRI - LAB REKURSI")
print("-" * 42)

cek("A1 faktorial", tes_faktorial)
cek("A2 jumlah_digit", tes_jumlah_digit)
cek("A3 balik_string", tes_balik_string)
cek("A4 is_palindrom", tes_palindrom)
cek("A5 pangkat_cepat", tes_pangkat_cepat)
cek("B1 fib_naif", tes_fib_naif)
cek("B2 fib_memo", tes_fib_memo)
cek("B3 binary_search_rek", tes_binary_search)
cek("B4 permutasi", tes_permutasi)
cek("B5 hanoi", tes_hanoi)
cek("B6 ratakan", tes_ratakan)

print("-" * 42)
print(f"Skor tes mandiri: {lulus}/{total} tes lulus")

if lulus == total:
    print("Semua tes mandiri lulus.")
else:
    print("Masih ada tes yang gagal. Periksa pesan GAGAL di atas.")
