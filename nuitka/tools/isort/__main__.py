#!/usr/bin/env python
#     Copyright 2017, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#

""" Sort import statements using isort for Nuitka source.

"""

from __future__ import print_function

import os
import subprocess
import sys

# Unchanged, running from checkout, use the parent directory, the nuitka
# package ought be there.
sys.path.insert(
    0,
    os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            ".."
        )
    )
)

from nuitka.tools.Basics import goHome, addPYTHONPATH # isort:skip
from nuitka.tools.ScanSources import scanTargets # isort:skip


def main():
    goHome()

    # So PyLint finds nuitka package.
    addPYTHONPATH(os.getcwd())

    target_files = []
    for filename in scanTargets(["nuitka", "bin"]):
        target_files.append(filename)

    target_files.append("nuitka/build/SingleExe.scons")

    subprocess.check_call(
        [
            "isort",
            "-ot",
            "-m3",
            "-ns",
            "__init__.py"
        ] + target_files
    )

if __name__ == "__main__":
    main()
