from pydantic import BaseModel, field_validator


class CreateConstructionLocationRequest(BaseModel):
    latitude: float
    longitude: float

    @classmethod
    @field_validator("latitude")
    def validate_latitude(cls, value):
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90 degrees.")
        return value

    @classmethod
    @field_validator("longitude")
    def validate_longitude(cls, value):
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180 degrees.")
        return value
