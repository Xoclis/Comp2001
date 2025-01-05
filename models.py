from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, DECIMAL
from sqlalchemy.orm import relationship
from config import db

# Association table for many-to-many relationship between Trail and Feature
trail_feature_association = Table(
    'Trail_Feature',  # Matches the table name in SQL
    db.Model.metadata,
    Column('TrailID', Integer, ForeignKey('cw2.Trail.TrailID'), primary_key=True),
    Column('Trail_FeatureID', Integer, ForeignKey('cw2.Feature.Trail_FeatureID'), primary_key=True)
)

class Trail(db.Model):
    __tablename__ = 'Trail'
    __table_args__ = {'schema': 'cw2'}  # Specify schema

    TrailID = Column(Integer, primary_key=True)
    Trail_name = Column(String(255), nullable=False)  # Matches SQL column name
    Trail_Summary = Column(String)  # Use String for NVARCHAR(MAX)
    Trail_Description = Column(String)
    Difficulty = Column(String(50))
    Location = Column(String(255))
    Length = Column(DECIMAL(10, 2))  # Matches DECIMAL(10,2) in SQL
    Elevation_gain = Column(DECIMAL(10, 2))
    Route_type = Column(String(50))
    OwnerID = Column(Integer, ForeignKey('cw2.User.UserID'))  # Link to USER table
    Pt1_Lat = Column(DECIMAL(10, 7))
    Pt1_Long = Column(DECIMAL(10, 7))
    Pt1_Desc = Column(String)
    Pt2_Lat = Column(DECIMAL(10, 7))
    Pt2_Long = Column(DECIMAL(10, 7))
    Pt2_Desc = Column(String)

    owner = relationship("User", back_populates="trails")  # Relationship with User
    features = relationship("Feature", secondary=trail_feature_association, back_populates="trails")

    def to_dict(self):
        return {
            "TrailID": self.TrailID,
            "Trail_name": self.Trail_name,
            "Trail_Summary": self.Trail_Summary,
            "Trail_Description": self.Trail_Description,
            "Difficulty": self.Difficulty,
            "Location": self.Location,
            "Length": self.Length,
            "Elevation_gain": self.Elevation_gain,
            "Route_type": self.Route_type,
            "OwnerID": self.OwnerID,
            "Pt1_Lat": self.Pt1_Lat,
            "Pt1_Long": self.Pt1_Long,
            "Pt1_Desc": self.Pt1_Desc,
            "Pt2_Lat": self.Pt2_Lat,
            "Pt2_Long": self.Pt2_Long,
            "Pt2_Desc": self.Pt2_Desc,
        }


class Feature(db.Model):
    __tablename__ = 'Feature'
    __table_args__ = {'schema': 'cw2'}  # Specify schema

    Trail_FeatureID = Column(Integer, primary_key=True)
    Trail_Feature = Column(String(255), nullable=False)

    trails = relationship("Trail", secondary=trail_feature_association, back_populates="features")


class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'cw2'}  # Specify schema

    UserID = Column(Integer, primary_key=True)
    Email_address = Column(String(255), unique=True, nullable=False)  # Matches SQL column name
    Role = Column(String(50), nullable=False)

    trails = relationship("Trail", back_populates="owner")  # Relationship with Trail
