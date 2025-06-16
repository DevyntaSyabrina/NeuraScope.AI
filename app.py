import streamlit as st
from PIL import Image, ImageEnhance
from deteksi import deteksi_objek
from modules.deteksi import deteksi_objek
from header import render_header  # Panggil header dari file terpisah

# Konfigurasi halaman
st.set_page_config(layout="centered", page_title="Deteksi Otomatis Benda")

# Tampilkan sticky header dan CSS styling
render_header()

# Fungsi peningkatan kualitas gambar
def enhance_image(img):
    img = ImageEnhance.Sharpness(img).enhance(2.0)
    img = ImageEnhance.Contrast(img).enhance(1.3)
    return img

# Inisialisasi session_state
if "img" not in st.session_state:
    st.session_state.img = None
if "hasil" not in st.session_state:
    st.session_state.hasil = None

# Tombol reset (tanpa pilihan input lagi)
if st.button("🔁 Reset"):
    st.session_state.clear()
    st.rerun()

# Fungsi proses dan deteksi gambar
def proses_gambar(input_img):
    if input_img:
        img = Image.open(input_img)
        img = enhance_image(img)
        with st.spinner("🔍 Mendeteksi objek..."):
            hasil, img_hasil = deteksi_objek(img)
            st.session_state.img = img_hasil
            st.session_state.hasil = hasil

# Input hanya dari kamera
camera_image = st.camera_input("Ambil Gambar 📸")
if camera_image:
    proses_gambar(camera_image)

# Tampilkan gambar hasil deteksi dan tabel di tengah menggunakan div center
if st.session_state.img:
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    st.image(st.session_state.img, caption="📷 Gambar dengan Hasil Deteksi", width=500)

    if st.session_state.hasil:
        st.markdown("### ✅ Hasil Deteksi")
        st.table({
            "Nama Benda": [x['nama'] for x in st.session_state.hasil],
            "Akurasi": [f"{x['akurasi']}%" for x in st.session_state.hasil]
        })
    else:
        st.info("📥 Gambar sudah dimuat. Namun belum ada hasil deteksi.")

    st.markdown('</div>', unsafe_allow_html=True)
