---
name: tidy-people-and-faces
description: Help the user organize the people Gumnut Photos recognizes by naming people, merging duplicate people, fixing faces assigned to the wrong person, and adding faces the detector missed. Use when the user asks who is in their library, wants to name or correct people, or says a person is split, mixed up, or missing from photos.
---

# Tidy people and faces

Gumnut groups detected faces into people automatically. The groups are
usually right but never perfect: one person can be split across several
records, a record can contain a few faces of someone else, and some faces are
missed or left unassigned when Gumnut was unsure. Only the user knows who
people are, so this job is a conversation: you find the likely problems and
show them, the user confirms, and then you make the change.

## Name the people who matter first

To find people worth naming, list unnamed people (`name_filter=unnamed`)
sorted by `asset_count_desc`: the largest unnamed groups are usually family
and close friends. Show a few at a time (`get_person` displays a person with
their photos) and ask who they are. Apply several names at once with
`bulk_update_people`.

Names are unique within a library. If naming an unnamed person fails with a
conflict because another person already has that name, the same person is
probably split across two records: offer to merge them instead.

People who are not worth naming, such as strangers in the background, can be
hidden (`is_hidden`) instead of deleted. Hiding is reversible and keeps them
out of the way.

## Merge a person who is split

Signs of a split: a name conflict as above, similar names ("Bob" and "Bobby
Smith"), or an unnamed group whose faces look like a named person at a
different age or with different glasses.

- Show both records side by side and get the user's confirmation before
  calling `merge_people`; it cannot be undone.
- Make the record the user has named, or the larger one, the primary person.
  The source records are deleted and their faces move to the primary.

## Fix faces assigned to the wrong person

To review a person's faces, use `list_faces` with `person_id`. Scan for faces
that do not belong, view the photo when you are unsure, and confirm with the
user. Then either move the face to the right person with `update_face`, or
detach it with `person_id=null` when the user does not know who it is.
Detaching is gentler than `delete_face`, which removes the detection
entirely; delete only boxes that are not faces at all.

For a photo the user is looking at, `list_faces` with `asset_id` and
`include=cluster_assignment` shows each face's nearest candidate people,
including for faces with no person yet. Treat the candidates as suggestions
to show the user, not answers.

## Add a face the detector missed

When the user says someone is in a photo but Gumnut does not show them:

1. Look at the photo with `view_asset` to find the face.
2. Draw the box with `create_face`. Its coordinates are pixels of the asset's
   reported `width` and `height`, not of the image `view_asset` returned,
   which is resized. Scale your coordinates up to the asset's dimensions.
3. Assign it to the person in the same call with `person_id`, or create the
   person first with `create_person` if they are new.

## Changes that cannot be undone

Merging people and deleting people or faces are permanent, so describe
exactly what will change and get an explicit yes first. Naming, hiding, and
moving a face to another person can all be reversed later.
