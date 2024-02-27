<?php
// Establecer la conexión con la base de datos
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "aargoritmio";

$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Verificar si se ha enviado una palabra clave
if (isset($_GET['keyword'])) {
    $keyword = $_GET['keyword'];

    // Consulta SQL para buscar productos por palabras clave
    $sql = "SELECT * FROM productos
            WHERE nombre LIKE '%$keyword%' OR descripcion LIKE '%$keyword%' OR categoria LIKE '%$keyword%'";

    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Mostrar resultados si se encontraron productos
        while ($row = $result->fetch_assoc()) {
            echo "Nombre: " . $row['nombre'] . "<br>";
            echo "Descripción: " . $row['descripcion'] . "<br>";
            echo "Precio: $" . $row['precio'] . "<br>";
            echo "<hr>";
        }
    } else {
        echo "No se encontraron productos.";
    }
}

// Cerrar la conexión
$conn->close();
?>
