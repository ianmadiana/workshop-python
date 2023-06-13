# BAB 10: Standard Library
1.  Antarmuka Sistem Operasi
    Operating System Interface mengacu pada modul yang digunakan untuk berinteraksi dengan sistem operasi. Modul yang paling umum digunakan untuk antarmuka sistem operasi di Python adalah os (operating system). Modul os menyediakan fungsi-fungsi yang memungkinkan Anda untuk melakukan berbagai tugas pada tingkat sistem operasi, seperti mengelola file dan direktori, menjalankan perintah shell, mengakses lingkungan sistem, dan sebagainya.
2.  File Wildcards
    File wildcards dalam Python adalah pola yang digunakan untuk mencocokkan atau memilih beberapa file berdasarkan pola yang diberikan. Dalam Python, modul glob digunakan untuk bekerja dengan file wildcards.
3.  Command Line Arguments
    Command Line Arguments dalam Python adalah argumen-argumen atau nilai-nilai yang diberikan ke sebuah program Python saat program tersebut dijalankan melalui baris perintah (command line). Argumen-argumen ini dapat digunakan untuk memberikan input, pengaturan, atau parameter tambahan kepada program. Dalam Python, kita dapat mengakses command line arguments melalui modul bawaan sys.
4.  Error Output Redirection and Program Termination
    Dalam Python, "Error Output Redirection" mengacu pada proses mengarahkan output kesalahan (error output) dari suatu program ke tempat lain, seperti file atau aliran (stream) lainnya, daripada ditampilkan di konsol atau terminal. Sementara itu, "Program Termination" merujuk pada penghentian program secara tiba-tiba atau normal. Dalam Python, Anda dapat menggunakan pernyataan sys.exit() untuk menghentikan program dengan mengembalikan nilai keluaran yang ditentukan.
5.  Pencocokan Pola String
    String Pattern Matching adalah proses mencocokkan pola tertentu dalam sebuah string. Di Python, terdapat beberapa metode dan modul yang dapat digunakan untuk melakukan string pattern matching, antara lain:
    - Metode find(): Metode ini digunakan untuk mencari indeks pertama kali kemunculan sebuah substring dalam sebuah string.
    - Modul re: Modul re (regular expression) digunakan untuk mencocokkan pola dengan menggunakan ekspresi reguler (regular expression).
    - Metode startswith() dan endswith(): Metode startswith() digunakan untuk memeriksa apakah sebuah string diawali dengan substring tertentu, sedangkan metode endswith() digunakan untuk memeriksa apakah sebuah string diakhiri dengan substring tertentu.
    - Metode split(): Metode split() digunakan untuk memisahkan string berdasarkan delimiter tertentu dan mengembalikan hasilnya sebagai list.
6.  Mathematics
    Matematika adalah salah satu aspek penting dalam pemrograman dengan Python. Python menyediakan berbagai modul dan fungsi matematika yang dapat digunakan untuk melakukan operasi matematika secara efisien.
7.  Internet Access
    Untuk mengakses internet menggunakan Python, Anda dapat menggunakan modul urllib.request untuk mengambil data dari URL dan modul smtplib untuk mengirim email melalui protokol SMTP.
8.  Dates and Times
    Modul datetime digunakan untuk bekerja dengan tanggal dan waktu. Modul ini menyediakan kelas-kelas dan fungsi-fungsi yang memungkinkan manipulasi, format, dan pemrosesan tanggal dan waktu.
9.  Data Compression
    Di Python, terdapat beberapa modul dan pustaka yang dapat digunakan untuk melakukan kompresi data. Dua modul yang umum digunakan adalah gzip dan zipfile.
10. Performance Measurement
    Modul timeit dalam Python digunakan untuk melakukan pengukuran kinerja atau performa suatu kode atau fungsi. Modul ini menyediakan fungsi yang memungkinkan pengukuran waktu eksekusi dengan presisi yang tinggi. Dengan menggunakan timeit, kita dapat membandingkan kinerja atau performa antara beberapa implementasi kode atau fungsi yang berbeda dan menentukan yang mana yang lebih efisien dalam hal waktu eksekusi.
11. Quality Control
    Quality Control Doctest adalah sebuah pendekatan dalam pengujian perangkat lunak yang menggunakan dokumen dokumentasi sebagai tes langsung. Pada Python, Doctest adalah modul bawaan yang memungkinkan pengujian kode Python dilakukan melalui contoh-contoh dalam dokumen string. Doctest secara otomatis mengekstraksi contoh-contoh dari dokumen string dan menjalankannya sebagai tes. Ini membantu untuk memastikan bahwa contoh-contoh tersebut memberikan hasil yang diharapkan dan berfungsi sebagaimana mestinya.
