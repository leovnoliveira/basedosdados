UPDATE comercio_especies_ameacadas
SET
    pais_importador = CASE WHEN pais_importador IN ('nan', '') THEN NULL ELSE pais_importador END,
    termo = CASE WHEN termo IN ('nan', '') THEN NULL ELSE termo END,
    unidade_de_medida = CASE WHEN unidade_de_medida IN ('nan', '') THEN NULL ELSE unidade_de_medida END,
    finalidade = CASE WHEN finalidade IN ('nan', '') THEN NULL ELSE finalidade END,
    fonte = CASE WHEN fonte IN ('nan', '') THEN NULL ELSE fonte END,
    pais_origem = CASE WHEN pais_origem IN ('nan', '') THEN NULL ELSE pais_origem END,
    pais_exportador = CASE WHEN pais_exportador IN ('nan', '') THEN NULL ELSE pais_exportador END;