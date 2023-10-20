from swarms.chunkers.base import BaseChunker
from swarms.chunkers.chunk_seperator import ChunkSeparator


class MarkdownChunker(BaseChunker):
    DEFAULT_SEPARATORS = [
        ChunkSeparator("##", is_prefix=True),
        ChunkSeparator("###", is_prefix=True),
        ChunkSeparator("####", is_prefix=True),
        ChunkSeparator("#####", is_prefix=True),
        ChunkSeparator("######", is_prefix=True),
        ChunkSeparator("\n\n"),
        ChunkSeparator(". "),
        ChunkSeparator("! "),
        ChunkSeparator("? "),
        ChunkSeparator(" "),
    ]
