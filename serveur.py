from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging
import os

# Chemin du dossier
dossier_projet = r"C:\Users\mathe\Desktop\new version phids"
os.chdir(dossier_projet)

# Fichiers nécessaires
fichier_html = os.path.join(dossier_projet, "phids_page.html")
fichier_log = os.path.join(dossier_projet, "access.log")
fichier_bloque = os.path.join(dossier_projet, "blocked_ips.txt")

# Création des fichiers s'ils n'existent pas
if not os.path.exists(fichier_log):
    open(fichier_log, "w").close()

if not os.path.exists(fichier_bloque):
    open(fichier_bloque, "w").close()

# Charger les IP bloquées
def charger_ips_bloquees():
    with open(fichier_bloque, "r") as f:
        return set(line.strip() for line in f.readlines())

ips_bloquees = charger_ips_bloquees()

# Config du log
logging.basicConfig(filename=fichier_log, level=logging.INFO, format="%(asctime)s - %(message)s")

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]

        # Vérification IP bloquée
        if client_ip in ips_bloquees:
            self.send_error(403, "Accès refusé - IP bloquée")
            print(f"❌ IP bloquée : {client_ip}")
            return

        # Log de la connexion
        logging.info(f"Connexion depuis : {client_ip}")
        print(f"✅ Connexion autorisée depuis : {client_ip}")

        # Rediriger automatiquement vers phids_page.html
        if self.path == "/" or self.path == "/index.html":
            self.path = "/phids_page.html"

        super().do_GET()

port = 8080
server_address = ('', port)

print(f"🚀 Serveur lancé sur http://localhost:{port}")
print("📡 En attente de connexions (Ctrl+C pour stopper)...")

httpd = HTTPServer(server_address, MyHandler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n🛑 Serveur arrêté.")
