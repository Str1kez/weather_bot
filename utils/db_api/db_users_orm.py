from sqlalchemy.sql.elements import or_, and_

from .base_model import db
from .user_table import User


async def insert_user(id, city):
    user = User(id=id, city=city)
    await user.create()


async def user_reduction(id):
    await db.delete(User).where(and_(~User.request_id.in_(
        db.select([User.request_id]).where(User.id == id).order_by(User.request_id.desc()).limit(3)),
        User.id == id)).gino.status()


async def select_cities(id):
    cities = await User.query.where(User.id == id).gino.all()
    return [x.city for x in cities]
