# backend/models/facility.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Facility:
    id: int
    name: str
    function: str
    square_feet: float
    address: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    
    @classmethod
    def from_dict(cls, data):
        """Create a Facility object from a dictionary (CSV row)"""
        return cls(
            id=data.get('id', 0),
            name=data.get('Facility Name', ''),
            function=data.get('Building Function', ''),
            square_feet=float(data.get('Sq. Ft.', 0)),
            address=data.get('Address', ''),
            latitude=data.get('latitude', None),
            longitude=data.get('longitude', None)
        )
    
    def to_dict(self):
        """Convert Facility object to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'function': self.function,
            'square_feet': self.square_feet,
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude
        }