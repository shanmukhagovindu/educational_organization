<?php
$name = $_POST['name'];
$visitor_email = $POST['email'];
$subject = $_POST['subject'];
$message = $_POST['message'];
// name, email, subject, message are names given in index.html

$email_from = 'http://127.0.0.1:5500/'//'info@shnmukhagovindu4.com'; //website email
$email_subject = 'New Form Submission'; //in this subject we can write any message
$email_body = "user name: $name.\n".
                "user Email: $visitor_email.\n".
                "Subject: $subject.\n".
                "User Message: $message.\n";

$to = 'shanmukhagovindu@gmail.com';
$headers = "From:$email_from\r\n";
$headers ="Reply-To:$visior_email"

mail($to,$email_subject,$email_body,$headers);
header("location:contact.html");
?>