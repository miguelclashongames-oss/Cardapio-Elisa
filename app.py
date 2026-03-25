import streamlit as st
import os

# Configurações da Página
st.set_page_config(page_title="Elisa - Doces Finos Artesanais", page_icon="🍫", layout="centered")

# --- CSS PERSONALIZADO (ZYNIX PREMIUM) ---
st.markdown("""
    <style>
    .stApp { background-color: #F8F9F5; color: #533E2B; }
    
    /* Títulos das Categorias Bem Maiores */
    .stExpander span {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #565F3A !important;
    }
    
    /* Botão de Ver Carrinho Chamativo */
    .btn-carrinho-central {
        background-color: #D0A08A;
        color: #533E2B;
        padding: 20px;
        text-align: center;
        border-radius: 15px;
        font-weight: bold;
        font-size: 20px;
        margin-top: 30px;
        border: 2px solid #565F3A;
    }

    .stSidebar { background-color: #565F3A; }
    .stSidebar h2, .stSidebar p, .stSidebar h4, .stSidebar span, .stSidebar div { color: #F1FAEE !important; }
    
    .stSidebar .stButton button {
        background-color: #D0A08A;
        color: #533E2B;
        border: none;
        border-radius: 20px;
        font-weight: bold;
        width: 100%;
    }
    
    .stButton button { background-color: #565F3A; color: white; border-radius: 20px; }

    /* Logo Máxima */
    [data-testid="stImage"] img { width: 100% !important; transform: scale(1.05); }
    </style>
""", unsafe_allow_html=True)

# --- LOGO ---
caminho_logo = os.path.join(os.path.dirname(__file__), "logo.png")
if os.path.exists(caminho_logo):
    st.image(caminho_logo, use_container_width=True)
else:
    st.warning("⚠️ Adicione o arquivo logo.png no GitHub.")

# --- BANCO DE DADOS ---
cardapio = {
    "🌮 TAPIOCAS SALGADAS": {
        "🧈 Manteiga": 10.0, "🥪 Presunto com Mussarela": 15.0, "🧀 Mussarela": 15.0,
        "🌭 Calabresa": 15.0, "🍅 Bauru": 20.0, "🥛 Calabresa com Requeijão": 20.0,
        "🍕 Calabresa com Mussarela": 20.0, "🍗 Frango": 15.0, "🧀 Frango com Mussarela": 20.0,
        "🍶 Frango com Requeijão": 20.0, "🥩 Carne Seca": 20.0, "🔥 Carne Seca com Requeijão": 25.0,
        "🥘 Carne Seca com Mussarela": 25.0, "🌵 Queijo Coalho": 25.0,
    },
    "🍯 TAPIOCAS DOCES": {
        "🥥 Coco com Leite Condensado": 20.0, "🍓 Mussarela com Goiabada": 20.0,
        "🍮 Doce de Leite": 20.0, "🍌 Banana com Leite Condensado": 20.0,
    },
    "🍕 MINI PIZZAS": {
        "🧀 Mussarela (Pizza)": 10.0, "🍕 Calabresa (Pizza)": 10.0, "🌿 Margarita": 12.0,
        "🍗 Frango (Pizza)": 15.0, "🥛 Calabresa c/ Requeijão": 12.0, "🍶 Frango c/ Requeijão": 17.0,
    },
    "🐣 OVOS AO LEITE": {
        "🍫 Ovo ao Leite 250g": 25.0, "🍫 Ovo ao Leite 390g": 35.0, 
        "🍫 Ovo ao Leite 500g": 40.0, "🍫 Ovo ao Leite 1kg": 90.0,
    },
    "✨ OVOS TRUFADOS": {
        "🍯 Ovo Trufado PP": 45.0, "🍯 Ovo Trufado P": 55.0, 
        "🍯 Ovo Trufado M": 90.0, "🍯 Ovo Trufado G": 140.0,
    },
    "🎮 OVOS INFANTIS": {
        "⚽ Ovo Bola": 35.0, "👟 Chuteira": 35.0, "🕹️ Controle de Video Game": 35.0,
        "❤️ Coração 500g": 35.0,
    },
    "🧁 TABLETES & KITS": {
        "🍫 Tablete G Prestigio/Confete": 25.0, "🍓 Tablete G Brigadeiro/Beijinho": 35.0,
        "🎁 Kit 3 Mini Ovos": 30.0, "🎁 Kit 4 Mini Ovos": 40.0, "🎁 Kit 5 Mini Ovos": 50.0,
    },
    "🍪 DIVERSOS": {
        "🍯 Pão de Mel": 10.0, "🍦 Cone Recheado": 10.0, "🍬 1kg de Bombom": 150.0,
    }
}

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = {}

# --- EXIBIÇÃO ---
for categoria, itens in cardapio.items():
    with st.expander(categoria, expanded=False):
        for item, preco in itens.items():
            c1, c2 = st.columns([3, 1])
            c1.markdown(f"**{item}** \n R$ {preco:.2f}")
            if c2.button("Add", key=f"btn_{categoria}_{item}"):
                if item in st.session_state.carrinho:
                    st.session_state.carrinho[item]['qtd'] += 1
                else:
                    st.session_state.carrinho[item] = {'preco': preco, 'qtd': 1}

# BOTÃO CHAMATIVO NO FINAL DA LISTA
if st.session_state.carrinho:
    st.markdown(f'<div class="btn-carrinho-central">🛒 {len(st.session_state.carrinho)} Itens no Carrinho (Ver na Lateral)</div>', unsafe_allow_html=True)

# --- SIDEBAR (CARRINHO) ---
st.sidebar.header("🛒 Seu Pedido")
total = 0.0
resumo = ""

if not st.session_state.carrinho:
    st.sidebar.info("Seu carrinho está vazio.")
else:
    for item, d in st.session_state.carrinho.items():
        sub = d['preco'] * d['qtd']
        total += sub
        st.sidebar.markdown(f"**{item}**")
