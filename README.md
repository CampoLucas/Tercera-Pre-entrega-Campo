<div id="user-content-toc">
  <ul>
      <summary><h1>Tercera pre-entrega</h1></summary>
      <p>by: Lucas Campo</p>
      <hr>
  </ul>
</div>

<h3>Objetivos generales</h3>
<div>
    <ul>
        <li>Desarrollar una WEB Django con patrón MTV subida a Github.</li>
    </ul>
</div>
<h3>Se debe entregar</h3>
<div>
    <ul>
        <li>Link de GitHub con el proyecto totalmente subido a la plataforma.</li>
        <li>Proyecto Web Django con patrón MVT que incluya:
            <ul>
                <li>Herencia de HTML.</li>
                <li>Por lo menos 3 clases en models.</li>
                <li>Un formulario para insertar datos a todas las clases de tu models.</li>
                <li>Un formulario para buscar algo en la BD</li>
                <li>Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.</li>
            </ul>
        </li>
    </ul>
</div>
<h3>Formato</h3>
<div>
    <ul>
        <li>ink al repositorio de GitHub con el nombre “Tercera pre-entrega+Apellido”.</li>
    </ul>
</div>
<hr>
<div>
    <div id="user-content-toc">
        <ul>
            <summary><h1>Pagina de ventas</h1></summary>
        </ul>
    </div>
    <p>Esta es una página web simple para administrar pedidos, productos y tiendas. Las siguientes características están disponibles:</p>
</div>


<div>
    <div id="user-content-toc">
        <ul>
            <summary><h2>Features</h2></summary>
        </ul>
    </div>
    <ul>
        <li>Agregar nuevos pedidos.</li>
        <li>Ver pedidos.</li>
        <li>Agregar nuevos productos.</li>
        <li>Ver productos.</li>
        <li>Agregar nuevas tiendas.</li>
        <li>Ver tiendas.</li>
        <li>Buscar productos.</li>
    </ul>
</div>

<div>
    <div id="user-content-toc">
        <ul>
            <summary><h2>Dependencias</h2></summary>
        </ul>
    </div>
    <ul>
        <li>Para ejecutar este proyecto, necesitará Python 3.x y Django 3.x.</li>
    </ul>
</div>

<div>
    <div id="user-content-toc">
        <ul>
            <summary><h2>Como ejecutar la pagina</h2></summary>
        </ul>
    </div>
    <p>Haga estos pasos en la terminal:</p>
    <ul>
        <li>Clone este repositorio: <strong>git clone https://github.com/CampoLucas/Tercera-Pre-entrega-Campo.git</strong></li>
        <li>Ejecutar migraciones: <strong>python manage.py migrate</strong></li>
        <li>Inicie el servidor de desarrollo: <strong>python manage.py runserver</strong></li>
        <li>Visite el sitio web en su navegador en <strong>http://localhost:8000</strong></li>
    </ul>
</div>
<div>
    <div id="user-content-toc">
        <ul>
            <summary><h2>Testeo</h2></summary>
        </ul>
    </div>
    <p>Se pueden probar estas caracteristicas:</p>
    <ul>
        <li>Agregar un producto.</li>
        <li>Listado de todos los productos.</li>
        <li>Añadir una orden.</li>
        <li>Listado de todas las ordenes.</li>
        <li>Añadir una tienda.</li>
        <li>Listado de todas las tiendas.</li>
        <li>Búsqueda de productos por nombre.</li>
    </ul>
</div>

<div>
    <div id="user-content-toc">
        <ul>
            <summary><h2>Estructura del codigo</h2></summary>
        </ul>
    </div>
    <p>El código está organizado de la siguiente manera:</p>
    <ul>
        <li>admin.py: configuración del sitio de administración de Django.</li>
        <li>forms.py: formularios de Django para agregar modelos.</li>
        <li>models.py: modelos de Django para pedidos, productos y tiendas.</li>
        <li>views.py: vistas de Django para manejar solicitudes y respuestas HTTP.</li>
        <li>urls.py: enrutamiento de URL de Django para mapear URL a vistas</li>
    </ul>
</div>

<div>
    <div id="user-content-toc">
        <ul>
            <summary><h2>Estructura del codigo</h2></summary>
        </ul>
    </div>
    <p>El código está organizado de la siguiente manera:</p>
    <ul>
        <li>admin.py: configuración del sitio de administración de Django.</li>
        <li>forms.py: formularios de Django para agregar modelos.</li>
        <li>models.py: modelos de Django para pedidos, productos y tiendas.</li>
        <li>views.py: vistas de Django para manejar solicitudes y respuestas HTTP.</li>
        <li>urls.py: enrutamiento de URL de Django para mapear URL a vistas</li>
    </ul>
    <p>Las direcciones URL y las vistas de cada función son:</p>
    <ul>
        <li>Página de inicio: <strong>localhost:8000/</strong></li>
        <li>Lista de todos los productos: <strong>localhost:8000/products/</strong></li>
        <li>Añadir un producto: <strong>localhost:8000/products/add/</strong></li>
        <li>Lista de todos las ordenes: <strong>localhost:8000/orders/</strong></li>
        <li>Añadir una orden: <strong>localhost:8000/orders/add/</strong></li>
        <li>Lista de todos las tiendas: <strong>localhost:8000/stores/</strong></li>
        <li>Añadir una tienda: <strong>localhost:8000/stores/add/</strong></li>
        <li>Buscar un producto por nombre: <strong>localhost:8000/products/search/</strong></li>
    </ul>
</div>

