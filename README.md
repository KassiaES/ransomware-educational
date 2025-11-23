# 🔒 Projeto Educacional: Simulação de Ransomware

## 📋 Visão Geral

Este projeto é um **exercício educacional** que demonstra o funcionamento básico de um ransomware de forma controlada e segura. O objetivo é compreender os mecanismos de criptografia utilizados por malwares e como desenvolver contramedidas.

⚠️ **IMPORTANTE**: Este código é apenas para fins educacionais e deve ser usado em ambiente controlado.

## 🎯 Objetivos de Aprendizado

- Compreender como funciona a criptografia simétrica
- Entender o mecanismo básico de ransomware
- Aprender sobre criptografia com a biblioteca `cryptography`
- Praticar desenvolvimento de scripts de segurança
- Conhecer técnicas de detecção e prevenção

## 📁 Estrutura do Projeto

```
Malware/
├── ransoware.py         # Script de criptografia (simulação do ransomware)
├── descrypty.py         # Script de descriptografia (ferramenta de recuperação)
├── test_files/          # Pasta com arquivos para teste
│   ├── dados_confidenciais
│   └── senhas.txt
├── secret.key          # Chave de criptografia (gerada automaticamente)
├── INFO_NOTE.txt       # Nota informativa (gerada pelo script)
└── README.md           # Este arquivo
```

## 🔧 Configuração do Ambiente

### Pré-requisitos
- Python 3.14.0+ instalado
- Biblioteca `cryptography`

### Instalação
1. **Clone ou baixe o projeto**
2. **Configure o ambiente Python:**
   ```powershell
   # O ambiente virtual será criado automaticamente
   ```

3. **Instale as dependências:**
   ```powershell
   pip install cryptography
   ```

## 🚀 Como Executar

### 1. Criptografia (Simulação do Ransomware)
```powershell
# Usando ambiente virtual
& ".\.venv\Scripts\python.exe" ransoware.py
```

**O que acontece:**
- ✅ Gera uma chave de criptografia única (`secret.key`)
- ✅ Criptografa todos os arquivos na pasta `test_files/`
- ✅ Cria uma nota informativa (`INFO_NOTE.txt`)
- ✅ Exibe: "Files have been processed for educational demonstration!"

### 2. Descriptografia (Ferramenta de Recuperação)
```powershell
# Usando ambiente virtual
& ".\.venv\Scripts\python.exe" descrypty.py
```

**O que acontece:**
- ✅ Carrega a chave de criptografia (`secret.key`)
- ✅ Descriptografa todos os arquivos na pasta `test_files/`
- ✅ Restaura os arquivos ao estado original
- ✅ Exibe: "All files have been decrypted!"

## 🔍 Funcionamento Técnico

### Algoritmo de Criptografia
- **Biblioteca**: `cryptography.fernet`
- **Tipo**: Criptografia simétrica (mesma chave para criptografar e descriptografar)
- **Algoritmo**: Fernet (AES 128 em modo CBC com HMAC SHA256 para autenticação)

### Fluxo de Execução

#### Criptografia (`ransoware.py`):
1. **Geração de Chave**: Cria uma chave criptográfica aleatória
2. **Descoberta de Arquivos**: Varre a pasta `test_files/` recursivamente
3. **Filtros de Segurança**: Ignora arquivos `.py` e `.key`
4. **Processo de Criptografia**: Para cada arquivo:
   - Lê o conteúdo original
   - Aplica criptografia Fernet
   - Sobrescreve com dados criptografados
5. **Documentação**: Cria nota informativa

#### Descriptografia (`descrypty.py`):
1. **Carregamento da Chave**: Lê a chave salva em `secret.key`
2. **Descoberta de Arquivos**: Localiza arquivos criptografados
3. **Processo de Descriptografia**: Para cada arquivo:
   - Lê os dados criptografados
   - Aplica descriptografia Fernet
   - Restaura o conteúdo original

## 🛡️ Medidas de Segurança Implementadas

### Proteções no Código
- **Filtros de Arquivo**: Não criptografa os próprios scripts
- **Exclusão de Chaves**: Não criptografa arquivos `.key`
- **Linguagem Educacional**: Mensagens não ameaçadoras
- **Escopo Limitado**: Opera apenas na pasta `test_files/`

