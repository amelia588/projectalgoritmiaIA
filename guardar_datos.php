<?php
// Datos de conexión a la base de datos
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "argoritmio";

// Recibir los datos del formulario
$nombre = $_POST['nombre'];
$correo = $_POST['correo'];
$telefono = $_POST['telefono'];
$direccion = $_POST['direccion'];

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Preparar la consulta SQL para insertar los datos en la tabla clientes
$sql = "INSERT INTO clientes (nombre, correo, telefono, direccion) VALUES ('$nombre', '$correo', '$telefono', '$direccion')";

// Ejecutar la consulta y verificar si se realizó correctamente
if ($conn->query($sql) === TRUE) {
    echo "Datos ingresados correctamente";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Cerrar la conexión
$conn->close();
?>
