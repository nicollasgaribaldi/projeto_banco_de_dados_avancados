CREATE OR REPLACE FUNCTION carregar_dimensoes_fatos()
RETURNS TRIGGER AS $$
BEGIN
    -- Inserir na dimensão carro
    PERFORM dblink_exec(
        'dbname=homologacao user=seu_usuario password=sua_senha',
        FORMAT('INSERT INTO dim_carro (car_name, type, drive)
                VALUES (''%s'', ''%s'', ''%s'') ON CONFLICT DO NOTHING;',
                NEW.car_name, NEW.type, NEW.drive)
    );

    -- Inserir na dimensão localização
    PERFORM dblink_exec(
        'dbname=homologacao user=seu_usuario password=sua_senha',
        FORMAT('INSERT INTO dim_localizacao (location)
                VALUES (''%s'') ON CONFLICT DO NOTHING;',
                NEW.location)
    );

    -- Inserir na dimensão combustível
    PERFORM dblink_exec(
        'dbname=homologacao user=seu_usuario password=sua_senha',
        FORMAT('INSERT INTO dim_combustivel (fuel)
                VALUES (''%s'') ON CONFLICT DO NOTHING;',
                NEW.fuel)
    );

    -- Inserir na fato
    PERFORM dblink_exec(
        'dbname=homologacao user=seu_usuario password=sua_senha',
        FORMAT('INSERT INTO fato_precos (carro_id, localizacao_id, combustivel_id, year, distance, owner, price)
                VALUES (
                    (SELECT id FROM dim_carro WHERE car_name = ''%s''),
                    (SELECT id FROM dim_localizacao WHERE location = ''%s''),
                    (SELECT id FROM dim_combustivel WHERE fuel = ''%s''),
                    %s, %s, %s, %s);',
                NEW.car_name, NEW.location, NEW.fuel, NEW.year, NEW.distance, NEW.owner, NEW.price)
    );

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
