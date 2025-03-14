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
    db.collection("livros").document(livro_id).update({
        "titulo": titulo,
        "autor": autor,
        "paginas": int(paginas),
        "ano": int(ano)
    })

def deletar_livro(livro_id):
    db.collection("livros").document(livro_id).delete()
