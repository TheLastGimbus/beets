from __future__ import annotations

from typing import Any

from typing_extensions import TypeAlias, TypedDict

JSONDict: TypeAlias = "dict[str, Any]"


class LRCLibAPI:
    class Item(TypedDict):
        """Lyrics data item returned by the LRCLib API."""

        id: int
        name: str
        trackName: str
        artistName: str
        albumName: str
        duration: float | None
        instrumental: bool
        plainLyrics: str
        syncedLyrics: str | None


class GeniusAPI:
    """Genius API data types.

    This documents *only* the fields that are used in the plugin.
    :attr:`SearchResult` is an exception, since I thought some of the other
    fields might be useful in the future.
    """

    class DateComponents(TypedDict):
        year: int
        month: int
        day: int

    class Artist(TypedDict):
        api_path: str
        header_image_url: str
        id: int
        image_url: str
        is_meme_verified: bool
        is_verified: bool
        name: str
        url: str

    class Stats(TypedDict):
        unreviewed_annotations: int
        hot: bool

    class SearchResult(TypedDict):
        annotation_count: int
        api_path: str
        artist_names: str
        full_title: str
        header_image_thumbnail_url: str
        header_image_url: str
        id: int
        lyrics_owner_id: int
        lyrics_state: str
        path: str
        primary_artist_names: str
        pyongs_count: int | None
        relationships_index_url: str
        release_date_components: GeniusAPI.DateComponents
        release_date_for_display: str
        release_date_with_abbreviated_month_for_display: str
        song_art_image_thumbnail_url: str
        song_art_image_url: str
        stats: GeniusAPI.Stats
        title: str
        title_with_featured: str
        url: str
        featured_artists: list[GeniusAPI.Artist]
        primary_artist: GeniusAPI.Artist
        primary_artists: list[GeniusAPI.Artist]

    class SearchHit(TypedDict):
        result: GeniusAPI.SearchResult

    class SearchResponse(TypedDict):
        hits: list[GeniusAPI.SearchHit]

    class Search(TypedDict):
        response: GeniusAPI.SearchResponse
