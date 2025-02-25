#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    open-mss
    ~~~~~~~~

    Mission Support System

    Message to inform the user how to install MSS.

    This file is part of MSS.

    :copyright: Copyright 2008-2014 Deutsches Zentrum fuer Luft- und Raumfahrt e.V.
    :copyright: Copyright 2011-2014 Marc Rautenhaus (mr)
    :copyright: Copyright 2016-2025 by the MSS team, see AUTHORS.
    :license: APACHE-2.0, see LICENSE for details.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


def main_cli():
    print("open-mss is a conda-forge package. You can install it with pixi.")
    print("")
    print("Get pixi from https://pixi.sh/latest/ for your operation system.")
    print("")
    print("pixi global install mss")
    print("")
    print("Usage:")
    print("    msui -h")
    print("    mswms -h")
    print("    mscolab -h")


if __name__ == "__main__":
    main_cli()
