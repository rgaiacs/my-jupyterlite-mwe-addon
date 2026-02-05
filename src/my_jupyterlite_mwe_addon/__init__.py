from jupyterlite_core.addons.base import BaseAddon

class MyAddon(BaseAddon):
    __all__ = ["status"]

    def status(self, manager):
        yield dict(name="hello", actions=[lambda: print("world")])

    def post_build(manager):
        def hello():
            print("Hello world!")

        yield dict(
            name="hello-world",
            actions=[[post_build, []]],
        )