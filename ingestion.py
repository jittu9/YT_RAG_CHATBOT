from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from logger import setup_logger
import re
from urllib.parse import urlparse, parse_qs

logger = setup_logger()


def extract_video_id(url: str) -> str:
    """
    Extracts YouTube video ID from different URL formats.
    """

    parsed_url = urlparse(url)

    # Case 1: https://www.youtube.com/watch?v=VIDEO_ID
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        query_params = parse_qs(parsed_url.query)
        return query_params.get("v", [None])[0]

    # Case 2: https://youtu.be/VIDEO_ID
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path.lstrip("/")

    # Case 3: https://www.youtube.com/embed/VIDEO_ID
    if "embed" in parsed_url.path:
        return parsed_url.path.split("/")[2]

    # Case 4: fallback using regex
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if match:
        return match.group(1)

    return None

def fetch_transcript(video_id: str) -> str:
    try:
        logger.info(f"Fetching transcript for video: {video_id}")
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.fetch(video_id, languages=["en"])
        transcript = " ".join(chunk.text for chunk in transcript_list)
        logger.info("Transcript fetched successfully")
        return transcript
    except TranscriptsDisabled:
        logger.error("Transcripts are disabled for this video")
        return None