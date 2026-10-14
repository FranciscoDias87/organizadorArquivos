# Organizador de Downloads

Automação em Python para organizar os arquivos da pasta Downloads em diretórios separados por tipo. O projeto demonstra como usar a biblioteca padrão do Python para inspecionar arquivos, classificá-los pela extensão, criar pastas e mover itens automaticamente.

## Objetivo

Reduzir a organização manual de uma pasta de Downloads, agrupando documentos, imagens, vídeos, planilhas, apresentações e outros arquivos em categorias.

## Funcionalidades

- Percorre os arquivos no primeiro nível da pasta configurada.
- Identifica a extensão sem diferenciar letras maiúsculas de minúsculas.
- Cria a pasta de destino quando necessário.
- Move cada arquivo para sua categoria.
- Direciona extensões não mapeadas para `Outros`.
- Exibe ao final a quantidade de arquivos processados e o caminho organizado.

## Categorias

| Extensões | Pasta de destino |
| --- | --- |
| `.png`, `.jpg`, `.jpeg` | `Imagens` |
| `.pdf` | `Documentos_Pdf` |
| `.mp4` | `Videos` |
| `.xls` | `Planilhas` |
| `.xlsx` | `Planilhas_Excel` |
| `.docx` | `Documentos_Word` |
| `.exe` | `Programas` |
| `.pptx` | `Apresentacoes_PowerPoint` |
| Outras extensões | `Outros` |

## Tecnologias

- Python 3
- `pathlib` para navegar pelos caminhos e inspecionar arquivos
- `shutil` para mover arquivos

O projeto utiliza apenas bibliotecas incluídas na instalação padrão do Python; não há dependências externas.

## Como executar

1. Instale o Python 3, caso ainda não esteja instalado.
2. Abra [organizaArquivosDownloads.py](./organizaArquivosDownloads.py) e confira o valor da variável `pasta`.
3. Altere esse caminho para a pasta que deseja organizar. O caminho configurado atualmente é `C:/Users/{usuario}/Downloads`.
4. Abra um terminal na pasta do projeto e execute:

   ```bash
   python organizaArquivosDownloads.py
   ```

   No Windows, também é possível usar:

   ```powershell
   py organizaArquivosDownloads.py
   ```

## Exemplo de resultado

Depois da execução, os arquivos são agrupados em pastas como:

```text
Downloads/
├── Documentos_Pdf/
├── Documentos_Word/
├── Imagens/
├── Outros/
├── Planilhas/
├── Planilhas_Excel/
├── Programas/
├── Videos/
└── Apresentacoes_PowerPoint/
```

As pastas são criadas conforme as categorias encontradas nos arquivos. O script processa somente arquivos diretamente dentro da pasta configurada; não percorre subpastas.

## Cuidados

O programa **move os arquivos da pasta configurada**. Antes de executá-lo em uma pasta com dados importantes, confira o caminho definido em `pasta` e faça uma cópia de segurança. Para experimentar, use primeiro uma pasta de teste com cópias de alguns arquivos.

## Possíveis evoluções

- Permitir escolher a pasta de origem ao executar o programa.
- Adicionar modo de simulação, sem mover arquivos.
- Registrar um relatório das operações realizadas.
- Ampliar e personalizar as categorias de extensões.
- Tratar erros de acesso, arquivos em uso e conflitos de nomes.
