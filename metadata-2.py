import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter

# Masaüstü yolunu alalım
MASAUSTU = os.path.join(os.path.expanduser("~"), "Desktop")

# Renk paletleri - AI gibi değil de bir config gibi duruyor
RENKLER = {
    "AMOLED": """
        QWidget { background-color: #000000; color: white; }
        QPushButton { background-color: #111; color: #ff5722; font-weight: bold; padding: 5px; }
        QTextEdit { background-color: #050505; color: #00ff88; border: 1px solid #333; }
    """,
    "Koyu": """
        QWidget { background-color: #1a1a1a; color: #eeeeee; }
        QPushButton { background-color: #333; color: #ff9800; font-size: 15px; }
        QTextEdit { background-color: #222; color: #00e676; }
    """,
    "Açık": """
        QWidget { background-color: #f0f0f0; color: #333; }
        QPushButton { background-color: #ddd; color: black; }
        QTextEdit { background-color: white; color: black; }
    """
}

class FireTraceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.secili_dosya = None
        self.arayuz_kur() # Arayüzü başlatan ana fonksiyon
        
    def arayuz_kur(self):
        # Pencere ayarları
        self.setWindowTitle("FireTrace v2.0 - Metadata Cleaner")
        self.setMinimumSize(500, 450) # Sabit boyut yerine minimum boyut (Tam ekran yapılabilir)
        
        # Ana dikey yerleşim
        v_box = QVBoxLayout()

        # Başlık kısmı
        self.ust_yazi = QLabel("🔥 FireTrace Metadata Temizleyici")
        self.ust_yazi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ust_yazi.setStyleSheet("font-size: 22px; font-weight: 800; margin: 10px;")
        v_box.addWidget(self.ust_yazi)

        # Tema seçici
        self.tema_secici = QComboBox()
        self.tema_secici.addItems(["AMOLED", "Koyu", "Açık"])
        self.tema_secici.currentTextChanged.connect(self.tema_degistir)
        v_box.addWidget(QLabel("Görünüm Seç:"))
        v_box.addWidget(self.tema_secici)

        # Butonlar
        self.dosya_btn = QPushButton("Dosya Seç")
        self.dosya_btn.clicked.connect(self.dosya_diyalog_ac)
        v_box.addWidget(self.dosya_btn)

        self.baslat_btn = QPushButton("🔥 VERİLERİ YAK (TEMİZLE)")
        self.baslat_btn.clicked.connect(self.islem_yap)
        v_box.addWidget(self.baslat_btn)

        # Log ekranı
        self.log_ekrani = QTextEdit()
        self.log_ekrani.setPlaceholderText("İşlem geçmişi burada görünecek...")
        self.log_ekrani.setReadOnly(True)
        v_box.addWidget(self.log_ekrani)

        # Alt bilgi
        self.alt_bilgi = QLabel("By FeulerUwU | 2024")
        self.alt_bilgi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.alt_bilgi.setStyleSheet("font-size: 9px; color: gray;")
        v_box.addWidget(self.alt_bilgi)

        self.setLayout(v_box)
        self.tema_degistir("AMOLED")

    def tema_degistir(self, t_adi):
        self.setStyleSheet(RENKLER.get(t_adi))

    def dosya_diyalog_ac(self):
        dosya, _ = QFileDialog.getOpenFileName(
            self, "Bir dosya seçin", "", 
            "Resimler (*.jpg *.jpeg *.png);;PDF Dokümanları (*.pdf)"
        )
        if dosya:
            self.secili_dosya = dosya
            dosya_adi = os.path.basename(dosya)
            self.log_ekrani.append(f"-> Dosya seçildi: {dosya_adi}")

    def islem_yap(self):
        if not self.secili_dosya:
            self.log_ekrani.append("(!) Hata: Henüz dosya seçmedin.")
            return

        ext = os.path.splitext(self.secili_dosya)[1].lower()
        isim = os.path.splitext(os.path.basename(self.secili_dosya))[0]
        kayit_yeri = os.path.join(MASAUSTU, f"{isim}_temiz{ext}")

        try:
            if ext in [".jpg", ".jpeg", ".png"]:
                self.resim_temizle(kayit_yeri)
            elif ext == ".pdf":
                self.pdf_temizle(kayit_yeri)
            else:
                self.log_ekrani.append("(!) Bu dosya türü desteklenmiyor.")
                return

            self.log_ekrani.append(f"[OK] İşlem başarılı! Masaüstüne bak: {isim}_temiz{ext}")

        except Exception as e:
            self.log_ekrani.append(f"[HATA] Bir şeyler ters gitti: {str(e)}")

    def resim_temizle(self, yol):
        img = Image.open(self.secili_dosya)
        # Veriyi yeniden oluşturup EXIF'i geride bırakıyoruz
        ayni_modda_yeni = Image.new(img.mode, img.size)
        ayni_modda_yeni.putdata(list(img.getdata()))
        ayni_modda_yeni.save(yol)

    def pdf_temizle(self, yol):
        okuyucu = PdfReader(self.secili_dosya)
        yazici = PdfWriter()

        for sayfa in okuyucu.pages:
            yazici.add_page(sayfa)

        with open(yol, "wb") as f:
            yazici.write(f)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = FireTraceApp()
    pencere.show()
    sys.exit(app.exec())