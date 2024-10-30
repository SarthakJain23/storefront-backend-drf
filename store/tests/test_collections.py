import pytest
from rest_framework import status

from model_bakery import baker

from store.models import Collection


@pytest.fixture
def create_collection(api_client):
    def _create_collection(collection):
        return api_client.post("/store/collections/", collection)

    return _create_collection


@pytest.mark.django_db
class TestCreateCollection:

    def test_if_user_is_anonymous(self, create_collection):
        # AAA (Arrange, Act, Assert)

        # Arrange - fetch instances of the models

        # Act - perform the action you want to test
        response = create_collection({"title": "a"})

        # Assert - check the result
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin(self, authenticate, create_collection):
        authenticate()
        response = create_collection({"title": "a"})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid(self, authenticate, create_collection):
        authenticate(is_staff=True)
        response = create_collection({"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None

    def test_if_data_is_valid(self, authenticate, create_collection):
        authenticate(is_staff=True)
        response = create_collection({"title": "a"})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_return_200(self, api_client):
        collection = baker.make(Collection)
        response = api_client.get(f"/store/collections/{collection.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": collection.id,
            "title": collection.title,
            "products_count": 0,
        }
