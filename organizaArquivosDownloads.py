from pathlib import Path
import shutil

pasta = Path("C:/Users/{usuario}/Downloads")

categorias = {
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".pdf": "Documentos_Pdf",
    ".mp4": "Videos",
    ".xls": "Planilhas",
    ".xlsx": "Planilhas_Excel",
    '.docx': "Documentos_Word",
    ".exe": "Programas",
    ".pptx": "Apresentacoes_PowerPoint",
}


arquivos = [arquivo for arquivo in pasta.iterdir() if arquivo.is_file()]

for arquivo in arquivos:
    destino = categorias.get(
        arquivo.suffix.lower(),
        "Outros"
    )
    pasta_destino = pasta / destino
    pasta_destino.mkdir(exist_ok=True)

    shutil.move(
        arquivo,
        pasta_destino / arquivo.name
    )

print(f"{len(arquivos)} arquivo(s) organizado(s) em: {pasta}")
