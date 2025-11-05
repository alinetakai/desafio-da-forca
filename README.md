<h1 align="center">🎯 Desafio da Forca – Jogo em Python 🐍</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen" alt="Status Badge">
  <img src="https://img.shields.io/badge/Licença-Livre-lightgrey" alt="License Badge">
</p>

<p align="center">
  <i>Um projeto de lógica e modularização em Python.</i><br>
  <b>Autor:</b> Aline Takai
</p>

---

## 🧩 Sobre o Projeto  👩‍💻

O **Desafio da Forca** é um jogo interativo desenvolvido em **Python**, com o objetivo de praticar **lógica de programação**, **funções** e **modularização**.  
O projeto demonstra como criar um jogo de terminal limpo e funcional, estruturado em partes independentes e reutilizáveis, seguindo boas práticas de código.
Este projeto também faz parte da minha jornada de aprendizado e aperfeiçoamento em **Python** e **automação**.  
Além de reforçar conceitos de **lógica**, ele demonstra boas práticas de **organização de código**, **clareza de funções** e **interação com o usuário**.  

---

## ⚙️ Funcionalidades  

✅ Exibição de título e formatação visual  
🔠 Mostra letras descobertas e traços para as ocultas  
🚫 Controla tentativas e letras erradas  
🏆 Detecta vitória ou derrota automaticamente  
🧩 Código dividido em funções organizadas  

---

## 🧠 Estrutura do Código  

| Função | Descrição |
|:-------|:-----------|
| `limpar_tela()` | Limpa o terminal conforme o sistema operacional |
| `exibir_titulo()` | Exibe o título e o cabeçalho do jogo |
| `mostrar_palavra(palavra, letras_certas)` | Mostra a palavra parcialmente descoberta |
| `verificar_letra(letra, palavra, letras_certas, letras_erradas)` | Atualiza acertos e erros |
| `verificar_vitoria(palavra, letras_certas)` | Verifica se o jogador completou a palavra |

---

## 🕹️ Como Jogar  

Clone ou baixe este repositório.

```bash
  git clone https://github.com/alinetakai/desafio-da-forca
```

Em seguida:

1️⃣ Execute o script `main.py`  
2️⃣ O jogo sorteará uma palavra secreta  
3️⃣ Digite uma letra por vez  
4️⃣ Cada erro reduz o número de tentativas  
5️⃣ Vença ao descobrir todas as letras antes que acabem as chances!  

---

## 💡 Exemplo de Execução  

```bash
🎯 JOGO DA FORCA 🎯
-------------------------
Palavra: _ _ _ _ _
Letras erradas: 
Tentativas restantes: 6

Digite uma letra: a
Boa! A letra "a" existe na palavra.
```
---

## 🧰 Tecnologias Utilizadas  

| Categoria | Detalhes |
|------------|-----------|
| 💻 **Linguagem** | Python 3.x |
| 📚 **Bibliotecas** | os, random |
| ⚙️ **Ambiente** | Terminal |
| 🧠 **Conceitos** | Estruturas de repetição, condicionais, funções e modularização |

---

## 🚀 Melhorias Futuras  

🔹 Adicionar lista de palavras externas (arquivo `.txt`)  
🔹 Implementar sistema de pontuação e ranking  
🔹 Criar interface gráfica (Tkinter ou PyQt)  
🔹 Adicionar modo “duelo” para dois jogadores  

---

## 📜 Licença  

- **Permissão de Uso:** Este projeto é de **código aberto** e pode ser utilizado para fins **educacionais**. 
- **Modificação e Distribuição:** Sinta-se à vontade para **clonar**, **modificar** e **aprimorar**! Qualquer pessoa pode modificar o código e redistribuí-lo, seja na forma original ou modificada, desde que citando autores.
- **Inclusão da Licença:** Ao redistribuir o software, a licença original e o aviso de direitos autorais devem ser incluídos no código fonte ou na documentação, garantindo que futuros usuários conheçam seus direitos.
- **Isenção de Garantia:** O software é fornecido "como está", sem garantias de qualquer tipo, explícitas ou implícitas. Os autores não são responsáveis por quaisquer danos decorrentes do uso do software.

---

## 👩‍💻 Autora

- [@alinetakai](https://github.com/alinetakai)

---

⭐ **Se você gostou deste projeto**, deixe uma estrela ⭐ no repositório e acompanhe meu portfólio para mais projetos de **automação e análise de dados**!

