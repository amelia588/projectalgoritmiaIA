<?php
// Datos de conexión a la base de datos
$servername = "localhost"; // Nombre del servidor
$username = "root"; // Nombre de usuario de la base de datos
$password = ""; // Contraseña de la base de datos
$dbname = "argoritmio"; // Nombre de la base de datos

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

// Correo electrónico del usuario a verificar
$email = "nuevo_usuario@example.com"; // Puedes cambiar esto por el correo que desees verificar

// Consulta SQL para verificar si el usuario es nuevo o existente
$sql = "SELECT 
            name,
            email,
            CASE
                WHEN EXISTS (SELECT 1 FROM Users WHERE email = '$email') THEN 'Usuario Existente'
                ELSE 'Nuevo Usuario'
            END AS status
        FROM Users
        WHERE email = '$email'";

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Mostrar los resultados
    while($row = $result->fetch_assoc()) {
        echo "Nombre: " . $row["name"]. " - Email: " . $row["email"]. " - Estado: " . $row["status"]. "<br>";
    }
} else {
    echo "No se encontraron resultados.";
}

// Cerrar conexión
$conn->close();
?>
