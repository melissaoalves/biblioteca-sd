from services.firebase_config import db

def adicionar_livro(titulo, autor, paginas, ano):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "paginas": int(paginas), 
        "ano": int(ano) 
    }
    db.collection("livros").add(livro)

def listar_livros():
    livros = db.collection("livros").stream()
    return [{"id": livro.id, **livro.to_dict()} for livro in livros]

def atualizar_livro(livro_id, titulo, autor, paginas, ano):
    livro_ref = db.collection("livros").document(livro_id)
    livro_atual = livro_ref.get()

    if not livro_atual.exists:
        return False, "Livro não encontrado."

    dados_atuais = livro_atual.to_dict()
    novos_dados = {}

    if titulo and titulo.strip():
        novos_dados["titulo"] = titulo

    if autor and autor.strip():
        novos_dados["autor"] = autor

    if paginas and paginas.strip():
        try:
            novos_dados["paginas"] = int(paginas)
        except ValueError:
            return False, "Número de páginas inválido."

    if ano and ano.strip():
        try:
            novos_dados["ano"] = int(ano)
        except ValueError:
            return False, "Ano inválido."

    if not novos_dados:
        return False, "Nenhum campo foi alterado."

    livro_ref.update(novos_dados)
    
    return True, "Livro atualizado com sucesso!"


def deletar_livro(livro_id):
    livro_ref = db.collection("livros").document(livro_id)

    if livro_ref.get().exists:
        livro_ref.delete()
        return True, "Livro removido com sucesso!"
    else:
        return False, "Livro não encontrado."

