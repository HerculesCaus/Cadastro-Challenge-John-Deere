<?php
session_start();
include('db_config.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST
    $sql = "SELECT id, password FROM usuarios WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();
    
    if ($stmt->num_rows > 0) {
        $stmt->bind_result($id, $hashed_password);
        $stmt->fetch();
    
        if (password_verify($password, $hashed_password)) {
            $_SESSION['user_id'] = $id;
            echo "Login realizado com sucesso!";
    
            // Registrar o IP do carrinho de carga
            $ip_address = $_SERVER['REMOTE_ADDR'];
            $sql = "INSERT INTO carrinhos (user_id, ip_address) VALUES (?, ?)";
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("is", $id, $ip_address);
            $stmt->execute();
    
            header("Location: dashboard.php");
            exit;
        } else {
            echo "Senha incorreta.";
        }
    } else {
        echo "Usuário não encontrado.";
    }
    
    $stmt->close();
    $conn->close();
}?>

<!DOCTYPE html> 
<html lang="pt-br"> <head> <meta charset="UTF-8"> <title>Login</title> </head> <body> <h2>Login de Usuário</h2> <form action="login.php" method="post"> Usuário: <input type="text" name="username" required><br> Senha: <input type="password" name="password" required><br> <input type="submit" value="Login"> </form> </body> </html> ```