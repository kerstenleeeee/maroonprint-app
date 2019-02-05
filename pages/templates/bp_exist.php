<!DOCTYPE html>
<html>
<body>

    <?php
    $connection = pg_connect ('postgres://kmguflpagdenqf:8c2521af5b3eff6d37e1db0d8ec336ce9575d5b422c7e2de745d2a6ee9bfadae@ec2-54-83-50-174.compute-1.amazonaws.com:5432/del92mq08q3k6l');
    if($connection) {
       echo 'connected';
    } else {
        echo 'there has been an error connecting';
    } 
?>

</body>
</html>