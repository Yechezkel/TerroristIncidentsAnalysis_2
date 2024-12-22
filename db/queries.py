from .connection import session_factory
from sqlalchemy import text, func, case, desc
from models.event import Event
from models.terror_organization import TerrorOrganization
from models.attack_type import AttackType



def get_top_5_most_harmful_terror_organization():
    session = session_factory()
    injuries_case = case((Event.injuries_num != -99, Event.injuries_num), else_=0)
    fatalities_case = case((Event.fatalities_num != -99, Event.fatalities_num), else_=0)
    total_victims = func.sum(injuries_case + fatalities_case).label("total_victims")
    try:
        query = (
            session.query(TerrorOrganization.id, TerrorOrganization.name, total_victims).join(Event).where(TerrorOrganization.name!="Unknown")
            .group_by(TerrorOrganization.id).order_by(desc(total_victims)).limit(5)
        )
        column_keys = ['id', 'name', 'total_victims']
        return [dict(zip(column_keys, row)) for row in query.all()]
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None
    finally:
        session.close()


def get_top_5_most_harmful_terror_organization_pure():
    pure_query = text("""
        SELECT t.id, t.name,
            SUM(
                CASE WHEN e.injuries_num != -99 THEN e.injuries_num ELSE 0 END +
                CASE WHEN e.fatalities_num != -99 THEN e.fatalities_num ELSE 0 END
            ) AS total_victims
        FROM terror_organizations t
        JOIN events e ON t.id = e.terror_organization_id
        WHERE t.name != 'Unknown'
        GROUP BY t.id
        ORDER BY total_victims DESC
        LIMIT 5;
        """)
    session = session_factory()
    try:
        result = session.execute(pure_query)
        column_keys = ['id', 'name', 'total_victims']
        return [dict(zip(column_keys, row)) for row in result.fetchall()]
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None
    finally:
        session.close()




def get_most_deadly_attack_types(limit=None):
    session = session_factory()
    injuries_case = case((Event.injuries_num != -99, Event.injuries_num), else_=0)
    fatalities_case = case((Event.fatalities_num != -99, Event.fatalities_num), else_=0)
    deadly_score = func.sum(injuries_case + (2*fatalities_case)).label("deadly_score")
    try:
        query = session.query(AttackType.id, AttackType.name, deadly_score).join(Event).where(AttackType.name!="Unknown").group_by(AttackType.id).order_by(desc(deadly_score))
        if limit:
            query = query.limit(limit)
        column_keys = ['id', 'name', 'deadly_score']
        return [dict(zip(column_keys, row)) for row in query.all()]
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None
    finally:
        session.close()

