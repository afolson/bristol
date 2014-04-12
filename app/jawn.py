from app import models, manager

manager.create_api(models.User, methods=['GET', 'POST', 'DELETE'])
manager.create_api(models.Poop, methods=['GET', 'POST', 'DELETE'])

