from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Javier RUA Tecnología - Inicio</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background-image: url('static/images/fondo.jpg');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                color: #333;
            }

            header, footer {
                background-color: #b81c1c;
                color: white;
                padding: 1rem;
                text-align: center;
            }

            main {
                padding: 2rem;
                max-width: 900px;
                margin: auto;
                background-color: white;
            }

            h1 {
                color: white;
            }

            h2 {
                color: #007bff;
                font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
            }

            ul {
                list-style-type: square;
                margin-left: 1.5rem;
            }

            .producto {
                margin-bottom: 2rem;
            }

            .imagenes-lado-a-lado {
                display: flex;
                gap: 20px;
                justify-content: center;
                align-items: center;
                flex-wrap: wrap;
                margin-top: 10px;
            }

            .imagenes-lado-a-lado img {
                width: 48%;
                max-width: 400px;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }

            .boton-precio {
                background-color: #007bff;
                color: white;
                padding: 8px 16px;
                display: inline-block;
                border-radius: 6px;
                font-weight: bold;
                font-size: 16px;
                margin-top: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }

            .producto img {
                width: 100%;
                max-width: 400px;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                margin-top: 10px;
            }
            .boton {
                background-color: #28a745;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                display: inline-block;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>¡Bienvenido a Javier RUA Moreno Tecnología!</h1>
            <p>Tu tienda de confianza en productos tecnológicos al mejor precio</p>
        </header>
        <main>
            <section>
                <h2>📦 Productos Destacados</h2>

                <div class="producto">
                    <h3>💻 Laptop Azus ROG Zephyrus G16 R9 32GB 1TB RTX4070 8GB W11 OLED 16</h3>
                    <p>Potente y ligera, ideal para uso diario y profesional.</p>
                    <div class="imagenes-lado-a-lado">
                        <img src="static/images/laptop1.png" alt="Laptop vista frontal">
                        <img src="static/images/laptop2.png" alt="Laptop vista lateral">
                        <div class="boton-precio">S/ 11.399.00</div>
                    </div>
                </div>

                <div class="producto">
                    <h3>🖥️ Monitor Gamer UltraGear™ UHD IPS, 1ms (GtG), 144Hz de 27''</h3>
                    <p>Disfruta de tus juegos con una experiencia fluida y colores vivos.</p>
                    <div class="imagenes-lado-a-lado">
                        <img src="static/images/monitor1.png" alt="Monitor Gamer 144Hz">
                        <img src="static/images/monitor2.png" alt="Monitor Gamer 144Hz">
                        <div class="boton-precio">S/ 2.699.00</div>
                    </div>
                </div>

                <div class="producto">
                    <h3>🧠 Computadora PC Gamer Falkor RGB Plus CORE I9 14900K 14TH 32GB DDR5 1TB RTX5080 16GB GDDR7 27' 180HZ Curvo</h3>
                    <p>Rendimiento extremo para tareas exigentes como diseño y gaming.</p>
                    <div class="imagenes-lado-a-lado">
                        <img src="static/images/computadora1.png" alt="Intel Core i9 14ª Gen">
                        <img src="static/images/computadora2.png" alt="Intel Core i9 14ª Gen">
                        <div class="boton-precio">S/ 15.499.00</div>
                    </div>
                </div>

                <div class="producto">
                    <h3>🎤 Micrófono Fifine Ampligame A6V, RGB, USB Cardioide, blanco</h3>
                    <p>El micrófono es una buena opción si lo que buscas es algo que puedas conectar y hablar sin configurar nada</p>
                    <div class="imagenes-lado-a-lado">
                        <img src="static/images/microfono1.png" alt="Micrófono Fifine Ampligame A6V">
                        <img src="static/images/microfono2.png" alt="Micrófono Fifine Ampligame A6V">
                        <div class="boton-precio">S/ 170.00</div>
                    </div>
                </div>

            </section>

            <section>
                <h2>🔥 Promociones del Mes</h2>
                <p>¡Descuentos de hasta el <strong>30%</strong> en laptops y accesorios durante todo el mes!</p>
                <a href="#" class="boton">Ver promociones</a>
            </section>

            <section>
                <h2>🛒 ¿Por qué elegirnos?</h2>
                <ul>
                    <li>Envíos a todo el país</li>
                    <li>Soporte técnico totalmente gratuito</li>
                    <li>Garantía de 1 año en todos nuestros productos</li>
                </ul>
            </section>

            <section>
                <h2>📞 Contáctanos</h2>
                <p>¿Tienes dudas o necesitas ayuda? <a href="https://wa.me/+51930408516">Escríbenos aquí</a>.</p>
            </section>
        </main>
        <footer>
            <p>&copy; 2025 Javier RUA Tecnología</p>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
