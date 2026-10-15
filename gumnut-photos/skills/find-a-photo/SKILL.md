---
name: find-a-photo
description: Find a specific photo or video the user remembers in their Gumnut Photos library from a partial description, such as "the picture of Dad holding the big fish" or "that receipt I photographed last spring". Use when the user is looking for one photo or a small set rather than browsing or curating.
---

# Find a specific photo

People remember a photo through a mix of exact facts ("Dad was in it"),
fuzzy facts ("sometime last spring"), and content ("holding a big fish").
Put the exact facts into filters, the content into the search query, and
treat the fuzzy facts as wide ranges you can tighten later.

## 1. Split the memory into filters and content

- **People** become `person_ids`, resolved by name with `list_people`. Several
  people means photos containing all of them, which narrows quickly.
- **Dates** become `local_datetime_after` and `local_datetime_before`. Widen
  remembered dates generously: "last spring" might really be March to July.
- **Places:** a place name goes in the query; a known area can use `center`
  and `radius`.
- **Content** (objects, activities, scenes, text visible in the photo) goes
  in the `search_assets` `query` as a short visual phrase: "man holding a
  large fish on a boat" rather than the user's whole sentence.
- **Kind of media:** `media_type=video` for videos. Videos match search
  through their text and metadata, not their visual content, so rely more on
  people, dates, and places to find a video.

## 2. Search, then relax one constraint at a time

Run the narrowest reasonable `search_assets` call first. If the photo is not
in the results:

1. Widen the date range.
2. Drop the person filter. The face may not be recognized or assigned.
3. Rephrase the content query with different words for the same thing.
4. Drop the location. Many photos have no location data.

Change one thing per attempt so you know which constraint was wrong. A
content search ranks only its top 200 candidates, so a specific query with
filters beats a vague query on its own.

For a narrow time window you can also skip search entirely: `list_assets`
with tight date bounds returns everything from those hours, in order.

## 3. Confirm the match

Generated descriptions identify most photos. When the user needs a detail the
description cannot confirm (text on a receipt or sign, a number, who is
holding what), look with `view_asset`. Its default size is large enough to
read text.

## 4. Show it

Display the photo with `get_asset`, or several close candidates with
`list_assets` and `ids=[...]`, and tell the user what made you pick it. If
you could not find it, say which constraints you tried, so they can correct
the one that was wrong.
