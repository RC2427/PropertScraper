<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <?php
            $bhk = "\r\n".$_POST['bhk'];
            $min = "\r\n".$_POST['min'];
            $max = "\r\n".$_POST['max'];
            $city =  $_POST['search-bar']; 
            $Posted = "\r\n".$_POST['Posted'];
            $type = "\r\nsale";
            
               
            $myfile = fopen('/home/rc/Documents/scrapetest2/scrape/formdata.txt',"w");
            fwrite($myfile, $city);
            fwrite($myfile, $bhk);
            fwrite($myfile, $min);
            fwrite($myfile, $max);
            fwrite($myfile, $Posted);
            fwrite($myfile, $type);
            fclose($myfile);
            
            $command = escapeshellcmd('python3 /home/rc/Documents/scrapetest2/scrape/main.py');
            $output = shell_exec($command);
            header("Location: untitled.html");
        ?>
    </body>
</html>
