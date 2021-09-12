"""
Copyright (C) 2021  Koviubi56

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import hashlib
from typing import Dict, Literal, Union
import PySimpleGUI as sg
from sys import exit


def _batch_mode(settings: dict) -> bool:
    return settings.get("enabled", False)


def main(
    batch_mode: Dict[Union[Literal["enabled", "file"]], Union[bool, str]] = {
        "enabled": False
    }
):
    """
    The main function

    Args:
        batch_mode (Dict[Union[Literal["enabled", "file"]], Union[bool, str]]): Batch mode settings. Syntax:
    ```py
    {
        "enabled": bool  # Enabled?
        # --- If enabled: ---
        "file": str  # The file. It will be opened as "with open(FILE) as f: ..."
    }
    ```
    """
    assert batch_mode.get("enabled") in [
        True,
        False,
    ], 'batch_mode["enabled"]: not True or False'
    if _batch_mode(batch_mode):
        assert isinstance(
            batch_mode.get("file"), str
        ), 'batch_mode["file"]: omitted or not a str'
    if not _batch_mode(batch_mode):
        event, values = sg.Window(
            "Get file",
            [
                [
                    sg.FileBrowse(
                        key="-FILE-", button_text="Browse a file", enable_events=True
                    ),
                ],
                [
                    sg.Text(
                        "This program is distributed in the hope that it will be useful, \nbut WITHOUT ANY WARRANTY; without even the implied warranty of \nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE."
                    ),
                ],
            ],
        ).read()

        if event == sg.WIN_CLOSED:
            exit()

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    sha512 = hashlib.sha512()
    sha3_512 = hashlib.sha3_512()
    blake2s = hashlib.blake2s()
    sha384 = hashlib.sha384()
    sha3_256 = hashlib.sha3_256()
    sha3_224 = hashlib.sha3_224()
    blake2b = hashlib.blake2b()
    sha3_384 = hashlib.sha3_384()
    sha224 = hashlib.sha224()

    try:
        with open(
            values["-FILE-"] if not _batch_mode(batch_mode) else batch_mode["file"]
        ) as f:
            while True:
                data = f.read(64_000).encode()
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
                sha256.update(data)
                sha512.update(data)
                sha3_512.update(data)
                blake2s.update(data)
                sha384.update(data)
                sha3_256.update(data)
                sha3_224.update(data)
                blake2b.update(data)
                sha3_384.update(data)
                sha224.update(data)
    except FileNotFoundError:
        if _batch_mode(batch_mode):
            raise
        sg.Popup(
            "File does not exists or you didn't choosed a file!",
            button_color="red",
            custom_text=("Error"),
            title="Error",
        )
        exit(1)
    if _batch_mode(batch_mode):
        return {
            h.name: h
            for h in {
                md5,
                sha1,
                sha256,
                sha512,
                sha3_512,
                blake2s,
                sha384,
                sha3_256,
                sha3_224,
                blake2b,
                sha3_384,
                sha224,
            }
        }

    while True:
        event, values = sg.Window(
            "File hashes",
            [
                [
                    sg.Text("MD5: "),
                    sg.InputText(default_text=md5.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("SHA1: "),
                    sg.InputText(default_text=sha1.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("SHA256: "),
                    sg.InputText(default_text=sha256.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("SHA512: "),
                    sg.InputText(default_text=sha512.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("SHA3 512: "),
                    sg.InputText(default_text=sha3_512.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("Blake2s: "),
                    sg.InputText(default_text=blake2s.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("SHA384: "),
                    sg.InputText(default_text=sha384.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("SHA3 256: "),
                    sg.InputText(default_text=sha3_256.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("SHA3 224: "),
                    sg.InputText(default_text=sha3_224.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("Blake2b: "),
                    sg.InputText(default_text=blake2b.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("SHA3 384: "),
                    sg.InputText(default_text=sha3_384.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("SHA224: "),
                    sg.InputText(default_text=sha224.hexdigest(), disabled=True),
                ],
                [
                    sg.Text("Paste a hash: "),
                    sg.InputText(key="-HASH-"),
                ],
                [sg.OK("Check hash or exit")],
            ],
        ).read()
        if event == sg.WIN_CLOSED:
            exit()
        if values["-HASH-"] == "":
            exit()
        if values["-HASH-"].lower() == md5.hexdigest().lower():
            sg.Popup("Correct MD5 hash!")
        elif values["-HASH-"].lower() == sha1.hexdigest().lower():
            sg.Popup("Correct SHA1 hash!")
        elif values["-HASH-"].lower() == sha256.hexdigest().lower():
            sg.Popup("Correct SHA256 hash!")
        elif values["-HASH-"].lower() == sha512.hexdigest().lower():
            sg.Popup("Correct SHA512 hash!")
        elif values["-HASH-"].lower() == sha3_512.hexdigest().lower():
            sg.Popup("Correct SHA3 512 hash!")
        elif values["-HASH-"].lower() == blake2s.hexdigest().lower():
            sg.Popup("Correct Blake2s hash!")
        elif values["-HASH-"].lower() == sha384.hexdigest().lower():
            sg.Popup("Correct SHA384 hash!")
        elif values["-HASH-"].lower() == sha3_256.hexdigest().lower():
            sg.Popup("Correct SHA3 256 hash!")
        elif values["-HASH-"].lower() == sha3_224.hexdigest().lower():
            sg.Popup("Correct SHA3 224 hash!")
        elif values["-HASH-"].lower() == blake2b.hexdigest().lower():
            sg.Popup("Correct Blake2b hash!")
        elif values["-HASH-"].lower() == sha3_384.hexdigest().lower():
            sg.Popup("Correct SHA3 384 hash!")
        elif values["-HASH-"].lower() == sha224.hexdigest().lower():
            sg.Popup("Correct SHA224 hash!")
        else:
            sg.Popup("Incorrect hash! You may got hacked!")


if __name__ == "__main__":
    main()
