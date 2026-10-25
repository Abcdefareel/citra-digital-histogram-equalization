# Laporan Analisis Perataan Histogram Gambar Berwarna

## Tujuan

Membandingkan gambar berwarna sebelum dan sesudah perataan histogram berdasarkan
nilai pixel dan distribusi histogram. Gambar tetap diproses dan ditampilkan
sebagai gambar berwarna; grayscale tidak digunakan.

## Metode

Perataan dilakukan pada kanal luminansi **Y** setelah gambar dikonversi sementara
ke ruang warna YCrCb. Kanal warna **Cr** dan **Cb** dipertahankan, lalu gambar
dikembalikan ke RGB/BGR. Dengan demikian, hasil tetap berwarna. Histogram RGB
di bawah dihitung terpisah untuk kanal merah, hijau, dan biru pada gambar asli
serta hasilnya.

Nilai pixel yang dilaporkan:

- **Min–maks**: intensitas terendah dan tertinggi (rentang 0–255).
- **Mean**: rata-rata intensitas kanal.
- **Std**: simpangan baku; nilai lebih besar menunjukkan sebaran intensitas
  yang lebih lebar.
- **Bin terisi**: jumlah tingkat intensitas dari 256 yang memiliki pixel.
- **Modus (jumlah)**: intensitas dengan pixel terbanyak beserta jumlah pixelnya.
- **Entropi**: ukuran keragaman distribusi histogram dalam bit; bukan ukuran
  kualitas visual secara langsung.

Statistik dihitung dari tiga gambar sumber yang tersedia di folder proyek.
Semua angka statistik dibulatkan dua desimal; entropi dibulatkan tiga desimal.

## 1. Analisis Nilai Pixel RGB

### `image 1.jpeg` — 1200 × 1600 pixel

| Kanal | Min–maks sebelum | Min–maks sesudah | Mean sebelum | Mean sesudah | Std sebelum | Std sesudah |
|---|---:|---:|---:|---:|---:|---:|
| Merah | 30–231 | 0–255 | 152.57 | 123.35 | 39.07 | 71.22 |
| Hijau | 38–232 | 0–255 | 159.85 | 130.51 | 42.82 | 76.01 |
| Biru | 55–234 | 1–255 | 164.87 | 135.55 | 43.35 | 76.12 |

### `Image 2.jpeg` — 3120 × 4160 pixel

| Kanal | Min–maks sebelum | Min–maks sesudah | Mean sebelum | Mean sesudah | Std sebelum | Std sesudah |
|---|---:|---:|---:|---:|---:|---:|
| Merah | 0–255 | 0–255 | 152.22 | 133.56 | 54.49 | 68.42 |
| Hijau | 0–255 | 0–255 | 145.50 | 126.86 | 63.06 | 75.77 |
| Biru | 0–255 | 0–255 | 139.94 | 121.80 | 66.49 | 78.40 |

### `Image 3.jpeg` — 736 × 645 pixel

| Kanal | Min–maks sebelum | Min–maks sesudah | Mean sebelum | Mean sesudah | Std sebelum | Std sesudah |
|---|---:|---:|---:|---:|---:|---:|
| Merah | 0–255 | 0–255 | 173.35 | 142.47 | 90.11 | 82.60 |
| Hijau | 0–255 | 0–255 | 156.34 | 125.44 | 79.25 | 74.42 |
| Biru | 0–255 | 0–255 | 136.26 | 105.55 | 73.37 | 72.20 |

## 2. Analisis Histogram RGB

Bin terisi menunjukkan banyaknya tingkat intensitas yang muncul. Modus
menunjukkan puncak histogram pada kanal tersebut. Perataan dilakukan pada
luminansi, sehingga histogram RGB tiap kanal tidak harus menjadi rata.

### `image 1.jpeg`

| Kanal | Bin terisi sebelum → sesudah | Modus sebelum (jumlah pixel) | Modus sesudah (jumlah pixel) | Entropi sebelum → sesudah |
|---|---:|---:|---:|---:|
| Merah | 202 → 254 | 229 (58,471) | 255 (58,328) | 6.983 → 7.604 |
| Hijau | 195 → 255 | 229 (65,324) | 255 (101,110) | 7.078 → 7.683 |
| Biru | 180 → 255 | 229 (101,013) | 255 (100,069) | 7.024 → 7.657 |

