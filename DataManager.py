import json
from DataBase import get_db_connection

def ips_possiveis(ambiguous_ip: str) -> list[str]:
    def is_valid_octet(s: str) -> bool:
        if not s or len(s) > 3 or (len(s) > 1 and s[0] == '0'):
            return False
        return 0 <= int(s) <= 255

    n = len(ambiguous_ip)
    if n < 4 or n > 12:
        return []

    result = []
    for i in range(1, min(4, n - 2)):
        for j in range(i + 1, min(i + 4, n - 1)):
            for k in range(j + 1, min(j + 4, n)):
                oct1 = ambiguous_ip[:i]
                oct2 = ambiguous_ip[i:j]
                oct3 = ambiguous_ip[j:k]
                oct4 = ambiguous_ip[k:]
                if (is_valid_octet(oct1) and is_valid_octet(oct2) and 
                    is_valid_octet(oct3) and is_valid_octet(oct4)):
                    ip = f"{oct1}.{oct2}.{oct3}.{oct4}"
                    result.append(ip)
    return sorted(result)

def insert_ip_data(ambiguous_ip: str) -> list[str]:
    resultado = ips_possiveis(ambiguous_ip)
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO possible_ips (ambiguous_ip, result)
            VALUES (?, ?)
        """, (ambiguous_ip, json.dumps(resultado)))
        conn.commit()
    return resultado

def get_all_ip_data() -> list[dict]:
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, ambiguous_ip, result FROM possible_ips")
        return [{"id": row[0], "ambiguous_ip": row[1], "result": json.loads(row[2])} 
                for row in cursor.fetchall()]