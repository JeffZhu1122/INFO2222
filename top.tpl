<!DOCTYPE html>
<html>
    <head>
        <title>INFO2222</title>
        <link rel="stylesheet" type="text/css" href="/css/pure.css">
        <link rel="stylesheet" type="text/css" href="/css/grid.css">
        <link rel="stylesheet" type="text/css" href="/css/main.css">
        <script src="/js/jquery.js"></script>
        <script type="application/javascript">

            function getsearchtarget()
            {

                //Get the select select list and store in a variable
                var e = document.getElementById("searchtarget");

                //Get the selected value of the select list
                var formaction = e.options[e.selectedIndex].value;

                //Update the form action
                document.searchform.action = formaction;

            }
            </script>
    </head>
    <body>
        <div class="body-container">
            <header class="page-header">
                <div class="container">
                    <div class="title">
                        <a href="/"><span class="inner"></span></a>
                    </div>
                    <ul class="page-nav">

                    </ul>
                </div>
            </header>