### Detecção e Prevenção
- **Windows Defender**: Pode detectar comportamento suspeito
- **Comportamento Controlado**: Limitado a pasta específica
- **Reversibilidade**: Sempre mantém a chave de descriptografia

## 🚨 Problemas Encontrados e Soluções

### 1. **Python não reconhecido**
**Problema**: `python : O termo 'python' não é reconhecido`
**Solução**: 
- Instalação do Python 3.14.0
- Configuração do PATH do sistema
- Criação de ambiente virtual

### 2. **Windows Defender bloqueando execução**
**Problema**: Antivírus detecta comportamento de ransomware
**Soluções aplicadas**:
- Alteração da linguagem para educacional
- Remoção de termos suspeitos ("ransom", "Bitcoin")
- Uso de mensagens informativas

### 3. **Erro de codificação de caracteres**
**Problema**: `UnicodeEncodeError` com emojis
**Solução**: Remoção de caracteres especiais das mensagens

### 4. **Conflito de nomes de variáveis**
**Problema**: `TypeError: expected str, bytes or os.PathLike object, not BufferedReader`
**Solução**: Renomeação de variáveis (`file` → `file_path`)

## 📚 Conceitos Aprendidos

### Criptografia
- **Fernet**: Implementação segura de criptografia simétrica
- **Chaves**: Geração, armazenamento e carregamento
- **Base64**: Codificação para transporte seguro

### Segurança
- **Detecção Comportamental**: Como antivírus detectam malware
- **Engenharia Social**: Técnicas de mensagens de ransomware
- **Mitigação**: Estratégias para reduzir detecção

### Programação
- **Manipulação de Arquivos**: Leitura/escrita binária
- **Recursão de Diretórios**: `os.walk()` para varredura
- **Tratamento de Erros**: Prevenção de falhas

## 🔬 Exercícios Propostos

### Básico
1. **Modifique o filtro** para criptografar apenas arquivos `.txt`
2. **Adicione logging** para registrar arquivos processados
3. **Implemente verificação** de integridade dos arquivos

### Intermediário
1. **Criptografia assimétrica**: Use RSA ao invés de Fernet
2. **Interface gráfica**: Crie GUI com tkinter
3. **Backup automático**: Salve cópias antes da criptografia

### Avançado
1. **Rede**: Implemente comunicação com servidor remoto
2. **Steganografia**: Esconda a chave em imagens
3. **Análise forense**: Ferramenta para detectar criptografia

## ⚖️ Aspectos Legais e Éticos

### ✅ Uso Permitido
- Pesquisa acadêmica e educacional
- Desenvolvimento de soluções de segurança
- Testes em ambiente controlado próprio
- Treinamento de equipes de segurança

### ❌ Uso Proibido
- Aplicação em sistemas de terceiros sem autorização
- Distribuição maliciosa
- Chantagem ou extorsão
- Qualquer atividade ilegal

## 📖 Referências e Recursos

### Documentação
- [Cryptography Library](https://cryptography.io/en/latest/)
- [Python os.walk()](https://docs.python.org/3/library/os.html#os.walk)
- [Fernet Specification](https://cryptography.io/en/latest/fernet/)

### Segurança
- [OWASP Cryptographic Storage Cheat Sheet](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

### Artigos Acadêmicos
- "Understanding Ransomware and Detection Strategies"
- "Symmetric vs Asymmetric Encryption in Malware"

## 🤝 Contribuições

Este é um projeto educacional. Sugestões para melhorias são bem-vindas:

1. **Documentação**: Melhorias na explicação
2. **Código**: Otimizações e boas práticas
3. **Exercícios**: Novos desafios educacionais
4. **Segurança**: Melhores práticas de proteção

## 📝 Licença

Este projeto é para fins **exclusivamente educacionais**. O uso inadequado é de responsabilidade do usuário.

---

**⚠️ Lembre-se**: O conhecimento sobre segurança deve ser usado para proteger, não para atacar. Este exercício visa formar profissionais capazes de defender sistemas contra ameaças reais.

---

*Projeto desenvolvido para fins educacionais em Novembro de 2025*