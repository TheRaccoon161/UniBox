from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models

@view_config(route_name='test', renderer='../templates/test.jinja2')
def my_test(request):
    query = request.dbsession.query(models.QA)
    q_as=query.all()
    return {'QA': q_as}