# Study guides

The study guides are organized by type, each with a downloadable PDF. See the [study guide index](../study-guide-index.md) for the full list.

| Folder | Prefix | Contents |
| --- | --- | --- |
| [general/](general/) | `gen-` | In-depth guides on a topic |
| [mini/](mini/) | `mini-` | Short guides on one under-covered idea |
| [current-events/](current-events/) | `ce-` | Course concepts applied to current markets |
| [supplements/](supplements/) | `supp-` | Reference material that supports the guides |

Files are named `<prefix>-<NN>-<title>.md`, all lowercase with hyphens, and each type is numbered separately. PDFs sit in a `pdf/` folder beside the markdown with the same file name.

Each guide that has practice questions also has a Canvas quiz in a `qti/` folder beside the markdown.

To rebuild after editing a guide, run `python tools/build_pdfs.py`, `python tools/guide_to_qti.py --all` and then `python tools/build_index.py` from the repository root (needs pandoc and xelatex).
