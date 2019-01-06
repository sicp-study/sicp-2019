#!/usr/bin/python
# Copyright (c) 2019 Red Hat
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
import argparse
import logging

from sicp import EvaluateSICP


def main():
    parser = argparse.ArgumentParser(description="Evaluate SICP assignments")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("files", nargs='+')
    args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s %(levelname)-5.5s %(name)s - %(message)s',
        level=logging.DEBUG if args.debug else logging.INFO)

    success = True

    for fpath in args.files:
        evaluate = EvaluateSICP()
        try:
            result = evaluate.validate(fpath)
        except Exception as e:
            result = str(e)
            success = False
            if args.debug:
                raise
        finally:
            evaluate.close()
        print("%s: %s" % (fpath, result))
    if not success:
        exit(1)


if __name__ == '__main__':
    main()
