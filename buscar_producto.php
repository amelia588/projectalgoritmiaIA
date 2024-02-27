<?php
// Datos de conexión a la base de datos
$servername = "localhost";
$username = "root";
$password = "";
$database = "argoritmio";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $database);

// Verificar la conexión
if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

// Término de búsqueda proporcionado por el usuario (aquí puedes obtenerlo desde un formulario, por ejemplo)
$termino_busqueda = "term_busqueda"; // Reemplaza esto con el término real proporcionado por el usuario

// Preparar la consulta SQL
$sql = "SELECT id, nombre, descripcion, precio, stock, categoria
        FROM productos
        WHERE nombre LIKE '%" . $termino_busqueda . "%'
        ORDER BY nombre";

// Ejecutar la consulta
$result = $conn->query($sql);

// Verificar si se encontraron resultados
if ($result->num_rows > 0) {
    // Mostrar los datos de cada fila
    while ($row = $result->fetch_assoc()) {
        echo "ID: " . $row["id"] . "<br>";
        echo "Nombre: " . $row["nombre"] . "<br>";
        echo "Descripción: " . $row["descripcion"] . "<br>";
        echo "Precio: " . $row["precio"] . "<br>";
        echo "Stock: " . $row["stock"] . "<br>";
        echo "Categoría: " . $row["categoria"] . "<br>";
        echo "-------------------------<br>";
    }
} else {
    echo "No se encontraron resultados.";
}

// Cerrar la conexión
$conn->close();
?>
