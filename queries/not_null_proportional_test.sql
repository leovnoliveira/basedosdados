SELECT
    COUNT(*) AS total,
    COUNT(fonte) AS nao_nulos,
    COUNT(fonte) * 1.0 / COUNT(*) AS proporcao_nao_nulo
FROM comercio_especies_ameacadas;

