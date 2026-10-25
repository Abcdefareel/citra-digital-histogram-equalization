"""
Praktikum 3 - Histogram & Perataan Histogram (Pengolahan Citra Digital)

Percobaan 1 (Histogram)
    - Tampilkan citra asli berwarna + histogramnya untuk 3 citra:
      kontras rendah, kontras bagus, kontras tinggi.
    - Hitung nilai pixel (min, max, mean, std) sebagai bahan analisis.

Percobaan 2 (Perataan Histogram / Histogram Equalization)
    - Ratakan histogram ketiga citra, lalu bandingkan sebelum vs sesudah.

Library: OpenCV, NumPy, matplotlib
"""

import os

import cv2
import numpy as np
from matplotlib import pyplot as plt

# ---------------------------------------------------------------------------
# PENGATURAN
# ---------------------------------------------------------------------------
FOLDER_HASIL = "hasil"   # tempat menyimpan gambar hasil
L = 256                  # jumlah derajat keabuan (0 sampai 255)
EKSTENSI_GAMBAR = (".bmp", ".jpeg", ".jpg", ".png", ".tif", ".tiff")


# ---------------------------------------------------------------------------
# FUNGSI BANTU
# ---------------------------------------------------------------------------
def pilih_gambar(folder="."):
    """Tampilkan menu CLI untuk memilih satu atau beberapa gambar."""
    daftar_gambar = sorted(
        nama
        for nama in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, nama))
        and nama.lower().endswith(EKSTENSI_GAMBAR)
    )

    if not daftar_gambar:
        raise FileNotFoundError(
            f"Tidak ada file gambar ({', '.join(EKSTENSI_GAMBAR)}) di folder '{folder}'."
        )

    print("Pilih gambar yang ingin diolah:")
    for nomor, nama in enumerate(daftar_gambar, start=1):
        print(f"  {nomor}. {nama}")
    print("  a. Semua gambar")

    while True:
        pilihan = input("Pilihan (nomor dipisahkan koma, atau 'a' untuk semua): ")
        pilihan = pilihan.strip().lower()
        if pilihan == "a":
            terpilih = daftar_gambar
            break

        nomor_pilihan = [bagian.strip() for bagian in pilihan.split(",")]
        if (
            pilihan
            and all(nomor.isdigit() for nomor in nomor_pilihan)
            and all(1 <= int(nomor) <= len(daftar_gambar) for nomor in nomor_pilihan)
        ):
            terpilih = [
                daftar_gambar[int(nomor) - 1]
                for nomor in dict.fromkeys(nomor_pilihan)
            ]
            break

        print("Pilihan tidak valid. Masukkan nomor yang tersedia atau 'a'.")

    return {
        nama: os.path.join(folder, nama)
        for nama in terpilih
    }


def muat_gambar(path):
    """Baca gambar asli berwarna."""
    gambar_asli = cv2.imread(path, cv2.IMREAD_COLOR)
    if gambar_asli is None:
        raise FileNotFoundError(
            f"Gambar '{path}' tidak ditemukan / bukan file gambar. "
            "Pastikan file yang dipilih adalah gambar yang valid."
        )
    return gambar_asli


def hitung_histogramkanal(kanal):
    """
    Frekuensi tiap intensitas warna 0..255.
    range=(0, L) memastikan 256 bin selalu mewakili nilai 0..255,
    bukan mengikuti min/max data (kalau tidak, indeks bin jadi bergeser).
    """
    frekuensi, _ = np.histogram(kanal.ravel(), bins=L, range=(0, L))
    return frekuensi


def hitung_histogram_warna(gambar_bgr):
    """Hitung histogram kanal merah, hijau, dan biru dari gambar asli."""
    gambar_rgb = cv2.cvtColor(gambar_bgr, cv2.COLOR_BGR2RGB)
    nama_kanal = ("Merah", "Hijau", "Biru")
    return {
        nama: hitung_histogramkanal(gambar_rgb[:, :, indeks])
        for indeks, nama in enumerate(nama_kanal)
    }


def statistik(A):
    """Nilai pixel yang dipakai untuk analisis."""
    return {
        "min": int(A.min()),
        "max": int(A.max()),
        "mean": float(A.mean()),   # kecerahan rata-rata
        "std": float(A.std()),     # ukuran kontras
    }


