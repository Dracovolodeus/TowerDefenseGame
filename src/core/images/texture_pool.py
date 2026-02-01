from pathlib import Path

from arcade import Texture, load_texture


class TexturePool:
    def __init__(self) -> None:
        self.images: dict[Path, Texture] = {}

    def get_texture(self, path: str | Path) -> Texture:
        if isinstance(path, str):
            path = Path(path)
        if path not in self.images:
            self.images[path] = load_texture(path)
        return self.images[path]