12. Batteries Included
    "Batteries Included" adalah istilah yang sering digunakan untuk menggambarkan kekayaan dan kelengkapan modul-modul dan pustaka standar yang disediakan oleh Python. Istilah ini mengacu pada fakta bahwa Python memiliki banyak modul dan pustaka yang sudah disertakan secara default dalam instalasi Python, sehingga pengguna dapat langsung menggunakannya tanpa perlu menginstal atau mengunduh modul tambahan. Dengan demikian, Python dikenal sebagai bahasa pemrograman yang "Batteries Included" karena menyediakan banyak alat dan pustaka yang sudah siap pakai, yang membantu pengguna untuk mengembangkan aplikasi dengan lebih cepat dan efisien.

# BAB 11: Standard Library Part II
1.  Output Formatting
    - Modul reprlib: Modul ini menyediakan fungsi repr() yang dapat digunakan untuk menghasilkan representasi teks terbatas dari objek. Ini berguna ketika Anda ingin menghasilkan representasi yang lebih ringkas dari objek yang kompleks, seperti daftar atau struktur data yang dalam.
    - Modul pprint: Modul ini menyediakan fungsi pprint() (pretty print) yang dapat digunakan untuk mencetak struktur data secara lebih rapi dan mudah dibaca. Fungsi ini berguna ketika Anda ingin mencetak struktur data yang kompleks dengan pemformatan yang baik.
    - Modul textwrap: Modul ini menyediakan fungsi-fungsi yang berguna untuk memformat teks menjadi paragraf dengan lebar yang ditentukan dan pemformatan lainnya.
    - Modul locale: Modul ini menyediakan fungsi-fungsi untuk pemformatan numerik berdasarkan pengaturan lokal yang berlaku pada sistem operasi. Ini berguna ketika Anda ingin memformat angka dengan pemisah ribuan, simbol desimal, dan konvensi lain yang sesuai dengan pengaturan lokal.
2.  Templating
    Modul string menyertakan kelas Templat serbaguna dengan sintaks sederhana yang cocok untuk diedit oleh pengguna akhir. Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi. Formatnya menggunakan nama placeholder yang dibentuk oleh $ dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengelilingi placeholder dengan tanda kurung memungkinkannya diikuti oleh lebih banyak huruf alfanumerik tanpa spasi.
3.  Bekerja dengan Tata Letak Rekaman Data Biner
    Modul struct menyediakan fungsi pack() dan unpack() untuk bekerja dengan format rekaman biner dengan panjang variabel. Contoh berikut menunjukkan cara mengulang informasi header dalam file ZIP tanpa menggunakan modul zipfile. Kode paket "H" dan "I" masing-masing mewakili dua dan empat byte angka yang tidak ditandatangani.
4.  Multi-threading
    Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Utas dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima input pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait sedang menjalankan I/O secara paralel dengan perhitungan di utas lainnya.
5.  Logging
    Modul logging menawarkan sistem logging berfitur lengkap dan fleksibel. Paling sederhana, pesan log dikirim ke file atau ke sys.stderr. Secara default, pesan informasi dan debug disembunyikan dan output dikirim ke kesalahan standar. Opsi keluaran lainnya termasuk merutekan pesan melalui email, datagram, soket, atau ke Server HTTP. Filter baru dapat memilih rute yang berbeda berdasarkan prioritas pesan: DEBUG, INFO, WARNING, ERROR, dan CRITICAL.
6.  Weak References
    Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus). Memori dibebaskan segera setelah referensi terakhir untuk itu telah dihilangkan.
7.  Alat untuk Bekerja dengan Lists
    Banyak kebutuhan struktur data dapat dipenuhi dengan tipe daftar bawaan. Namun, terkadang ada kebutuhan untuk penerapan alternatif dengan pertukaran kinerja yang berbeda:
    - Modul array menyediakan objek array() yang seperti daftar yang hanya menyimpan data homogen dan menyimpannya dengan lebih kompak.
    - Modul collections menyediakan objek deque() yang seperti daftar dengan penambahan lebih cepat dan muncul dari sisi kiri tetapi pencarian lebih lambat di tengah.
    - Modul heapq menyediakan fungsi untuk mengimplementasikan tumpukan berdasarkan daftar reguler. Entri bernilai terendah selalu disimpan di posisi nol.
8.  Decimal Floating Point Arithmetic
    Modul desimal menawarkan tipe data Desimal untuk aritmatika floating point desimal.
    - aplikasi keuangan dan penggunaan lain yang membutuhkan representasi desimal yang tepat,
    - kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan,
    - pelacakan tempat desimal yang signifikan, atau
    - aplikasi di mana pengguna mengharapkan hasil untuk mencocokkan perhitungan yang dilakukan manual.
