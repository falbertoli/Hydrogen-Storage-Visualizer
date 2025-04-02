# backend/models/regulation.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Regulation:
    id: int
    name: str
    info: str
    min_storage_gal: Optional[float]
    max_storage_gal: Optional[float]
    safety_distance_ft: float
    
    @classmethod
    def from_dict(cls, data):
        """Create a Regulation object from a dictionary (CSV row)"""
        return cls(
            id=data.get('regulation_id', 0),
            name=data.get('regulation_name', ''),
            info=data.get('regulation_info', ''),
            min_storage_gal=float(data.get('storage_gal_min')) if data.get('storage_gal_min') != '' else None,
            max_storage_gal=float(data.get('storage_gal_max')) if data.get('storage_gal_max') != '' else None,
            safety_distance_ft=float(data.get('safety_distance_ft', 0))
        )
    
    def to_dict(self):
        """Convert Regulation object to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'info': self.info,
            'min_storage_gal': self.min_storage_gal,
            'max_storage_gal': self.max_storage_gal,
            'safety_distance_ft': self.safety_distance_ft
        }