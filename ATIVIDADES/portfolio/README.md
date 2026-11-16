# Portfólio Profissional — Desenvolvimento de Sistemas

**Aluno:** Renato Lima  
**Link do site publicado:** https://github.com/renatolima92

---

## 📋 Descrição do Portfólio
Este projeto consiste no desenvolvimento e evolução de um portfólio pessoal responsivo, criado a partir da estrutura base trabalhada em aula e aprimorado para simular uma página real de apresentação profissional na área de Tecnologia da Informação.

O objetivo do site é centralizar informações sobre minha trajetória acadêmica, habilidades técnicas, projetos desenvolvidos e canais de contato profissional.

---

## 🛠️ Tecnologias Utilizadas
* **HTML5:** Estruturação semântica das seções da página.
* **CSS3:** Estilização customizada, variáveis visuais, efeitos de transição e animações.
* **Bootstrap 5.3:** Sistema de grid responsivo, barra de navegação (`navbar`), `carousel`, cards e barras de progresso.
* **Devicon & Bootstrap Icons:** Ícones vetoriais para representação das ferramentas e links sociais.
* **Git & GitHub Pages:** Controle de versão e hospedagem gratuita do site estático.

---

## ⚙️ Funcionamento do Projeto
O site funciona como uma *Single Page Application* (página única) dividida em seções estratégicas acessíveis através de um menu de navegação fixo no topo (`sticky-top`):
1. **Banner Principal (Carousel):** Apresentação visual com slides rotativos e botões de redirecionamento rápido.
2. **Perfil:** Apresentação pessoal, foto, dados básicos (localização, objetivo e área de interesse) e grade de tecnologias dominadas.
3. **Formação & Qualificações:** Linha do tempo acadêmica e indicadores visuais de proficiência.
4. **Projetos:** Vitrine em formato de cards exibindo os principais trabalhos realizados, tecnologias aplicadas e links para os repositórios no GitHub.
5. **Contato:** Cartão centralizado com botões de acesso direto para e-mail, GitHub e LinkedIn.

---

## ✨ Recursos Novos Adicionados (Evolução do Projeto)
Para ir além do modelo base desenvolvido em aula, foram implementados os seguintes recursos:
1. **Nova Seção de Formação e Proficiência:** Inclusão de uma seção dedicada à trajetória educacional (com linha do tempo visual) e barras de progresso (`progress-bar`) indicando o nível de familiaridade com cada tecnologia.
2. **Animações e Micro-interações (`hover` e transições CSS):** Aplicação de efeitos de elevação nos cards (`translateY`), zoom suave nas imagens dos projetos ao passar o cursor e transição na foto de perfil.
3. **Efeito Visual no Carousel (*Glassmorphism*):** Adição de legendas sobrepostas com fundo translúcido desfocado (`backdrop-filter: blur`) e botões de ação direta nos slides.
4. **Navegação Fluida e Botão "Voltar ao Topo":** Rolagem suave entre as seções (`scroll-behavior: smooth`) e botão flutuante fixo no canto inferior direito.

---

## 💻 Como os Recursos Foram Implementados
* **Animações e Hover:** Criou-se a classe CSS `.card-hover` utilizando a propriedade `transition: transform 0.3s ease, box-shadow 0.3s ease;` combinada com a pseudo-classe `:hover` para deslocar os elementos no eixo Y e intensificar a sombra. Nas imagens dos projetos, utilizou-se um contêiner com `overflow: hidden` para permitir o `scale(1.06)` sem vazar das bordas arredondadas.
* **Seção de Formação:** Implementada com o sistema de colunas do Bootstrap (`row` e `col-lg-6`), utilizando pseudo-elementos CSS (`::before`) para desenhar os marcadores circulares da linha do tempo e o componente nativo `.progress` do Bootstrap para as barras de habilidades.
* **Efeito no Carousel:** Inserido o componente `.carousel-caption` dentro de cada `.carousel-item`, estilizado com fundo semitransparente (`rgba`) e desfoque de fundo (`backdrop-filter: blur(8px)`), além de reduzir o brilho das imagens (`filter: brightness(0.65)`) para garantir legibilidade do texto.