<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Página com mapa das posições dos carrinhos</title>
</head>

<header>
    <?php include 'menu-logado.php'; ?>
</header>

<body>

    <div id="mapa">
        <div id="carrinho"></div>
    </div>
    
    <div class="inputs-content">
    <div id="inputs">
        <input type="number" id="inputX" placeholder="Posição X">
        <input type="number" id="inputY" placeholder="Posição Y">
    </div>
</div>

    <script>
        const carrinho = document.getElementById('carrinho');
        const inputX = document.getElementById('inputX');
        const inputY = document.getElementById('inputY');
        const mapa = document.getElementById('mapa');

        function atualizarPosicao() {
            const x = parseInt(inputX.value, 10);
            const y = parseInt(inputY.value, 10);
            const alturaMapa = mapa.clientHeight;

            if (!isNaN(x) && !isNaN(y)) {
                carrinho.style.left = `${x}px`;
                carrinho.style.top = `${alturaMapa - y}px`; // Ajusta para que o ponto (0, 0) esteja no canto inferior esquerdo
            }
        }


        inputX.addEventListener('input', atualizarPosicao);
        inputY.addEventListener('input', atualizarPosicao);
    </script>

</body>
</html>
