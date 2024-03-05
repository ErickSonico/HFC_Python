from http.server import BaseHTTPRequestHandler, HTTPServer
from base64 import b64decode

# Configura los usuarios y contraseñas permitidos
USERS = {
    "usuario1": "pass1",
    "usuario2": "pass2"
}

# Subclase de BaseHTTPRequestHandler para manejar las solicitudes
class AuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Verifica si se proporcionaron credenciales de autenticación
        auth_header = self.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Basic '):
            self.send_auth_required_response()
            return

        # Decodifica las credenciales de autenticación
        encoded_credentials = auth_header.split(' ')[1]
        decoded_credentials = b64decode(encoded_credentials).decode('utf-8')
        username, password = decoded_credentials.split(':')

        # Verifica las credenciales de autenticación
        if not self.check_auth(username, password):
            self.send_auth_required_response()
            return

        # Si las credenciales son válidas, sirve el contenido protegido
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Contenido protegido')

    # Función para verificar las credenciales de autenticación
    def check_auth(self, username, password):
        return USERS.get(username) == password

    # Función para enviar una respuesta de autenticación requerida
    def send_auth_required_response(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="Acceso restringido"')
        self.end_headers()
        self.wfile.write(b'Credenciales incorrectas')

# Inicia el servidor en el puerto 8000
server_address = ('', 8000)
httpd = HTTPServer(server_address, AuthHandler)
print('Servidor en línea en el puerto 8000...')
httpd.serve_forever()