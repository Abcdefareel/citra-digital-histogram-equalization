# Laporan Analisis Histogram Tiga Gambar

## Tujuan dan Metode

Laporan ini membandingkan histogram dan nilai pixel pada tiga gambar sebelum
dan sesudah perataan histogram. Perataan diterapkan pada luminansi **Y** dalam
ruang warna YCrCb, sementara kanal warna Cr dan Cb dipertahankan. Hasil
dikembalikan ke warna; histogram merah, hijau, dan biru (RGB) dihitung untuk
gambar asli maupun hasil perataan.

Frekuensi pada histogram adalah jumlah pixel pada tingkat intensitas tertentu
(0–255). Rentang, mean, dan simpangan baku dihitung per kanal RGB. Hasil
perataan yang disimpan telah diverifikasi cocok dengan algoritma di
`praktikum_histogram.py`.

## Ringkasan Perubahan Statistik RGB

Angka pada kolom mean dan simpangan baku adalah intensitas RGB pada skala 0–255.

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

## Perbandingan Histogram dan Frekuensi

Tabel berikut menunjukkan jumlah tingkat intensitas yang terisi, puncak
(modus) histogram, frekuensi pixel pada modus, dan entropi untuk tiap kanal.
Entropi menunjukkan keragaman distribusi, bukan kualitas visual secara
langsung.

### `image 1.jpeg`

| Kanal | Bin terisi sebelum → sesudah | Modus sebelum (frekuensi) | Modus sesudah (frekuensi) | Entropi sebelum → sesudah |
|---|---:|---:|---:|---:|
| Merah | 202 → 254 | 229 (58,471) | 255 (58,328) | 6.983 → 7.604 |
| Hijau | 195 → 255 | 229 (65,324) | 255 (101,110) | 7.078 → 7.683 |
| Biru | 180 → 255 | 229 (101,013) | 255 (100,069) | 7.024 → 7.657 |

### `Image 2.jpeg`

| Kanal | Bin terisi sebelum → sesudah | Modus sebelum (frekuensi) | Modus sesudah (frekuensi) | Entropi sebelum → sesudah |
|---|---:|---:|---:|---:|
| Merah | 256 → 256 | 156 (140,698) | 67 (147,842) | 7.570 → 7.751 |
| Hijau | 256 → 256 | 157 (152,779) | 6 (103,372) | 7.595 → 7.898 |
| Biru | 256 → 256 | 185 (136,109) | 0 (933,471) | 7.630 → 7.631 |

### `Image 3.jpeg`

| Kanal | Bin terisi sebelum → sesudah | Modus sebelum (frekuensi) | Modus sesudah (frekuensi) | Entropi sebelum → sesudah |
|---|---:|---:|---:|---:|
| Merah | 256 → 252 | 255 (42,719) | 255 (10,708) | 6.960 → 7.717 |
| Hijau | 256 → 253 | 255 (19,371) | 255 (11,629) | 7.677 → 7.885 |
| Biru | 256 → 252 | 255 (14,494) | 0 (11,721) | 7.830 → 7.785 |

### Tabel Frekuensi Lengkap (256 Intensitas)

Untuk melihat frekuensi **setiap intensitas 0–255** sebelum dan sesudah
perataan pada ketiga kanal RGB, buka [tabel frekuensi lengkap (CSV)](./hasil/frekuensi_histogram_rgb.csv).
CSV tersebut berisi 256 baris intensitas dan 18 kolom frekuensi: kanal merah,
hijau, dan biru sebelum serta sesudah untuk masing-masing dari tiga gambar.
Jumlah frekuensi pada setiap kanal sama dengan jumlah pixel gambar.

### Grafik Perbandingan Sebelum dan Sesudah

#### `image 1.jpeg`

![Grafik perbandingan histogram image 1](<./hasil/perbandingan_image 1.jpeg.png>)

#### `Image 2.jpeg`

![Grafik perbandingan histogram Image 2](<./hasil/perbandingan_Image 2.jpeg.png>)

#### `Image 3.jpeg`

![Grafik perbandingan histogram Image 3](<./hasil/perbandingan_Image 3.jpeg.png>)

## Statistik Luminansi

Luminansi Y adalah kanal yang benar-benar diratakan dalam proses ini.

| Gambar | Kondisi | Min–maks | Mean | Std | Bin terisi | Entropi |
|---|---|---:|---:|---:|---:|---:|
| `image 1.jpeg` | Sebelum | 38–230 | 158.20 | 41.18 | 193 | 7.031 |
| `image 1.jpeg` | Sesudah | 1–255 | 128.91 | 74.29 | 144 | 6.893 |
| `Image 2.jpeg` | Sebelum | 0–255 | 146.92 | 60.65 | 256 | 7.607 |
| `Image 2.jpeg` | Sesudah | 0–255 | 128.32 | 73.65 | 185 | 7.368 |
| `Image 3.jpeg` | Sebelum | 0–255 | 159.15 | 79.38 | 256 | 7.704 |
| `Image 3.jpeg` | Sesudah | 3–255 | 128.27 | 73.90 | 192 | 7.437 |

## Kesimpulan

1. Setelah perataan, mean luminansi ketiga gambar berada di sekitar 128–129.
   Simpangan baku luminansi meningkat pada `image 1.jpeg` dan `Image 2.jpeg`,
   sedangkan pada `Image 3.jpeg` sedikit menurun.
2. Mean RGB hasil lebih rendah pada ketiga gambar. Simpangan baku RGB meningkat
   pada semua kanal `image 1.jpeg` dan `Image 2.jpeg`, tetapi menurun pada
   sebagian besar kanal `Image 3.jpeg`.
3. Histogram RGB hasil tidak selalu lebih rata. Misalnya, modus kanal biru
   `Image 2.jpeg` sesudah perataan berada pada intensitas 0 dengan 933,471
   pixel. Hal ini dapat terjadi karena yang diratakan adalah luminansi Y,
   bukan masing-masing kanal RGB.
4. Perubahan distribusi intensitas tidak dengan sendirinya membuktikan bahwa
   kualitas visual meningkat. Hasil tetap perlu dinilai dengan membandingkan
   gambar sebelum dan sesudah.
