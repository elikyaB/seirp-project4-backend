"""CreateFoodsTable Migration."""

from masoniteorm.migrations import Migration


class CreateFoodsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("foods") as table:
            table.increments("id")
            table.integer("I_Code")
            table.string("Ingredient")
            table.jsonb("Nutrients")
            table.timestamps()
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("foods")
