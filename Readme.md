# Sequran AI

Mesin Pencari Al-Quran menggunakan Bahasa Python, FastAPI, dan Machine Learning (Cosine Similarity).

### Deskripsi Project

Project ini bertujuan untuk membuat sebuah mesin pencari Al-Quran yang memanfaatkan bahasa pemrograman Python, framework FastAPI, dan algoritma Machine Learning (Cosine Similarity). Mesin pencari ini akan memungkinkan pengguna untuk mencari terjemahan dalam Al-Quran berdasarkan kata kunci yang diberikan.

### Demo Aplikasi

```bash
http://135.181.26.148:25117/search?query={keyword}

Contoh:
http://135.181.26.148:25117/search?query=iman
http://135.181.26.148:25117/search?query=takwa
```

[Video Penjelasan](https://youtu.be/gZ5Z6Lv1qsU)
[Link Docker Image](https://hub.docker.com/r/ramadita12/sequran-ai)

### Penggunaan Sistem Operasi dalam Proses Containseraization

Sistem operasi memainkan peran penting dalam proses containerization, terutama dalam hal menjalankan dan mengisolasi kontainer. Berikut adalah penjelasan tentang bagaimana sistem operasi digunakan dalam proses containerization:

<details>
<summary>Click to expand</summary>

- **Kernel Linux**: Containerization umumnya menggunakan kernel Linux sebagai dasar untuk menjalankan kontainer. Kernel Linux menyediakan fitur-fitur penting seperti kontrol sumber daya, isolasi, dan pemisahan antarproses yang diperlukan untuk menjalankan kontainer dengan aman dan efisien.

- **Namespace**: Kernel Linux menggunakan konsep "namespace" untuk mengisolasi sumber daya sistem antara kontainer. Namespace memungkinkan setiap kontainer memiliki tampilan terisolasi dari sistem operasi, termasuk ruang nama proses, ruang nama jaringan, sistem berkas, dan lain-lain. Dengan demikian, kontainer tidak dapat melihat atau berinteraksi langsung dengan sumber daya yang ada di luar kontainer tersebut.

- **Cgroups**: Cgroups (control groups) adalah fitur kernel Linux yang memungkinkan pengaturan dan pembatasan sumber daya yang digunakan oleh setiap kontainer. Dengan menggunakan cgroups, kita dapat mengatur batasan CPU, memori, I/O (Input/Output), dan sumber daya lainnya untuk masing-masing kontainer. Hal ini penting untuk memastikan setiap kontainer berjalan dengan sumber daya yang terisolasi dan adil.

- **Filesystem**: Sistem operasi juga berperan dalam mengelola sistem berkas yang digunakan oleh kontainer. Kontainer umumnya menggunakan sistem berkas yang berbeda dari sistem operasi host, dan sistem berkas kontainer dapat dibangun menggunakan teknologi seperti OverlayFS atau AUFS. Sistem berkas ini memungkinkan setiap kontainer memiliki tampilan terisolasi dari sistem berkas yang mereka gunakan, sehingga masing-masing kontainer dapat memiliki salinan sendiri dari berkas konfigurasi, pustaka, dan kode aplikasi.

- **Image dan Container Runtime**: Sistem operasi juga berperan dalam menjalankan image dan kontainer. Image kontainer biasanya dibangun di atas sistem operasi dasar, seperti image Alpine Linux atau Ubuntu. Ketika kontainer dijalankan, runtime kontainer seperti Docker, containerd, atau Kubernetes akan menggunakan image sebagai dasar untuk membuat instance yang berjalan dalam kontainer. Runtime kontainer bertanggung jawab atas pengelolaan siklus hidup kontainer, termasuk pembuatan, penghentian, dan penghapusan kontainer.

</details>

Secara keseluruhan, sistem operasi menyediakan fondasi yang kuat untuk menjalankan kontainer dengan aman, mengisolasi sumber daya antara kontainer, dan menyediakan fitur-fitur penting seperti pengaturan sumber daya dan manajemen sistem berkas. Dengan menggunakan fitur-fitur ini, proses containerization dapat dilakukan dengan efisien dan dapat diandalkan.

### Peran Containseraization dalam Mempermudah Pengembangan Aplikasi

Containerization membantu mempermudah pengembangan aplikasi dengan beberapa cara:

<details> 
<summary>Click to expand</summary>

1. **Portabilitas**: Dengan containerization, aplikasi dan dependensinya dikemas dalam kontainer yang dapat dijalankan secara konsisten di berbagai lingkungan, baik di mesin pengembangan, uji coba, maupun produksi. Kontainer menyediakan lingkungan yang terisolasi dan independen, sehingga memungkinkan pengembang untuk dengan mudah memindahkan aplikasi dari satu lingkungan ke lingkungan lain tanpa khawatir tentang perbedaan konfigurasi dan dependensi sistem yang mungkin ada.

2. **Konsistensi**: Dalam pengembangan aplikasi, penting untuk memastikan bahwa lingkungan pengembangan, pengujian, dan produksi serupa agar dapat menghindari masalah yang timbul karena perbedaan konfigurasi. Dengan containerization, pengembang dapat memastikan bahwa aplikasi dijalankan dalam lingkungan yang serupa di semua tahap siklus pengembangan. Hal ini membantu mencegah masalah yang terkait dengan ketidakkonsistenan dan memungkinkan tim pengembang untuk fokus pada pengembangan aplikasi itu sendiri.

3. **Replikasi Lingkungan**: Containerisasi memungkinkan pengembang untuk dengan mudah menduplikasi lingkungan yang sama di beberapa mesin atau mesin virtual. Ini memudahkan kolaborasi antara anggota tim pengembang, karena setiap pengembang dapat dengan mudah mengatur dan menjalankan lingkungan yang sama dengan yang digunakan oleh tim lainnya. Replikasi lingkungan juga memungkinkan pengujian dan debug aplikasi dalam lingkungan yang identik dengan produksi.

4. **Skalabilitas**: Dalam kontainer, aplikasi dapat dikemas bersama dengan dependensinya dalam unit yang dapat diperbesar secara horizontal. Ini berarti pengembang dapat dengan mudah menambah atau mengurangi jumlah kontainer yang berjalan sesuai dengan kebutuhan aplikasi. Dengan skalabilitas yang mudah, pengembang dapat merespons dengan cepat terhadap perubahan beban kerja dan memastikan ketersediaan yang baik serta performa aplikasi yang optimal.

5. **Manajemen Dependensi**: Containerization memungkinkan pengembang untuk mengemas semua dependensi aplikasi, termasuk pustaka dan perangkat lunak lainnya, dalam kontainer. Ini membantu dalam mengatasi masalah dependensi yang kompleks dan meminimalkan konflik yang mungkin terjadi antara versi perangkat lunak yang berbeda. Pengembang dapat memastikan bahwa setiap kontainer memiliki dependensi yang tepat dan bekerja secara terisolasi dari dependensi sistem yang ada.

</details>

Dalam keseluruhan, containerization membantu mempermudah pengembangan aplikasi dengan menyediakan portabilitas, konsistensi, replikasi lingkungan, skalabilitas, dan manajemen dependensi yang lebih baik. Ini memungkinkan pengembang untuk fokus pada pengembangan aplikasi itu sendiri dan mempercepat proses pengiriman aplikasi yang stabil dan dapat diandalkan.

### Peran DevOps dalam Proses Pengembangan Aplikasi

DevOps adalah sebuah pendekatan atau filosofi dalam pengembangan perangkat lunak yang menggabungkan praktik-praktik pengembangan (Development) dan operasional (Operations) secara erat. Tujuan utama dari DevOps adalah mempercepat dan meningkatkan kualitas pengiriman perangkat lunak melalui kerjasama antara tim pengembang dan tim operasional.

DevOps membantu pengembangan aplikasi dengan beberapa cara berikut:

<details>
<summary>Click to expand</summary>

1. **Kolaborasi Tim**: DevOps mendorong kolaborasi yang erat antara tim pengembang dan tim operasional. Dalam model tradisional, tim pengembang dan tim operasional bekerja secara terpisah dan jarang berinteraksi. Dalam DevOps, kedua tim bekerja bersama-sama sepanjang siklus hidup aplikasi. Kolaborasi yang lebih dekat ini memungkinkan pertukaran pengetahuan, pemahaman yang lebih baik tentang kebutuhan operasional, dan pemecahan masalah yang lebih cepat. Tim pengembang dan tim operasional saling mendukung dan berkontribusi untuk meningkatkan kualitas dan keandalan aplikasi.

2. **Otomatisasi**: DevOps mendorong otomatisasi dalam proses pengembangan dan pengiriman aplikasi. Otomatisasi membantu mengurangi kesalahan manusia, meningkatkan efisiensi, dan mempercepat waktu pengiriman. Contohnya, otomatisasi dapat digunakan untuk mengotomatiskan proses pengujian, integrasi kontinu, dan penyebaran aplikasi. Dengan menggunakan alat-alat otomatisasi yang tepat, pengembang dapat dengan mudah mengulang pengujian, mengotomatiskan penyebaran aplikasi ke lingkungan produksi, dan meningkatkan keandalan dan stabilitas aplikasi.

3. **Pengiriman Terus-Menerus**: DevOps mendorong pengiriman aplikasi secara terus-menerus (continuous delivery) atau pengiriman terus-menerus (continuous deployment). Ini berarti pengembang bekerja untuk membuat proses pengiriman aplikasi menjadi lebih otomatis dan dapat diulang secara konsisten. Dengan pengiriman terus-menerus, setiap perubahan yang dilakukan dalam kode sumber dapat diuji dan diimplementasikan secara otomatis dan cepat. Hal ini mengurangi risiko dan waktu yang diperlukan untuk memperkenalkan perubahan ke dalam produksi. Pengiriman terus-menerus memungkinkan pengembang untuk lebih responsif terhadap kebutuhan bisnis dan mempercepat waktu pemasaran aplikasi.

4. **Monitoring dan Responsif**: DevOps mendorong penggunaan alat pemantauan dan tindakan responsif yang kuat untuk mendeteksi dan menangani masalah operasional secara cepat. Tim pengembang dan tim operasional bekerja bersama untuk memastikan bahwa sistem dan aplikasi berjalan dengan baik di lingkungan produksi. Dengan pemantauan yang baik, masalah dapat diidentifikasi lebih awal dan tindakan responsif dapat diambil untuk memperbaiki masalah tersebut. Hal ini membantu meningkatkan keandalan dan performa aplikasi secara keseluruhan.
</details>

Dalam keseluruhan, DevOps membantu pengembangan aplikasi dengan memfasilitasi kolaborasi tim, mendorong otomatisasi, mengadopsi pengiriman terus-menerus, dan mengedepankan pemantauan dan responsif yang efektif. Dengan menerapkan pendekatan DevOps, tim pengembang dapat menghasilkan aplikasi yang lebih berkualitas, dapat diandalkan, dan dengan cepat merespons perubahan kebutuhan bisnis.

### Contoh Kasus Penerapan DevOps di Aplikasi Netflix

Salah satu contoh kasus penerapan DevOps yang terkenal adalah di Netflix. Netflix adalah perusahaan hiburan digital yang populer, yang menyediakan layanan streaming konten seperti film, acara TV, dan dokumenter kepada pelanggan di seluruh dunia. Di bawah ini adalah contoh bagaimana Netflix menerapkan DevOps dalam praktik pengembangan dan pengiriman aplikasinya:

<details>
<summary>Click to expand</summary>

1. **Kolaborasi Tim**: Di Netflix, tim pengembang perangkat lunak dan tim operasional bekerja secara erat dan berkolaborasi. Mereka memiliki sistem yang dikenal sebagai "You Build It, You Run It" yang mendorong pemilik produk untuk mengambil tanggung jawab penuh terhadap pengembangan, pengujian, dan pengiriman aplikasi mereka. Hal ini memastikan transparansi dan kolaborasi antara tim pengembang dan tim operasional dalam siklus pengembangan aplikasi.

2. **Otomatisasi dan Infrastruktur sebagai Kode**: Netflix memanfaatkan otomatisasi untuk mengotomatiskan berbagai aspek dalam siklus hidup pengembangan aplikasi. Mereka menggunakan praktik Infrastruktur sebagai Kode (Infrastructure as Code) untuk mengelola dan menyebarkan infrastruktur mereka. Netflix menggunakan alat-alat seperti Spinnaker (alat manajemen penyebaran) dan Simian Army (alat pengujian ketahanan) untuk mempercepat dan mengotomatiskan pengujian, penyebaran, dan pemulihan aplikasi mereka.

3. **Pengiriman Terus-Menerus**: Netflix menerapkan pengiriman terus-menerus untuk mempercepat waktu pengiriman perubahan aplikasi mereka. Mereka menggunakan sistem pengujian otomatis yang kuat untuk memastikan bahwa setiap perubahan diuji secara menyeluruh sebelum diterapkan ke produksi. Pengiriman terus-menerus ini memungkinkan Netflix untuk merilis perubahan ke aplikasi mereka dengan cepat, dengan minimal risiko dan dampak negatif terhadap pengguna.

4. **Arsitektur Microservice**: Netflix menerapkan arsitektur microservice yang terdiri dari banyak layanan yang dapat diskalakan secara independen. Setiap tim pengembang bertanggung jawab atas satu atau beberapa layanan mikro, yang memungkinkan mereka untuk mengembangkan, menguji, dan memperbarui layanan secara independen. Dengan menggunakan kontainer dan alat orkestrasi seperti Docker dan Kubernetes, Netflix dapat mengelola, mendistribusikan, dan memperbarui layanan mereka dengan mudah dan efisien.

5. **Pemantauan dan Responsif**: Netflix memiliki sistem pemantauan yang kuat untuk memantau performa aplikasi dan infrastruktur mereka. Mereka menggunakan alat pemantauan real-time dan analisis data untuk mendeteksi masalah secara cepat. Jika ada masalah yang terdeteksi, tim operasional secara responsif menangani masalah tersebut dan mengambil tindakan pemulihan dengan cepat untuk memastikan kelancaran pengiriman konten kepada pelanggan.

</details>

Penerapan DevOps di Netflix membantu perusahaan tersebut untuk secara efisien mengelola infrastruktur yang kompleks, meningkatkan kecepatan pengiriman, dan menjaga kualitas serta keandalan layanan yang mereka berikan kepada pelanggan.
