-- Function SafeDiv divides (and returns) the first by the second number
-- or returns 0 if the second number is equal to 0

DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER //

CREATE FUNCTION SafeDiv(INT a, INT b)
BEGIN
    IF (b == 0) THEN
        RETURN 0
    RETURN (a / b);
    END IF ;
END //

DELIMITER ;