### `Image 2.jpeg`

| Kanal | Bin terisi sebelum → sesudah | Modus sebelum (jumlah pixel) | Modus sesudah (jumlah pixel) | Entropi sebelum → sesudah |
|---|---:|---:|---:|---:|
| Merah | 256 → 256 | 156 (140,698) | 67 (147,842) | 7.570 → 7.751 |
| Hijau | 256 → 256 | 157 (152,779) | 6 (103,372) | 7.595 → 7.898 |
| Biru | 256 → 256 | 185 (136,109) | 0 (933,471) | 7.630 → 7.631 |

### `Image 3.jpeg`

| Kanal | Bin terisi sebelum → sesudah | Modus sebelum (jumlah pixel) | Modus sesudah (jumlah pixel) | Entropi sebelum → sesudah |
|---|---:|---:|---:|---:|
| Merah | 256 → 252 | 255 (42,719) | 255 (10,708) | 6.960 → 7.717 |
| Hijau | 256 → 253 | 255 (19,371) | 255 (11,629) | 7.677 → 7.885 |
| Biru | 256 → 252 | 255 (14,494) | 0 (11,721) | 7.830 → 7.785 |

## 3. Statistik Luminansi yang Diratakan

Tabel ini menunjukkan kanal yang benar-benar menjadi masukan proses
perataan histogram. Luminansi Y adalah komponen kecerahan di ruang warna,
bukan gambar grayscale yang ditampilkan sebagai output.

| Gambar | Luminansi | Min–maks | Mean | Std | Bin terisi | Entropi |
|---|---|---:|---:|---:|---:|---:|
| `image 1.jpeg` | Sebelum | 38–230 | 158.20 | 41.18 | 193 | 7.031 |
| `image 1.jpeg` | Sesudah | 1–255 | 128.91 | 74.29 | 144 | 6.893 |
| `Image 2.jpeg` | Sebelum | 0–255 | 146.92 | 60.65 | 256 | 7.607 |
| `Image 2.jpeg` | Sesudah | 0–255 | 128.32 | 73.65 | 185 | 7.368 |
| `Image 3.jpeg` | Sebelum | 0–255 | 159.15 | 79.38 | 256 | 7.704 |
| `Image 3.jpeg` | Sesudah | 3–255 | 128.27 | 73.90 | 192 | 7.437 |

## 4. Kesimpulan

1. Perataan memperluas rentang luminansi untuk `image 1.jpeg` dan mengubah
   sebaran luminansi ketiga gambar. Mean luminansi hasil berada di sekitar
   128–129, sedangkan simpangan bakunya meningkat untuk `image 1.jpeg` dan
   `Image 2.jpeg`; pada `Image 3.jpeg` simpangan baku sedikit menurun.
2. Pada kanal RGB, mean sesudah perataan lebih rendah untuk seluruh gambar.
   Simpangan baku meningkat pada seluruh kanal `image 1.jpeg` dan `Image 2.jpeg`,
   tetapi menurun pada sebagian besar kanal `Image 3.jpeg`. Jadi dampak
   perataan terhadap sebaran pixel berbeda antar gambar.
3. Histogram kanal RGB hasil tidak selalu lebih rata. Contohnya, modus kanal
   biru `Image 2.jpeg` menjadi intensitas 0 dengan 933,471 pixel. Ini tidak
   bertentangan dengan proses: yang diratakan adalah luminansi Y, bukan
   masing-masing kanal RGB secara terpisah, sementara konversi ruang warna
   dan penjagaan Cr/Cb dapat mengubah distribusi RGB hasil.
4. Perbandingan histogram dan statistik menjelaskan perubahan distribusi
   intensitas, tetapi tidak cukup untuk menyimpulkan bahwa kualitas visual
   selalu meningkat. Penilaian visual tetap perlu dilakukan dengan
   membandingkan gambar berwarna sebelum dan sesudah.
