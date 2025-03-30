# Backreferencing

# Backreferencing is preferred method for
# adding chapters into a book, because it's
# neutral about the exact location of the
# pages:
# - @@[YourSite](yourlink)

# Forward-referencing is the same with one @.

# Currently, each controller-detected piece is at top level,
# and we might later decide what to do: inside code blocks,
# markdown should be highlighted but not rendered in
# comments: it's as readable in highlighed version, and
# also manually copyable.

import mistune

mistune.Markdown("index.md")

