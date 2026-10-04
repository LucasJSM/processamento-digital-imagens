# 🖼️ Processamento Digital de Imagens

Este repositório contém três atividades práticas de **Processamento Digital de Imagens** utilizando **OpenCV** e **Matplotlib**. O objetivo é demonstrar operações fundamentais como visualização, conversão de espaço de cores, redimensionamento, composição de canais RGB e aplicação de filtros de suavização.

---

## 📁 Estrutura do Projeto

- 📂 av1/ — Primeiro Trabalho
    - 📄 `q1.py` — Exibição de imagem
    - 📄 `q2.py` — Conversão para escala de cinza
    - 📄 `q3.py` — Separação e recomposição de canais RGB
- 📂 av2/ — Segundo Trabalho
    - 📄 `q1.py` — Aplicação e comparação de filtros de suavização (Blur, Gaussiano e Mediana)
- 📂 `images/` — Imagens utilizadas nas atividades
- 📄 `split_rgb_channels.py` — Script para separar os canais RGB de uma imagem e salvar separadamente
- 📄 requirements.txt — Lista de dependências do projeto

---

## 🛠️ Requisitos e Instalação

Antes de executar os scripts, certifique-se de ter o **Python 3** instalado.

Instale as dependências com o comando:

```bash
pip install -r requirements.txt
```

## 🚀 Como Executar
Você pode executar cada questão individualmente via terminal:

```Bash
# Questão 1
python av1/q1.py

# Questão 2
python av1/q2.py

# Questão 3
python av1/q3.py

# Questão AV2
python av2/q1.py
```

## ✨ Extras

Use o script `split_rgb_channels.py` para separar uma imagem nos canais **azul**, **vermelho** e **verde**.

1. Adicione uma imagem `.jpg` à pasta `images/`.
2. Altere a variável `img_name` para o nome da sua imagem, onde o script irá procurar por `images/{img_name}.jpg`.
3. Execute o comando na raiz do projeto:

```bash
python split_rgb_channels.py
```

Os canais separados serão salvos em `images/` com os nomes 
1. `image_name_blue.jpg`
2. `image_name_red.jpg`
3. `image_name_green.jpg`.
