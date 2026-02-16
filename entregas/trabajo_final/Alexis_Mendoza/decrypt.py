import base64
import os
import sys

# Ruta al archivo cifrado
file_path = 'RETOS_A_IMPLEMENTAR.md'

if not os.path.exists(file_path):
    print(f"❌ Error: No encuentro el archivo '{file_path}'")
    sys.exit(1)

try:
    print(f"🔍 Leyendo {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '---PAYLOAD---' not in content:
        print("❌ Error: El archivo no parece estar encriptado (falta la marca ---PAYLOAD---).")
        sys.exit(1)
        
    # Extraer payload
    payload = content.split('---PAYLOAD---')[1].strip()
    print(f"✅ Payload encontrado (empieza con: {payload[:15]}...)")
    
    # Decodificar
    print("🔓 Decodificando...")
    decoded_bytes = base64.b64decode(payload)
    
    # Intentar decodificar a texto
    decoded_text = decoded_bytes.decode('utf-8')
    
    print("\n" + "="*40)
    print("   DOCUMENTO DESBLOQUEADO - TOP SECRET")
    print("="*40 + "\n")
    print(decoded_text)
    print("\n" + "="*40)

except Exception as e:
    print(f"\n❌ ERROR FATAL: {e}")
    # Mostrar primeros bytes para debug si falla
    try:
        print(f"Bytes problemáticos (inicio): {decoded_bytes[:10]}")
    except:
        pass
