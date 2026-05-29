# -*- coding: utf-8 -*-

# =========================
# CONFIGURAÇÕES
# =========================

usuario_principal = "carlos"
usuario_secundario = "wiener"

senha_fixa = "peter"

arquivo_senhas = "..\passwords.txt"

# Arquivos de saída
arquivo_combo = "output.txt"
arquivo_users = "final-users.txt"
arquivo_passwords = "final-passwords.txt"

# =========================
# LEITURA DAS SENHAS
# =========================

with open(arquivo_senhas, "r", encoding="utf-8") as f:
    senhas = [linha.strip() for linha in f if linha.strip()]

contador = 0

# =========================
# GERAÇÃO DOS ARQUIVOS
# =========================

with open(arquivo_combo, "w", encoding="utf-8") as combo_out, \
     open(arquivo_users, "w", encoding="utf-8") as users_out, \
     open(arquivo_passwords, "w", encoding="utf-8") as pass_out:

    for senha in senhas:

        # -------------------------
        # carlos:senha
        # -------------------------
        combo_out.write(f"{usuario_principal}:{senha}\n")

        # users/passwords separados
        users_out.write(f"{usuario_principal}\n")
        pass_out.write(f"{senha}\n")

        contador += 1

        # -------------------------
        # A cada 2 entradas:
        # wienter:peter
        # -------------------------
        if contador % 2 == 0:

            combo_out.write(f"{usuario_secundario}:{senha_fixa}\n")

            users_out.write(f"{usuario_secundario}\n")
            pass_out.write(f"{senha_fixa}\n")

# =========================
# FINAL
# =========================

print("Arquivos gerados com sucesso:")
print(f"- {arquivo_combo}")
print(f"- {arquivo_users}")
print(f"- {arquivo_passwords}")