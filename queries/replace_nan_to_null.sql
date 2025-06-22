UPDATE comercio_especies_ameacadas
SET 
	pais_importador = NULLIF(pais_importador, 'nan'),
	pais_exportador = NULLIF(pais_exportador, 'nan'),
    pais_origem     = NULLIF(pais_origem, 'nan'),
    unidade_de_medida = NULLIF(unidade_de_medida, 'nan'),
    finalidade = NULLIF(finalidade, 'nan'),
    fonte = NULLIF(fonte, 'nan'),
	termo = NULLIF(termo, 'nan'),
	quantidade_importada_reportada = NULLIF(quantidade_importada_reportada, 'nan'),
	quantidade_exportada_reportada = NULLIF(quantidade_exportada_reportada, 'nan');
	