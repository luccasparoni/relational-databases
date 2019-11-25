
-- Consulta: Onde cada staff estava trabalhando
-- Para essa consulta, é considerado que os staffs apenas participam das atrações que trabalham (não podem participar de outras atrações)
-- É necessário ter duas horas para realizar a consulta, que retorna onde cada staff estava naquele periodo informado (pode ocorrer ais de um retorno
-- caso o staff tenha mudado de lugar)
SELECT P.NOME, A.NOME, PT.HORARIO FROM PARTICIPANTE AS P JOIN STAFF AS S ON 
P.CODIGO_INGRESSO = S.INGRESSO JOIN PARTICIPA_EVENTO AS PT ON P.CODIGO_INGRESSO = PT.PARTICIPANTE
JOIN ATRACAO AS A ON PT.ATRACAO = A.NUMERO WHERE (PT.HORARIO > TO_DATE('INICIO_HORA', 'DD-MM-YYYY')
 AND PT.HORARIO < TO_DATE('FINAL_HORA', 'DD-MM-YYYY'))


-- Consulta: Quantas pessoas visitaram cada atração.
select A.NOME, count(*) from PARTICIPANTE as P join PARTICIPA_EVENTO as E on P.CODIGO_INGRESSO = E.PARTICIPANTE join ATRACAO as A on E.ATRACAO = A.NUMERO where A.NOME = 'algum_nome'


-- Consulta: Quais equipamentos estavam sendo usados nos horários e por qual staff;
-- Aqui há duas consultas possíveis:

-- Qual equipamento estava com qual staff em determinado periodo de tempo
SELECT P.NOME, U.HORARIO, E.ID, E.DESCRICAO FROM PARTICIPANTE AS P JOIN STAFF AS S ON 
P.CODIGO_INGRESSO = S.INGRESSO JOIN UTILIZA AS U ON P.CODIGO_INGRESSO = U.STAFF JOIN 
EQUIPAMENTO AS E ON U.EQUIPAMENTO = E.ID WHERE U.HORARIO = 'ALGUM HORARIO'


-- Caso por staff
SELECT P.NOME, U.HORARIO, E.ID, E.DESCRICAO FROM PARTICIPANTE AS P JOIN STAFF AS S ON 
P.CODIGO_INGRESSO = S.INGRESSO JOIN UTILIZA AS U ON P.CODIGO_INGRESSO = U.STAFF JOIN 
EQUIPAMENTO AS E ON U.EQUIPAMENTO = E.ID WHERE P.CODIGO_INGRESSO
 = 'ID DO STAFF'

-- Consulta: Qual foi o principal público de cada influenciador;
--  @4 - Aqui tem um problema, nao tem duração da participação do brother na atracao, entao só bateria se fosse
-- o mesmo horario extaamente
-- Mostra o número de pessoas, bem como a idade minima e a maxima do maior grupo de pessoas (divididos
-- em 25 anos de diferenca, e genero) que o influenciador atingiu
SELECT P.GENERO, MAX(IDADE) AS IDADE_MINIMA, MIN(IDADE) AS IDADE_MAXIMA, COUNT(*) AS NRO_PUBLICO
FROM PARTICIPANTE AS P JOIN PARTICIPA_EVENTO AS PE ON P.CODIGO_INGRESSO = PE.PARTICIPANTE
JOIN ATRACAO AS A ON PE.ATRACAO = A.NUMERO WHERE A.NOME = 'INFLUENCY.ME' AND PE.DATA_HORA IN (
    SELECT DATA_HORA FROM PARTICIPANTE AS P JOIN PARTICIPA_EVENTO AS PE ON 
    P.CODIGO_INGRESSO = PE.PARTICIPANTE JOIN ATRACAO AS A ON PE.ATRACAO = A.NUMERO WHERE A.NOME = 'INFLUENCY.ME'
    AND P.NOME = 'ALGUM_NOME_DE_INFLUENCER'
) GROUP BY TRUNCATE(IDADE/25,0) ORDER BY NRO_PUBLICO, GENERO DESC

-- Quais palestras foram mais frequentadas;

SELECT PL.TEMA, COUNT(*) AS NRO_ESPECTADORES FROM PARTICIPANTE AS P
JOIN PARTICIPA_EVENTO AS PE ON P.CODIGO_INGRESSO = PE.PARTICIPANTE
JOIN ATRACAO AS A ON PE.ATRACAO = A.NUMERO WHERE A.NOME = 'PALESTRA' AND PE.DATA_HORA IN (

 )


-- Qual a porcentagem de jogos de cada plataforma; 
-- Retorna a porcetagem de presença de cada plataforma, a soma pode ser maior que 100, uma vez
-- que um jogo pode estar presente em mais de uma plataforma
SELECT P.PLATAFORMA, COUNT(*)*100/(SELECT COUNT(*) FROM PLATAFORMA_JOGO) AS PORCENTAGEM_PLATAFORMA
FROM JOGO AS J JOIN PLATAFORMA_JOGO AS PJ ON J.NUMERO_MESA = PJ.JOGO GROUP BY PJ.PLATAFORMA ORDER BY
PORCENTAGEM_PLATAFORMA DESC


-- Consulta: Quantos devs são filiados a alguma empresa.

SELECT E.NOME, COUNT(*) AS NUMERO_AFILIADOS FROM DEV AS D JOIN ESTUDIO_DE_DESENVOLVIMENTO AS ED 
ON D.ESTUDIO = ED.CNPJ WHERE E.NOME = 'ALGUM_NOME'

