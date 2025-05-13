import os

chapter_data = {
    "chapter": 3,
    "verses": [
        "Não exaltar os talentosos previne a rivalidade.",
        "Não valorizar tesouros raros evita o roubo.",
        "Não exibir o desejável impede a confusão do coração.",
        "O sábio governa esvaziando os corações e preenchendo os estômagos."
    ]
}

def generate_html_page():
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Lê o template original do arquivo index-2.html
    with open("index-2.html", "r", encoding="utf-8") as f:
        template = f.read()

    chapter = chapter_data["chapter"]
    
    # Adiciona link de volta para a página inicial
    link_html = '<p><a href="https://pdrodoc.github.io/tao/index.html" style="color: #569cd6;">← Voltar </a></p>'
    # Gera os versos formatados com numeração e classes HTML
    verses_html = link_html + "\n" + "\n".join(
        [f'<p><span class="line-number">{i+1}</span><span class="verse">{v}</span></p>' for i, v in enumerate(chapter_data["verses"])]
    )

    # Substitui o conteúdo estático do template com placeholders ou via string
    new_html = template

    # Substitui o número do capítulo no título
    new_html = new_html.replace("Capítulo 1", f"Capítulo {chapter}")

    # Substitui os versos entre <p>...</p> até encontrar as dedicatórias
    start = new_html.find('<p><span class="line-number">1')
    end = new_html.find('<p class="dedication">')
    if start != -1 and end != -1:
        new_html = new_html[:start] + verses_html + "\n" + new_html[end:]

    # Salva novo HTML
    filename = f"{output_dir}/index-{chapter}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"Generated: {filename}")

if __name__ == "__main__":
    print("Generating HTML using index-2.html as template...")
    generate_html_page()
    print("Done. Be aware, don't slip.")