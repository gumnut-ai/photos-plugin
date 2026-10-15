---
name: choose-best-photos
description: Choose the best photos from a set in a Gumnut Photos library, such as highlights from a trip, a cover photo, a slideshow, or photos to share or print. Use when the user asks for the best, favorite, or most representative photos of a person, place, period, event, or album.
---

# Choose the best photos

"Best" means best for this user and this purpose, not just technically best.
Gumnut gives you two kinds of evidence: what the library records about each
photo (who, what, where, when, and how well it was captured) and how the user
has already organized it (albums, favorites, named people, stacks). The
purpose decides how much each one counts.

## Turn the request into who, what, where, when, and why

- **Who:** named people, resolved to person IDs. A photo "of the kids"
  usually means photos containing those specific people, not any children.
- **What:** subjects, activities, or moods ("at the beach", "candid",
  "the cake") for a content search.
- **Where and when:** places and explicit date bounds. Convert phrases such as
  "last summer" before searching.
- **Why:** the purpose sets the size and the standard. A cover needs one
  strong, representative frame; a slideshow needs variety and a story; a
  large print needs a sharp, well-exposed image. If the user gave no count,
  choose one that fits the purpose and say so.

Ask only about ambiguity that would change the result, such as a name that
matches several people or two trips that both match "Japan".

## Gather candidates

An album the user made for the event is strong evidence of what belongs, but
it may be incomplete or a bulk import, so widen with people, date, and place
filters when the request reaches beyond it. Use content search for what is in
the photos. A content search ranks a limited candidate pool, so for a large
event search in slices (per day, person, or activity) rather than once for
everything.

## Weigh the evidence for the purpose

- **Favorites** (a rating of 5) show what the user values. They carry the
  most weight for a personal retrospective or slideshow; for a large print, a
  favorite still has to be technically sound.
- **The requested people** should be prominent, not specks in the
  background. Face bounding boxes compared with the photo's dimensions show
  prominence without opening the image. Photos with several of the requested
  people together are often the ones users value most.
- **The generated `description`** tells you what is happening (the toast, the
  summit, the first steps), including expressions and composition.
- **`quality_score`** keeps blurry, badly exposed, or accidental shots out.
  It is coarse, so similar frames often tie; compare those by eye. A slightly
  soft photo of a milestone can still beat a sharp photo of a parking lot, and
  an unscored photo is not a bad one.

## Remove near-duplicates and build variety

- Assets that share a `stack_id` are one burst or group of similar shots. Keep
  one per stack, normally a favorite or the best-looking frame, unless the
  user wants the burst.
- Photos seconds apart with near-identical descriptions are usually the same
  moment even without a stack.
- For a story or slideshow, cover the event's span, its places, and its
  people rather than ten photos from the best hour.

## Look at images when it could change the choice

Records are the efficient way to narrow a large set. Look at the images
themselves (`view_asset`) whenever visual judgment could change the pick:
choosing a cover, comparing similar frames, checking eyes and expressions, or
reviewing a small shortlist where looking at every candidate is cheap.
