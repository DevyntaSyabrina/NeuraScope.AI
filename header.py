import streamlit as st

def render_header():
    st.markdown("""
        <style>
        /* Sticky Header Styling */
        .sticky-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #1f77b4;
            color: white;
            z-index: 9999;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            padding-top: 50px;
            padding-bottom: 10px;
            text-align: center;

            /* Flexbox for centering */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .sticky-header h2 {
            margin: 0;
            font-size: 40px;
        }

        .sticky-header h4 {
            margin: 5px 0 10px 0; /* top, right/left, bottom */
            font-weight: normal;
            color: #ecf0f1;
            font-size: 16px;
        }

        /* Spacer to offset header height */
        .spacer {
            margin-top: 120px;
        }

        @media screen and (max-width: 480px) {
            .sticky-header h2 {
                font-size: 22px;
            }

            .sticky-header h4 {
                font-size: 14px;
            }

            .spacer {
                margin-top: 70px;
            }
        }
        </style>

        <div class="sticky-header">
            <h2>📸 NeuraScope 🔍</h2>
            <h4>Sistem Cerdas Berbasis AI untuk Deteksi Gambar Otomatis</h4>
        </div>
        <div class="spacer"></div>
    """, unsafe_allow_html=True)
