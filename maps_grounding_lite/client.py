from .models.search_places import (
    SearchPlacesRequest,
    SearchPlacesResponse
)

class MapsGroundingLiteClient:

    async def search_places(
        self,
        request: SearchPlacesRequest,
    ) -> SearchPlacesResponse:
        """
        Search for places based on a text query and optional location bias.

        Args:
            request (SearchPlacesRequest): The request object containing the search parameters.
        """
        return SearchPlacesResponse(
            places=[],
            summary=f"Search for places with query: {request.text_query}, language: {request.language_code}, region: {request.region_code}, location bias: {request.location_bias}"
        )