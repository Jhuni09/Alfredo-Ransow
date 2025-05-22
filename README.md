# 🔐 Script de Criptografia de Arquivos com Python

Este script criptografa automaticamente arquivos em pastas específicas do usuário no Windows utilizando a biblioteca `cryptography`. A chave de criptografia é gerada automaticamente e salva em um arquivo `.key`.

## ⚠️ ATENÇÃO

Este código sobrescreve arquivos **reais** com conteúdo criptografado. Não use em ambientes de produção ou com arquivos importantes, a menos que compreenda totalmente o funcionamento.

## 📌 Funcionalidades

- Geração de chave de criptografia com `Fernet`
- Busca automática de arquivos em:
  - `Documents`
  - `Downloads`
  - `Pictures`
  - `Videos`
  - `AppData/Local`
  - `AppData/Roaming`
- Criptografia de todos os arquivos encontrados (exceto os ignorados)
- Salvamento da chave em `chave.key` para posterior descriptografia

## 🚫 Arquivos Ignorados

Os seguintes arquivos são ignorados durante o processo de criptografia:

- `alfredo.py`
- `maicondouglas.py`
- `chave.key`
- `desktop.ini`

## 🗃️ Estrutura

