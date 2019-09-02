"""Database models"""

import datetime

from sqlalchemy import MetaData, Column, ForeignKey, Integer, String, SmallInteger, DateTime, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


meta = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})
Base = declarative_base(metadata=meta)

class Region(Base):
    """Model for region"""
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gold_limit = Column(SmallInteger)
    oil_limit = Column(SmallInteger)
    ore_limit = Column(SmallInteger)
    uranium_limit = Column(SmallInteger)
    diamond_limit = Column(SmallInteger)


class DeepExploration(Base):
    """Model for deep exploration"""
    __tablename__ = 'deep_exploration'
    id = Column(Integer, primary_key=True)
    date_time_end = Column(DateTime)
    region_id = Column(Integer)
    resource_type = Column(SmallInteger)
    region_id = Column(Integer, ForeignKey('region.id'))
    region_track = relationship(
        "Region",
        backref=backref("deep_explorations", lazy="dynamic")
    )


class ResourceTrack(Base):
    """Model for resource track"""
    __tablename__ = 'resource_track'
    id = Column(Integer, primary_key=True)
    resource_type = Column(SmallInteger)
    date_time = Column(DateTime, default=datetime.datetime.utcnow)
    state_id = Column(Integer, ForeignKey('state.id'))
    state = relationship(
        "State",
        backref=backref("resource_tracks", lazy="dynamic")
    )


class ResourceStat(Base):
    """Model for resource stat"""
    __tablename__ = 'resource_stat'
    id = Column(Integer, primary_key=True)
    explored = Column(SmallInteger)
    deep_exploration = Column(SmallInteger)
    limit_left = Column(SmallInteger)

    resource_track_id = Column(Integer, ForeignKey('resource_track.id'))
    resource_track = relationship(
        "ResourceTrack",
        backref=backref("resource_stats", lazy="dynamic")
    )

    region_id = Column(Integer, ForeignKey('region.id'))
    region = relationship(
        "Region",
        backref=backref("resource_stats", lazy="dynamic")
    )


state_region = Table('state_region', Base.metadata,
    Column('state_id', Integer, ForeignKey('state.id')),
    Column('region_id', Integer, ForeignKey('region.id'))
)

class State(Base):
    """Model for state"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    regions = relationship("Region", secondary=state_region)

class Department(Base):
    """Model for department"""
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_type = Column(Integer)


class DepartmentStat(Base):
    """Model for departent stat"""
    __tablename__ = 'department_stat'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    points = Column(SmallInteger)

    player_id = Column(Integer, ForeignKey('player.id'))
    player = relationship(
        "Player",
        backref=backref("department_stats", lazy="dynamic")
    )

    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(
        "Department",
        backref=backref("stats", lazy="dynamic")
    )


player_party = Table('player_party', Base.metadata,
    Column('player_id', Integer, ForeignKey('player.id')),
    Column('party_id', Integer, ForeignKey('party.id'))
)

player_residency = Table('player_residency', Base.metadata,
    Column('player_id', Integer, ForeignKey('player.id')),
    Column('region_id', Integer, ForeignKey('region.id'))
)

player_location  = Table('player_location', Base.metadata,
    Column('player_id', Integer, ForeignKey('player.id')),
    Column('region_id', Integer, ForeignKey('region.id'))
)

class Player(Base):
    """Model for player"""
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nation = Column(String)
    residencies = relationship("Region", secondary=player_residency)
    locations = relationship("Region", secondary=player_location)
    parties = relationship("Region", secondary=player_party)


class Party(Base):
    """Model for party"""
    __tablename__ = 'party'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String(512))
    from_date_time = Column(DateTime)
    until_date_time = Column(DateTime)


class Election(Base):
    """Model for election"""
    __tablename__ = 'election'
    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('state.id'))
    convocation_date_time = Column(DateTime)

    state = relationship(
        "State",
        backref=backref("elections", lazy="dynamic")
    )


class ElectionStat(Base):
    """Model for election stat"""
    __tablename__ = 'election_stat'
    id = Column(Integer, primary_key=True)
    percentage = Column(SmallInteger)
    seats = Column(SmallInteger)

    election_id = Column(Integer, ForeignKey('election.id'))
    election = relationship(
        "Election",
        backref=backref("election_stats", lazy="dynamic")
    )
