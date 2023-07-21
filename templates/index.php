<!DOCTYPE html>
<html>
<head>
    <title>Combined HTML and PHP</title>
</head>
<body>
    <h1>Hello, <?php echo "World"; ?>!</h1>
    <p>This is a simple PHP website combined with HTML.</p>
    <?php
        $current_time = date('Y-m-d H:i:s');
        echo "<p>Current Server Time: {$current_time}</p>";
    ?>
</body>
</html>
