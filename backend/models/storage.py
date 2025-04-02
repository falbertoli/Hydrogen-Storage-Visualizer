# backend/models/storage.py
from dataclasses import dataclass
from typing import Dict, Optional, List

@dataclass
class StorageConfiguration:
    id: int
    hydrogen_volume: float
    num_tanks: int
    footprint_area: float
    location: Dict[str, float]  # Contains lat and lng
    created_at: str  # ISO format date string
    
    def to_dict(self):
        """Convert StorageConfiguration object to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'hydrogen_volume': self.hydrogen_volume,
            'num_tanks': self.num_tanks,
            'footprint_area': self.footprint_area,
            'location': self.location,
            'created_at': self.created_at
        }