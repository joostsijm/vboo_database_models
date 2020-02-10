"""Database models"""

import datetime

from sqlalchemy import MetaData, Column, ForeignKey, Integer, String, \
    SmallInteger, DateTime, BigInteger, Date, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


meta = MetaData(naming_convention={
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
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
    points = Column(Integer)
    resource_type = Column(SmallInteger)
    region_id = Column(Integer, ForeignKey('region.id'))
    region = relationship(
        'Region',
        backref=backref('deep_explorations', lazy='dynamic')
    )


class ResourceTrack(Base):
    """Model for resource track"""
    __tablename__ = 'resource_track'
    id = Column(Integer, primary_key=True)
    resource_type = Column(SmallInteger)
    date_time = Column(DateTime)
    state_id = Column(Integer, ForeignKey('state.id'))
    state = relationship(
        'State',
        backref=backref('resource_tracks', lazy='dynamic')
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
        'ResourceTrack',
        backref=backref('resource_stats', lazy='dynamic')
    )

    region_id = Column(Integer, ForeignKey('region.id'))
    region = relationship(
        'Region',
        backref=backref('resource_stats', lazy='dynamic')
    )


class StateRegion(Base):
    """Model for state region"""
    __tablename__ = 'state_region'
    state_id = Column(Integer, ForeignKey('state.id'), primary_key=True)
    region_id = Column(Integer, ForeignKey('region.id'), primary_key=True)
    from_date_time = Column(DateTime, primary_key=True)
    until_date_time = Column(DateTime)


class State(Base):
    """Model for state"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    regions = relationship('Region', secondary='state_region')
    capital_id = Column(Integer, ForeignKey('region.id'))
    capital = relationship(
        'Region',
        backref=backref('state_capital', lazy='dynamic')
    )

class Department(Base):
    """Model for department"""
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_type = Column(Integer)

    state_id = Column(Integer, ForeignKey('state.id'))
    state = relationship(
        'State',
        backref=backref('elections', lazy='dynamic')
    )


class DepartmentStat(Base):
    """Model for departent stat"""
    __tablename__ = 'department_stat'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    points = Column(SmallInteger)

    player_id = Column(BigInteger, ForeignKey('player.id'))
    player = relationship(
        'Player',
        backref=backref('department_stats', lazy='dynamic')
    )

    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(
        'Department',
        backref=backref('stats', lazy='dynamic')
    )


class PlayerParty(Base):
    """Model fro player party"""
    __tablename__ = 'player_party'
    player_id = Column(BigInteger, ForeignKey('player.id'), primary_key=True)
    party_id = Column(Integer, ForeignKey('party.id'), primary_key=True)
    from_date_time = Column(DateTime, primary_key=True)
    until_date_time = Column(DateTime)


class PlayerLocation(Base):
    """Model for player location"""
    __tablename__ = 'player_location'
    player_id = Column(BigInteger, ForeignKey('player.id'), primary_key=True)
    region_id = Column(Integer, ForeignKey('region.id'), primary_key=True)
    from_date_time = Column(DateTime, primary_key=True)
    until_date_time = Column(DateTime)


class PlayerResidency(Base):
    """Model for player residency"""
    __tablename__ = 'player_residency'
    player_id = Column(BigInteger, ForeignKey('player.id'), primary_key=True)
    region_id = Column(Integer, ForeignKey('region.id'), primary_key=True)
    from_date_time = Column(DateTime, primary_key=True)
    until_date_time = Column(DateTime)


class StateWorkPermit(Base):
    """Model for state work permit"""
    __tablename__ = 'state_work_permit'
    state_id = Column(Integer, ForeignKey('state.id'), primary_key=True)
    player_id = Column(BigInteger, ForeignKey('player.id'), primary_key=True)
    from_date_time = Column(DateTime, primary_key=True)
    until_date_time = Column(DateTime)


class Player(Base):
    """Model for player"""
    __tablename__ = 'player'
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    nation = Column(String)
    registration_date = Column(Date)
    residencies = relationship('Region', secondary='player_residency')
    locations = relationship('Region', secondary='player_location')
    parties = relationship('Region', secondary='player_party')
    state_work_permits = relationship('State', secondary='state_work_permit')


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
    convocation_date_time = Column(DateTime)

    state_id = Column(Integer, ForeignKey('state.id'))
    state = relationship(
        'State',
        backref=backref('elections', lazy='dynamic')
    )


class ElectionStat(Base):
    """Model for election stat"""
    __tablename__ = 'election_stat'
    id = Column(Integer, primary_key=True)
    percentage = Column(SmallInteger)
    seats = Column(SmallInteger)

    election_id = Column(Integer, ForeignKey('election.id'))
    election = relationship(
        'Election',
        backref=backref('election_stats', lazy='dynamic')
    )
    party_id = Column(Integer, ForeignKey('party.id'))
    party = relationship(
        'Party',
        backref=backref('election_stats', lazy='dynamic')
    )


class MilitaryAcademy(Base):
    """Model for military academy"""
    __tablename__ = 'military_academy'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    player_id = Column(BigInteger, ForeignKey('player.id'))
    player = relationship(
        'User',
        backref=backref('military_academies', lazy='dynamic')
    )

    region_id = Column(Integer, ForeignKey('region.id'))
    region = relationship(
        'Region',
        backref=backref('military_academies', lazy='dynamic')
    )


class Factory(Base):
    """Model for factory"""
    __tablename__ = 'factory'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    resource_type = Column(SmallInteger)

    player_id = Column(BigInteger, ForeignKey('player.id'))
    player = relationship(
        'User',
        backref=backref('factories', lazy='dynamic')
    )


class FactoryTrack(Base):
    """Model for facctory track"""
    __tablename__ = 'factory_track'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)

    state_id = Column(Integer, ForeignKey('state.id'))
    state = relationship(
        'State',
        backref=backref('factory_tracks', lazy='dynamic')
    )


class FactoryLocation(Base):
    """Model for factory location"""
    __tablename__ = 'factory_location'
    factory_id = Column(Integer, ForeignKey('factory.id'), primary_key=True)
    region_id = Column(Integer, ForeignKey('region.id'), primary_key=True)
    from_date_time = Column(DateTime, primary_key=True)
    until_date_time = Column(DateTime)


class FactoryStat(Base):
    """Model for factory"""
    __tablename__ = 'factory_stat'
    id = Column(Integer, primary_key=True)
    level = Column(SmallInteger)
    workers = Column(SmallInteger)
    experience = Column(Integer)
    wage = Column(Integer)

    factory_id = Column(Integer, ForeignKey('factory.id'))
    factory = relationship(
        'FactoryTrack',
        backref=backref('factory_stats', lazy='dynamic')
    )
    factory_track_id = Column(Integer, ForeignKey('factory_track.id'))
    factory_track = relationship(
        'FactoryTrack',
        backref=backref('factory_stats', lazy='dynamic')
    )


class MarketTrack(Base):
    """Model for market track"""
    __tablename__ = 'market_track'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    player_resources = Column(Boolean, server_default='f', default=False)
    state_resources = Column(Boolean, server_default='f', default=False)
    items = Column(Boolean, server_default='f', default=False)


class PlayerMarketStat(Base):
    """Model for market stat"""
    __tablename__ = 'player_market_stat'
    id = Column(Integer, primary_key=True)
    item_type = Column(SmallInteger)
    price = Column(Integer)
    amount = Column(BigInteger)
    half_t_average = Column(Integer)
    one_t_average = Column(Integer)
    two_t_average = Column(Integer)
    five_t_average = Column(Integer)
    total_offers = Column(Integer)

    player_id = Column(BigInteger, ForeignKey('player.id'))
    player = relationship(
        'Player',
        backref=backref('player_market_stats', lazy='dynamic')
    )

    market_track_id = Column(Integer, ForeignKey('market_track.id'))
    market_track = relationship(
        'MarketTrack',
        backref=backref('player_market_stats', lazy='dynamic')
    )


class StateMarketStat(Base):
    """Model for market stat"""
    __tablename__ = 'state_market_stat'
    id = Column(Integer, primary_key=True)
    item_type = Column(SmallInteger)
    price = Column(Integer)
    amount = Column(BigInteger)

    region_id = Column(Integer, ForeignKey('region.id'))
    region = relationship(
        'Region',
        backref=backref('region_market_stats', lazy='dynamic')
    )

    market_track_id = Column(Integer, ForeignKey('market_track.id'))
    market_track = relationship(
        'MarketTrack',
        backref=backref('state_market_stats', lazy='dynamic')
    )

class TelegramAccount(Base):
    """Model for Telegram account"""
    __tablename__ = 'telegram_account'
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    registration_date = Column(DateTime)

class TelegramHandle(Base):
    """Model for Telegram handle"""
    __tablename__ = 'telegram_handle'
    id = Column(Integer, primary_key=True)
    handle = Column(String)
    registration_date = Column(DateTime)

    telegram_account_id = Column(BigInteger, ForeignKey('telegram_account.id'))
    telegram_account = relationship(
        'TelegramAccount',
        backref=backref('account_handles', lazy='dynamic')
    )

class PlayerTelegram(Base):
    """Model for belongs to"""
    __tablename__ = 'player_telegram'
    player_id = Column(BigInteger, ForeignKey('player.id'), primary_key=True)
    telegram_id = Column(BigInteger, ForeignKey('telegram_account.id'), primary_key=True)
    from_date_time = Column(DateTime, primary_key=True)
    until_date_time = Column(DateTime)

class TelegramVerification(Base):
    """Model for Telegram verification"""
    __tablename__ = 'telegram_verification'
    player_id = Column(BigInteger, ForeignKey('player.id'), primary_key=True)
    telegram_id = Column(BigInteger, ForeignKey('telegram_account.id'), primary_key=True)
    code = Column(String)
    date_time = Column(DateTime)
    confirmed = Column(Boolean, server_default='f', default=False)
