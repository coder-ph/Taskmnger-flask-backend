
import datetime
from Backend.src.startup.loggings import logger


class ApiError(Exception):
    def __init__(self, message, status_code=400, error_code = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.timestamp = datetime.datetime.now(datetime.timezone)
        logger.error(f"{self.__class__.__name__}: {message}")
        
    def to_dict(self):
        return {
            'error': self.message,
            "error_code": self.error_code,
            "timestamp": self.timestamp
            }

class InvalidAccessError(ApiError):
    def __init__(self, message="Unauthorized access", error_code="ACCESS_DENIED"):
        super().__init__(message, 403, error_code)
    
class InvalidObjectError(ApiError):
    def __init__(self, message="Invalid Object", error_code="INVALID_DATA"):
        super().__init__(message, 400, error_code)

class DBError(ApiError):
    def __init__(self, message="Database Error", error_code="DB_ERROR"):
        super().__init__(message, 500, error_code)
        
class InternalServerError(ApiError):
    def __init__(self, message="Internal Server Error", error_code="SERVER_ERROR"):
        super().__init__(message,500, error_code)
        
class EnvError(ApiError):
    def __init__(self, message="Environment variable error", error_code="ENV_ERROR"):
        super().__init__(message, 500, error_code)
    