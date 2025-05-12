from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>¡Hola, esta es mi página web en producción con Python!</h1>
    <p>Bienvenido a <strong>RUA Tecnologia</strong>, tu tienda de confianza en productos tecnológicos.</p>

    <h2>📦 Productos Destacados</h2>
    <ul>
        <li>💻 Laptop Lenovo Ryzen 7 – Potente y ligera para todo uso.</li>
        <li>🖥️ Monitor Gamer 144Hz – Calidad de imagen y velocidad para videojuegos.</li>
        <li>🧠 Procesador Intel Core i9 13ª Gen – Máximo rendimiento para tareas exigentes.</li>
    </ul>

    <h2>🔥 Promociones del Mes</h2>
    <p>¡Descuentos de hasta el <strong>30%</strong> en laptops y accesorios durante todo el mes!</p>

    <h2>🛒 ¿Por qué elegirnos?</h2>
    <ul>
        <li>Envíos a todo el país</li>
        <li>Soporte técnico gratuito</li>
        <li>Garantía de 1 año en todos los productos</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True)
