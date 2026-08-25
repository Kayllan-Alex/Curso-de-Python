import hashlib

# S.H.A significa Secure Hash Algorithm, que é um algoritmo de hash criptográfico projetado para garantir a integridade dos dados. Ele gera um valor de hash único para cada entrada, tornando difícil para os invasores modificar os dados sem ser detectado.

texto = "Kayllan"
cod = texto.encode("utf-8")
hash = hashlib.sha256(cod).hexdigest()

print(cod)
print(hash)
