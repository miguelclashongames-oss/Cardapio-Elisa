import streamlit as st
import os

# Configurações da Página
st.set_page_config(page_title="Elisa - Doces Finos Artesanais", page_icon="🍫", layout="centered")

# --- CSS PARA DEIXAR TUDO GRANDE E LIMPO ---
st.markdown("""
    <style>
    .stApp { background-color: #F8F9F5; color: #533E2B; }
    
    /* Títulos das Categorias Gigantes */
    .stExpander span {
        font-size: 26px !important;
        font-weight: bold !important;
        color: #565F3A !important;
    }
    
    /* Botão de Adicionar mais visível */
    .stButton button { 
        background-color: #565F3A; 
        color: white; 
        border-radius: 10px;
        width: 100%;
        font-weight: bold;
    }

    /* Logo Máxima */
    [data-testid="stImage"] img { width: 100% !important; }
    
    /* Estilo do Carrinho no final da página */
    .caixa-pedido {
        background-color: #565F3A;
        padding: 20px;
        border-radius: 15px;
        color: white !important;
        margin-top: 30px;
    }
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

# --- EXIBIÇÃO DOS ITENS ---
for categoria, itens in cardapio.items():
    with st.expander(categoria, expanded=False):
        for item, preco in itens.items():
            c1, c2 = st.columns([3, 1])
            c1.markdown(f"**{item}** \n R$ {preco:.2f}")
            if c2.button("ADICIONAR", key=f"btn_{categoria}_{item}"):
                if item in st.session_state.carrinho:
                    st.session_state.carrinho[item]['qtd'] += 1
                else:
                    st.session_state.carrinho[item] = {'preco': preco, 'qtd': 1}
                st.rerun() # ISSO FAZ O CARRINHO ATUALIZAR NA HORA!

st.markdown("---")

# --- CARRINHO NO FINAL DA PÁGINA (MAIS FÁCIL PARA O CLIENTE) ---
st.header("🛒 Seu Pedido")

if not st.session_state.carrinho:
    st.info("Escolha os itens acima para montar seu pedido!")
else:
    total = 0.0
    resumo_texto = ""
    
    for item, dados in st.session_state.carrinho.items():
        subtotal = dados['preco'] * dados['qtd']
        total += subtotal
        st.write(f"✅ {dados['qtd']}x **{item}** - R$ {subtotal:.2f}")
        resumo_texto += f"- {dados['qtd']}x {item} (R$ {subtotal:.2f})\n"
    
    st.markdown(f"### **Total: R$ {total:.2f}**")
    
    if st.button("🗑️ Limpar Tudo"):
        st.session_state.carrinho = {}
        st.rerun()

    st.markdown("---")
    st.subheader("📝 Finalizar Pedido")
    nome_cliente = st.text_input("Seu Nome (Obrigatório):")
    endereco_cliente = st.text_input("Endereço (Deixe vazio para Retirada):")
    st.info("🛵 Entrega via Uber Moto - Consulte o valor comigo!")

    if st.button("🚀 ENVIAR PEDIDO PARA O WHATSAPP"):
        if nome_cliente:
            whats_elisa = "5511999999999" # <-- COLOQUE O NÚMERO REAL AQUI!
            local = endereco_cliente if endereco_cliente else "Retirada no Local"
            msg = (f"Olá Elisa! Pedido de Zynix App:\n\n*Cliente:* {nome_cliente}\n*Local:* {local}\n\n*Itens:*\n{resumo_texto}\n"
                   f"*Total: R$ {total:.2f}*")
            
            # Link do WhatsApp
            link_zap = f"https://wa.me/{whats_elisa}?text={msg.replace(' ', '%20').replace('\n', '%0A')}"
            st.markdown(f'<a href="{link_zap}" target="_blank" style="text-decoration: none;"><div style="background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 18px;">✅ TUDO CERTO! CLIQUE AQUI PARA MANDAR NO ZAP</div></a>', unsafe_allow_html=True)
        else:
            st.error("⚠️ Digite seu nome antes de enviar!")

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Desenvolvido por Zynix Studios")
