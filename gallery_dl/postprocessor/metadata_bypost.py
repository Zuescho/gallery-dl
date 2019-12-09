# -*- coding: utf-8 -*-

# Copyright 2019 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Write metadata to JSON files"""

from .metadata import __postprocessor__ as MetadataPP


class Metadata_bypostPP(MetadataPP):

    def __init__(self, pathfmt, options):
        MetadataPP.__init__(self, pathfmt, options)

    def prepare(self, pathfmt):
        # Only run this processor on metadata messages, not individual images.
        if pathfmt.kwdict.get("metadata_only"):
            MetadataPP.run(self, pathfmt)

    def run(self, pathfmt):
         return

__postprocessor__ = Metadata_bypostPP
