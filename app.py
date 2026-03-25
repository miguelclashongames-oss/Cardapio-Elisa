import streamlit as st
import os

# Configurações da Página
st.set_page_config(page_title="Elisa - Doces Finos Artesanais", page_icon="🍫", layout="centered")

# --- CSS PERSONALIZADO (ZYNIX STUDIOS) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #F8F9F5;
        color: #533E2B;
    }
    h1, h2, h3, h4, p, .stExpander p {
        color: #565F3A !important;
        font-family: 'Georgia', serif;
    }
    .stSidebar {
        background-color: #565F3A;
    }
    .stSidebar h2, .stSidebar p, .stSidebar h4, .stSidebar span {
        color: #F1FAEE !important;
    }
    .stSidebar .stButton button {
        background-color: #D0A08A;
        color: #533E2B;
        border: none;
        border-radius: 20px;
        font-weight: bold;
    }
    .stButton button {
        background-color: #565F3A;
        color: white;
        border-radius: 20px;
    }
    /* Forçar a imagem a ocupar 100% da largura */
    [data-testid="stImage"] img {
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- EXIBIR A LOGO (LARGURA TOTAL) ---
caminho_logo = os.path.join(os.path.dirname(__file__), "logo.png")
if os.path.exists(caminho_logo):
    st.image(caminho_logo, use_container_width=True)
    st.markdown("---")
else:
    st.warning("⚠️ Arquivo logo.png não encontrado no GitHub.")

# --- BANCO DE DADOS DO CARDÁPIO ---
cardapio = {
    "🌮 Tapiocas Salgadas": {
        "🧈 Manteiga": 10.00,
        "🥪 Presunto com Mussarela": 15.00,
        "🧀 Mussarela": 15.00,
        "🌭 Calabresa": 15.00,
        "🍅 Bauru": 20.00,
        "🥛 Calabresa com Requeijão": 20.00,
        "🍕 Calabresa com Mussarela": 20.00,
        "🍗 Frango": 15.00,
        "🧀 Frango com Mussarela": 20.00,
        "🍶 Frango com Requeijão": 20.00,
        "🥩 Carne Seca": 20.00,
        "🔥 Carne Seca com Requeijão": 25.00,
        "🥘 Carne Seca com Mussarela": 25.00,
        "🌵 Queijo Coalho": 25.00,
    },
    "🍯 Tapiocas Doces": {
        "🥥 Coco com Leite Condensado": 20.00,
        "🍓 Mussarela com Goiabada": 20.00,
        "🍮 Doce de Leite": 20.00,
        "🍌 Banana com Leite Condensado": 20.00,
    },
    "🍕 Mini Pizzas": {
        "🧀 Mussarela (Pizza)": 10.00,
        "🍕 Calabresa (Pizza)": 10.00,
        "🌿 Margarita": 12.00,
        "🍗 Frango (Pizza)": 15.00,
        "🥛 Calabresa c/ Requeijão": 12.00,
        "🍶 Frango c/ Requeijão": 17.00,
    },
    "🐣 Ovos Trufados e de Colher": {
        "✨ Ovo Trufado PP (250g)": 25.00,
        "🎁 Ovo Trufado P (350g)": 35.00,
        "⭐ Ovo Trufado M (500g)": 50.00,
        "🏆 Ovo Trufado GG (1kg)": 90.00,
        "🥄 Ovo de Colher PP (250g)": 30.00,
        "🥣 Ovo de Colher P (350g)": 40.00,
        "💎 Ovo de Colher N (500g)": 55.00,
    }
}

# --- LÓGICA DO CARRINHO ---
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = {}

for categoria, itens in cardapio.items():
    with st.expander(f"📍 {categoria}", expanded=True):
        for item, preco in itens.items():
            c1, c2 = st.columns([3, 1])
            c1.markdown(f"<p style='font-size: 16px; margin: 0;'><b>{item}</b> - R$ {preco:.2f}</p>", unsafe_allow_html=True)
            chave_botao = f"btn_{categoria}_{item}".replace(" ", "_")
            if c2.button("Add", key=chave_botao):
                if item in st.session_state.carrinho:
                    st.session_state.carrinho[item]['qtd'] += 1
                else:
                    st.session_state.carrinho[item] = {'preco': preco, 'qtd': 1}
                st.toast(f"{item} adicionado!")

# --- BARRA LATERAL (CHECKOUT E AVISO DE ENTREGA) ---
st.sidebar.header("🛒 Seu Pedido")
total = 0.0
resumo = ""

if not st.session_state.carrinho:
    st.sidebar.info("Carrinho vazio.")
else:
    for item, d in st.session_state.carrinho.items():
        sub = d['preco'] * d['qtd']
        total += sub
        st.sidebar.write(f"{d['qtd']}x {item} - R$ {sub:.2f}")
        resumo += f"- {d['qtd']}x {item} (R$ {sub:.2f})\n"
    
    st.sidebar.success(f"**Total Produtos: R$ {total:.2f}**")
    
    # AVISO IMPORTANTE SOBRE O UBER MOTO
    st.sidebar.warning("🛵 **Entrega via Uber Moto**\n\nO custo do envio é por conta do cliente. Consulte o valor comigo pelo WhatsApp!")

    if st.sidebar.button("Limpar Carrinho"):
        st.session_state.carrinho = {}
        st.rerun()

    st.sidebar.markdown("---")
    nome = st.sidebar.text_input("Seu Nome:")
    end = st.sidebar.text_input("Endereço de Entrega:")
    
    if st.sidebar.button("🚀 Enviar Pedido"):
        if nome and end and total > 0:
            # --- COLOQUE O NÚMERO DA ELISA AQUI ---
            whats_elisa = "5511999999999" 
            
            mensagem_zap = (
                f"Olá Elisa! Pedido de Zynix App:\n\n"
                f"*Cliente:* {nome}\n"
                f"*Endereço:* {end}\n\n"
                f"*Itens:*\n{resumo}\n"
                f"*Total: R$ {total:.2f}*\n"
                f"_(Ciente que o frete via Uber Moto é à parte)_"
            )
            
            link_final = f"https://wa.me/{whats_elisa}?text={mensagem_zap.replace(' ', '%20').replace('\n', '%0A')}"
            st.sidebar.markdown(f"✅ [CONFIRMAR NO WHATSAPP]({link_final})")
        else:
            st.sidebar.error("Preencha nome/endereço!")

st.markdown("---")
st.caption("Desenvolvido por Zynix Studios")
