from googleapiclient.discovery import build
from secret import get_secret


class Ytdata:
    def __init__(self):
        self.api_key = get_secret("API_KEY")
        self.location = "52.308056, 4.764167"
        self.radius = "1km"

    def _query(self):
        url = f"https://www.googleapis.com/youtube/v3/search/list"
        service = build('youtube', 'v3', developerKey=self.api_key)
        qs = service.search().list(
            part='snippet',
            location=self.location,
            locationRadius=self.radius,
            type="video",
            publishedBefore="2012-12-31T00:00:00Z",
            publishedAfter="2012-01-01T00:00:00Z"
        )
        response = qs.execute()
        return len(response["items"])


yt = Ytdata()
cnt = yt._query()
print(
    f"{cnt} videos were uploaded to YouTube in the 2012 with the "
    f"specified location: Amsterdam Airport Schiphol” (radius is limited to 1 km)"
)
