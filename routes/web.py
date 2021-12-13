"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "UserController@index").name("index"),
        Get("/@token", "UserController@show").name("show"),
        Post("/login", "UserController@login").name("login"),
        Post("/", "UserController@create").name("create"),
        Put("/@token", "UserController@update").name("update"),
        Delete('/@token', "UserController@destroy").name("destroy")
    ], prefix="/user", name="user"),

    RouteGroup([
        Get("/", "FoodController@index").name("index"),
        Get("/@id", "FoodController@show").name("show")
    ], prefix="/food", name="food")
]
