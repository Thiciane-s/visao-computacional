# Visao computacional

## Descrição Geral
Este código utiliza a biblioteca YOLO (You Only Look Once) para detecção de objetos em tempo real por meio de uma webcam e controla LEDs conectados a um Arduino com base nos objetos detectados. Dependendo da classe do objeto identificado (como "person", "cell phone" ou "dog"), diferentes LEDs são acionados. O programa continua em execução até que a tecla 'q' seja pressionada.


## Dependências e Bibliotecas
ultralytics: Utilizada para carregar e inferir modelos YOLO para detecção de objetos.
cv2 (OpenCV): Para captura e manipulação de vídeo.
math: Para arredondamento e cálculos matemáticos simples.
pyfirmata: Para comunicação entre o Python e o Arduino.
time: Para controle do tempo (ex.: delays).

## Inicialização do Arduino
Porta COM: O Arduino é conectado à porta 'COM5' (deve ser ajustada caso a porta seja diferente).
LEDs: Três LEDs estão conectados às portas digitais 6 (verde), 7 (amarelo) e 8 (vermelho) do Arduino.
Delay Inicial: Um delay de 2 segundos é adicionado para assegurar a inicialização da comunicação.
Configuração da Webcam
A webcam é iniciada com resolução de 640x480 pixels.
A captura de vídeo é gerenciada pela biblioteca cv2.

## Modelo YOLO
Um modelo YOLO pré-treinado (yolov8n.pt) é carregado para a detecção.
A lista de classes contém as categorias que o modelo pode identificar, como "person", "dog", "cell phone", entre outras.

## Lógica Principal
Captura do Frame:
A cada iteração do loop, um frame é capturado pela webcam.
Inferência:
O modelo YOLO detecta objetos no frame capturado.
Cada detecção retorna informações como:
Coordenadas da Caixa Delimitadora (Bounding Box): Especificam a posição do objeto detectado.
Confiança da Predição: Representa a precisão do modelo.
Classe do Objeto: Índice da classe correspondente.
Desenho na Imagem: 
Um retângulo é desenhado ao redor do objeto detectado.
A classe do objeto e a confiança são exibidas na tela.
Controle dos LEDs:
Dependendo da classe do objeto detectado:
"person": LED vermelho acende.
"cell phone": LED amarelo acende.
"dog": LED verde acende.
Todos os LEDs são apagados após cada iteração para evitar sobreposição.
Exibição do Vídeo:

O frame processado (com as caixas delimitadoras e nomes das classes) é exibido em uma janela chamada 'Webcam'.
A execução do loop para ao pressionar a tecla 'q'.
Encerramento
Quando o loop é interrompido:
A câmera é liberada.
Todas as janelas do OpenCV são fechadas.
Observações Importantes

## Configuração do Arduino:

Certifique-se de que o Arduino está configurado corretamente, e os LEDs estão conectados às portas especificadas.
Verifique se a biblioteca pyfirmata está instalada e configurada.
Ajustes de Porta:

Caso o Arduino esteja conectado a outra porta COM, altere a variável port para a porta correspondente.

