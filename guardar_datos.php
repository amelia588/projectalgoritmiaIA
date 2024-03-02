<?php
// Datos de conexión a la base de datos
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "argoritmio";

// Letra inicial a buscar
$letra_inicial = $_GET['letra']; // Puedes obtener esta letra desde un formulario o de cualquier otra fuente

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Preparar la consulta SQL para buscar productos por la letra inicial
$sql = "SELECT * FROM productos WHERE nombre LIKE '$letra_inicial%'";

// Ejecutar la consulta
$result = $conn->query($sql);

// Verificar si se encontraron resultados
if ($result->num_rows > 0) {
    // Mostrar los resultados
    echo "<h2>Productos cuyos nombres comienzan con la letra '$letra_inicial':</h2>";
    echo "<ul>";
    while($row = $result->fetch_assoc()) {
        echo "<li>" . $row["nombre"] . "</li>";
    }
    echo "</ul>";
} else {
    echo "No se encontraron productos cuyos nombres comiencen con la letra '$letra_inicial'";
}

// Cerrar la conexión
$conn->close();
?>