def cetak_statistik(judul, stat):
    print(
        f"  {judul:<10} min={stat['min']:>3}  max={stat['max']:>3}  "
        f"rentang={stat['max'] - stat['min']:>3}  "
        f"mean={stat['mean']:7.2f}  std={stat['std']:6.2f}"
    )


# ---------------------------------------------------------------------------
# PERCOBAAN 2: FUNGSI PERATAAN HISTOGRAM
# ---------------------------------------------------------------------------
def perataanHistogram(A):
    """
    Histogram equalization.
    Rumus (materi): w_baru = round( C_w * (L-1) / n )
        C_w = distribusi kumulatif sampai derajat keabuan w
        n   = jumlah seluruh pixel (nx * ny)
    """
    nilai_bin = L - 1                                   # 255 = nilai pixel maksimal

    # 1) histogram: berapa pixel untuk tiap derajat keabuan
    frekuensi = hitung_histogramkanal(A)

    # 2) distribusi kumulatif: jumlahkan frekuensi dari 0 sampai w
    kumulatif_histogram = frekuensi.cumsum()

    # 3) normalisasi ke 0..255 -> tabel nilai baru untuk tiap nilai lama
    probabilty_frekuensi = np.round(
        (kumulatif_histogram / float(A.size)) * nilai_bin
    )

    # 4) ganti setiap pixel dengan nilai barunya (pencarian tabel).
    #    Sama dengan loop for i, for j: B[i,j] = tabel[A[i,j]], tapi lebih cepat.
    B = probabilty_frekuensi[A]

    # 5) ubah ke uint8 agar bisa disimpan dan ditampilkan sebagai gambar
    return B.astype(np.uint8)


def perataan_warna(gambar_bgr):
    """Ratakan luminansi gambar berwarna dan pertahankan informasi warnanya."""
    gambar_ycrcb = cv2.cvtColor(gambar_bgr, cv2.COLOR_BGR2YCrCb)
    luminansi, channel_cr, channel_cb = cv2.split(gambar_ycrcb)
    luminansi_hasil = perataanHistogram(luminansi)
    hasil_ycrcb = cv2.merge((luminansi_hasil, channel_cr, channel_cb))
    return cv2.cvtColor(hasil_ycrcb, cv2.COLOR_YCrCb2BGR)


# ---------------------------------------------------------------------------
# PERCOBAAN 1: HISTOGRAM
# ---------------------------------------------------------------------------
def percobaan_histogram(citra):
    print("=" * 70)
    print("PERCOBAAN 1 - HISTOGRAM")
    print("=" * 70)

    warna_kanal = {
        "Merah": "red",
        "Hijau": "green",
        "Biru": "blue",
    }

    for nama, gambar in citra.items():
        print(f"\n{nama}")
        histogram = hitung_histogram_warna(gambar)
        gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)
        for nama_kanal, kanal_rgb in zip(
            ("Merah", "Hijau", "Biru"), cv2.split(gambar_rgb)
        ):
            cetak_statistik(nama_kanal, statistik(kanal_rgb))

        fig, ax = plt.subplots(1, 3, figsize=(16, 4))
        fig.suptitle(f"Histogram - {nama}")

        ax[0].imshow(gambar_rgb)
        ax[0].set_title("Citra asli")
        ax[0].axis("off")

        for nama_kanal, frekuensi in histogram.items():
            ax[1].plot(frekuensi, color=warna_kanal[nama_kanal], label=nama_kanal)
        ax[1].set_xlim(0, 255)
        ax[1].set_title("Histogram warna")
        ax[1].set_xlabel("Intensitas warna")
        ax[1].set_ylabel("Jumlah pixel")
        ax[1].legend()

        for nama_kanal, frekuensi in histogram.items():
            kumulatif = frekuensi.cumsum() / frekuensi.sum()
            ax[2].plot(kumulatif, color=warna_kanal[nama_kanal], label=nama_kanal)
        ax[2].set_xlim(0, 255)
        ax[2].set_ylim(0, 1)
        ax[2].set_title("Distribusi kumulatif warna")
        ax[2].set_xlabel("Intensitas warna")
        ax[2].legend()

        fig.tight_layout()
        fig.savefig(os.path.join(FOLDER_HASIL, f"histogram_{nama}.png"), dpi=120)


