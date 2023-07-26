from sqlalchemy import Column, Integer, String, Date, Boolean, Table, UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

player_league = Table("player_league",
                      Base.metadata,
                      Column("player_id", ForeignKey("player.player_id")),
                      Column("league_id", ForeignKey("league.league_id")),
                      UniqueConstraint("player_id", "league_id")
                      )

footballer_team = Table("footballer_team",
                        Base.metadata,
                        Column("footballer_id", ForeignKey("footballer.footballer_id")),
                        Column("team_id", ForeignKey("team.team_id")),
                        UniqueConstraint("footballer_id", "team_id")
                        )


class Player(Base):
    __tablename__ = "player"
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    total_score = Column(Integer)
    team_id = Column(Integer, ForeignKey("team.team_id"))

    leagues = relationship("League",
                           secondary=player_league,
                           order_by="(League.league_name)",
                           back_populates="players")
    team = relationship("Team", back_populates="player")


class League(Base):
    __tablename__ = "league"
    league_id = Column(Integer, primary_key=True, autoincrement=True)
    league_name = Column(String)
    num_players = Column(Integer)

    players = relationship("Player",
                           secondary=player_league,
                           order_by="(Player.total_score)",
                           back_populates="leagues")


class Team(Base):
    __tablename__ = "team"
    team_id = Column(Integer, primary_key=True, autoincrement=True)

    player_id = Column(Integer, ForeignKey("player.player_id"))

    player = relationship("Player", back_populates="team")

    footballers = relationship("Footballer",
                               secondary=footballer_team,
                               order_by="(Footballer.position, Footballer.second_name)",
                               back_populates="teams"
                               )


class Footballer(Base):
    __tablename__ = "footballer"
    footballer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    second_name = Column(String)
    position = Column(String)

    teams = relationship("Teams",
                         secondary=footballer_team,
                         order_by="(Team.team_id)",
                         back_populates="footballers",
                         )
