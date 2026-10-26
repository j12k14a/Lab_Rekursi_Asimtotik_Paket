# Latihan Lab Struktur Data: Rekursi & Analisis Asimtotik
# Python 3.10+

def faktorial(n):
    # Big-O: O(n) waktu, O(n) ruang call stack
    if n < 0:
        raise ValueError("n harus >= 0")
    if n <= 1:  # base case
        return 1
    return n * faktorial(n - 1)


def jumlah_digit(n):
    # Big-O: O(log n) waktu, O(log n) ruang call stack
    if n < 0:
        raise ValueError("n harus >= 0")
    if n < 10:  # base case
        return n
    return (n % 10) + jumlah_digit(n // 10)


def balik_string(s):
    # Big-O: O(n^2) waktu karena slicing string berulang, O(n) ruang
    if len(s) <= 1:  # base case
        return s
    return s[-1] + balik_string(s[:-1])


def is_palindrom(s):
    # Big-O: O(n^2) waktu karena slicing berulang, O(n) ruang
    s = s.lower()
    if len(s) <= 1:  # base case
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrom(s[1:-1])


def pangkat_cepat(x, n):
    # Big-O: O(log n) perkalian (tidak menghitung biaya bilangan besar), O(log n) ruang
    if n < 0:
        raise ValueError("n harus >= 0")
    if n == 0:  # base case
        return 1
    setengah = pangkat_cepat(x, n // 2)
    hasil = setengah * setengah
    if n % 2 == 1:
        hasil *= x
    return hasil


def fib_naif(n):
    # Big-O: O(2^n) waktu, O(n) ruang call stack
    if n < 0:
        raise ValueError("n harus >= 0")
    if n <= 1:  # base case
        return n
    return fib_naif(n - 1) + fib_naif(n - 2)


def fib_memo(n, memo=None):
    # Big-O: O(n) waktu, O(n) ruang
    if n < 0:
        raise ValueError("n harus >= 0")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:  # base case
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def binary_search_rek(arr, target, lo=0, hi=None):
    # Big-O: O(log n) waktu, O(log n) ruang call stack
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:  # base case: target tidak ditemukan
        return -1
    tengah = (lo + hi) // 2
    if arr[tengah] == target:
        return tengah
    if target < arr[tengah]:
        return binary_search_rek(arr, target, lo, tengah - 1)
    return binary_search_rek(arr, target, tengah + 1, hi)


def permutasi(s):
    # Big-O: O(n * n!) waktu secara kasar untuk membangun seluruh string, O(n * n!) ruang output
    if len(s) <= 1:  # base case
        return [s]
    hasil = []
    for i, karakter in enumerate(s):
        sisa = s[:i] + s[i + 1:]
        for p in permutasi(sisa):
            hasil.append(karakter + p)
    return hasil


def hanoi(n, asal="A", tujuan="C", bantu="B"):
    # Big-O: O(2^n) waktu dan O(2^n) ruang untuk menyimpan daftar langkah
    if n < 0:
        raise ValueError("n harus >= 0")
    if n == 0:  # base case
        return []
    langkah = hanoi(n - 1, asal, bantu, tujuan)
    langkah.append((asal, tujuan))
    langkah.extend(hanoi(n - 1, bantu, tujuan, asal))
    return langkah


def ratakan(data):
    # Big-O: O(N) waktu untuk N elemen total (abaikan biaya salin list), O(N) ruang hasil
    if not isinstance(data, list):
        return [data]
    if len(data) == 0:  # base case
        return []
    pertama = ratakan(data[0])
    sisanya = ratakan(data[1:])
    return pertama + sisanya
