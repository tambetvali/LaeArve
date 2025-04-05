# # Link Conversion: Source to Web and Back
# 
# This file defines two conversion functions for mapping links between a physical source folder and a web address.
# In our scenario:
#
# - **Link:** is the input string (a URL) which may be:
#    - A root-relative link (starting with “/”),
#    - A relative link (starting with a letter), or
#    - A fully qualified web link (starting with “http://”).
#
# - **Source folder:** is the folder in your physical code tree that you wish to map from.
#    In this example, it is given as `"sourcefolder"`.
#
# - **Target folder (or web address):** is the folder that appears in the web version.
#    In this example, it is given as `"webaddress"`.
#
# **Mapping logic:**
#
# 1. In `convert_source_to_target(link, sourcefolder, webaddress)`:
#    - If the input link is a relative link or already starts with “http://”, it is left unchanged.
#    - If it is a root-relative link and it starts with the exact prefix `sourcefolder` (character‑for‑character),
#      then that prefix is replaced by `webaddress`.
#    - Otherwise, the link is returned as-is.
#
# 2. In `convert_target_to_source(link, sourcefolder, webaddress)`:
#    - If the input link is a relative link or already starts with “http://”, it is not converted.
#    - If it starts with the exact prefix `webaddress`, that prefix is replaced with `sourcefolder`.
#    - Otherwise, the link is returned unchanged.
#
# **Note:** This conversion is designed so that if you convert a link from source → target and then back (target → source),
# the result is exactly the same (digitwise) as the original. This means that any trailing slash (or its absence) in the
# provided constants is preserved.
#
# Below are the two functions and a test suite showing several cases—including cases with and without trailing slashes.

def convert_source_to_target(link, sourcefolder, webaddress):
    """
    Convert a source link into its web target link.

    Parameters:
      link (str): The input URL.
                  - If the link is relative (i.e. does not start with "/") or starts with "http://",
                    it is returned unchanged.
      sourcefolder (str): The physical source folder prefix. Examples: "/sourcefolder" or "/sourcefolder/"
      webaddress (str): The web target folder prefix. Examples: "/webaddress" or "/webaddress/"

    Conversion:
      - If the link starts exactly with sourcefolder, that prefix is replaced by webaddress.
      - Otherwise the link is returned as-is.
    """
    # Leave fully-qualified or relative links unchanged.
    if link.startswith("http://") or not link.startswith("/"):
        return link

    # If the link starts exactly with the sourcefolder prefix, replace it with webaddress.
    if link.startswith(sourcefolder):
        return webaddress + link[len(sourcefolder):]
    else:
        return link

def convert_target_to_source(link, sourcefolder, webaddress):
    """
    Convert a web target link back into the original physical source link.

    Parameters:
      link (str): The input URL.
                  - If the link is relative or starts with "http://", it remains unchanged.
      sourcefolder (str): The physical source folder prefix.
      webaddress (str): The web target folder prefix.

    Conversion:
      - If the link starts exactly with webaddress, that prefix is replaced by sourcefolder.
      - Otherwise the link is returned as-is.
    """
    # Leave fully-qualified or relative links unchanged.
    if link.startswith("http://") or not link.startswith("/"):
        return link

    # If the link starts exactly with the webaddress prefix, replace it with sourcefolder.
    if link.startswith(webaddress):
        return sourcefolder + link[len(webaddress):]
    else:
        return link

# --- Testing the conversion functions ---
if __name__ == "__main__":
    # We test two cases: one where both the sourcefolder and webaddress have no trailing slash,
    # and one where both have a trailing slash.
    cases = [
        {
            "description": "No trailing slash",
            "sourcefolder": "/sourcefolder",
            "webaddress": "/webaddress",
            "tests": [
                "/sourcefolder/file.txt",
                "/sourcefolder/subdir/code.py",
                "/sourcefolder",         # the link is exactly the sourcefolder itself
                "/other/place/doc.md",   # link that does not match the source folder
                "relative/path.md",      # relative link (remains unchanged)
                "http://example.com"     # fully-qualified link (remains unchanged)
            ]
        },
        {
            "description": "With trailing slash",
            "sourcefolder": "/sourcefolder/",
            "webaddress": "/webaddress/",
            "tests": [
                "/sourcefolder/file.txt",
                "/sourcefolder/subdir/code.py",
                "/sourcefolder/",        # the link matches the entire sourcefolder
                "/another/place/doc.md", # link that does not match the source folder
                "relative/path.md",      # relative link (remains unchanged)
                "http://example.com"     # fully-qualified link (remains unchanged)
            ]
        }
    ]

    for case in cases:
        print("Testing case:", case["description"])
        src = case["sourcefolder"]
        web = case["webaddress"]
        for original in case["tests"]:
            # Convert source link to target link.
            converted = convert_source_to_target(original, src, web)
            # Then convert it back from target to source.
            reverted = convert_target_to_source(converted, src, web)
            print(f"Original:         {original}")
            print(f"  -> To target:  {converted}")
            print(f"  -> Back to src:{reverted}")
            if reverted == original:
                print("  Round-trip PASSED")
            else:
                print("  Round-trip FAILED")
        print()
