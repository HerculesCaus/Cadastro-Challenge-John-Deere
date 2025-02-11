<?php
$servername = "localhost";
$username = "root"; // altere conforme o seu usuário do MySQL
$password = ""; // altere conforme a senha do seu MySQL
$dbname = "sistema_login";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}
?>