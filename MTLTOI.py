import os
import json
from google.cloud import translate_v2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"your Key Directory"# ex: C:\Users\User\Desktop\code\Test\google_key.json

with open('LocalText.json', encoding='utf-8') as meu_json: # File to translate
    dados = json.load(meu_json)

translate_client = translate_v2.Client()
target = 'pt'

max_batch_size = 100  # Tamanho máximo do lote (ajuste conforme necessário) / Maximum batch size (adjust as needed)
output_list = []

for i in range(0, len(dados), max_batch_size):
    batch = dados[i:i+max_batch_size]
    batch_texts = [entry['en'] for entry in batch]

    # Divide o lote em lotes menores, se necessário, para evitar exceder o limite de tamanho / Divide the batch into smaller batches if necessary to avoid exceeding the size limit
    sub_batch_size = max_batch_size
    while sub_batch_size > 1:
        try:
            sub_batches = [batch_texts[j:j+sub_batch_size] for j in range(0, len(batch_texts), sub_batch_size)]
            outputs = []
            for sub_batch in sub_batches:
                outputs.extend(translate_client.translate(sub_batch, target_language=target))
            break  # Se a tradução for bem-sucedida, sai do loop /If the translation is successful, exit the loop 
        except Exception as e:
            sub_batch_size = sub_batch_size // 2  # Reduz o tamanho do sublote pela metade e tenta novamente

    for entry, output in zip(batch, outputs): #To translate the other json it is necessary to put its format here/ It is set to LocalText / Para traduzir os outros arquivos json é necessario mudar a formatação aqui para a do json
        translated_entry = {
            "id": entry['id'],
            "key": entry['key'],
            "ch": entry['ch'],
            "tc": entry['tc'],
            "en": output['translatedText']
        }
        output_list.append(translated_entry)
        print(output)

try:
    with open('LocalTextMTL.json', 'w', encoding='utf-8') as f: #Final File Create the file before running the script
        json.dump(output_list, f, ensure_ascii=False, indent=2)
except Exception as e:
    print(f"Erro ao salvar o arquivo JSON / Erro to save the file: {str(e)}")

#By PetryckSlater(Boss)
