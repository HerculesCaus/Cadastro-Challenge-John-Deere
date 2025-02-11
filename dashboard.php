<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

echo "Bem-vindo ao seu dashboard!";
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
</head>
<body>
    <h2>Painel do Usuário</h2>
    <p>Você está logado.</p>
    <a href="logout.php">Logout</a>
</body>
</html>