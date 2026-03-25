import streamlit as st
import os

# Configurações de Elite
st.set_page_config(page_title="Elisa - Doces Finos", page_icon="🍫", layout="centered")

# --- DESIGN ANTI-HULK ZYNIX (HTML PURO PARA OS BOTÕES) ---
st.markdown("""
    <style>
    /* Fundo Sofisticado */
    .stApp { 
        background: linear-gradient(180deg, #FDFDFB 0%, #F5F5F0 100%); 
        color: #4A3728; 
    }
    
    /* REMOVER QUALQUER EFEITO DE FOCO OU SELEÇÃO VERDE PADRÃO */
    button:focus, button:active, .stButton button:focus {
        outline: none !important;
        box-shadow: none !important;
        background-color: #565F3A !important;
        color: white !important;
    }

    /* ESTILO DO BOTÃO REAL (FORÇADO) */
    div.stButton > button {
        background-color: #565F3A !important; 
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
        height: 45px !important;
        font-weight: bold !important;
        font-size: 14px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        display: block !important;
    }

    /* Mudar para Rose apenas no Hover, sem o verde do Streamlit */
    div.stButton > button:hover {
        background-color: #D0A08A !important;
        color: white !important;
    }

    .stExpander {
        border: 1px solid #D0A08A !important;
        border-radius: 12px !important;
        background-color: white !important;
        margin-bottom: 10px;
    }
    
    [data-testid="stImage"] img {
        width: 100% !important;
        border-radius: 0 0 20px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGO ---
caminho_logo = os.path.join(os.path.dirname(__file__), "logo.png")
if os.path.exists(caminho_logo):
    st.image(caminho_logo, use_container_width=True)

# --- BANCO DE DATOS ---
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

# --- INTERFACE ---
st.markdown("### ✨ Selecione seus produtos:")

for categoria, itens in cardapio.items():
    with st.expander(categoria):
        for item, preco in itens.items():
            col_txt, col_btn = st.columns([2.5, 1.5])
            col_txt.markdown(f"**{item}**\n<span style='color: #D0A08A;'>R$ {preco:.2f}</span>", unsafe_allow_html=True)
            
            # O BOTÃO AGORA TEM UM ESTILO FORÇADO PARA NÃO FICAR VERDE
            if col_btn.button("ADICIONAR", key=f"add_{categoria}_{item}"):
                if item in st.session_state.carrinho:
                    st.session_state.carrinho[item]['qtd'] += 1
                else:
                    st.session_state.carrinho[item] = {'preco': preco, 'qtd': 1}
                st.rerun()

st.markdown("---")

# --- CARRINHO ---
st.header("🛒 Seu Carrinho")

if not st.session_state.carrinho:
    st.info("O carrinho está vazio.")
else:
    total = 0.0
    resumo_msg = ""
    for item, info in st.session_state.carrinho.items():
        sub = info['preco'] * info['qtd']
        total += sub
        st.write(f"✅ {info['qtd']}x {item} — **R$ {sub:.2f}**")
        resumo_msg += f"- {info['qtd']}x {item} (R$ {sub:.2f})\n"
    
    st.markdown(f"## **Total: R$ {total:.2f}**")
    
    if st.button("LIMPAR TUDO"):
        st.session_state.carrinho = {}
        st.rerun()

    st.markdown("---")
    st.subheader("🏁 Finalização")
    nome_user = st.text_input("Nome:")
    end_user = st.text_input("Endereço (Opcional):")

    if st.button("GERAR PEDIDO"):
        if nome_user:
            whats_num = "5511999999999" # TROQUE PELO NÚMERO REAL
            local = end_user if end_user else "Retirada no Local"
            texto = (f"Olá Elisa! Novo pedido:\n\n*Cliente:* {nome_user}\n*Entrega:* {local}\n\n*Itens:*\n{resumo_msg}\n*Total: R$ {total:.2f}*")
            link = f"https://wa.me/{whats_num}?text={texto.replace(' ', '%20').replace('\n', '%0A')}"
            
            st.markdown(f'''
                <a href="{link}" target="_blank" style="text-decoration: none;">
                    <div style="background-color: #25D366; color: white; padding: 18px; text-align: center; border-radius: 12px; font-weight: bold;">
                        🚀 ENVIAR PARA O WHATSAPP
                    </div>
                </a>
            ''', unsafe_allow_html=True)
        else:
            st.error("Digite seu nome!")

st.markdown("<br><hr><center><small>Desenvolvido por Zynix</small></center>", unsafe_allow_html=True)
