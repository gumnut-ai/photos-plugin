---
name: build-event-album
description: Build or update a Gumnut Photos album for a trip, event, or period, such as a vacation, a wedding, a holiday, or a child's first year. Use when the user wants photos gathered into an album, wants an existing album filled in, or wants to know which photos from an event are not in an album yet.
---

# Build an album for an event

An event album needs two things the user rarely states exactly: the event's
boundaries (when and where it happened) and how selective to be. Pin the
boundaries down from the library before collecting photos, and make a large
selection visible before writing it.

## 1. Check for an existing album

Look before creating. `list_albums` has no name filter, so page through it
and compare names, descriptions, and date ranges with the event. When you
already hold a photo from the event, `list_albums` with `asset_id` finds its
albums directly. If an album already covers the event, offer to add to it
rather than making a second one.

## 2. Find the event's boundaries

Users remember events loosely ("our trip in May", "Mia's birthday party").
Turn that into explicit bounds using the library itself:

- **When:** call `get_asset_counts` with `group_by=day` over a generous window
  around the remembered dates. A trip shows up as a run of busy days; a party
  as one busy afternoon. Both date bounds are exclusive, so set
  `local_datetime_after` just before the first busy day and
  `local_datetime_before` to the start of the day after the last one. Pass
  bounds without a timezone (no `Z` or offset) so a trip abroad stays on its
  local calendar.
- **Where:** if the event has a place, `get_geo_clusters` over the region
  shows where the photos concentrate. Use those clusters to confirm you have
  the right trip, or to separate it from home photos taken on the same days.
  Photos without location data can still belong to the event, so do not
  filter on location alone.
- **Who:** for events defined by people ("Grandma's 90th"), resolve the names
  with `list_people` and use `person_ids` to find the core of the event, then
  widen by date to catch the photos those people are not in.

Confirm the boundaries with the user when they are not obvious, for example
"I found photos from May 3 to May 11, mostly in Kyoto and Osaka. Is that the
trip?"

## 3. Decide how selective to be

- **Everything from the event** suits an archive album. Collect all assets
  inside the boundaries, then drop obvious strays: screenshots, photos of
  documents, and accidental shots, which the `description` and a very low
  `quality_score` usually reveal.
- **Highlights** suit an album to share. Follow the choose-best-photos skill
  for the selection.

If the user did not say which, ask, or propose highlights and offer the full
set.

Either way, collapse bursts: assets that share a `stack_id` are near-identical
shots. An archive album can keep them all; a highlights album normally keeps
one frame per stack.

## 4. Show the selection, then write it

For a large or uncertain selection, show the proposed set first with
`list_assets` and `ids=[...]` (pass a `limit` above the default 20), along
with the count and anything you left out and why. If the user already asked
for the album and the boundaries are clear, go ahead:

1. Create the album with `create_album`, using a name the user would
   recognize and a short description of the event.
2. Add the photos with `add_assets_to_album` in batches of up to 200 IDs.
   Retrying a failed batch is safe.
3. Show the result with `get_album`.

Albums only reference photos. To take a photo out of an album, use
`remove_assets_from_album`, not `trash_assets`.

## Finding photos that still need an album

`album_filter=not_in_album` on `list_assets`, `get_asset_counts`, or
`get_geo_clusters` shows photos that are in no album at all. Counting them by
month or clustering them on a map is a good way to suggest which events are
still unorganized.
