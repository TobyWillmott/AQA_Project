from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Player, Team, League, Footballer

toby = Player(username="tobywillmott", password="password123", total_socre=0)
toby_team = Team()
toby_league = League(league_name="Thebestleague", num_players=0)

toby.leagues.append(toby_league)
toby.team = toby_team

engine = create_engine("sqlite:///fantasy_football.db", echo=True)
with Session(engine) as sess:
    sess.add(toby)
    sess.add(toby_team)
    sess.add(toby_league)
    sess.commit()
