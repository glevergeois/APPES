<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>APPES</title>
</head>
<body>
    <h1>Connexion à la bdd</h1>

    <?php
$servername = 'localhost';
$username = 'root';
$password = '';
$database = 'appes';

$conn = new mysqli($servername, $username, $password, $database);

if($conn->connect_error){
    die('Erreur : ' .$conn->connect_error);
} else {
    echo 'Connexion réussie';

    $json_file = 'fishes.json';
    $json_data = file_get_contents($json_file);

    $data_array = json_decode($json_data, true);

    foreach ($data_array as $record) {

        $scientific_name = $conn->real_escape_string($record['Nom scientifique']);
        $name = $conn->real_escape_string($record['Nom commun']);
        $clrf = $conn->real_escape_string($record['Categorie Liste rouge France']);
        $clrm = $conn->real_escape_string($record['Categorie Liste rouge mondiale']);
        $tendancy = $conn->real_escape_string($record['Tendance']);

        $danger_level_id = 11;

        switch ($clrf) {
            case 'Ex':
                $danger_level_id = 1;
                break;
            case 'Re':
                $danger_level_id = 2;
                break;
            case 'Cr':
                $danger_level_id = 3;
                break;
            case 'En':
                $danger_level_id = 4;
                break;
            case 'Vu':
                $danger_level_id = 5;
                break;
            case 'Nt':
                $danger_level_id = 6;
                break;
            case 'Lc':
                $danger_level_id = 7;
                break;
            case 'Dd':
                $danger_level_id = 8;
                break;
            case 'Na':
                $danger_level_id = 9;
                break;
            case 'Ne':
                $danger_level_id = 10;
                break;
        }

        $sql = "INSERT INTO `species` (`id`, `name`, `scientific_name`, `wingspan`, `withers_height`, `color`, `life_esperancy`, `description`, `tendancy`, `clrf`, `clrm`, `Danger_Level_id`, `Diet_id`) 
                VALUES (NULL, '$name', '$scientific_name', NULL, NULL, NULL, NULL, NULL, 'downa', '$clrf', '$clrm', '$danger_level_id', '11');";

        $result = $conn->query($sql);

        if (!$result) {
            echo "Erreur d'insertion : " . $conn->error;
        }
    }
}
?>



</body>
</html>