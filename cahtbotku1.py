
import streamlit as st

# Pengetahuan tentang kegiatan 17 Agustus di sekolah
knowledge_base = [
    ("Apa saja lomba yang diadakan pada 17 Agustus?", "Lomba yang diadakan antara lain: lomba balap karung, lomba makan kerupuk, lomba tarik tambang, lomba panjat pinang, lomba bakiak, lomba kelereng, lomba memasukkan pensil ke dalam botol, lomba estafet air, lomba balap sendok, lomba balap sarung, lomba futsal, lomba voli, lomba cerdas cermat, lomba menghias kelas, lomba kebersihan kelas, lomba pidato, lomba puisi, lomba menggambar, lomba mewarnai, lomba fashion show, lomba yel-yel, lomba drama, lomba paduan suara, lomba senam, lomba memasak, lomba membuat poster, lomba fotografi, lomba video kreatif, lomba tumpeng, lomba membuat kerajinan, lomba tebak kata."),
    ("Kapan upacara bendera dilaksanakan?", "Upacara bendera dilaksanakan pada tanggal 17 Agustus pukul 07.00 pagi di lapangan sekolah."),
    ("Siapa yang menjadi petugas upacara?", "Petugas upacara biasanya dipilih dari siswa-siswi kelas atas dan guru-guru sebagai pembina upacara."),
    ("Apa saja perlengkapan yang harus dibawa saat upacara?", "Perlengkapan yang harus dibawa antara lain: topi, dasi, ikat pinggang, sepatu hitam, kaos kaki putih, dan seragam lengkap."),
    ("Apakah ada dress code khusus saat lomba?", "Peserta lomba diharapkan mengenakan pakaian olahraga atau pakaian yang telah ditentukan panitia."),
    ("Bagaimana cara mendaftar lomba?", "Pendaftaran lomba dapat dilakukan melalui ketua kelas atau langsung ke panitia lomba di ruang OSIS."),
    ("Apakah orang tua boleh hadir saat upacara?", "Orang tua diperbolehkan hadir untuk menyaksikan upacara dan lomba-lomba yang diadakan."),
    ("Apakah ada hadiah untuk pemenang lomba?", "Ya, pemenang lomba akan mendapatkan hadiah berupa piala, piagam, dan bingkisan menarik."),
    ("Apa tema peringatan 17 Agustus tahun ini?", "Tema peringatan 17 Agustus tahun ini adalah 'Semangat Kemerdekaan, Wujudkan Prestasi dan Kreativitas'."),
    ("Apakah ada lomba untuk guru?", "Ya, ada lomba khusus untuk guru seperti lomba memasak dan lomba tarik tambang."),
    ("Bagaimana jika hujan saat upacara?", "Jika hujan, upacara akan dipindahkan ke aula atau ruangan tertutup yang cukup luas."),
    ("Apakah ada gladi bersih upacara?", "Gladi bersih upacara biasanya dilakukan sehari sebelum pelaksanaan upacara."),
    ("Siapa yang menjadi pembina upacara?", "Pembina upacara biasanya adalah kepala sekolah atau guru senior."),
    ("Apakah ada lomba kebersihan kelas?", "Ya, lomba kebersihan kelas diadakan untuk meningkatkan kesadaran siswa akan pentingnya kebersihan."),
    ("Kapan pengumuman pemenang lomba?", "Pengumuman pemenang lomba dilakukan setelah seluruh rangkaian lomba selesai pada hari yang sama."),
    ("Apakah ada penampilan seni?", "Ya, akan ada penampilan seni seperti tari tradisional, paduan suara, dan drama kemerdekaan."),
    ("Bagaimana tata tertib saat upacara?", "Siswa harus berbaris rapi, tidak berbicara, dan mengikuti instruksi petugas upacara dengan tertib."),
    ("Apakah ada konsumsi untuk peserta?", "Panitia menyediakan konsumsi berupa snack dan minuman untuk peserta lomba dan upacara."),
    ("Apakah boleh membawa kamera saat acara?", "Boleh, namun harus tetap menjaga ketertiban dan tidak mengganggu jalannya acara."),
    ("Bagaimana cara menjadi panitia?", "Siswa yang ingin menjadi panitia dapat mendaftar ke OSIS atau guru pembina."),
    ("Apakah ada lomba estafet air?", "Ya, lomba estafet air menjadi salah satu lomba favorit di sekolah."),
    ("Apakah ada lomba untuk SD, SMP, dan SMA?", "Lomba disesuaikan dengan jenjang sekolah, namun beberapa lomba bisa diikuti oleh semua jenjang."),
    ("Apakah ada lomba online?", "Tahun ini tidak ada lomba online, semua lomba diadakan secara langsung di sekolah."),
    ("Bagaimana jika tidak bisa hadir upacara?", "Siswa yang berhalangan hadir wajib memberikan surat izin kepada wali kelas atau panitia."),
    ("Apakah ada dokumentasi acara?", "Ya, panitia menyediakan tim dokumentasi untuk mengabadikan seluruh rangkaian acara."),
    ("Apakah ada lomba membuat tumpeng?", "Ya, lomba membuat tumpeng diikuti oleh perwakilan kelas."),
    ("Apakah ada lomba menghias kelas?", "Lomba menghias kelas diadakan untuk memeriahkan suasana kemerdekaan."),
    ("Apakah ada lomba pidato kemerdekaan?", "Ya, lomba pidato kemerdekaan diadakan untuk melatih kemampuan berbicara siswa."),
    ("Apakah ada lomba puisi?", "Lomba puisi diadakan dengan tema kemerdekaan Indonesia."),
    ("Apakah ada lomba menggambar dan mewarnai?", "Lomba menggambar dan mewarnai diadakan untuk siswa SD dengan tema kemerdekaan.")
]

def chatbot_response(user_input):
    for q, a in knowledge_base:
        if user_input.lower() in q.lower():
            return a
    # Coba cari jawaban yang mirip
    for q, a in knowledge_base:
        if any(word in q.lower() for word in user_input.lower().split()):
            return a
    return "Maaf, saya belum memiliki informasi tentang itu. Silakan tanyakan hal lain seputar kegiatan 17 Agustus di sekolah."

st.set_page_config(page_title="Chatbot 17 Agustus Sekolah", page_icon="🇮🇩")
st.title("🤖 Chatbot 17 Agustus di Sekolah 🇮🇩")
st.write("Selamat datang! Tanyakan apa saja seputar kegiatan 17 Agustus di sekolah, seperti lomba, upacara, dan lainnya.")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Tulis pertanyaan Anda di sini:")

if st.button("Tanya"):
    if user_input:
        response = chatbot_response(user_input)
        st.session_state['chat_history'].append((user_input, response))

if st.session_state['chat_history']:
    st.write("## Riwayat Percakapan")
    for i, (q, a) in enumerate(st.session_state['chat_history'], 1):
        st.markdown(f"**Anda:** {q}")
        st.markdown(f"**Chatbot:** {a}")
