from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from datetime import datetime

@dataclass
class Facility:
    name: str
    function: str
    square_feet: float
    address: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    id: Optional[int] = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Facility':
        return cls(
            id=int(data.get('id')) if data.get('id') else None,
            name=data['name'],
            function=data['function'],
            square_feet=float(data['square_feet']),
            address=data['address'],
            # Latitude and longitude will default to None
        )
    
    def geocode(self):
      """Update latitude and longitude based on address"""
      from geocoding import geocode_address
      lat, lon = geocode_address(self.address)
      if lat and lon:
          self.latitude = lat
          self.longitude = lon
          return True
      return False

@dataclass
class Regulation:
    name: str
    info: str
    safety_distance_ft: float
    min_storage_gal: Optional[float] = None
    max_storage_gal: Optional[float] = None
    id: Optional[int] = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Regulation':
        return cls(
            id=int(data.get('id')) if data.get('id') else None,
            name=data['name'],
            info=data['info'],
            safety_distance_ft=float(data['safety_distance_ft']),
            min_storage_gal=float(data['min_storage_gal']) if data.get('min_storage_gal') and data['min_storage_gal'] else None,
            max_storage_gal=float(data['max_storage_gal']) if data.get('max_storage_gal') and data['max_storage_gal'] else None
        )
    
@dataclass
class StorageConfiguration:
    hydrogen_volume: float
    num_tanks: int
    footprint_area: float
    latitude: float
    longitude: float
    created_at: Optional[str] = None
    id: Optional[int] = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'StorageConfiguration':
        return cls(
            id=data.get('id'),
            hydrogen_volume=float(data['hydrogen_volume']),
            num_tanks=int(data['num_tanks']),
            footprint_area=float(data['footprint_area']),
            latitude=float(data['latitude']),
            longitude=float(data['longitude']),
            created_at=data.get('created_at')
        )
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'hydrogen_volume': self.hydrogen_volume,
            'num_tanks': self.num_tanks,
            'footprint_area': self.footprint_area,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'created_at': self.created_at or datetime.now().isoformat()
        }