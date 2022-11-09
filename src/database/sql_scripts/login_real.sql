CREATE OR REPLACE FUNCTION login(giv_username text,giv_password text)
RETURNS bool
LANGUAGE plpgsql
AS
$$


DECLARE
	v_username VARCHAR(30);
BEGIN
	SELECT email
	INTO v_username
	FROM Credential
	WHERE password = giv_password;

	IF v_username = giv_username THEN
		RETURN TRUE;
	ELSE
		RETURN FALSE;
	END IF;
END;
$$;

