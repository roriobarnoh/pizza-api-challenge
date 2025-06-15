from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    # Clear existing data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create restaurants
    r1 = Restaurant(name="Mama's Pizza", address="123 Pizza St")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Dough Ave")
    db.session.add_all([r1, r2])

    # Create pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="BBQ Chicken", ingredients="BBQ Sauce, Chicken, Cheese, Onion")
    db.session.add_all([p1, p2, p3])

    db.session.commit()

    # Create restaurant-pizza relationships
    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r1.id)
    rp3 = RestaurantPizza(price=12, pizza_id=p3.id, restaurant_id=r2.id)
    db.session.add_all([rp1, rp2, rp3])

    db.session.commit()
    print("✅ Done seeding!")
