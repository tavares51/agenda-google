# Configuração da API do Google Agenda

Este guia explica como configurar a API do Google Agenda para integrá-la ao seu projeto.

## Pré-requisitos

1. Conta no Google.
2. Acesso ao [Google Cloud Console](https://console.cloud.google.com/).
3. Instalação do Python (se for utilizar bibliotecas como `google-api-python-client`) ou outro SDK suportado.

---

## Passo 1: Criar um Projeto no Google Cloud

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2. Clique em **Select a project** (ou **Criar Projeto**).
3. Dê um nome ao seu projeto e clique em **Criar**.
4. Selecione o projeto recém-criado no menu superior.

---

## Passo 2: Habilitar a API do Google Agenda

1. No menu lateral, vá para **APIs e serviços > Biblioteca**.
2. Pesquise por **Google Calendar API**.
3. Clique na API encontrada e, em seguida, clique em **Ativar**.

---

## Passo 3: Criar Credenciais de Acesso

1. No menu lateral, vá para **APIs e serviços > Credenciais**.
2. Clique em **Criar Credenciais** > **ID do cliente OAuth**.
3. Configure o tipo de aplicativo:
   - Escolha "Aplicativo da Web" (ou outro tipo, conforme seu caso).
   - Adicione URLs de redirecionamento autorizadas, se necessário.
4. Clique em **Criar**.
5. Baixe o arquivo JSON das credenciais e salve em um local seguro no seu projeto.

---

## Passo 4: Configuração no Código

### Python (Exemplo)

1. Instale as bibliotecas necessárias:

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

2. Execute: o comando

```python
py main.py
```
