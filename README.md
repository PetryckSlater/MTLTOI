## English:
The code was created for the translation of game files by MTL(Machine translator) using the Google API, It reads data from a JSON file ('LocalText.json') containing entries with text in English. The code translates the English text into Portuguese using the Google Cloud Translation API and saves the translated entries into a new JSON file ('LocalTextMTL.json').

Here's a brief tutorial on how to set up the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to authenticate with Google Cloud services:

1. Create a Google Cloud project: Start by creating a new project in the Google Cloud Console (https://console.cloud.google.com). If you already have a project, you can skip this step.

2. Enable the Translation API: In the Google Cloud Console, navigate to the "APIs & Services" section and enable the Google Cloud Translation API for your project.

3. Create a service account: In the Google Cloud Console, go to the "IAM & Admin" section and select "Service Accounts". Create a new service account or use an existing one. Note down the service account's email address and the path to the generated JSON key file.

4. Generate a JSON key file: Under the "Actions" column for your service account, click on the "Manage Keys" button. Then, click on the "Add Key" button and select "Create new key". Choose the JSON key type and click "Create". Save the generated JSON key file to a secure location on your machine.

5. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable: Open your terminal or command prompt and run the following command, replacing `[PATH]` with the actual file path to your JSON key file:
   - For Windows:
     ```
     set GOOGLE_APPLICATION_CREDENTIALS=[PATH]
     ```
   - For Linux or macOS:
     ```
     export GOOGLE_APPLICATION_CREDENTIALS=[PATH]
     ```

   Make sure to include the actual file path to the JSON key file, for example:
   ```
   set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\YourUsername\Downloads\your-key-file.json
   ```

6. Verify the environment variable: To verify if the environment variable is set correctly, you can print it in your code using the following Python snippet:
   ```python
   import os
   print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
   ```

   If the output displays the correct file path to your JSON key file, then the environment variable is set up correctly.

## Portuguese:
O codigo foi criado para a tradução de arquivos do jogo por MTL(Machine translator) usando a API do Google,  Ele lê os dados de um arquivo JSON ('LocalText.json') contendo entradas com texto em inglês. O código traduz o texto em inglês para o português usando a API de Tradução do Google Cloud e salva as entradas traduzidas em um novo arquivo JSON ('LocalTextMTL.json').

Aqui está um breve tutorial sobre como configurar a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS` para autenticar com os serviços do Google Cloud:

1. Crie um projeto no Google Cloud: Comece criando um novo projeto no Console do Google Cloud (https://console.cloud.google.com). Se você já possui um projeto, pode pular esta etapa.

2. Habilite a API de Tradução: No Console do Google Cloud, vá para a seção "APIs e Serviços" e habilite a API de Tradução do Google Cloud para o seu projeto.

3. Crie uma conta de serviço: No Console do Google Cloud, vá para a seção "IAM e Administração" e selecione "Contas de serviço". Crie uma nova conta de serviço ou use uma existente. Anote o endereço de e-mail da conta de serviço e o caminho para o arquivo JSON de chave gerado.

4. Gere um arquivo JSON de chave: Na coluna "Ações" da sua conta de serviço, clique no botão "Gerenciar chaves". Em seguida, clique no botão "Adicionar chave" e selecione "Criar nova chave". Escolha o tipo de chave JSON e clique em "Criar". Salve o arquivo JSON de chave gerado em um local seguro em seu computador.

5. Configure a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS`: Abra o seu terminal ou prompt de comando e execute o seguinte comando, substituindo `[CAMINHO]` pelo caminho real do arquivo JSON de chave:
   - No Windows:
     ```
     set GOOGLE_APPLICATION_CREDENTIALS=[CAMINHO]
     ```
   - No Linux ou macOS:
     ```
     export GOOGLE_APPLICATION_CREDENTIALS=[CAMINHO]
     ```

   Certifique-se de incluir o caminho real do arquivo JSON de chave. Por exemplo:
   ```
   set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\SeuUsuario\Downloads\seu-arquivo-de-chave.json
   ```

6. Verifique a variável de ambiente: Para verificar se a variável de ambiente está configurada corretamente, você pode imprimi-la em seu código usando o seguinte trecho de código Python:
   ```python
   import os
   print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
   ```

   Se a saída exibir o caminho correto para o arquivo JSON de chave, significa que a variável de ambiente está configurada corretamente.

Pronto! Agora você configurou a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS`, permitindo que seu código faça a autenticação com os serviços do Google Cloud usando as credenciais fornecidas.
