import pandas as pd
import streamlit as st

# 1. Konfigurasi Halaman Web
st.set_page_config(
    page_title="AsiaDrama Match Ultimate", page_icon="🎬", layout="wide"
)

st.title("🎬 AsiaDrama Match: Rekomendasi Drama Asia Terlengkap")
st.write(
    "Temukan koleksi drama terbaik dari Korea, Thailand, Indonesia, dan China berdasarkan 10 Genre terpopuler!"
)
st.markdown("---")

# 2. Database Baru: Hanya 4 Negara (Total 32 Drama, 10 Genre)
data_drama = {
    "Judul": [
        # === KOREA ===
        "Crash Landing on You",
        "Business Proposal",
        "Goblin (Guardian: The Lonely and Great God)",
        "Vincenzo",
        "Twenty-Five Twenty-One",
        "Mouse",
        # === INDONESIA ===
        "Gadis Kretek",
        "Layangan Putus",
        "Kupu Malam",
        "My Lecturer My Husband",
        "Pertaruhan The Series 2",
        "Nanti Kita Cerita Tentang Hari Ini",
        # === THAILAND ===
        "Girl From Nowhere",
        "F4 Thailand: Boys Over Flowers",
        "Wu: The Series",
        "High School Frenemy",
        "Beauty Newbie",
        "The Dark Dice",
        "Faceless Love",
        "Home School",
        # === CHINA ===
        "Hidden Love",
        "Love Between Fairy and Devil",
        "The Untamed",
        "Put Your Head on My Shoulder",
        "Reset",
        "Archives of the Nanyang Mystery",
        "Time Raiders",
        "The Spirealm",
        "Zhan Zhao Adventures",
        "A Journey to Love",
        "Desire Catcher",
        "Legend of Zhang Hai",
    ],
    "Negara": [
        # Korea
        "Korea",
        "Korea",
        "Korea",
        "Korea",
        "Korea",
        "Korea",
        # Indonesia
        "Indonesia",
        "Indonesia",
        "Indonesia",
        "Indonesia",
        "Indonesia",
        "Indonesia",
        # Thailand
        "Thailand",
        "Thailand",
        "Thailand",
        "Thailand",
        "Thailand",
        "Thailand",
        "Thailand",
        "Thailand",
        # China
        "China",
        "China",
        "China",
        "China",
        "China",
        "China",
        "China",
        "China",
        "China",
        "China",
        "China",
        "China",
    ],
    "Genre": [
        # Korea
        "Romance-Melodrama",
        "Comedy-Romance",
        "Fantasy-Wuxia",
        "Action-Thriller",
        "Youth-School",
        "Mystery-Thriller",
        # Indonesia
        "Historical-Drama",
        "Family-Conflict",
        "Family-Conflict",
        "Comedy-Romance",
        "Action-Thriller",
        "Historical-Drama",
        # Thailand
        "Mystery-Thriller",
        "Youth-School",
        "Action-Thriller",
        "Friendship-Drama",
        "Comedy-Romance",
        "Mystery-Thriller",
        "Comedy-Romance",
        "Mystery-Thriller",
        # China
        "Modern-Romance",
        "Fantasy-Wuxia",
        "Fantasy-Wuxia",
        "Modern-Romance",
        "Mystery-Thriller",
        "Detective-Crime",
        "Action-Thriller",
        "Mystery-Thriller",
        "Detective-Crime",
        "Historical-Drama",
        "Detective-Crime",
        "Historical-Drama",
    ],
    "Rating": [
        # Korea
        "8.7",
        "8.1",
        "8.9",
        "8.5",
        "8.6",
        "8.8",
        # Indonesia
        "8.2",
        "7.9",
        "7.4",
        "7.7",
        "8.1",
        "7.8",
        # Thailand
        "7.6",
        "8.0",
        "7.8",
        "8.2",
        "7.9",
        "7.5",
        "7.7",
        "8.1",
        # China
        "8.9",
        "8.8",
        "9.0",
        "8.0",
        "8.6",
        "7.8",
        "7.9",
        "8.4",
        "7.6",
        "8.5",
        "8.0",
        "8.3",
    ],
    "Poster": [
        # === KOREA ===
        "Crash Landing on You.jpg",
        "Business Proposal.jpg",
        "Goblin.jpg",
        "Vincenzo.jpg",
        "Twenty-Five Twenty-One.jpg",
        "Mouse.jpg",
        # === INDONESIA ===
        "Gadis Kretek.jpg",
        "Layangan Putus.jpg",
        "Kupu kupu malam.jpg",
        "My Lecturer My Husband.jpg",
        "Pertaruhan the series 2.jpg", # sesuaikan persis tulisan di GitHub-mu
        "Nanti Kita Cerita Tentang ...", # sesuaikan persis tulisan di GitHub-mu
        # === THAILAND ===
        "Girl From Nowhere.jpg",
        "F4 Thailand Boys Over Flowers...", # sesuaikan persis tulisan di GitHub-mu
        "Wu The Series.jpg",
        "High School Frenemy.jpg",
        "Beauty Newbie.jpg",
        "The Dark Dice.jpg",
        "Faceless Love.jpg",
        "Home School.jpg",
        # === CHINA ===
        "Hidden Love.jpg",
        "Love between fairy and de...", # sesuaikan persis tulisan di GitHub-mu
        "The Untamed.jpg",
        "Put Your Head On My Sho...", # sesuaikan persis tulisan di GitHub-mu
        "Reset.jpg",
        "Archives The Nanyang Myster...", # sesuaikan persis tulisan di GitHub-mu
        "Time Raiders.jpg",
        "The Spirealm.jpg",
        "Zhan Zhao Abentures.jpg", # sesuaikan persis tulisan di GitHub-mu
        "A Journey to Love.jpg",
        "Desire Catcher.jpg",
        "Legend of Zhang Hai.jpg",
    ],
    "Sinopsis": [
        # Korea
        "Pewaris kaya Korea Selatan tidak sengaja mendarat darurat di Korea Utara akibat paralayang.",
        "Kisah komedi romantis tentang seorang karyawan yang menggantikan temannya di kencan buta dengan CEO-nya.",
        "Seorang jenderal perang era Goryeo dikutuk menjadi Goblin abadi dan mencari pengantin manusianya.",
        "Seorang pengacara mafia keturunan Korea-Italia kembali ke tanah kelahirannya untuk mengambil emas.",
        "Kisah perjuangan cinta, cita-cita, dan persahabatan anak muda saat krisis moneter Asia 1998.",
        "Seorang polisi muda yang jujur menghadapi teror berantai dari seorang psikopat kejam.",
        # Indonesia
        "Kisah pencarian cinta dan sejarah industri rokok kretek di Indonesia pada era 1960-an.",
        "Kemelut rumah tangga yang hancur akibat kehadiran orang ketiga yang memicu konflik mendalam.",
        "Perjuangan seorang mahasiswi cerdas yang terpaksa menjalani kehidupan ganda di malam hari.",
        "Kisah perjodohan tak terduga antara seorang mahasiswi perfeksionis dengan dosen galak.",
        "Perjuangan keras kakak-beradik dalam mempertahankan hidup di jalanan yang keras.",
        "Drama keluarga tentang tiga bersaudara yang menyimpan rahasia di balik keharmonisan rumah.",
        # Thailand
        "Nanno, seorang gadis misterius, pindah sekolah untuk membongkar kebohongan para murid.",
        "Adaptasi Thailand dari F4, menceritakan gadis miskin melawan kelompok penguasa sekolah.",
        "Kisah aksi menegangkan yang penuh misteri dan konspirasi di Thailand.",
        "Konflik sengit sekaligus ikatan persahabatan yang rumit antara dua murid di sekolah.",
        "Kisah seorang gadis yang melakukan operasi plastik untuk memulai hidup baru di kuliah namun menghadapi tantangan baru.",
        "Teror permainan dadu misterius yang membawa ketakutan dan misteri psikologis mencekam bagi para remaja.",
        "Komedi romantis tentang seorang bos yang mengidap penyakit tidak bisa mengenali wajah orang (prosopagnosia) dan sekretarisnya.",
        "Sekolah berasrama elite di tengah hutan yang menyembunyikan aturan kejam dan rahasia kelam kurikulumnya.",
        # China
        "Kisah romantis manis yang tumbuh sejak masa sekolah antara seorang gadis dengan teman kakaknya.",
        "Kisah cinta fantasi epik antara peri air yang menggemaskan dengan Raja Iblis yang kejam.",
        "Dua kultivator berbakat bekerja sama memecahkan rangkaian misteri pembunuhan di dunia persilatan.",
        "Kisah cinta manis saat seorang mahasiswi akuntansi harus tinggal serumah dengan mahasiswa jenius fisika.",
        "Sepasang anak muda terjebak di dalam siklus waktu (time loop) ledakan bus misterius.",
        "Penyelidikan detektif mengungkap misteri supranatural dan kasus kriminal kuno yang aneh di wilayah Nanyang.",
        "Petualangan menegangkan para penjelajah makam kuno dalam mencari rahasia keabadian dan melawan kutukan.",
        "Kisah misteri dunia virtual di mana para pemain harus melewati 12 pintu koridor berbahaya untuk bertahan hidup.",
        "Kisah kepahlawanan Zhan Zhao bersama Hakim Bao dalam menegakkan keadilan dan menumpas kejahatan di era Dinasti Song.",
        "Perjalanan epik para pembunuh bayaran dan kesatria dalam misi spionase penuh aksi dan pengorbanan politik.",
        "Pertarungan psikologis dan hipnoterapi antara detektif dan ahli hipnosis dalam memecahkan kasus kriminal rumit.",
        "Kisah perjalanan hidup Zhang Hai yang melakukan balas dendam taktis demi menegakkan kebenaran di istana kekaisaran.",
    ],
}

