from typing import List, Protocol, TypeVar

Entity = TypeVar("Entity", covariant=True)
Query = TypeVar("Query", covariant=True)


class Repository(Protocol[Entity, Query]):
    def select_one(self, query: Query) -> Entity:
        ...  # pragma: no cover

    def select_all(self, query: Query) -> List[Entity]:
        ...  # pragma: no cover

    def save(self, entity: Entity) -> Entity:
        ...  # pragma: no cover
