# 📚 Sistema de Gerenciamento de Biblioteca

Este é um sistema de gerenciamento de livros desenvolvido em **Python**, utilizando **PyQt6** para a interface gráfica e **Firebase Firestore** para armazenamento dos dados.

---

## 📥 **Instalação**

### 🔧 **Requisitos**
Certifique-se de ter instalado:
- ✅ **Python 3.8+**
- ✅ **Pip** (gerenciador de pacotes do Python)

### 📌 **Passos para instalação**

1️⃣ **Clone o repositório**
```bash
git clone https://github.com/melissaoalves/biblioteca-sd.git
cd biblioteca-sd
```

2️⃣ **Crie um ambiente virtual** 
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```

3️⃣ **Instale as dependências**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Configure o Firebase**  
O projeto utiliza **Firebase Authentication e Firestore Database**.  
Siga os passos abaixo para configurar corretamente:

- 🔗 **Acesse o [Firebase Console](https://console.firebase.google.com/)**  
- 🆕 **Crie um novo projeto** e configure um app do tipo **Web**.  
- 🏗 **Ative o Firestore Database** no modo **test**.  
- 🔐 **Ative a autenticação por Email/Senha**:  
  - Vá até **Authentication** → **Método de Login**.  
  - Ative a opção **Email/Senha**.  
- 🔑 **Baixe a chave JSON do Firebase**:  
  - Vá até **Configurações do Projeto** → **Contas de Serviço**.  
  - Gere uma **nova chave privada** e baixe o arquivo JSON.  
  - Renomeie para **`firebase_credentials.json`** e mova para a pasta `services/`.  
- 📝 **Crie um arquivo `.env` na raiz do projeto** e adicione as seguintes variáveis:  
```ini
FIREBASE_API_KEY=SUA_CHAVE
FIREBASE_AUTH_DOMAIN=SEU_AUTH_DOMAIN
FIREBASE_DATABASE_URL=SEU_DATABASE_URL
FIREBASE_PROJECT_ID=SEU_PROJECT_ID
FIREBASE_STORAGE_BUCKET=SEU_STORAGE_BUCKET
FIREBASE_MESSAGING_SENDER_ID=SEU_MESSAGING_SENDER_ID
FIREBASE_APP_ID=SEU_APP_ID
```

5️⃣ **Execute o sistema**
   ```bash
   python app.py
   ```

