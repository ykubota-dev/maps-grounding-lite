from pydantic import BaseModel, ConfigDict, Field

#Request/Response共通
class LatLng(BaseModel):
    latitude: float = Field(ge=-90.0, le=90.0)
    longitude: float = Field(ge=-180.0, le=180.0)

#Request関連
class Circle(BaseModel):
    center: LatLng
    radius_meters: float | None = Field(
        default=None,
        alias="radiusMeters",
        ge=0,
        le=50_000,
    )

class LocationBias(BaseModel):
    circle: Circle | None = None

class SearchPlacesRequest(BaseModel):
    text_query: str = Field(
        alias="textQuery",
        min_length=1,
    )
    language_code: str | None = Field(
        default=None,
        alias="languageCode",
    )
    region_code: str | None = Field(
        default=None,
        alias="regionCode",
    )
    location_bias: LocationBias | None = Field(
        default=None,
        alias="locationBias",
    )

#Response関連
class GoogleMapsLinks(BaseModel):
    directions_url: str | None = Field(alias="directionsUrl")
    place_url: str = Field(alias="placeUrl")
    write_a_review_url: str = Field(alias="writeAReviewUrl")
    reviews_url: str = Field(alias="reviewsUrl")
    photos_url: str = Field(alias="photosUrl")

class Attribution(BaseModel):
    "場所とともに表示される必須の帰属表示"
    title: str
    url: str

class PlaceView(BaseModel):
    place: str
    id: str
    google_maps_links: GoogleMapsLinks = Field(alias="googleMapsLinks")
    attribution: Attribution
    latlng: LatLng | None = None

class SearchPlacesResponse(BaseModel):
    places: list[PlaceView]
    summary: str