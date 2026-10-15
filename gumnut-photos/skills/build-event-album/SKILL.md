---
name: build-event-album
description: Build or update a Gumnut Photos album for a trip, event, or period, such as a vacation, a wedding, a holiday, or a child's first year. Use when the user wants photos gathered into an album, wants an existing album filled in, or wants to know which photos from an event are not in an album yet.
---

# Build an album for an event

An event album needs two things the user rarely states exactly: the event's
boundaries (when and where it happened) and how selective to be. Pin the
boundaries down from the library before collecting photos.

## Check for an existing album

Look before creating. If an album already covers the event, offer to add to
it rather than making a second one. When you already hold a photo from the
event, check which albums contain it.

## Find the event's boundaries

Users remember events loosely ("our trip in May", "Mia's birthday party").
Turn that into explicit bounds using the library itself:

- **When:** daily asset counts (`get_asset_counts`) over a generous window
  around the remembered dates show the event as a run of busy days, or one
  busy afternoon for a party.
- **Where:** geo clusters (`get_geo_clusters`) show where the photos
  concentrate, which confirms the right trip or separates it from home photos
  taken on the same days. Photos without location data can still belong to
  the event, so do not filter on location alone.
- **Who:** for events defined by people ("Grandma's 90th"), find the core of
  the event with those people, then widen by date to catch the photos they
  are not in.

Confirm the boundaries with the user when they are not obvious, for example
"I found photos from May 3 to May 11, mostly in Kyoto and Osaka. Is that the
trip?"

## Decide how selective to be

- **An archive** keeps everything inside the event's boundaries, including
  bursts and the tickets, maps, signs, and notes photographed along the way.
  Leave out only what falls outside the event, and name any other exclusion
  you make so the user can put it back.
- **Highlights** suit an album to share. Follow the choose-best-photos skill,
  which keeps one frame per burst.

If the user did not say which, ask, or propose highlights and offer the full
set.

## Show and write the selection

Collect the whole set inside the boundaries, paging until nothing is left,
before you count or add it. When the selection is large or the boundaries
were uncertain, show the user a sample sized for them to judge, with the total
count and what you left out, before writing. If they already asked for the
album and the boundaries are clear, go ahead.

## Finding photos that still need an album

To suggest events that are still unorganized, count or cluster photos with
`album_filter=not_in_album` by month or on a map.
