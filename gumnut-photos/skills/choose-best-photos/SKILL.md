---
name: choose-best-photos
description: Choose the best photos from a set in a Gumnut Photos library, such as highlights from a trip, a cover photo, a slideshow, or photos to share or print. Use when the user asks for the best, favorite, or most representative photos of a person, place, period, event, or album.
---

# Choose the best photos

"Best" means best for this user and this purpose, not just technically best.
Gumnut gives you two kinds of evidence: what the library records about each
photo (who, what, where, when, and how well it was captured) and how the user
has already organized it (albums, favorites, named people, stacks). Use both.
Read the records first and look at pixels last.

## 1. Turn the request into who, what, where, and when

Before searching, work out what the user told you and what they left open:

- **Who:** named people. Resolve each name to a person ID with `list_people`
  and `name`. A photo "of the kids" usually means photos containing those
  specific people, not any children.
- **What:** subjects, activities, or moods ("at the beach", "candid",
  "the cake"). These go in the `search_assets` `query`.
- **Where:** a place name goes in `query`; known coordinates or a map area use
  `center` and `radius` or `bbox`.
- **When:** convert phrases such as "last summer" into explicit
  `local_datetime_after` and `local_datetime_before` bounds. Times are the
  photo's local wall-clock time, so a trip abroad stays on its local calendar.
- **Purpose and size:** a cover needs one strong, representative frame; a
  slideshow needs variety and a story; a print needs high technical quality.
  If the user gave no count, choose one that fits the purpose and say so.

Ask only about ambiguity that would change the result, such as two people with
the same name or two different trips that match "Japan".

## 2. Gather candidates from the strongest source first

1. **An existing album.** If the user already made an album for the event,
   start there (`list_assets` with `album_id`). Its membership is the user's
   own judgment of what belongs. `list_albums` has no name filter, so page
   through it and match names and descriptions yourself.
2. **Structured filters.** People, dates, and coordinates are exact. Prefer
   `list_assets` when no content `query` is needed.
3. **Content search.** Use `search_assets` for what is in the photos. A content
   search ranks at most its top 200 candidates, so for a large event search
   per day, per person, or per activity rather than once for everything.

Request only the expansions you will use: `include=people` when choosing by
who appears, `include=metadata` for place names, camera details, and rating.

## 3. Rank with the user's signals ahead of technical quality

Weigh the evidence roughly in this order:

1. **Favorites and ratings.** A rating of 5 is a favorite. The user's own pick
   outweighs any score. `ratings=[5]` is a quick way to find them.
2. **The people who matter for the request.** Photos where the requested
   people are present and visible beat photos where they are a speck in the
   background. Photos with several of the requested people together are
   often the ones users value most.
3. **The description.** Gumnut's generated `description` tells you what is
   happening, including expressions, action, and composition. Use it to find
   the moments: the toast, the summit, the first steps.
4. **`quality_score`.** Use it to keep blurry, badly exposed, or accidental
   shots out of a "best" set and to break ties between similar photos. It
   judges the image, not its meaning: a slightly soft photo of a milestone
   beats a sharp photo of a parking lot. Scores take a few distinct values,
   so many photos tie; `null` means unscored, not bad.

## 4. Remove near-duplicates and build variety

- **Stacks:** assets that share a `stack_id` are one burst or group of similar
  shots. Keep one per stack, normally a favorite or the highest-quality frame,
  unless the user wants the burst.
- **Unstacked near-duplicates:** photos seconds apart with near-identical
  descriptions are usually the same moment. Keep the best one.
- **Spread:** for a story or slideshow, cover the event's span (beginning,
  middle, and end), its different places, and the people involved, rather
  than ten photos from the best hour.

## 5. Look at finalists only where it matters

`view_asset` shows you the pixels, but it is slow and costly compared with
reading records. Use it on a shortlist when the decision depends on something
records cannot tell you: closed eyes, a face hidden by a hat, which of two
similar frames is sharper, or text in the image. Do not view every candidate.

## 6. Present the choice and offer the next step

- Show the selection with `list_assets` and `ids=[...]` so it renders as a
  gallery, in the order you recommend.
- Explain the picks briefly: why these, what you left out, and anything you
  were unsure about, such as a face Gumnut did not recognize.
- Offer the next step instead of taking it: putting the photos in an album
  (see the build-event-album skill), marking favorites, or swapping picks.
