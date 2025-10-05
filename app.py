from flask import Flask, request, jsonify

app = Flask(__name__)

def limpar_cpf(cpf: str) -> str:
    return "".join(filter(str.isdigit, cpf or ""))

def cpf_invalido_conhecido(digits: str) -> bool:
    # Rejeita sequências repetidas (ex.: 000..., 111..., etc.)
    return digits == digits[0] * 11

def calcular_digito(cpf_parcial: str, fator_inicial: int) -> int:
    soma = sum(int(d) * f for d, f in zip(cpf_parcial, range(fator_inicial, 1, -1)))
    resto = (soma * 10) % 11
    return 0 if resto == 10 else resto

def validar_cpf(cpf: str) -> bool:
    cpf_digits = limpar_cpf(cpf)
    if len(cpf_digits) != 11:
        return False
    if cpf_invalido_conhecido(cpf_digits):
        return False

    dv1 = calcular_digito(cpf_digits[:9], 10)
    if dv1 != int(cpf_digits[9]):
        return False

    dv2 = calcular_digito(cpf_digits[:10], 11)
    if dv2 != int(cpf_digits[10]):
        return False

    return True

@app.get("/")
def root():
    return "A API está rodando", 200

@app.post("/verificar")
def verificar():
    payload = request.get_json(silent=True) or {}
    cpf = payload.get("cpf")
    if not cpf:
        return jsonify({"valido": False, "mensagem": "Campo 'cpf' é obrigatório."}), 400

    eh_valido = validar_cpf(cpf)
    return jsonify({"valido": eh_valido, "cpf": limpar_cpf(cpf)}), 200

if __name__ == "__main__":
    # Executa no host 0.0.0.0 para funcionar dentro do container
    app.run(host="0.0.0.0", port=8000)
