from app import models, manager

manager.create_api(User, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Poop, methods=['GET', 'POST', 'DELETE'])

