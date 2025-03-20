from  werkzeug.security import generate_password_hash, check_password_hash

class Hash:
    @staticmethod
    def hash_password(password):
        if not password:
            raise ValueError ('password cannot be empty')
        return generate_password_hash(password, method="pbkdf2:sha512", salt_length=16)
    
    @staticmethod
    def verify_password(hashed_password, password):
        if not hashed_password or not password:
            raise ValueError ("Hashed password and password cannot be empty")
        return check_password_hash(hashed_password, password)