df = pd.DataFrame(data_drama)

# 3. Sidebar Filter Kontrol
st.sidebar.header("⚙️ Filter Pencarian")

# Filter 1: Pilih Negara (Hanya 4 Negara)
list_negara = ["Semua Negara"] + list(df["Negara"].unique())
negara_pilihan = st.sidebar.selectbox("Pilih Negara Asal Drama:", list_negara)

# Filter 2: Pilih Genre
list_genre = ["Semua Genre"] + sorted(list(df["Genre"].unique()))
genre_pilihan = st.sidebar.selectbox("Pilih Genre Drama:", list_genre)

# Filter 3: Slider Rating
rating_minimal = st.sidebar.slider(
    "Rating Minimal:", 7.0, 10.0, 7.4, step=0.1
)

# 4. Proses Penyaringan Data (Filtering)
hasil_filter = df[df["Rating"].astype(float) >= rating_minimal]

if negara_pilihan != "Semua Negara":
    hasil_filter = hasil_filter[hasil_filter["Negara"] == negara_pilihan]

if genre_pilihan != "Semua Genre":
    hasil_filter = hasil_filter[hasil_filter["Genre"] == genre_pilihan]

# 5. Menampilkan Hasil ke Halaman Web
st.subheader(f"✨ Hasil Rekomendasi Drama ({len(hasil_filter)} ditemukan)")

if hasil_filter.empty:
    st.warning(
        "Tidak ada drama yang cocok dengan kombinasi tersebut. Coba turunkan filter rating atau ganti pilihan lainnya!"
    )
else:
    kolom = st.columns(2)
    for indeks, baris in hasil_filter.reset_index().iterrows():
        posisi_kolom = indeks % 2

        with kolom[posisi_kolom]:
            with st.container(border=True):
                kolom_kiri, kolom_kanan = st.columns([1, 2])

                with kolom_kiri:
                    try:
                        st.image(baris["Poster"], use_container_width=True)
                    except Exception:
                        st.error("⚠️ Poster Belum Ada")
                        st.caption(f"Ekstensi file wajib .jpg")

                with kolom_kanan:
                    st.markdown(f"### {baris['Judul']}")
                    st.markdown(f"⭐ **Rating:** {baris['Rating']}/10")
                    st.markdown(
                        f"📍 **Negara:** {baris['Negara']} | 📁 **Genre:** {baris['Genre']}"
                    )
                    st.write(baris["Sinopsis"])

# 6. Lihat Tabel Database di Bawah
with st.expander("👁️ Lihat Seluruh Database Tabel (DataFrame)"):
    st.dataframe(df)
