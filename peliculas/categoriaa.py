from . import db
from flask import Blueprint, render_template

bp = Blueprint('categoriaa', __name__, url_prefix="/categoria")

@bp.route('/')
def categoria():
    consulta = """
        SELECT name, last_update FROM category
        ORDER BY last_update, name; 
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_categoria = res.fetchall()
    pagina = render_template('categoria.html', actores=lista_categoria)
    

    return pagina