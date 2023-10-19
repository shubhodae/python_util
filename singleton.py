def singleton_decorator(singleton_class):
    singleton_dict = dict()

    def get_instance(*args, **kwargs):
        if singleton_class not in singleton_dict:
            singleton_dict[singleton_class] = singleton_class(*args, **kwargs)
        return singleton_dict[singleton_class]

    return get_instance


@singleton_decorator
class MongoDBConnction:
    def __init__(self) -> None:
        print("MongoDB connection....")


if __name__ == "__main__":
    print("Hello Wold")

    connection_one = MongoDBConnction()
    connection_two = MongoDBConnction()

    print(connection_one == connection_two)
