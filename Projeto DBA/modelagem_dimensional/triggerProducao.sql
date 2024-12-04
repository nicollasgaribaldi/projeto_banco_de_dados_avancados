CREATE TRIGGER trigger_carregar_dimensoes_fatos
AFTER INSERT ON carros
FOR EACH ROW EXECUTE FUNCTION carregar_dimensoes_fatos();
