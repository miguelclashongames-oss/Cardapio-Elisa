import streamlit as st

# Configurações da Página (Ícone e Título da aba)
st.set_page_config(page_title="Cardápio Digital - Zynix", page_icon="🍔")

# Título Principal
st.title("🍔 Cardápio Digital - Elisa")
st.markdown("---")

# 1. Definir os Produtos (Você pode alterar os nomes e preços aqui)
cardapio = {
    "Lanches": {
        "X-Burguer": 15.00,
        "X-Salada": 18.00,
        "X-Tudo": 25.00,
    },
    "Acompanhamentos": {
        "Batata Frita": 12.00,
        "Nuggets (10 unidades)": 15.00,
    },
    "Bebidas": {
        "Coca-Cola Lata": 6.00,
        "Suco de Laranja": 8.00,
        "Água": 4.00
    }
}

# 2. Inicializar o Carrinho (Memória do App)
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = {}

# 3. Mostrar os Itens do Cardápio
for categoria, itens in cardapio.items():
    st.subheader(f"📍 {categoria}")
    for item, preco in itens.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{item}** - R$ {preco:.2f}")
        with col2:
            if st.button(f"Adicionar", key=item):
                if item in st.session_state.carrinho:
                    st.session_state.carrinho[item]['qtd'] += 1
                else:
                    st.session_state.carrinho[item] = {'preco': preco, 'qtd': 1}
                st.toast(f"{item} adicionado!")

st.markdown("---")

# 4. Barra Lateral - Resumo do Pedido
st.sidebar.header("🛒 Seu Carrinho")
total = 0.0
resumo_texto = ""

if not st.session_state.carrinho:
    st.sidebar.write("O carrinho está vazio.")
else:
    for item, dados in st.session_state.carrinho.items():
        subtotal = dados['preco'] * dados['qtd']
        total += subtotal
        st.sidebar.write(f"{dados['qtd']}x {item} - R$ {subtotal:.2f}")
        resumo_texto += f"- {dados['qtd']}x {item} (R$ {subtotal:.2f})\n"
    
    st.sidebar.markdown(f"### **Total: R$ {total:.2f}**")
    
    if st.sidebar.button("Limpar Carrinho"):
        st.session_state.carrinho = {}
        st.rerun()

    # 5. Finalizar Pedido
    st.sidebar.markdown("---")
    nome_cliente = st.sidebar.text_input("Qual o seu nome?")
    endereco = st.sidebar.text_input("Endereço de Entrega:")
    
    if st.sidebar.button("🚀 Enviar para o WhatsApp"):
        if nome_cliente and endereco:
            # --- COLOQUE O NÚMERO DA ELISA ABAIXO ---
            numero_elisa = "5511930357518" # Exemplo: 55 + DDD + Numero
            
            mensagem = (
                f"Olá Elisa! Novo pedido do seu cardapio:\n\n"
                f"*Cliente:* {nome_cliente}\n"
                f"*Endereço:* {endereco}\n\n"
                f"*Itens:*\n{resumo_texto}\n"
                f"*Total: R$ {total:.2f}*"
            )
            
            # Gera o link formatado
            link_final = f"https://wa.me/{numero_elisa}?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
            st.sidebar.markdown(f"✅ [CLIQUE AQUI PARA CONFIRMAR]({link_final})")
        else:
            st.sidebar.error("Por favor, preencha o nome e o endereço.")