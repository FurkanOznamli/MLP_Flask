🧠 Sigorta Ücreti Tahmin Modeli
Machine Learning (Multiple Linear Regression) + Flask Web Uygulaması
🖼 Proje Önizlemesi

Buraya arayüzün ekran görüntüsünü koy:
📌 Önerilen dosya adı: static/ui_screenshot.png

<img width="1918" height="916" alt="image" src="https://github.com/user-attachments/assets/ffb44bca-5a75-47d3-9c5f-69f803add11e" />


🎯 Projenin Amacı

Bu projede sağlık sigortası ücretini tahmin etmek için:

1️⃣ Çoklu Doğrusal Regresyon (Multiple Linear Regression) modeli kuruldu.
2️⃣ Model .pkl formatında kaydedildi.
3️⃣ Flask tabanlı bir web arayüzü ile kullanıcıdan veri alınıp gerçek zamanlı tahmin yapılması sağlandı.

Veri bilimi sürecinin tüm aşamaları .ipynb dosyasında açıklamalı olarak gösterilmiştir.

1️⃣ Veri Ön İşleme (Data Preprocessing)
📌 Öznitelik (Feature) Seçimi

Kullandığım veri setinde şu öznitelikler bulunuyordu:

age → yaş

bmi → vücut kitle indeksi

children → çocuk sayısı

sex → cinsiyet

smoker → sigara içiyor mu

region → bölge

charges → hedef değişken (sigorta ücreti)

Bu özniteliklerin hepsi anlamlı olduğu için veri setinden çıkarılacak “gereksiz” bir kolon yoktu.
Ayrıca öznitelik sayısı 7 olup ödev gereği belirlenen maksimum 10 sınırının içerisindedir.

📌 Kayıp Veri (Missing Values) Analizi

.isnull().sum() ile veri incelendi:
<img width="1006" height="686" alt="image" src="https://github.com/user-attachments/assets/d4563236-db59-4dfe-839f-fca767fb4880" />



Hiçbir eksik veri bulunmadığı için doldurma (imputation) işlemi yapılmasına gerek olmadı.
Eksik veri olsaydı ortalama/medyan ile doldurmayı tercih ederdik.

📌 Kategorik Verilerin Kodlanması (Encoding)
🎯 One-Hot Encoding neden tercih edildi?

Cinsiyet, sigara, bölge gibi değişkenler nominal (sırasız) kategoriktir.

Label Encoding kullanılsaydı:

male = 1, female = 0 gibi değerler atanacak

Model bu sayıları sıralı sanıp yanlış ilişki kuracaktı.

✔ Bu nedenle One-Hot Encoding en doğru yöntemdir:

Kategoriler ayrı sütunlarda 0/1 şeklinde gösterilir.

“Dummy Variable Trap” oluşmaması için drop="first" kullanıldı.

📌 Veri Ölçekleme (Optional)

Veri setindeki sayısal kolonlar benzer ölçeklerde olduğu için StandardScaler kullanmak gerekli görülmedi.

Eğer çok büyük ölçek farkı olsaydı doğrusal regresyonun performansı düşebilirdi. Bu projede ölçek farkı ciddi olmadığı için ölçekleme yapılmadı.

2️⃣ Geriye Doğru Eleme (Backward Elimination)

Modelin istatistiksel anlamlılığını ölçmek için:

Tüm özelliklerle OLS modeli kuruldu

p-value değerleri kontrol edildi

p > 0.05 olan kolonlar tek tek elenerek model sadeleştirildi

Sonuç:

✔ Tüm kategorik dönüşümlü sütunlar modele anlamlı katkı sağladı
✔ Bazı dummy sütunları elendi
✔ En düşük hata veren optimum model elde edildi

Buraya OLS özet çıktısının ekran görüntüsünü koyabilirsin:
📌 Önerilen dosya adı: static/ols_summary.png

<img width="700" height="574" alt="image" src="https://github.com/user-attachments/assets/48405bce-ce8c-4629-a3c5-a771db801639" />


3️⃣ Model Kurulumu ve Değerlendirme

Eğitim/Test ayrımı yapıldıktan sonra Multiple Linear Regression modeli eğitildi.

📌 Performans Metrikleri:

<img width="446" height="215" alt="image" src="https://github.com/user-attachments/assets/56ae0999-6c84-40b2-91e3-6be6f7afb501" />


📌  Yorum

R² skorunun 0.78 olması modelin sigorta ücretindeki değişimin %78’ini açıkladığını gösterir → iyi bir sonuç.

MAE ≈ 4181 dolar, ortalama tahmin hatasını ifade eder.

MSE değeri yüksek olsa da, ücretlerin 2000–40000 bandında değiştiği düşünülürse normaldir.

Buraya metrik tablolarının görüntüsünü koyabilirsin.

4️⃣ Flask Arayüz Uygulaması

Model .pkl dosyasına kaydedildi:

sigorta_ucreti_tahmin_modeli.pkl


Flask uygulaması:

app.py içinde modeli yükler

Kullanıcıdan form verisini alır

One-Hot Encoding dönüşümlerini tekrar uygular

Tahmini hesaplayıp ekranda gösterir

💻 Kullanıcıdan Alınan Veriler:

Yaş

BMI

Çocuk sayısı

Cinsiyet

Sigara durumu

Bölge

<img width="1916" height="914" alt="image" src="https://github.com/user-attachments/assets/3c55ef43-b177-47c6-be9e-ba2828ae2dad" />

👤 Geliştirici

Nahit Furkan Öznamlı
2212721020
