# BAB 9: OOP di Python	
Kelas menyediakan cara untuk menggabungkan data dan fungsionalitas bersama. Membuat kelas baru menciptakan tipe objek baru, yang memungkinkan pembuatan instance baru dari tipe tersebut. Setiap instance kelas dapat memiliki atribut yang terpasang untuk menjaga keadaannya. Instance kelas juga dapat memiliki metode (yang didefinisikan oleh kelasnya) untuk memodifikasi keadaannya. <br />
## Classes
1. Pentingnya Nama dan Objek
Objek memiliki individualitas, dan beberapa nama (dalam beberapa lingkup) dapat diikat ke objek yang sama. Hal ini dikenal sebagai aliasing dalam bahasa pemrograman lain.
2. Lingkup dan Ruang Nama Python
Namespace adalah pemetaan dari nama ke objek. Sebagian besar namespace saat ini diimplementasikan sebagai kamus Python, tetapi hal itu biasanya tidak terlihat dengan cara apa pun (kecuali kinerja), dan ini dapat berubah di masa depan. Contoh-contoh namespace termasuk: himpunan nama bawaan (yang berisi fungsi seperti abs() dan nama pengecualian bawaan); nama-nama global dalam sebuah modul; dan nama-nama lokal dalam pemanggilan fungsi.
3. A First Look at Classes
    - Definisi Sintaks Kelas <br/>
    Kelas adalah salah satu konsep utama dalam pemrograman berorientasi objek (OOP) di Python. Kelas adalah blueprint atau template untuk menciptakan objek. Objek-objek yang dibuat berdasarkan kelas disebut instance. Dalam Python, saat kita mendefinisikan sebuah kelas, kita hanya membuat sebuah blueprint atau template untuk objek yang akan dibuat berdasarkan definisi tersebut. Namun, untuk benar-benar menggunakan kelas dan membuat objek dari kelas tersebut, kita perlu mengeksekusi definisi kelas itu sendiri.
    - Objek Kelas <br/>
    Referensi atribut menggunakan sintaks standar yang digunakan untuk semua referensi atribut di Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di ruang nama kelas saat objek kelas dibuat.
    - Objek Instance <br/>
    Dalam pemrograman berorientasi objek, objek adalah instansi (instance) dari sebuah kelas. Ketika sebuah kelas didefinisikan, hanya membentuk cetak biru atau blueprint untuk objek yang akan dibuat. Ketika objek diciptakan dari kelas, objek tersebut disebut sebagai "instance" dari kelas tersebut.
    - Objek Metode <br/>
    Dalam Python, metode adalah fungsi yang terikat dengan objek tertentu. Ketika suatu metode dipanggil pada objek, objek tersebut secara otomatis menjadi argumen pertama dalam pemanggilan metode. Objek ini kemudian direferensikan melalui parameter "self" di dalam definisi metode.
    - Variabel Kelas dan Variabel Instance <br/>
    Dalam pemrograman berorientasi objek dengan Python, terdapat dua jenis variabel yang umum digunakan: variabel kelas (class variables) dan variabel instance (instance variables). Variabel kelas adalah variabel yang terkait dengan kelas itu sendiri dan dibagikan oleh semua instansiasi objek dari kelas tersebut. Mereka didefinisikan di dalam kelas tetapi di luar metode. Variabel kelas dapat diakses melalui nama kelas atau melalui instansiasi objek dari kelas tersebut. Perubahan pada variabel kelas akan mempengaruhi semua objek yang berasal dari kelas tersebut. Variabel instance, di sisi lain, adalah variabel yang terkait dengan setiap objek yang diinstansiasi dari kelas. Setiap objek memiliki salinan variabel instance sendiri dan perubahan pada variabel instance hanya mempengaruhi objek tersebut.
4. Random Remarks
Atribut data dapat direferensikan oleh metode maupun oleh pengguna biasa ("klien") dari suatu objek. Dengan kata lain, kelas tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni. Nyatanya, tidak ada apa pun dalam Python yang memungkinkan untuk memaksakan penyembunyian data — semuanya didasarkan pada konvensi.
5. Pewarisan
Pewarisan (inheritance) adalah konsep penting dalam pemrograman berorientasi objek di Python. Ini adalah mekanisme di mana sebuah kelas dapat mewarisi atribut dan metode dari kelas lainnya. Dalam pewarisan, kelas yang mewarisi disebut sebagai kelas anak atau subclass, sedangkan kelas yang memberikan warisan disebut sebagai kelas induk atau superclass. Subclass mewarisi semua atribut dan metode yang didefinisikan dalam superclass, dan subclass dapat menambahkan atau mengubah perilaku tersebut sesuai kebutuhannya. <br/>
    - Multiple Inheritance <br/>
    Multiple Inheritance adalah konsep dalam pemrograman Python di mana sebuah kelas dapat mewarisi sifat-sifat dan perilaku dari lebih dari satu kelas induk. Dalam Python, kita dapat membuat kelas turunan yang mewarisi dari beberapa kelas sekaligus. Untuk menggunakan multiple inheritance, kita dapat mendefinisikan kelas turunan dengan menyebutkan kelas-kelas induk yang ingin kita warisi, dipisahkan oleh koma, di dalam tanda kurung setelah nama kelas turunan.
6. Variabel Pribadi
Private variables (variabel pribadi) adalah variabel yang memiliki konvensi penamaan tertentu untuk menandakan bahwa variabel tersebut seharusnya hanya diakses secara internal oleh sebuah kelas atau objek. Dalam Python, konvensi yang umum digunakan adalah dengan menggunakan awalan garis bawah ganda (underscore) sebelum nama variabel, misalnya "_nama_variabel".
7. Odds and Ends
Kadang-kadang berguna untuk memiliki jenis data yang mirip dengan "record" dalam Pascal atau "struct" dalam C, yang menggabungkan beberapa item data yang memiliki nama.
8. Iterators
Dalam Python, iterator adalah objek yang mengimplementasikan metode khusus seperti __iter__() dan __next__() yang memungkinkan iterasi melalui elemen-elemen koleksi secara sekuensial. Iterator dapat digunakan untuk mengambil elemen-elemen satu per satu dari struktur data seperti daftar (list), tupel (tuple), set, atau objek-objek kustom yang kita definisikan sendiri.
9. Generator
Generator dalam Python adalah fungsi khusus yang menghasilkan serangkaian nilai secara bertahap. Mereka digunakan untuk menghasilkan nilai secara efisien satu per satu, bukan menghasilkan semua nilai dalam satu waktu. Generator dapat membantu menghemat memori dan waktu eksekusi.
10. Ekspresi Generator
Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaks yang mirip dengan pemahaman daftar tetapi dengan tanda kurung, bukan tanda kurung siku. Ekspresi ini dirancang untuk situasi di mana generator langsung digunakan oleh fungsi penutup. Ekspresi generator lebih kompak tetapi kurang fleksibel daripada definisi generator lengkap dan cenderung lebih ramah memori daripada pemahaman daftar yang setara.
    
