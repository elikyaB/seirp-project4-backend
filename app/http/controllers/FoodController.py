""" A FoodController Module """

from masonite.controllers import Controller
from masonite.request import Request
from masoniteorm.query import QueryBuilder
from app.Food import Food


class FoodController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", FoodController)
        """
        id = self.request.param("id")
        return Food.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", FoodController)
        """
        builder = QueryBuilder(model=Food).table("foods").all()
        return builder

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", FoodController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", FoodController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", FoodController)
        """

        pass