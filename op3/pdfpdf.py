import re
from PyPDF2 import PdfReader

sublevel_ids = {'H8.', 'E1.', 'I2.'}

with open("DIME2.pdf", "rb") as f:
    reader = PdfReader(f)
    full_text = ""
    for page in reader.pages:
        txt = page.extract_text()
        if txt:
            full_text += txt + "\n"

pattern = r'([A-Z]\d*(?:\.\d+)?\.)\s*([\s\S]*?)(?=(?:[A-Z]\d*(?:\.\d+)?\.)|$)'
matches = re.findall(pattern, full_text, re.DOTALL)

campos = []
for id_actual, bloque in matches:
    lines = [l.strip() for l in bloque.splitlines() if l.strip()]
    if not lines:
        continue
    if id_actual in {'J.', 'G.'}:
        campos.append({
            'id': id_actual,
            'titulo': lines[0],
            'valor': lines[1] if len(lines) > 1 else ""
        })
        for line in lines[2:]:
            if re.match(r'^(Liquidación|Tipo|Sub totales)', line):
                continue
            m = re.match(r'^(GA|IVA)\b', line)
            if m:
                code = m.group(1)
                last_val = line.split()[-1]
                campos.append({
                    'id': f"{id_actual.rstrip('.')}.{code}",
                    'titulo': code,
                    'valor': last_val
                })
                continue
            if id_actual == 'G.' and line.startswith("Total tributos a pagar"):
                parts = line.split()
                title = " ".join(parts[:-1])
                value = parts[-1]
                campos.append({
                    'id': f"{id_actual.rstrip('.')}.TOTAL",
                    'titulo': title,
                    'valor': value
                })
        continue

    if id_actual in sublevel_ids:
        base = id_actual.rstrip('.')
        current_id = ""
        current_title = ""
        current_value = ""
        last_num = -1
        base_lines = []
        rest_lines = []
        found_first_number = False
        for line in lines:
            if re.match(r'^\d+\s+', line):
                found_first_number = True
            if not found_first_number:
                base_lines.append(line)
            else:
                rest_lines.append(line)
        if base_lines:
            base_titulo = base_lines[0]
            base_valor = " ".join(base_lines[1:]).strip() if len(base_lines) > 1 else ""
            campos.append({
                'id': id_actual,
                'titulo': base_titulo,
                'valor': base_valor
            })
        for line in rest_lines:
            m = re.match(r'^(\d+)\s+(.*)', line)
            if m:
                num = int(m.group(1))
                title_or_value = m.group(2).strip()

                if num > last_num:
                    if current_id:
                        campos.append({
                            'id': current_id,
                            'titulo': current_title,
                            'valor': current_value.strip()
                        })
                    current_id = f"{base}.{num}"
                    current_title = title_or_value
                    current_value = ""
                    last_num = num
                else:
                    current_value += " " + line.strip()
            else:
                current_value += " " + line.strip()

        if current_id:
            campos.append({
                'id': current_id,
                'titulo': current_title,
                'valor': current_value.strip()
            })
        continue
    titulo = lines[0]
    valor = " ".join(lines[1:]).strip() if len(lines) > 1 else ""
    campos.append({
        'id': id_actual,
        'titulo': titulo,
        'valor': valor
    })
for c in campos:
    if c['valor']:
        m = re.match(r'^([^\d,]*\([\w\s]+\))\s+([\d,\.]+)$', c['valor'])
        if m:
            c['titulo'] += " " + m.group(1).strip()
            c['valor'] = m.group(2).strip()

clean_campos = []
prev = None
for c in campos:
    if c['id'] == 'A.' and prev and prev['id'] in {'B1.', 'B2.'}:
        if prev['valor']:
            prev['valor'] += " " + c['titulo'] + " " + c['valor']
        else:
            prev['valor'] = c['titulo'] + " " + c['valor']
    else:
        clean_campos.append(c)
        prev = c
campos = clean_campos

for i, c in enumerate(campos):
    if c['id'] == 'H8.9' and not c['valor']:
        if i + 1 < len(campos):
            next_c = campos[i + 1]
            m = re.match(r'^H8\.(\d+)$', next_c['id'])
            if m:
                c['valor'] = m.group(1)

with open("camposN.txt", "w", encoding="utf-8") as out:
    for c in campos:
        out.write(f"{c['id']}  Título: {c['titulo']}  =>  Valor: {c['valor']}\n")

print(f"Exportados {len(campos)} campos a 'camposm.txt'")
