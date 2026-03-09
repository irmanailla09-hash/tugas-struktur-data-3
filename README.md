# tugas-struktur-data-3
Soal 1 – Modified Binary Search

Pada soal pertama dibuat sebuah fungsi yang digunakan untuk mengetahui berapa kali suatu nilai muncul dalam sebuah daftar data yang sudah tersusun secara berurutan. Metode yang digunakan adalah Binary Search yang telah dimodifikasi.
Binary Search merupakan algoritma pencarian yang bekerja dengan cara membagi data menjadi dua bagian secara berulang hingga nilai yang dicari ditemukan. Pada kasus ini, proses pencarian dilakukan dua kali. Pencarian pertama bertujuan untuk menemukan posisi kemunculan pertama dari nilai yang dicari, sedangkan pencarian kedua digunakan untuk mencari posisi kemunculan terakhir.
Setelah kedua posisi tersebut diketahui, jumlah kemunculan nilai dapat dihitung dengan cara mencari selisih antara posisi terakhir dan posisi pertama, kemudian ditambah satu.
Penggunaan metode ini membuat proses pencarian menjadi lebih efisien karena memiliki kompleksitas waktu O(log n) sehingga tidak perlu memeriksa seluruh elemen data satu per satu.

Soal 2 – Bubble Sort dengan Analisis Langkah

Pada soal kedua digunakan algoritma Bubble Sort untuk mengurutkan data. Bubble Sort merupakan salah satu metode pengurutan yang sederhana, di mana prosesnya dilakukan dengan membandingkan dua elemen yang berdekatan lalu menukarnya jika urutannya tidak sesuai.
Proses perbandingan ini dilakukan secara berulang dalam beberapa putaran sampai seluruh elemen berada pada urutan yang benar.
Dalam implementasi ini juga dihitung beberapa hal penting, yaitu jumlah perbandingan yang terjadi, jumlah pertukaran data yang dilakukan, serta jumlah putaran yang diperlukan untuk menyelesaikan proses pengurutan.
Selain itu diterapkan juga teknik early termination, yaitu kondisi di mana proses pengurutan dapat dihentikan lebih awal jika dalam satu putaran tidak terjadi pertukaran data. Hal tersebut menandakan bahwa data sudah berada dalam keadaan terurut sehingga tidak perlu melanjutkan proses berikutnya.

Soal 3 – Hybrid Sort

Pada soal ketiga dibuat sebuah algoritma pengurutan yang disebut Hybrid Sort. Algoritma ini merupakan kombinasi dari dua metode pengurutan yang berbeda, yaitu Insertion Sort dan Selection Sort.
Prinsip kerja Hybrid Sort adalah memilih metode pengurutan yang paling sesuai berdasarkan ukuran data yang akan diurutkan. Jika jumlah elemen relatif kecil, maka algoritma akan menggunakan Insertion Sort karena metode ini lebih efisien untuk data berukuran kecil. Sebaliknya, jika jumlah data lebih besar, maka algoritma akan menggunakan Selection Sort.
Setelah proses pengurutan selesai dilakukan, program juga menghitung jumlah operasi yang terjadi selama proses berlangsung, seperti jumlah perbandingan dan jumlah pertukaran elemen.
Penggabungan dua algoritma ini bertujuan untuk memperoleh performa pengurutan yang lebih baik dengan memanfaatkan kelebihan dari masing-masing metode.

Soal 4 – Menggabungkan Tiga Sorted List

Pada soal keempat dibuat fungsi yang bertugas untuk menggabungkan tiga buah daftar data yang sudah terurut menjadi satu daftar baru yang tetap terurut.
Proses penggabungan dilakukan dengan menggunakan tiga penunjuk atau pointer yang masing-masing menunjuk ke posisi elemen pada setiap list. Ketiga elemen yang sedang ditunjuk kemudian dibandingkan untuk menentukan nilai yang paling kecil.
Nilai terkecil tersebut kemudian dimasukkan ke dalam daftar hasil. Setelah itu, pointer pada list yang elemennya dipilih akan digeser ke posisi berikutnya. Proses ini terus dilakukan hingga seluruh elemen dari ketiga list telah diproses.
Metode ini cukup efisien karena setiap elemen hanya diperiksa satu kali, sehingga kompleksitas waktunya adalah O(n).

Soal 5 – Inversion Counter

Pada soal terakhir dihitung jumlah inversion yang terdapat dalam sebuah array. Inversion adalah pasangan dua indeks di mana elemen yang berada di posisi sebelumnya memiliki nilai lebih besar daripada elemen yang berada setelahnya.
Sebagai contoh, pada data [3, 1, 2], pasangan (3,1) dan (3,2) termasuk inversion karena angka yang lebih besar muncul sebelum angka yang lebih kecil.
Untuk menyelesaikan permasalahan ini digunakan dua pendekatan yang berbeda.
Pendekatan pertama adalah metode naive, yaitu dengan membandingkan setiap elemen dengan seluruh elemen yang berada setelahnya. Jika ditemukan kondisi di mana elemen pertama lebih besar, maka dihitung sebagai satu inversion. Metode ini cukup sederhana namun memiliki kompleksitas waktu O(n²) sehingga kurang efisien untuk data berukuran besar.
Pendekatan kedua menggunakan algoritma Merge Sort yang dimodifikasi. Dalam metode ini, perhitungan inversion dilakukan pada saat proses penggabungan dua bagian array. Cara ini jauh lebih efisien karena memiliki kompleksitas waktu O(n log n).
Dengan demikian, untuk jumlah data yang besar, metode merge sort akan memberikan kinerja yang jauh lebih cepat dibandingkan metode naive.
