# Goku Black — AI Vision

Um sistema de visão computacional baseado em IA com interface web futurista, inspirado no personagem Goku Black de Dragon Ball. Utiliza aprendizado de máquina para classificação de imagens em tempo real via webcam.

## 🚀 Demonstração

![Interface Goku Black AI Vision](https://via.placeholder.com/800x400/1a1a20/ffffff?text=Goku+Black+AI+Vision+Demo)

## ✨ Características

- **Classificação em Tempo Real**: Análise contínua de imagens capturadas pela webcam
- **Interface Futurista**: Design inspirado em Goku Black com tema escuro e efeitos visuais
- **Modelo Treinável**: Baseado no Teachable Machine do Google
- **Responsivo**: Funciona em dispositivos móveis e desktop
- **Efeitos Visuais**: Partículas flutuantes, linhas de varredura e animações

## 🛠️ Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **IA/ML**: TensorFlow.js, Teachable Machine Image
- **UI Framework**: Bootstrap 5.3.2
- **Fontes**: Google Fonts (Cinzel Decorative, Rajdhani, Orbitron)

## 📋 Pré-requisitos

- Navegador web moderno com suporte a WebRTC (Chrome, Firefox, Safari, Edge)
- Permissões de câmera habilitadas
- Conexão com internet para carregar o modelo de IA

## 🚀 Instalação e Uso

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/goku-black-ai-vision.git
   cd goku-black-ai-vision
   ```

2. **Abra o arquivo**:
   - Abra `index.html` em seu navegador web
   - Ou use um servidor local (recomendado para melhor compatibilidade):
     ```bash
     python -m http.server 8000
     ```
     Acesse: `http://localhost:8000`

3. **Permita acesso à câmera**:
   - Clique em "Ativar Câmera"
   - Autorize o acesso à webcam quando solicitado

4. **Comece a classificar**:
   - O sistema irá carregar o modelo de IA automaticamente
   - Posicione objetos/imagens diante da câmera
   - Veja as previsões em tempo real no painel lateral

## 🎯 Como Funciona

1. **Inicialização**: Carrega o modelo pré-treinado do Teachable Machine
2. **Captura**: Ativa a webcam e captura frames continuamente
3. **Processamento**: Aplica o modelo de IA para classificar a imagem
4. **Exibição**: Mostra as probabilidades de cada classe detectada

## 📁 Estrutura do Projeto

```
goku-black-ai-vision/
├── index.html                 # Página principal da aplicação
├── test-assistent-programing/ # Exemplos de programação assistida por IA
│   ├── debug.py              # Script de debug (vazio)
│   ├── num_primo.py          # Verificador de números primos
│   ├── refatoracao.py        # Exemplo de refatoração de código
│   ├── explicacao_refatocao.md    # Explicação da refatoração
│   └── explicção_num_primo.md     # Explicação do algoritmo primo
└── README.md                 # Este arquivo
```

## 🔧 Exemplos de Programação

A pasta `test-assistent-programing` contém exemplos de código Python criados com assistência de IA, demonstrando:

### Verificador de Números Primos (`num_primo.py`)
- Implementação otimizada do algoritmo de verificação de primalidade
- Validação de entrada e tratamento de erros
- Documentação completa com docstrings

### Refatoração de Código (`refatoracao.py`)
- Exemplo de transformação de código procedural para funcional
- Melhoria de legibilidade e manutenibilidade
- Uso de built-ins do Python para eficiência

## 🎨 Personalização

### Alterando o Tema
O design pode ser personalizado editando as variáveis CSS em `:root` no arquivo `index.html`:

```css
:root {
  --gold: #c9a84c;        /* Cor principal */
  --black: #050507;       /* Fundo escuro */
  --purple: #6b21a8;      /* Acento roxo */
  /* ... outras variáveis */
}
```

### Treinando um Novo Modelo
Para usar seu próprio modelo do Teachable Machine:

1. Acesse [Teachable Machine](https://teachablemachine.withgoogle.com/)
2. Treine um modelo de classificação de imagens
3. Exporte o modelo e hospede os arquivos
4. Atualize a URL no código JavaScript:
   ```javascript
   const URL = "https://sua-url-do-modelo/";
   ```

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- **Teachable Machine** por fornecer a plataforma de ML acessível
- **TensorFlow.js** pela biblioteca de machine learning no navegador
- **Bootstrap** pelo framework CSS responsivo
- **Google Fonts** pelas fontes tipográficas

## 📞 Contato

- **Autor**: [Seu Nome]
- **Email**: seu-email@exemplo.com
- **GitHub**: [seu-usuario](https://github.com/seu-usuario)

---

*"O plano mortal zero começa agora." - Goku Black*</content>
<parameter name="filePath">c:\Users\YGORLUISFIGUEIREDOBA\Documents\imageModel\README.md