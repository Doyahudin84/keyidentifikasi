import streamlit as st

def kunci_determinan():
    st.title("Kunci Determinasi Tumbuhan (Kingdom Plantae)")

    # Pertanyaan pertama: Apakah tumbuhan berbiji?
    biji = st.radio("Apakah tumbuhan berbiji?", ["Pilih Jawaban", "Ya", "Tidak"])

    if biji == 'Ya':
        # Jika tumbuhan berbiji, tentukan apakah bijinya tertutup atau terbuka
        biji_tertutup = st.radio("Apakah biji tertutup dalam buah?", ["Pilih Jawaban", "Ya", "Tidak"])

        if biji_tertutup == 'Ya':
            # Angiospermae (Tumbuhan Berbiji Tertutup)
            biji_keping = st.radio("Apakah biji berkeping satu (monokotil) atau dua (dikotil)?", ["Pilih Jawaban", "Satu", "Dua"])

            if biji_keping == 'Satu':
                st.write("Tumbuhan ini termasuk Monokotil (Contoh: Padi, Jagung, Kelapa, Anggrek).")
            elif biji_keping == 'Dua':
                st.write("Tumbuhan ini termasuk Dikotil (Contoh: Jati, Mangga, Mawar).")

        elif biji_tertutup == 'Tidak':
            # Gimnospermae (Tumbuhan Berbiji Terbuka)
            st.write("Tumbuhan ini termasuk Gimnospermae (Contoh: Pinus, Cemara, Ginkgo).")

    elif biji == 'Tidak':
        # Jika tumbuhan tidak berbiji, kita klasifikasikan ke paku atau lumut
        jenis_tumbuhan = st.radio("Apakah tumbuhan ini memiliki akar, batang, dan daun sejati?", ["Pilih Jawaban", "Ya", "Tidak"])

        if jenis_tumbuhan == 'Ya':
            # Paku-pakuan (Pteridophyta)
            st.write("Tumbuhan ini termasuk Paku-pakuan (Contoh: Paku Tanah, Paku Ekor Kuda).")

        elif jenis_tumbuhan == 'Tidak':
            # Lumut (Bryophyta)
            st.write("Tumbuhan ini termasuk Lumut (Contoh: Lumut Kerak, Lumut Hati).")


def main():
    st.sidebar.title("Menu")
    st.sidebar.write("Aplikasi Kunci Determinasi Tumbuhan")

    # Menjalankan fungsi kunci_determinan
    kunci_determinan()

    # Pilihan untuk mengulangi
    if st.button("Ulangi"):
        st.experimental_rerun()

if __name__ == '__main__':
    main()
