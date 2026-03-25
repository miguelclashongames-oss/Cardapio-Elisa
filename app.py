import streamlit as st
import os

# Configurações de Elite
st.set_page_config(page_title="Elisa - Doces Finos", page_icon="🍫", layout="centered")

# --- DESIGN EXCLUSIVO ZYNIX (SEM BUGS DE COR) ---
st.markdown("""
    <style>
    /* Fundo com degradê sofisticado Zynix */
    .stApp { 
        background: linear-gradient(180deg, #FDFDFB 0%, #F5F5F0 100%); 
        color: #4A3728; 
    }
    
    /* Categorias com bordas arredondadas e sombra leve */
    .stExpander {
        border: 1px solid #D0A08A !important;
        border-radius: 15px !important;
        background-color: white !important;
        margin-bottom: 15px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    }
    .stExpander span {
        font-size: 22px !important;
        font-weight: 800 !important;
        color: #565F3A !important;
    }
    
    /* CORREÇÃO DEFINITIVA DO BOTÃO VERDE */
    div.stButton > button:first-child {
        background-color: #565F3A !important; /* Verde Botânico fixo */
        color: white !important; /* Texto sempre branco */
        border-radius: 10px !important;
        width: 100% !important;
        font-weight: bold !important;
        font-size: 14px !important;
        height: 45px !important;
        border: none !important;
        opacity: 1 !important; /* Garante que não fique transparente */
    }

    /* Efeito de clique mais elegante */
    div.stButton > button:active {
        background-color: #D0A08A !important;
        transform: scale(0.98);
    }

    /* Estilo do Carrinho e Inputs */
    .stTextInput input {
        border-radius: 10px !important;
        border: 1px solid #D0A08A !important;
    }
    
    /* Logo em Destaque Total */
    [data-testid="stImage"] img {
        width: 100% !important;
        border-radius: 0px 0px 20px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGO ---
camin_logo = os.path.join(os.path.dirname(__file__), "logo.png")
if os.path.exists(camin_logo):
    st.image(camin_logo, use_container_width=True)
else:
    st.warning("⚠️ Carregue a 'logo.png' para ativar o visual.")

# --- CARDÁPIO ATUALIZADO ---
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
            c1, c2 = st.columns([2.5, 1.5])
            c1.markdown(f"**{item}** \n<span style='color: #D0A08A; font-weight: bold;'>R$ {preco:.2f}</span>", unsafe_allow_html=True)
            if c2.button("ADICIONAR", key=f"add_{categoria}_{item}"):
                if item in st.session_state.carrinho:
                    st.session_state.carrinho[item]['qtd'] += 1
                else:
                    st.session_state.carrinho[item] = {'preco': preco, 'qtd': 1}
                st.rerun()

st.markdown("---")

# --- RESUMO FINAL ---
st.header("🛒 Seu Carrinho")

if not st.session_state.carrinho:
    st.info("O carrinho está vazio. Comece a adicionar!")
else:
    total = 0.0
    resumo_msg = ""
    
    for item, info in st.session_state.carrinho.items():
        sub = info['preco'] * info['qtd']
        total += sub
        st.write(f"✅ {info['qtd']}x {item} — **R$ {sub:.2f}**")
        resumo_msg += f"- {info['qtd']}x {item} (R$ {sub:.2f})\n"
    
    st.markdown(f"## **Total: R$ {total:.2f}**")
    
    if st.button("Limpar Carrinho"):
        st.session_state.carrinho = {}
        st.rerun()

    st.markdown("---")
    st.subheader("🏁 Finalização")
    nome_user = st.text_input("Seu Nome:")
    end_user = st.text_input("Endereço (Opcional - Vazio para Retirada):")
    
    st.markdown("""
        <div style="background-color: #FDFDFB; padding: 12px; border-radius: 10px; border: 1px dashed #565F3A; margin-top: 10px;">
            <p style="color: #565F3A; margin: 0; font-size: 14px;">🛵 <b>Aviso de Entrega:</b> Usamos Uber Moto. O valor do frete é combinado diretamente no WhatsApp.</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("GERAR PEDIDO"):
        if nome_user:
            whats_num = "5511999999999" # <-- MUDE PARA O NÚMERO DA ELISA
            local_entrega = end_user if end_user else "Retirada no Local"
            texto = (f"Olá Elisa! Novo pedido:\n\n*Cliente:* {nome_user}\n*Entrega:* {local_entrega}\n\n*Itens:*\n{resumo_msg}\n*Total: R$ {total:.2f}*")
            link_final = f"https://wa.me/{whats_num}?text={texto.replace(' ', '%20').replace('\n', '%0A')}"
            
            st.markdown(f'''
                <a href="{link_final}" target="_blank" style="text-decoration: none;">
                    <div style="background-color: #25D366; color: white; padding: 18px; text-align: center; border-radius: 12px; font-weight: bold; font-size: 18px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
                        🚀 ENVIAR AGORA PARA O WHATSAPP
                    </div>
                </a>
            ''', unsafe_allow_html=True)
        else:
            st.error("⚠️ Por favor, digite seu nome.")

st.markdown("<br><hr><center><small>Desenvolvido por Zynix</small></center>", unsafe_allow_html=True)