# ---------------------------------------------------------------------------
# PERCOBAAN 2: PERATAAN HISTOGRAM
# ---------------------------------------------------------------------------
def percobaan_perataan(citra):
    print("\n" + "=" * 70)
    print("PERCOBAAN 2 - PERATAAN HISTOGRAM")
    print("=" * 70)

    warna_kanal = {
        "Merah": "red",
        "Hijau": "green",
        "Biru": "blue",
    }

    for nama, gambar_asli in citra.items():
        hasil = perataan_warna(gambar_asli)

        print(f"\n{nama}")
        histogram_sebelum = hitung_histogram_warna(gambar_asli)
        histogram_sesudah = hitung_histogram_warna(hasil)
        kanal_sebelum = cv2.split(
            cv2.cvtColor(gambar_asli, cv2.COLOR_BGR2RGB)
        )
        kanal_sesudah = cv2.split(cv2.cvtColor(hasil, cv2.COLOR_BGR2RGB))
        for indeks, nama_kanal in enumerate(warna_kanal):
            print(f"  Kanal {nama_kanal}")
            cetak_statistik("sebelum", statistik(kanal_sebelum[indeks]))
            cetak_statistik("sesudah", statistik(kanal_sesudah[indeks]))

        path_hasil = os.path.join(FOLDER_HASIL, f"perataan_{nama}.png")
        if not cv2.imwrite(path_hasil, hasil):
            raise OSError(f"Gagal menyimpan hasil perataan ke '{path_hasil}'.")

        fig, ax = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle(f"Perataan Histogram - {nama}")

        ax[0, 0].imshow(cv2.cvtColor(gambar_asli, cv2.COLOR_BGR2RGB))
        ax[0, 0].set_title("Sebelum (warna asli)")
        ax[0, 0].axis("off")

        ax[0, 1].imshow(cv2.cvtColor(hasil, cv2.COLOR_BGR2RGB))
        ax[0, 1].set_title("Sesudah perataan (warna)")
        ax[0, 1].axis("off")

        for nama_kanal, frekuensi in histogram_sebelum.items():
            ax[1, 0].plot(
                frekuensi,
                color=warna_kanal[nama_kanal],
                label=nama_kanal,
            )
        ax[1, 0].set_xlim(0, 255)
        ax[1, 0].set_title("Histogram warna sebelum")
        ax[1, 0].set_xlabel("Intensitas warna")
        ax[1, 0].set_ylabel("Jumlah pixel")
        ax[1, 0].legend()

        for nama_kanal, frekuensi in histogram_sesudah.items():
            ax[1, 1].plot(
                frekuensi,
                color=warna_kanal[nama_kanal],
                label=nama_kanal,
            )
        ax[1, 1].set_xlim(0, 255)
        ax[1, 1].set_title("Histogram warna sesudah")
        ax[1, 1].set_xlabel("Intensitas warna")
        ax[1, 1].set_ylabel("Jumlah pixel")
        ax[1, 1].legend()

        fig.tight_layout()
        fig.savefig(os.path.join(FOLDER_HASIL, f"perbandingan_{nama}.png"), dpi=120)


# ---------------------------------------------------------------------------
# PROGRAM UTAMA
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    os.makedirs(FOLDER_HASIL, exist_ok=True)

    berkas_terpilih = pilih_gambar()
    citra = {
        nama: muat_gambar(path) for nama, path in berkas_terpilih.items()
    }

    for nama, gambar in citra.items():
        path_hasil_asli = os.path.join(FOLDER_HASIL, f"asli_{nama}.png")
        if not cv2.imwrite(path_hasil_asli, gambar):
            raise OSError(f"Gagal menyimpan gambar asli ke '{path_hasil_asli}'.")

    percobaan_histogram(citra)
    percobaan_perataan(citra)

    print(f"\nSemua gambar hasil tersimpan di folder '{FOLDER_HASIL}/'")
    plt.show()
