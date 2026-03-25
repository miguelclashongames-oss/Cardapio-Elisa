import streamlit as st

# Configurações da Página
st.set_page_config(page_title="Elisa Lanches & Chocolates", page_icon="🍫")

# --- LOGO CHAMATIVA (ESTILO ZYNIX) ---
st.markdown("""
    <style>
    .logo-text {
        font-family: 'Arial Black', sans-serif;
        color: #E63946;
        font-size: 40px;
        text-align: center;
        text-shadow: 2px 2px #F1FAEE;
        margin-bottom: 0px;
    }
    .sub-logo {
        color: #457B9D;
        font-size: 18px;
        text-align: center;
        margin-top: -10px;
        font-weight: bold;
    }
    </style>
    <p class="logo-text">ELISA LANCHES</p>
    <p class="sub-logo">& CHOCOLATES</p>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- BANCO DE DADOS DO CARDÁPIO COM EMOJIS ---
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

# Exibir os itens
for categoria, itens in cardapio.items():
    with st.expander(categoria, expanded=True):
        for item, preco in itens.items():
            c1, c2 = st.columns([3, 1])
            c1.write(f"**{item}** - R$ {preco:.2f}")
            
            # Chave única para evitar erro de elemento duplicado
            chave_botao = f"btn_{categoria}_{item}".replace(" ", "_")
            
            if c2.button("Adicionar", key=chave_botao):
                if item in st.session_state.carrinho:
                    st.session_state.carrinho[item]['qtd'] += 1
                else:
                    st.session_state.carrinho[item] = {'preco': preco, 'qtd': 1}
                st.toast(f"{item} adicionado!")

# --- BARRA LATERAL (CHECKOUT) ---
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
    
    st.sidebar.success(f"**Total: R$ {total:.2f}**")
    
    if st.sidebar.button("Limpar Tudo"):
        st.session_state.carrinho = {}
        st.rerun()

    st.sidebar.markdown("---")
    nome = st.sidebar.text_input("Seu Nome:")
    end = st.sidebar.text_input("Endereço ou Mesa:")
    
    if st.sidebar.button("🚀 Enviar Pedido"):
        if nome and end and total > 0:
            # --- LEMBRE DE TROCAR O NÚMERO ABAIXO PARA O DA ELISA ---
            whats_elisa = "5511954906016" 
            
            mensagem_zap = (
                f"Olá Elisa! Pedido via cardapio digital:\n\n"
                f"*Cliente:* {nome}\n"
                f"*Local:* {end}\n\n"
                f"*Itens:*\n{resumo}\n"
                f"*Total: R$ {total:.2f}*"
            )
            
            link_final = f"https://wa.me/{whats_elisa}?text={mensagem_zap.replace(' ', '%20').replace('\n', '%0A')}"
            st.sidebar.markdown(f"✅ [CLIQUE AQUI PARA ENVIAR]({link_final})")
        else:
            st.sidebar.warning("Preencha seus dados e adicione itens!")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido por Zynix Studios")
