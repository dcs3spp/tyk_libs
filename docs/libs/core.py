import re
import semver


def extract_semver(text: str) -> str:
    """
    Extract a semantic version string from text

    @param text (str) The text to extract semver from

    @return Extracted semver

    @raises ValueError
        When fails to extract a semantic version string
    """

    cleaned = text.strip().lower()

    match = re.search("[\d\.]+", cleaned)
    if not match:
        raise ValueError(f"No semver found in {text}")

    parsed = match.group(0)
    result = parsed

    try:
        _ = int(parsed)
    except ValueError:
        ver = semver.Version.parse(parsed)
        result = f"{ver.major}.{ver.minor}"

    return result
