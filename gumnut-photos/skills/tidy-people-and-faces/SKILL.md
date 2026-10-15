---
name: tidy-people-and-faces
description: Help the user organize the people Gumnut Photos recognizes by naming people, merging duplicate people, fixing faces assigned to the wrong person, and adding faces the detector missed. Use when the user asks who is in their library, wants to name or correct people, or says a person is split, mixed up, or missing from photos.
---

# Tidy people and faces

Gumnut groups detected faces into people automatically. The groups are
usually right but never perfect: one person can be split across several
records, a record can contain a few faces of someone else, and some faces are
missed or left unassigned when Gumnut was unsure.

## Name people

The largest unnamed groups (`name_filter=unnamed`, sorted by
`asset_count_desc`) are usually family and close friends, so they are the
best place to start.

Identity can come from the user or from the photos themselves. Name tags,
yearbook pages, team rosters, playbills, and captions show faces next to
names, and Gumnut does not read them on its own. When the task allows naming
and the text clearly belongs to one face, apply the name. Ask when it is
unclear which face a name belongs to, or when the evidence conflicts.

People who are not worth naming, such as strangers in the background, can be
hidden (`is_hidden`). Hiding is reversible and keeps them out of the way.

## Name conflicts and split people

Names are unique within a library, including hidden people. A conflict can
mean the same person is split across two records, or that two different
people share a name. Compare the two records before proposing a merge; if
they are different people, suggest a distinguishing name such as a surname
or initial.

Other signs of a split: similar names ("Bob" and "Bobby Smith"), or an
unnamed group whose faces look like a named person at a different age or with
different glasses.

## Fix faces assigned to the wrong person

Move a face to the right person with `update_face`, or detach it with
`person_id=null` when nobody knows who it is. Detaching is gentler than
`delete_face`, which removes the detection; delete only boxes that are not
faces at all. For a face with no person yet, `list_faces` with
`include=cluster_assignment` suggests the nearest people; treat those as
suggestions, not answers.

## Add a face the detector missed

Draw the box with `create_face`. Its coordinates are pixels of the asset's
reported `width` and `height`, not of the image `view_asset` returned, which
is resized, so scale your coordinates up to the asset's dimensions.

## Merges and deletions

Merging people and deleting people or faces have no direct undo. Describe
exactly what will change and get an explicit yes first. A merge keeps the
primary person and deletes the others. Their faces could be reassigned to new
people by hand later, but the original records are gone, so when recovery
might matter, note which faces came from which person and each record's name
and settings before merging.
