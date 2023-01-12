<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Document</title>
</head>
<style>
    .container {
    margin-top: 50px;
    /* margin-left: auto; */
}
img {
    margin-top: 30px;
}
button#run {
    margin-top:10px;
    padding: 5px 10px 5px 10px;
    border: 1px solid;
    /* font-family: poppins; */
    border-radius: 6px;
    border: none;
    background: #252525;
    color: white;
}
button#run:hover{
    color: black;
    background: white;
    border:1px solid #252525;

}
</style>
<body>
    <div class="container">
        <center>
        <h3>SCAN ME</h3>
        <!-- <div class="qr">{{res}}</div></center> -->
        <img src="{{result}}">
    </div></center>
    <center>
    <button type="submit" id="run" class="run_again">New Qr</button></center>
</body>

</html>

<script>
    $(document).ready(function(){
        $('#run').click(function() {
        location.reload();
        });
    })
</script>
<!-- <script>
    $(document).ready(function () {
        $.ajax({
            url: '/'
        type: "POST"
        data: JSON.stringify({ "res": res }),
            contentType: "application/json;charset=UTF-8",
            return false
        })
    })
</script> -->

<!-- <script>
    $(document).ready(function(){
        setInterval(function (){
            // alert("reload")
            // console.log("reloading")
            document.location.reload();
        },20000);
    });
</script> -->