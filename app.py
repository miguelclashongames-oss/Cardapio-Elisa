import streamlit as st
import os

# Configurações de Elite
st.set_page_config(page_title="Elisa - Doces Finos", page_icon="🍫", layout="centered")

# --- DESIGN SIGNATURE ZYNIX ---
st.markdown("""
    <style>
    /* Fundo e Tipografia */
    .stApp { background-color: #FDFDFB; color: #4A3728; }
    
    /* Categorias com Estilo */
    .stExpander {
        border: 1px solid #D0A08A !important;
        border-radius: 15px !important;
        background-color: white !important;
        margin-bottom: 10px;
    }
    .stExpander span {
        font-size: 22px !important;
        font-weight: 800 !important;
        color: #565F3A !important;
    }
    
    /* BOTÃO ADICIONAR - CORREÇÃO VISUAL */
    .stButton button {
        background-color: #565F3A !important; /* Verde Botânico */
        color: white !important; /* Texto SEMPRE visível */
        border-radius: 8px !important;
        width: 100% !important;
        font-weight: bold !important;
        border: none !important;
        height: 45px;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #D0A08A !important; /* Rosé no Hover */
        transform: scale(1.02);
    }

    /* Caixa de Finalização */
    .caixa-final {
        background-color: #565F3A;
        padding: 25px;
        border-radius: 20px;
        color: white;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Logo em Destaque */
    [data-testid="stImage"] img {
        width: 100% !important;
        border-radius: 0px 0px 30px 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGO ---
caminho_logo = os.path.join(os.path.dirname(__file__), "logo.png")
if os.path.exists(caminho_logo):
    st.image(caminho_logo, use_container_width=True)
else:
    st.warning("⚠️ Adicione 'logo.png' no GitHub para ativar o visual completo.")

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

# --- INTERFACE DE COMPRA ---
st.markdown("### ✨ Faça sua escolha abaixo:")

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

# --- CARRINHO DINÂMICO ---
st.header("🛒 Resumo do Pedido")

if not st.session_state.carrinho:
    st.info("Seu carrinho está vazio. Adicione delícias acima!")
else:
    total = 0.0
    resumo_zap = ""
    
    for item, info in st.session_state.carrinho.items():
        sub = info['preco'] * info['qtd']
        total += sub
        st.write(f"🔹 {info['qtd']}x {item} — **R$ {sub:.2f}**")
        resumo_zap += f"- {info['qtd']}x {item} (R$ {sub:.2f})\n"
    
    st.markdown(f"## **Total: R$ {total:.2f}**")
    
    if st.button("Limpar Escolhas"):
        st.session_state.carrinho = {}
        st.rerun()

    st.markdown("---")
    
    # Finalização
    st.subheader("🏁 Finalizar Pedido")
    nome = st.text_input("Seu Nome:")
    endereco = st.text_input("Endereço (ou deixe vazio para retirar):")
    
    st.markdown("""
        <div style="background-color: #F1FAEE; padding: 10px; border-radius: 10px; border-left: 5px solid #565F3A;">
            <small style="color: #565F3A;">🛵 <b>Aviso:</b> Entregas via Uber Moto. Consulte o valor do frete no WhatsApp.</small>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Espaçador

    if st.button("✅ ENVIAR PARA O WHATSAPP"):
        if nome:
            whats_elisa = "5511999999999" # TROQUE PELO NÚMERO REAL
            local = endereco if endereco else "Retirada no Local"
            msg = (f"Olá Elisa! Pedido via Web:\n\n*Cliente:* {nome}\n*Local:* {local}\n\n*Itens:*\n{resumo_zap}\n*Total: R$ {total:.2f}*")
            link = f"https://wa.me/{whats_elisa}?text={msg.replace(' ', '%20').replace('\n', '%0A')}"
            
            # Botão de WhatsApp Estilizado
            st.markdown(f'''
                <a href="{link}" target="_blank" style="text-decoration: none;">
                    <div style="background-color: #25D366; color: white; padding: 18px; text-align: center; border-radius: 12px; font-weight: bold; font-size: 20px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);">
                        📱 FINALIZAR NO WHATSAPP
                    </div>
                </a>
            ''', unsafe_allow_html=True)
        else:
            st.error("Por favor, preencha seu nome para continuar.")

st.markdown("<br><br><center><small>Desenvolvido por Zynix</small></center>", unsafe_allow_html=True)
