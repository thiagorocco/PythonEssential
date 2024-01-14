from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def criar_pdf(nome_arquivo):
    # Cria um objeto PDF
    pdf = canvas.Canvas(nome_arquivo, pagesize=letter)

    # Adiciona um cabeçalho
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(300, 750, "Exemplo de Relatório em PDF com ReportLab")

    # Adiciona um parágrafo
    pdf.setFont("Helvetica", 12)
    pdf.drawString(72, 700, "Este é um exemplo simples de relatório em PDF usando a biblioteca ReportLab em Python.")

    # Adiciona uma lista
    lista_itens = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    pdf.setFont("Helvetica", 12)
    y = 680
    for item in lista_itens:
        pdf.drawString(72, y, f"• {item}")
        y -= 20

    # Fecha o objeto PDF
    pdf.save()

# Nome do arquivo PDF a ser criado
nome_arquivo = "exemplo_relatorio.pdf"

# Cria o PDF chamando a função
criar_pdf(nome_arquivo)
