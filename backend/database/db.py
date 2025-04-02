import sqlite3
import os
from datetime import datetime

class Database:
    def __init__(self, db_path='database/hydrogen_storage.db'):
        self.db_path = db_path
        self._create_tables_if_not_exist()
    
    def _get_connection(self):
        """Get SQLite connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        return conn
    
    def _create_tables_if_not_exist(self):
        """Create database tables if they don't exist"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Create facilities table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS facilities (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            function TEXT NOT NULL,
            square_feet REAL NOT NULL,
            address TEXT NOT NULL,
            latitude REAL,
            longitude REAL
        )
        ''')
        
        # Create regulations table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS regulations (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            info TEXT NOT NULL,
            min_storage_gal REAL,
            max_storage_gal REAL,
            safety_distance_ft REAL NOT NULL
        )
        ''')
        
        # Create storage configurations table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS storage_configurations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hydrogen_volume REAL NOT NULL,
            num_tanks INTEGER NOT NULL,
            footprint_area REAL NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            created_at TEXT NOT NULL
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def insert_facilities(self, facilities):
        """Insert multiple facilities"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        for facility in facilities:
            cursor.execute('''
            INSERT OR REPLACE INTO facilities (id, name, function, square_feet, address, latitude, longitude)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                facility.id,
                facility.name,
                facility.function,
                facility.square_feet,
                facility.address,
                facility.latitude,
                facility.longitude
            ))
        
        conn.commit()
        conn.close()
    
    def insert_regulations(self, regulations):
        """Insert multiple regulations"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        for regulation in regulations:
            cursor.execute('''
            INSERT OR REPLACE INTO regulations (id, name, info, min_storage_gal, max_storage_gal, safety_distance_ft)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                regulation.id,
                regulation.name,
                regulation.info,
                regulation.min_storage_gal,
                regulation.max_storage_gal,
                regulation.safety_distance_ft
            ))
        
        conn.commit()
        conn.close()
    
    def insert_storage_configuration(self, storage):
        """Insert a new storage configuration"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO storage_configurations 
        (hydrogen_volume, num_tanks, footprint_area, latitude, longitude, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            storage.hydrogen_volume,
            storage.num_tanks,
            storage.footprint_area,
            storage.latitude,
            storage.longitude,
            datetime.now().isoformat()
        ))
        
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id