import streamlit as st

# Configurações da Página
st.set_page_config(page_title="Elisa Lanches & Chocolates", page_icon="🍫")

# --- LOGO CHAMATIVA (CSS/HTML) ---
st.markdown("""
    <style>
    .logo-text {
        font-family: 'Arial Black', sans-serif;
        color: #E63946; /* Vermelho Chamativo */
        font-size: 45px;
        text-align: center;
        text-shadow: 2px 2px #F1FAEE;
        margin-bottom: 0px;
    }
    .sub-logo {
        color: #457B9D; /* Azul Escuro */
        font-size: 20px;
        text-align: center;
        margin-top: -10px;
        font-weight: bold;
    }
    </style>
    <p class="logo-text">ELISA LANCHES</p>
    <p class="sub-logo">& CHOCOLATES</p>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- BANCO DE DADOS DO CARDÁPIO ---
cardapio = {
    "🌮 Tapiocas Salgadas": {
        "Manteiga": 10.00,
        "Presunto com Mussarela": 15.00,
        "Mussarela": 15.00,
        "Calabresa": 15.00,
        "Bauru": 20.00,
        "Calabresa com Requeijão": 20.00,
        "Calabresa com Mussarela": 20.00,
        "Frango": 15.00,
        "Frango com Mussarela": 20.00,
        "Frango com Requeijão": 20.00,
        "Carne Seca": 20.00,
        "Carne Seca com Requeijão": 25.00,
        "Carne Seca com Mussarela": 25.00,
        "Queijo Coalho": 25.00,
    },
    "🍯 Tapiocas Doces": {
        "Coco com Leite Condensado": 20.00,
        "Mussarela com Goiabada": 20.00,
        "Doce de Leite": 20.00,
        "Banana com Leite Condensado": 20.00,
    },
    "🍕 Mini Pizzas": {
        "Mussarela": 10.00,
        "Calabresa": 10.00,
        "Margarita": 12.00,
        "Frango": 15.00,
        "Calabresa com Requeijão": 12.00,
        "Frango com Requeijão": 17.00,
    },
    "🐣 Ovos Trufados e de Colher": {
        "Ovo PP (250g)": 0.00, # AJUSTE OS PREÇOS AQUI
        "Ovo P (350g)": 0.00,
        "Ovo M/N (500g)": 0.00,
        "Ovo GG (1kg)": 0.00,
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
            if c2.button("Adicionar", key=item):
                if item in st.session_state.carrinho:
                    st.session_state.carrinho[item]['qtd'] += 1
                else:
                    st.session_state.carrinho[item] = {'preco': preco, 'qtd': 1}
                st.toast(f"{item} no carrinho!")

# --- BARRA LATERAL (CHECKOUT) ---
st.sidebar.header("🛒 Seu Pedido")
total = 0.0
resumo = ""

if not st.session_state.carrinho:
    st.sidebar.info("Seu carrinho está vazio.")
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
    end = st.sidebar.text_input("Endereço/Mesa:")
    
    if st.sidebar.button("Finalizar no WhatsApp"):
        if nome and end:
            # TROQUE PELO WHATSAPP REAL DA ELISA
            whats = "5511999999999" 
            msg = f"Olá Elisa! Pedido via Zynix App:\n\n*Cliente:* {nome}\n*Local:* {end}\n\n*Itens:*\n{resumo}\n*Total: R$ {total:.2f}*"
            link = f"https://wa.me/{whats}?text={msg.replace(' ', '%20').replace('\n', '%0A')}"
            st.sidebar.markdown(f"[✅ ENVIAR AGORA PARA ELISA]({link})")
        else:
            st.sidebar.warning("Preencha nome e endereço!")

# Rodapé da sua agência
st.markdown("---")
st.caption("Desenvolvido por Zynix Studios")
