<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Verificação de E-mail</title>
    <!-- Bootstrap inline -->
    <style>
        /* --- Bootstrap customizado --- */
        body {
            font-family: Arial, sans-serif;
            background-color: #000000; /* fundo preto */
            color: #ffffff;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 2rem;
            text-align: center;
            background-color: #1a1a1a; /* contraste leve */
            border-radius: 8px;
        }

        h1, h2, h3 {
            color: #ff0000; /* vermelho */
        }

        p {
            line-height: 1.6;
        }

        .btn {
            display: inline-block;
            font-weight: 400;
            text-align: center;
            text-decoration: none;
            vertical-align: middle;
            user-select: none;
            border: 1px solid transparent;
            padding: 0.75rem 1.25rem;
            font-size: 1rem;
            border-radius: 0.25rem;
            transition: color 0.15s, background-color 0.15s, border-color 0.15s;
            cursor: pointer;
        }

        .btn-primary {
            color: #fff;
            background-color: #ff0000; /* botão vermelho */
            border-color: #ff0000;
        }

        .btn-primary:hover {
            background-color: #cc0000; /* hover mais escuro */
            border-color: #cc0000;
            text-decoration: none;
            color: #fff;
        }

        .footer {
            margin-top: 2rem;
            font-size: 12px;
            color: #cccccc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="mb-3">Olá, {{ $user->name }}!</h1>
        <p>Obrigado por se cadastrar. Clique no botão abaixo para verificar seu e-mail:</p>
        <a href="{{ $url }}" class="btn btn-primary">Verificar E-mail</a>
        <div class="footer">
            <p>Se você não se cadastrou, ignore este e-mail.</p>
        </div>
    </div>
</body>
</html>
