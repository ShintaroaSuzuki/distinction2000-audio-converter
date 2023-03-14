import sys
from collections import defaultdict
from pathlib import Path
from typing import Literal

import pydub

args = sys.argv


assert (
    len(args) == 2 or len(args) == 3
), "Usage: main.py <input_dir> <output_dir(optional)>"

assert Path(args[1]).is_dir(), "Input directory does not exist"

assert len(args) == 2 or not Path(args[2]).is_file(), "Output directory is a file"


def handle_file(
    *,
    file: Path,
    output_dir: Path,
    d: defaultdict,
    max_len: int,
    type: Literal["academic", "snapshot"],
) -> None:
    k = file.stem[:5] + type
    d[k].append(file)
    if len(d[k]) == max_len:
        combined = pydub.AudioSegment.empty()
        for f in sorted(d[k]):
            combined += pydub.AudioSegment.from_file(f, "mp3")
        combined.export(
            output_dir.joinpath(f"{file.stem[:-1]}.mp3"),
            format="mp3",
        )
        del d[k]


def main() -> None:
    input_dir = Path(args[1])
    output_dir = (
        Path(args[2])
        if len(args) > 2
        else input_dir.with_stem(input_dir.stem + "_output")
    )

    if not output_dir.exists():
        output_dir.mkdir()

    d = defaultdict(list[Path])

    for file in input_dir.iterdir():
        if file.suffix == ".mp3":
            if file.stem.startswith("Ch_"):
                common_params = {
                    "file": file,
                    "output_dir": output_dir,
                    "d": d,
                }
                if "snapshot" in file.stem:
                    if file.stem.startswith("Ch_11") or file.stem.startswith("Ch_25"):
                        handle_file(
                            **common_params,
                            max_len=2,
                            type="snapshot",
                        )
                    elif file.stem.startswith("Ch_33") or file.stem.startswith("Ch_34"):
                        handle_file(
                            **common_params,
                            max_len=3,
                            type="snapshot",
                        )
                    else:
                        handle_file(**common_params, max_len=1, type="snapshot")
                elif "academic" in file.stem:
                    handle_file(
                        **common_params,
                        max_len=4,
                        type="academic",
                    )


if __name__ == "__main__":
    main()
