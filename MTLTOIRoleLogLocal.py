import os
import json
from google.cloud import translate_v2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"Your key"  # ex: C:\Users\User\Desktop\code\Test\google_key.json

with open('RoleLogLocal.json', encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

translate_client = translate_v2.Client()
target = 'pt'

max_batch_size = 100  # Tamanho máximo do lote (ajuste conforme necessário) / Maximum batch size (adjust as needed)
output_list = []

for i in range(0, len(dados), max_batch_size):
    batch = dados[i:i + max_batch_size]
    batch_texts = [entry['en'] for entry in batch]

    sub_batch_size = max_batch_size
    while sub_batch_size > 1:
        try:
            sub_batches = [batch_texts[j:j + sub_batch_size] for j in range(0, len(batch_texts), sub_batch_size)]
            outputs = []
            for sub_batch in sub_batches:
                outputs.extend(translate_client.translate(sub_batch, target_language=target))
            break
        except Exception as e:
            sub_batch_size = sub_batch_size // 2

    for entry, output in zip(batch, outputs):
        translated_entry = {
            "id": entry['id'],
            "keyID": entry['keyID'],
            "part": entry['part'],
            "goal": entry['goal'],
            "active": entry['active'],
            "characterGroup": entry['characterGroup'],
            "relation": entry['relation'],
            "condition": entry['condition'],
            "weight": entry['weight'],
            "group": entry['group'],
            "icon": entry['icon'],
            "pointColor": entry['pointColor'],
            "vocal": entry['vocal'],
            "emotionID": entry['emotionID'],
            "ch": entry['ch'],
            "tc": entry['tc'],
            "en": output['translatedText']
        }
        output_list.append(translated_entry)
        print(output)

try:
    with open('RoleLogLocalMTL.json', 'w', encoding='utf-8') as f:
        json.dump(output_list, f, ensure_ascii=False, indent=2)
except Exception as e:
    print(f"Erro ao salvar o arquivo JSON: {str(e)}")

# By PetryckSlater(Boss)
