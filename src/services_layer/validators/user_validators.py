from marshmallow import Schema, fields, validates, ValidationError

class UserSchema(Schema):
    email = fields.Email(required=True, error_messages = {
        "required": "Email is required",
        "Invalid": "Invalid email adress"
    })
    
    password = fields.Str(required=True, error_messages={
        "required": "Password is required"
    })
    
    role = fields.Str(required=True, validate= lambda x: x in ["student","Teacher",  "Admin"], error_messages={
        "required": "Role is required",
        "validator_failed": "role must be either student, admin or teacher"
    })
    
    phone = fields.Str(required=False)
    
    @validates("password")
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError ("password must be at least 8 characters")