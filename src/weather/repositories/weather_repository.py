import logging

from weather.models import Locations
from weather.utils.repository import SQLRepository

logger = logging.getLogger('web')


class LocationsRepository(SQLRepository):

    def find_all(self, userid):
        stmt = Locations.objects.filter(userid=userid).all()
        return stmt

    def get_one(self, id, userid):
        logger.debug(f"Getting location with id={id} and userid={userid}")
        try:
            stmt = Locations.objects.get(id=id, userid=userid)
            logger.debug(f"Found location: {stmt}")
            return stmt
        except:
            logger.error(f"No location found with id={id} and userid={userid}")
            return None

    def add_one(self, city, latitude, longitude, user):
        stmt = Locations.objects.create(name=city, latitude=latitude, longitude=longitude, userid=user)
        stmt.save()

    def delete_one(self, pk):
        result = Locations.objects.filter(id=pk).delete()
